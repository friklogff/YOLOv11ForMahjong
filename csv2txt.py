import os
import pandas as pd

# 设置文件夹路径
train_folder = r"E:\Downloads\mahjong-dataset-master\train"
images_folder = os.path.join(train_folder, "images")
output_folder = os.path.join(train_folder, "labels")

# 创建输出文件夹（如果不存在）
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 加载 data.csv 文件
data_csv = os.path.join(train_folder, "data.csv")
data = pd.read_csv(data_csv)

# 定义花牌的类别索引
bonus_tiles = [35, 36, 37, 38, 39, 40, 41, 42]

# 筛选出非花牌的行
filtered_data = data[~data['label'].isin(bonus_tiles)]

# 遍历筛选后的数据，生成 YOLO 格式的标注文件
for index, row in filtered_data.iterrows():
    image_name = row['image-name']
    label = row['label'] - 1  # YOLO 的类别索引从 0 开始
    label_name = row['label-name']

    # 假设目标框占据整个图像
    # YOLO 格式的标注信息：类别索引 <x_center> <y_center> <width> <height>
    # 坐标和尺寸归一化到 [0, 1] 范围内
    yolo_label_file = os.path.join(output_folder, os.path.splitext(image_name)[0] + '.txt')

    # 写入 YOLO 格式的标注信息
    with open(yolo_label_file, 'w') as f:
        f.write(f"{label} 0.5 0.5 1.0 1.0\n")  # 目标框占据整个图像

print("完成 YOLO 格式转换！")