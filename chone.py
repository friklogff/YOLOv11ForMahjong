import os
import random
from PIL import Image, ImageDraw

# 设置路径
image_dir = r"E:\Downloads\mahjong-dataset-master\train\augmented_images"
label_dir = r"E:\Downloads\mahjong-dataset-master\train\augmented_labels"

# 获取所有图像和标注文件
image_files = [os.path.join(image_dir, f) for f in os.listdir(image_dir) if f.endswith('.jpg')]
label_files = [os.path.join(label_dir, f) for f in os.listdir(label_dir) if f.endswith('.txt')]

# 随机选择一张图像和对应的标注文件
image_path = random.choice(image_files)
label_path = os.path.join(label_dir, os.path.basename(image_path).replace('.jpg', '.txt'))

# 加载图像
image = Image.open(image_path).convert('RGB')

# 加载标注文件
with open(label_path, 'r') as f:
    labels = f.readlines()

# 创建一个绘图对象
draw = ImageDraw.Draw(image)

# 遍历标注文件中的每一行
for label in labels:
    class_id, x_center, y_center, width, height = map(float, label.strip().split())
    # 将归一化的标注信息转换为像素坐标
    x = int((x_center - width / 2) * image.width)
    y = int((y_center - height / 2) * image.height)
    w = int(width * image.width)
    h = int(height * image.height)
    # 绘制边界框
    draw.rectangle([x, y, x + w, y + h], outline='red', width=2)
    # 在边界框上方绘制类别标签
    draw.text((x, y - 10), str(int(class_id)), fill='red')

# 显示图像
image.show()