import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Путь к папке с исходными изображениями
input_folder = "with_salt"  # Папка с изображениями

# Создание папок для сохранения результатов
output_folders = {
    "eroded": "results/eroded",  # Папка для изображений после эрозии
    "diff": "results/diff"       # Папка для разностных изображений
}

# Создаем папки, если они не существуют
for folder in output_folders.values():
    os.makedirs(folder, exist_ok=True)

# Получаем список всех файлов в папке original
image_files = [f for f in os.listdir(input_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]

# Проверка, есть ли изображения в папке
if not image_files:
    print(f"Ошибка: в папке {input_folder} нет изображений.")
    exit()

# Обработка каждого изображения
for image_file in image_files:
    # Полный путь к изображению
    image_path = os.path.join(input_folder, image_file)

    # Загрузка изображения в оттенках серого
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Проверка, загружено ли изображение
    if image is None:
        print(f"Ошибка: не удалось загрузить изображение {image_file}.")
        continue

    # Создание дискового структурирующего элемента 3×3
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))

    # Морфологическая эрозия (сжатие)
    eroded_image = cv2.erode(image, kernel, iterations=1)

    # Разностное изображение (разница между исходным и эродированным)
    diff_image = cv2.absdiff(image, eroded_image)

    # Сохранение результатов
    base_name = os.path.splitext(image_file)[0]  # Имя файла без расширения
    cv2.imwrite(os.path.join(output_folders["eroded"], f"{base_name}_eroded.jpg"), eroded_image)
    cv2.imwrite(os.path.join(output_folders["diff"], f"{base_name}_diff.jpg"), diff_image)

    # Отображение результатов
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))  # 3 изображения в ряд
    axes[0].imshow(image, cmap='gray')
    axes[0].set_title("Исходное изображение")
    axes[1].imshow(eroded_image, cmap='gray')
    axes[1].set_title("После эрозии")
    axes[2].imshow(diff_image, cmap='gray')
    axes[2].set_title("Разностное изображение")

    for ax in axes:
        ax.axis("off")

    plt.show()