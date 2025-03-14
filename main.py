import cv2
import numpy as np
import matplotlib.pyplot as plt

# Загрузка изображения (укажи свой путь)
image_path = "your_image.png"  # Замените на путь к вашему изображению
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Грузим в оттенках серого

# Применяем фильтрацию (например, медианный фильтр)
filtered_image = cv2.medianBlur(image, 3)

# Разностное изображение
diff_image = cv2.absdiff(image, filtered_image)  # Модуль разности для полутонового

# Создание дискового структурирующего элемента 3×3
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))

# Морфологическая эрозия (сжатие)
eroded_image = cv2.erode(image, kernel, iterations=1)

# Отображение результатов
fig, axes = plt.subplots(1, 4, figsize=(15, 5))
axes[0].imshow(image, cmap='gray')
axes[0].set_title("Исходное изображение")
axes[1].imshow(filtered_image, cmap='gray')
axes[1].set_title("Фильтрованное изображение")
axes[2].imshow(diff_image, cmap='gray')
axes[2].set_title("Разностное изображение")
axes[3].imshow(eroded_image, cmap='gray')
axes[3].set_title("Эрозия (сжатие)")

for ax in axes:
    ax.axis("off")

plt.show()
