from PIL import Image, ImageFilter
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

# Функция для выполнения эрозии без OpenCV
def erode_image(image_array, kernel_size=3):
    padded = np.pad(image_array, pad_width=kernel_size//2, mode='edge')
    eroded = np.zeros_like(image_array)
    
    for i in range(image_array.shape[0]):
        for j in range(image_array.shape[1]):
            eroded[i, j] = np.min(padded[i:i+kernel_size, j:j+kernel_size])
    
    return eroded

# Обработка каждого изображения
for image_file in image_files:
    # Полный путь к изображению
    image_path = os.path.join(input_folder, image_file)
    
    # Загрузка изображения в оттенках серого
    image = Image.open(image_path).convert("L")
    image_array = np.array(image)
    
    # Проверка, загружено ли изображение
    if image_array is None:
        print(f"Ошибка: не удалось загрузить изображение {image_file}.")
        continue
    
    # Морфологическая эрозия (сжатие)
    eroded_image_array = erode_image(image_array, kernel_size=3)
    eroded_image = Image.fromarray(eroded_image_array)
    
    # Разностное изображение (разница между исходным и эродированным)
    diff_image_array = np.abs(image_array - eroded_image_array)
    diff_image = Image.fromarray(diff_image_array)
    
    # Сохранение результатов
    base_name = os.path.splitext(image_file)[0]  # Имя файла без расширения
    eroded_image.save(os.path.join(output_folders["eroded"], f"{base_name}_eroded.jpg"))
    diff_image.save(os.path.join(output_folders["diff"], f"{base_name}_diff.jpg"))
    
    # Отображение результатов
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))  # 3 изображения в ряд
    axes[0].imshow(image_array, cmap='gray')
    axes[0].set_title("Исходное изображение")
    axes[1].imshow(eroded_image_array, cmap='gray')
    axes[1].set_title("После эрозии")
    axes[2].imshow(diff_image_array, cmap='gray')
    axes[2].set_title("Разностное изображение")
    
    for ax in axes:
        ax.axis("off")
    
    plt.show()
