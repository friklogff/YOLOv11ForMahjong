

# YOLOv11ForMahjong

## 项目简介
YOLOv11ForMahjong 是一个基于 YOLOv11 模型的麻将牌识别项目。该项目旨在通过计算机视觉技术实现对中文麻将牌的高效识别和定位。通过使用 YOLOv11 模型，我们能够快速准确地检测和识别麻将牌，适用于多种应用场景，如游戏辅助、文化研究等。

## CSDN
[【YOLOv11 】麻将牌识别的“黑科技”：YOLOv11 模型训练全攻略](https://blog.csdn.net/qq_42531954/article/details/145428228)


## 项目结构
```
.
├── .idea                    # 项目配置文件夹
├── aug-images               # 增强后的图像数据集
│   ├── train                # 训练集
│   │   ├── images           # 训练集图像
│   │   └── labels           # 训练集标注文件
│   └── val                  # 验证集
│       ├── images           # 验证集图像
│       └── labels           # 验证集标注文件
├── raw-data                 # 原始数据集
│   ├── train                # 训练集
│   │   ├── images           # 训练集图像
│   │   └── labels           # 训练集标注文件
│   └── val                  # 验证集
│       ├── images           # 验证集图像
│       └── labels           # 验证集标注文件
├── model                    # 模型配置文件夹
│   └── yolo11.pt          # YOLOv11 模型配置文件
├── run                      # 运行结果保存文件夹
├── yaml                     # YAML 配置文件夹
├── Arial.Unicode.ttf        # 字体文件
├── aughf.py                 # 数据增强脚本
├── aug_mj_train.py          # 模型训练脚本
├── bz.py                    # 数据处理脚本
├── chone.py                 # 数据处理脚本
├── conbin.py                # 数据处理脚本
├── csv2txt.py               # 标注格式转换脚本
├── flowconbin.py            # 数据处理脚本
├── gui.py                   # 图形用户界面脚本
├── hf.py                    # 数据处理脚本
├── imglitter.py             # 图像处理脚本
├── LICENSE                  # 项目许可证
├── mj_aug_val.py            # 增强数据集验证脚本
├── mj_val.py                # 模型验证脚本
├── predict.py               # 模型预测脚本
└── README.md                # 项目说明文档
```

## 数据集
数据集主要从 [Camerash/mahjong-dataset](https://github.com/Camerash/mahjong-dataset) 获取，包含以下内容：
- **原始未分割图像**：`./raw-data/raw-images`
- **未缩放的麻将牌图像**：`./raw-data/raw-tiles`
- **缩放后的图像**：`./raw-data/tiles-resized`
- **标注数据**：`./raw-data/tiles-data`
- **未标注的图像**：`./raw-data/untagged-images-raw` 和 `./raw-data/untagged-tiles`






## 使用说明
### 安装依赖
```bash
pip install -r requirements.txt
```

### 模型
### 评估模型
```bash
python mj_val.py
```

```bash
python mj_aug_val.py
```
### 图片预测

```bash
python predict.py
```
## 项目贡献
欢迎贡献代码和数据！如果您有任何问题或建议，请随时提交 Issue 或 Pull Request。

## 许可
本项目开源，采用 MIT 许可证。更多信息请参阅 `LICENSE` 文件。

## 参考文献
- [Camerash/mahjong-dataset](https://github.com/Camerash/mahjong-dataset)
- [YOLOv11 官方文档](https://docs.ultralytics.com/zh)
