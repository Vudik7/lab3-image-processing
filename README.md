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

<a name="ex1"> <h2>Пример №1</h2> </a>

---

- #### Исходное изображение

    ![Original](original/cat.jpg)

- #### Изображение с шумом и перцем

    ![](res/cat.jpg_svsp0.5_amount0.05/with_salt_0.5_0.05_cat.jpg)

### Задание

|**Xолм**|**Впадина**|**Разностное**|
|--------|-----------|--------------|
|![](res/cat.jpg_svsp0.5_amount0.05/median_hill_0.5_0.05_cat.jpg)|![](res/cat.jpg_svsp0.5_amount0.05/median_depression_0.5_0.05_cat.jpg)|![](res/cat.jpg_svsp0.5_amount0.05/xor_hill_depression_0.5_0.05_cat.jpg)


<a name="ex2"> <h2>Пример №2</h2> </a>

---

- #### Исходное изображение

    ![Original](original/cat.jpg)

- #### Изображение с шумом и перцем

    ![](res/cat.jpg_svsp0.5_amount0.3/with_salt_0.5_0.3_cat.jpg)

### Задание

|**Xолм**|**Впадина**|**Разностное**|
|--------|-----------|--------------|
|![](res/cat.jpg_svsp0.5_amount0.3/median_hill_0.5_0.3_cat.jpg)|![](res/cat.jpg_svsp0.5_amount0.3/median_depression_0.5_0.3_cat.jpg)|![](res/cat.jpg_svsp0.5_amount0.3/xor_hill_depression_0.5_0.3_cat.jpg)


<a name="ex3"> <h2>Пример №3</h2> </a>

---

- #### Исходное изображение

    ![Original](original/cat_invert.jpg)

- #### Изображение с шумом и перцем

    ![](res/cat_invert.jpg_svsp0.5_amount0.05/with_salt_0.5_0.05_cat_invert.jpg)

### Задание

|**Xолм**|**Впадина**|**Разностное**|
|--------|-----------|--------------|
|![](res/cat_invert.jpg_svsp0.5_amount0.05/median_hill_0.5_0.05_cat_invert.jpg)|![](res/cat_invert.jpg_svsp0.5_amount0.05/median_depression_0.5_0.05_cat_invert.jpg)|![](res/cat_invert.jpg_svsp0.5_amount0.05/xor_hill_depression_0.5_0.05_cat_invert.jpg)


<a name="ex4"> <h2>Пример №4</h2> </a>
---
- #### Исходное изображение

    ![Original](original/cat_invert.jpg)


- #### Изображение с шумом и перцем

    ![](res/cat_invert.jpg_svsp0.5_amount0.3/with_salt_0.5_0.3_cat_invert.jpg)

### Задание

|**Xолм**|**Впадина**|**Разностное**|
|--------|-----------|--------------|
|![](res/cat_invert.jpg_svsp0.5_amount0.3/median_hill_0.5_0.3_cat_invert.jpg)|![](res/cat_invert.jpg_svsp0.5_amount0.3/median_depression_0.5_0.3_cat_invert.jpg)|![](res/cat_invert.jpg_svsp0.5_amount0.3/xor_hill_depression_0.5_0.3_cat_invert.jpg)

<a name="ex5"> <h2>Пример №5</h2> </a>

---

- #### Исходное изображение

    ![Original](original/cat2.jpg)

- #### Изображение с шумом и перцем

    ![](res/cat2.jpg_svsp0.5_amount0.05/with_salt_0.5_0.05_cat2.jpg)

### Задание

|**Xолм**|**Впадина**|**Разностное**|
|--------|-----------|--------------|
|![](res/cat2.jpg_svsp0.5_amount0.05/median_hill_0.5_0.05_cat2.jpg)|![](res/cat2.jpg_svsp0.5_amount0.05/median_depression_0.5_0.05_cat2.jpg)|![](res/cat2.jpg_svsp0.5_amount0.05/xor_depression_0.5_0.05_cat2.jpg)

<a name="ex6"> <h2>Пример №6</h2> </a>

---

- #### Исходное изображение

    ![Original](original/screen2.png)

- #### Изображение с шумом и перцем

    ![](res/screen2.png_svsp0.5_amount0.09/with_salt_0.5_0.09_screen2.png)

### Задание №1

- #### Ядро в виде холма

    ![](res/screen2.png_svsp0.5_amount0.09/median_hill_0.5_0.09_screen2.png)

- #### Ядро в виде впадины

    ![](res/screen2.png_svsp0.5_amount0.09/median_depression_0.5_0.09_screen2.png)

### Задание №2

- #### Разностное изображение

    ![](res/screen2.png_svsp0.5_amount0.09/xor_hill_depression_0.5_0.09_screen2.png)

<a name="ex7"> <h2>Пример №7</h2> </a>

---

- #### Исходное изображение

    ![Original](original/spiral1.png)

- #### Изображение с шумом и перцем

    ![](res/spiral1.png_svsp0.5_amount0.1/with_salt_0.5_0.1_spiral1.png)

### Задание №1

- #### Ядро в виде холма

    ![](res/spiral1.png_svsp0.5_amount0.1/median_hill_0.5_0.1_spiral1.png)

- #### Ядро в виде впадины

    ![](res/spiral1.png_svsp0.5_amount0.1/median_depression_0.5_0.1_spiral1.png)

### Задание №2

- #### Разностное изображение

    ![](res/spiral1.png_svsp0.5_amount0.1/xor_hill_depression_0.5_0.1_spiral1.png)

<a name="ex8"> <h2>Пример №8</h2> </a>

---

- #### Исходное изображение

    ![Original](original/text1.jpg)

- #### Изображение с шумом и перцем

    ![](res/text1.jpg_svsp0.5_amount0.1/with_salt_0.5_0.1_text1.jpg)

### Задание №1

- #### Ядро в виде холма

    ![](res/text1.jpg_svsp0.5_amount0.1/median_hill_0.5_0.1_text1.jpg)

- #### Ядро в виде впадины

    ![](res/text1.jpg_svsp0.5_amount0.1/median_depression_0.5_0.1_text1.jpg)

### Задание №2

- #### Разностное изображение

    ![](res/text1.jpg_svsp0.5_amount0.1/xor_hill_depression_0.5_0.1_text1.jpg)

<a name="ex9"> <h2>Пример №9</h2> </a>

---

- #### Исходное изображение

    ![Original](original/pixel_art.jpg)

- #### Изображение с шумом и перцем

    ![](res/pixel_art.jpg_svsp0.5_amount0.05/with_salt_0.5_0.05_pixel_art.jpg)

### Задание №1

- #### Ядро в виде холма

    ![](res/pixel_art.jpg_svsp0.5_amount0.05/median_hill_0.5_0.05_pixel_art.jpg)

- #### Ядро в виде впадины

    ![](res/pixel_art.jpg_svsp0.5_amount0.05/median_depression_0.5_0.05_pixel_art.jpg)

### Задание №2

- #### Разностное изображение

    ![](res/pixel_art.jpg_svsp0.5_amount0.05/xor_hill_depression_0.5_0.05_pixel_art.jpg)
