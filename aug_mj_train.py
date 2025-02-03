from ultralytics import YOLO
import os

if __name__ == '__main__':
    # 加载模型配置
    model = YOLO('ultralytics/cfg/models/11/yolo11.yaml')
    
    # 构建last.pt文件的路径
    last_weights_path = os.path.join('/home/aistudio/ultralytics/mj-train/runs/train/train/weights/', 'best.pt')
    
    # 加载最后保存的权重（如果有）
    model.load(last_weights_path)
    
    # 开始训练模型
    results = model.train(
        data='/home/aistudio/ultralytics/aug-mj-data.yaml',
        epochs=300,  # 训练的总轮数
        imgsz=640,  # 输入图像的大小
        cache=False,  # 是否缓存数据增强效果
        batch=32,  # 每批处理的图像数量
        device='0',  # 指定训练设备，'0'表示使用第一个GPU
        single_cls=False,  # 是否为单类别检测
        optimizer='SGD',  # 使用SGD优化器
        resume=True,  # 从上次训练中断处继续训练
        amp=False,  # 使用自动混合精度训练
        lr0=0.01,  # 初始学习率
        momentum=0.937,  # SGD的动量参数
        weight_decay=0.0005,  # 权重衰减，L2正则化
        close_mosaic=10,  # 在前10个epoch不使用mosaic数据增强
        save_period=10,  # 每10个epoch保存一次模型
        workers=8,  # 数据加载的工作线程数，根据您的CPU核心数调整
        project='aug-mj-train/runs/',  # 训练项目的保存路径

    )

    # 打印训练结果
    print(results)