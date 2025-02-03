from ultralytics import YOLO
import cv2

if __name__ == '__main__':
    # 加载模型
    model = YOLO(model=r'model/many/fff300.pt')

    # 读取图片
    image_path = r'aug-images/val/images/augmented_38.jpg'
    image = cv2.imread(image_path)

    # 调整图片分辨率

    # 进行推理
    results = model.predict(source=image,
                            save=True,
                            show=True,
                            conf=0.1,  # 调整置信度阈值
                            project='run/predict')

    # 处理结果
    for result in results:
        print(result)
