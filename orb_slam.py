import cv2
import numpy as np
import pickle

# Функция для вычисления траектории движения на основе совпадений ключевых точек
def calculate_trajectory(matches, keypoints, previous_keypoints):
    trajectory = []
    for match in matches:
        query_idx = match.queryIdx
        train_idx = match.trainIdx

        # Получаем координаты ключевых точек из совпадений
        query_point = keypoints[query_idx].pt
        train_point = previous_keypoints[train_idx].pt

        # Вычисляем смещение между точками
        dx = train_point[0] - query_point[0]
        dy = train_point[1] - query_point[1]

        # Добавляем смещение к траектории
        trajectory.append((dx, dy))

    return trajectory

# Инициализация ORB SLAM
orb = cv2.ORB_create()
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
previous_frame = None
previous_keypoints = None
trajectory = []

# Загрузка видеофайла
cap = cv2.VideoCapture('video.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    keypoints, descriptors = orb.detectAndCompute(gray, None)

    if previous_frame is not None:
        matches = bf.match(descriptors, previous_descriptors)
        matches = sorted(matches, key=lambda x: x.distance)

        # Вычисляем траекторию движения камеры
        current_trajectory = calculate_trajectory(matches, keypoints, previous_keypoints)
        trajectory.extend(current_trajectory)

    previous_frame = gray
    previous_keypoints = keypoints
    previous_descriptors = descriptors

cap.release()

# Сохранение результатов в файл trajectory.pkl
with open('trajectory.pkl', 'wb') as file:
    pickle.dump(trajectory, file)
