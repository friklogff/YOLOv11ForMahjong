import os
from PIL import Image, ImageDraw

def display_and_annotate_mahjong(image_path, output_dir, rows, cols):
    # 读取图像
    image = Image.open(image_path)
    img_width, img_height = image.size

    # 计算每个麻将牌的宽度和高度
    tile_width = img_width / cols
    tile_height = img_height / rows

    # 创建一个可绘制的图像副本
    draw = ImageDraw.Draw(image)

    # 创建输出目录（如果不存在）
    os.makedirs(output_dir, exist_ok=True)

    # 准备写入标注文件
    base_name = os.path.basename(image_path)
    txt_file_path = os.path.join(output_dir, os.path.splitext(base_name)[0] + '.txt')
    with open(txt_file_path, 'w') as f:
        # 遍历每个麻将牌
        for row in range(rows):
            for col in range(cols):
                # 计算麻将牌的边界框坐标
                x_min = col * tile_width
                y_min = row * tile_height
                x_max = x_min + tile_width
                y_max = y_min + tile_height

                # 绘制边界框
                draw.rectangle([x_min, y_min, x_max, y_max], outline="red", width=2)

                # 显示图像
                image.show()

                # 等待用户输入 ID
                class_id = input(f"Enter the class ID for the mahjong tile at row {row}, col {col}: ")

                # 计算麻将牌的中心点坐标（相对于图像尺寸）
                rel_x_center = (x_min + x_max) / 2 / img_width
                rel_y_center = (y_min + y_max) / 2 / img_height
                rel_width = tile_width / img_width
                rel_height = tile_height / img_height

                # 生成 YOLO 格式的标注行
                annotation_line = f"{class_id} {rel_x_center} {rel_y_center} {rel_width} {rel_height}"

                # 写入标注文件
                f.write(annotation_line + '\n')

                # 清除边界框
                draw.rectangle([x_min, y_min, x_max, y_max], outline="red", width=2)

# 示例用法
image_path = r'E:\Downloads\mahjong-dataset-master\raw-images\10.jpg'
output_dir = r'E:\Downloads\mahjong-dataset-master\raw-images\yolo_annotations'
rows = 12  # 输入行数
cols = 12  # 输入列数
display_and_annotate_mahjong(image_path, output_dir, rows, cols)
