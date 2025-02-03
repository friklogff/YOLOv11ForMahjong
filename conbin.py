import os
import random
from PIL import Image

# 设置路径
image_dir = r"E:\Downloads\mahjong-dataset-master\train\filtered_images"
label_dir = r"E:\Downloads\mahjong-dataset-master\train\labels"
output_image_dir = r"E:\Downloads\mahjong-dataset-master\train\augmented_images"
output_label_dir = r"E:\Downloads\mahjong-dataset-master\train\augmented_labels"
os.makedirs(output_image_dir, exist_ok=True)
os.makedirs(output_label_dir, exist_ok=True)

# 获取所有图像和标注文件
image_files = [os.path.join(image_dir, f) for f in os.listdir(image_dir) if f.endswith('.jpg')]
label_files = [os.path.join(label_dir, f) for f in os.listdir(label_dir) if f.endswith('.txt')]

# 定义拼接图像的大小
canvas_size = (1280, 1280)  # 定义画布大小
num_images_to_place = 14  # 每张拼接图像放置的麻将牌数量
overlap_threshold = 0.1  # 重叠面积阈值（0.1 表示重叠面积不超过 10%）
max_attempts = 50  # 最大尝试次数

def compute_iou(box1, box2):
    """计算两个边界框的交并比（IoU）"""
    x1, y1, w1, h1 = box1
    x2, y2, w2, h2 = box2

    # 计算交集区域
    inter_x1 = max(x1, x2)
    inter_y1 = max(y1, y2)
    inter_x2 = min(x1 + w1, x2 + w2)
    inter_y2 = min(y1 + h1, y2 + h2)
    inter_area = max(0, inter_x2 - inter_x1) * max(0, inter_y2 - inter_y1)

    # 计算并集区域
    area1 = w1 * h1
    area2 = w2 * h2
    union_area = area1 + area2 - inter_area

    return inter_area / union_area if union_area != 0 else 0

def place_image(canvas, image, position, placed_boxes):
    """将图像放置到画布上，并检查重叠情况"""
    x, y = position
    w, h = image.size

    # 检查与已放置的图像的重叠情况
    for box in placed_boxes:
        iou = compute_iou((x, y, w, h), box)
        if iou > overlap_threshold:
            return False, placed_boxes  # 重叠超过阈值，返回 False

    # 如果没有重叠或重叠在允许范围内，则放置图像
    # 检查图像是否有透明通道
    if image.mode == 'RGBA':
        canvas.paste(image, position, image)  # 使用透明通道作为遮罩
    else:
        canvas.paste(image, position)  # 不使用遮罩
    placed_boxes.append((x, y, w, h))
    return True, placed_boxes

# 遍历生成新的拼接图像
for i in range(1280):  # 生成100张拼接图像
    canvas = Image.new('RGB', canvas_size, (255, 255, 255))  # 创建白色画布
    labels = []  # 用于存储YOLO格式的标注信息
    placed_boxes = []  # 用于存储已放置的边界框

    for _ in range(num_images_to_place):
        # 随机选择一张图像和对应的标注文件
        image_path = random.choice(image_files)
        label_path = os.path.join(label_dir, os.path.basename(image_path).replace('.jpg', '.txt'))

        # 加载图像
        image = Image.open(image_path).convert('RGB')

        # 加载标注文件
        with open(label_path, 'r') as f:
            label = f.read().strip().split()
        class_id = int(label[0])  # 获取类别索引
        x_center, y_center, width, height = map(float, label[1:5])  # 获取归一化的标注信息

        # 将标注信息转换为像素坐标
        x = int((x_center - width / 2) * image.width)
        y = int((y_center - height / 2) * image.height)
        w = int(width * image.width)
        h = int(height * image.height)

        placed = False
        attempts = 0
        while not placed and attempts < max_attempts:
            position = (random.randint(0, canvas_size[0] - w),
                        random.randint(0, canvas_size[1] - h))
            placed, placed_boxes = place_image(canvas, image, position, placed_boxes)
            attempts += 1

        if placed:
            # 更新YOLO格式的标注
            new_x_center = (position[0] + w / 2) / canvas_size[0]
            new_y_center = (position[1] + h / 2) / canvas_size[1]
            new_width = w / canvas_size[0]
            new_height = h / canvas_size[1]
            labels.append(f"{class_id} {new_x_center:.6f} {new_y_center:.6f} {new_width:.6f} {new_height:.6f}")

    # 保存拼接后的图像
    output_image_path = os.path.join(output_image_dir, f"augmented_{i}.jpg")
    canvas.save(output_image_path)

    # 保存YOLO格式的标注文件
    output_label_path = os.path.join(output_label_dir, f"augmented_{i}.txt")
    with open(output_label_path, 'w') as f:
        for label in labels:
            f.write(label + '\n')

print("数据增强完成，生成的图像和标注文件已保存到", output_image_dir, "和", output_label_dir)