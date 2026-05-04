import os
import cv2
import numpy as np

def load_data(data_dir, img_size=224):
    images = []
    labels = []

    for label in os.listdir(data_dir):
        path = os.path.join(data_dir, label)
        class_num = 0 if label == "no" else 1

        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_array = cv2.imread(img_path)
            img_array = cv2.resize(img_array, (img_size, img_size))

            images.append(img_array)
            labels.append(class_num)

    return np.array(images), np.array(labels)