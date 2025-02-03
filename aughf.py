import os
import random
import shutil





# 设置路径
images_dir = r"E:\Downloads\mahjong-dataset-master\train\augmented_images"
labels_dir = r"E:\Downloads\mahjong-dataset-master\train\augmented_labels"
train_images_dir = r"E:\Downloads\mahjong-dataset-master\train\mj-dataset\aug-images\train\images"
train_labels_dir = r"E:\Downloads\mahjong-dataset-master\train\mj-dataset\aug-images\train\labels"
val_images_dir = r"E:\Downloads\mahjong-dataset-master\train\mj-dataset\aug-images\val\images"
val_labels_dir = r"E:\Downloads\mahjong-dataset-master\train\mj-dataset\aug-images\val\labels"

# 创建目标目录
os.makedirs(train_images_dir, exist_ok=True)
os.makedirs(train_labels_dir, exist_ok=True)
os.makedirs(val_images_dir, exist_ok=True)
os.makedirs(val_labels_dir, exist_ok=True)

# 获取所有图像和标注文件
image_files = [f for f in os.listdir(images_dir) if f.endswith('.jpg')]
label_files = [f.replace('.jpg', '.txt') for f in image_files]

# 设置划分比例
train_ratio = 0.8  # 80% 用于训练
random.seed(42)  # 设置随机种子以保证结果可复现

# 随机打乱文件顺序
random.shuffle(image_files)

# 计算划分点
split_index = int(len(image_files) * train_ratio)

# 划分训练集和验证集
train_images = image_files[:split_index]
val_images = image_files[split_index:]

# 复制文件到训练集和验证集目录
for image_file in train_images:
    shutil.copy(os.path.join(images_dir, image_file), os.path.join(train_images_dir, image_file))
    label_file = image_file.replace('.jpg', '.txt')
    shutil.copy(os.path.join(labels_dir, label_file), os.path.join(train_labels_dir, label_file))

for image_file in val_images:
    shutil.copy(os.path.join(images_dir, image_file), os.path.join(val_images_dir, image_file))
    label_file = image_file.replace('.jpg', '.txt')
    shutil.copy(os.path.join(labels_dir, label_file), os.path.join(val_labels_dir, label_file))

print(f"数据集划分完成，训练集图像数量: {len(train_images)}，验证集图像数量: {len(val_images)}")