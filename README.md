# Лабораторная работа №3

## Тема: Фильтрация изображений и морфологические операции

|**Студент:**|*Вудвуд Андрей*|
|------------|--------------|
|**Группа:** |*Б22-564*     |
|**Вариант:**|*19*           |
---

## Примеры

1. [Котик - малым шума](#ex1)
2. [Котик - немного шума](#ex2)
3. [Котик - инвертированный](#ex3)
4. [Котик - инвертированный](#ex4)
5. [Другой котик - немного шума](#ex5)
6. [Иероглиф](#ex6)
7. [Спираль](#ex7)
8. [Текст](#ex8)
9. [Пиксель-арт](#ex9)

## План

---

- ### Задание №1: Морфологическое сжатие (эрозия). Структурирующий элемент — диск 3×3

- ### Задание №2: Разностное изображение (попиксельный xor или модуль разности)


<a name="ex1"></a>
## Пример №1

- #### Исходное изображение

![Original](../images/cat.jpg)

- #### Изображение с шумом и перцем

![](images/cat.jpg_svsp0.5_amount0.05/with_salt_0.5_0.05_cat.jpg)

### Задание

| **Эрозия (диск)**                                                      | **Разностное**                                                           |
|------------------------------------------------------------------------|--------------------------------------------------------------------------|
| ![](images/cat.jpg_svsp0.5_amount0.05/erosion_disk_0.5_0.05_cat.jpg)   | ![](images/cat.jpg_svsp0.5_amount0.05/xor_erosion_0.5_0.05_cat.jpg)      |

---

<a name="ex2"></a>
## Пример №2

- #### Исходное изображение

![Original](../images/cat.jpg)

- #### Изображение с шумом и перцем

![](images/cat.jpg_svsp0.5_amount0.3/with_salt_0.5_0.3_cat.jpg)

### Задание

| **Эрозия (диск)**                                                      | **Разностное**                                                           |
|------------------------------------------------------------------------|--------------------------------------------------------------------------|
| ![](images/cat.jpg_svsp0.5_amount0.3/erosion_disk_0.5_0.3_cat.jpg)     | ![](images/cat.jpg_svsp0.5_amount0.3/xor_erosion_0.5_0.3_cat.jpg)        |

---

<a name="ex3"></a>
## Пример №3

- #### Исходное изображение

![Original](../images/cat_invert.jpg)

- #### Изображение с шумом и перцем

![](images/cat_invert.jpg_svsp0.5_amount0.05/with_salt_0.5_0.05_cat_invert.jpg)

### Задание

| **Эрозия (диск)**                                                      | **Разностное**                                                           |
|------------------------------------------------------------------------|--------------------------------------------------------------------------|
| ![](images/cat_invert.jpg_svsp0.5_amount0.05/erosion_disk_0.5_0.05_cat_invert.jpg) | ![](images/cat_invert.jpg_svsp0.5_amount0.05/xor_erosion_0.5_0.05_cat_invert.jpg) |

---

<a name="ex4"></a>
## Пример №4

- #### Исходное изображение

![Original](../images/cat_invert.jpg)

- #### Изображение с шумом и перцем

![](images/cat_invert.jpg_svsp0.5_amount0.3/with_salt_0.5_0.3_cat_invert.jpg)

### Задание

| **Эрозия (диск)**                                                      | **Разностное**                                                           |
|------------------------------------------------------------------------|--------------------------------------------------------------------------|
| ![](images/cat_invert.jpg_svsp0.5_amount0.3/erosion_disk_0.5_0.3_cat_invert.jpg) | ![](images/cat_invert.jpg_svsp0.5_amount0.3/xor_erosion_0.5_0.3_cat_invert.jpg) |

---

<a name="ex5"></a>
## Пример №5

- #### Исходное изображение

![Original](../images/cat2.jpg)

- #### Изображение с шумом и перцем

![](images/cat2.jpg_svsp0.5_amount0.05/with_salt_0.5_0.05_cat2.jpg)

### Задание

| **Эрозия (диск)**                                                      | **Разностное**                                                           |
|------------------------------------------------------------------------|--------------------------------------------------------------------------|
| ![](images/cat2.jpg_svsp0.5_amount0.05/erosion_disk_0.5_0.05_cat2.jpg) | ![](images/cat2.jpg_svsp0.5_amount0.05/xor_erosion_0.5_0.05_cat2.jpg)    |

---

<a name="ex6"></a>
## Пример №6

- #### Исходное изображение

![Original](../images/screen2.png)

- #### Изображение с шумом и перцем

![](images/screen2.png_svsp0.5_amount0.09/with_salt_0.5_0.09_screen2.png)

### Задание №1

- #### Эрозия (диск)

![](images/screen2.png_svsp0.5_amount0.09/erosion_disk_0.5_0.09_screen2.png)

### Задание №2

- #### Разностное изображение

![](images/screen2.png_svsp0.5_amount0.09/xor_erosion_0.5_0.09_screen2.png)

---

<a name="ex7"></a>
## Пример №7

- #### Исходное изображение

![Original](../images/spiral1.png)

- #### Изображение с шумом и перцем

![](images/spiral1.png_svsp0.5_amount0.1/with_salt_0.5_0.1_spiral1.png)

### Задание №1

- #### Эрозия (диск)

![](images/spiral1.png_svsp0.5_amount0.1/erosion_disk_0.5_0.1_spiral1.png)

### Задание №2

- #### Разностное изображение

![](images/spiral1.png_svsp0.5_amount0.1/xor_erosion_0.5_0.1_spiral1.png)

---

<a name="ex8"></a>
## Пример №8

- #### Исходное изображение

![Original](../images/text1.jpg)

- #### Изображение с шумом и перцем

![](images/text1.jpg_svsp0.5_amount0.1/with_salt_0.5_0.1_text1.jpg)

### Задание №1

- #### Эрозия (диск)

![](images/text1.jpg_svsp0.5_amount0.1/erosion_disk_0.5_0.1_text1.jpg)

### Задание №2

- #### Разностное изображение

![](images/text1.jpg_svsp0.5_amount0.1/xor_erosion_0.5_0.1_text1.jpg)

---

<a name="ex9"></a>
## Пример №9

- #### Исходное изображение

![Original](../images/pixel_art.jpg)

- #### Изображение с шумом и перцем

![](images/pixel_art.jpg_svsp0.5_amount0.05/with_salt_0.5_0.05_pixel_art.jpg)

### Задание №1

- #### Эрозия (диск)

![](images/pixel_art.jpg_svsp0.5_amount0.05/erosion_disk_0.5_0.05_pixel_art.jpg)

### Задание №2

- #### Разностное изображение

![](images/pixel_art.jpg_svsp0.5_amount0.05/xor_erosion_0.5_0.05_pixel_art.jpg)