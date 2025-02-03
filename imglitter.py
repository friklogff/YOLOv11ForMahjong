import os
import shutil
import pandas as pd

# 设置文件夹路径
train_folder = r"E:\Downloads\mahjong-dataset-master\train"
images_folder = os.path.join(train_folder, "images")
output_folder = os.path.join(train_folder, "filtered_images")

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

# 将筛选后的数据保存到新的 CSV 文件中
filtered_csv = os.path.join(train_folder, "filtered_data.csv")
filtered_data.to_csv(filtered_csv, index=False)

# 复制对应的图像文件到新的文件夹
for image_name in filtered_data['image-name']:
    source_image_path = os.path.join(images_folder, image_name)
    target_image_path = os.path.join(output_folder, image_name)

    if os.path.exists(source_image_path):
        shutil.copy(source_image_path, target_image_path)
    else:
        print(f"Image not found: {source_image_path}")

print("完成筛选和复制操作！")