import os
import shutil
from sklearn.model_selection import train_test_split

# 设置文件夹路径
filtered_images_folder = r"E:\Downloads\mahjong-dataset-master\train\filtered_images"
labels_folder = r"E:\Downloads\mahjong-dataset-master\train\labels"
dataset_folder = r"E:\Downloads\mahjong-dataset-master\dataset"

# 创建 dataset 文件夹及其子文件夹
os.makedirs(os.path.join(dataset_folder, "images", "train"), exist_ok=True)
os.makedirs(os.path.join(dataset_folder, "images", "val"), exist_ok=True)
os.makedirs(os.path.join(dataset_folder, "labels", "train"), exist_ok=True)
os.makedirs(os.path.join(dataset_folder, "labels", "val"), exist_ok=True)

# 获取所有图像文件名
image_files = [f for f in os.listdir(filtered_images_folder) if f.endswith('.jpg')]

# 划分训练集和验证集（80% 训练，20% 验证）
train_images, val_images = train_test_split(image_files, test_size=0.2, random_state=42)


# 复制图像和标注文件到对应的训练集和验证集文件夹
def copy_files(file_list, source_folder, target_images_folder, target_labels_folder):
    for file_name in file_list:
        # 复制图像文件
        source_image_path = os.path.join(source_folder, file_name)
        target_image_path = os.path.join(target_images_folder, file_name)
        shutil.copy(str(source_image_path), str(target_image_path))

        # 复制对应的标注文件
        label_file_name = os.path.splitext(file_name)[0] + '.txt'
        source_label_path = os.path.join(labels_folder, label_file_name)
        target_label_path = os.path.join(target_labels_folder, label_file_name)
        shutil.copy(str(source_label_path), str(target_label_path))


# 复制训练集文件
copy_files(train_images, filtered_images_folder,
           os.path.join(dataset_folder, "images", "train"),
           os.path.join(dataset_folder, "labels", "train"))

# 复制验证集文件
copy_files(val_images, filtered_images_folder,
           os.path.join(dataset_folder, "images", "val"),
           os.path.join(dataset_folder, "labels", "val"))

print("数据集划分完成！")