# Лабораторная работа №2

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

---

<a name="ex1"> <h2>Пример №1</h2> </a>

- #### Исходное изображение

    ![Original](original/cat.jpg)

- #### Изображение с шумом и перцем

    ![With Salt](with_salt/with_salt_0.5_0.05_cat.jpg)

### Задание

|**Эрозия (диск)**|**Разностное**|
|-----------------|--------------|
|![Eroded](res/cat.jpg_svsp0.5_amount0.05/median_hill_0.5_0.05_cat.jpg)|![Diff](res/cat.jpg_svsp0.5_amount0.05/xor_hill_depression_0.5_0.05_cat.jpg)|

---

<a name="ex2"> <h2>Пример №2</h2> </a>

- #### Исходное изображение

    ![Original](original/cat.jpg)

- #### Изображение с шумом и перцем

    ![With Salt](with_salt/with_salt_0.5_0.3_cat.jpg)

### Задание

|**Эрозия (диск)**|**Разностное**|
|-----------------|--------------|
|![Eroded](res/cat.jpg_svsp0.5_amount0.3/median_hill_0.5_0.3_cat.jpg)|![Diff](res/cat.jpg_svsp0.5_amount0.3/xor_hill_depression_0.5_0.3_cat.jpg)|

---

<a name="ex3"> <h2>Пример №3</h2> </a>

- #### Исходное изображение

    ![Original](original/cat_invert.jpg)

- #### Изображение с шумом и перцем

    ![With Salt](with_salt/with_salt_0.5_0.05_cat_invert.jpg)

### Задание

|**Эрозия (диск)**|**Разностное**|
|-----------------|--------------|
|![Eroded](res/cat_invert.jpg_svsp0.5_amount0.05/median_hill_0.5_0.05_cat_invert.jpg)|![Diff](res/cat_invert.jpg_svsp0.5_amount0.05/xor_hill_depression_0.5_0.05_cat_invert.jpg)|

---

<a name="ex4"> <h2>Пример №4</h2> </a>

- #### Исходное изображение

    ![Original](original/cat_invert.jpg)

- #### Изображение с шумом и перцем

    ![With Salt](with_salt/with_salt_0.5_0.3_cat_invert.jpg)

### Задание

|**Эрозия (диск)**|**Разностное**|
|-----------------|--------------|
|![Eroded](res/cat_invert.jpg_svsp0.5_amount0.3/median_hill_0.5_0.3_cat_invert.jpg)|![Diff](res/cat_invert.jpg_svsp0.5_amount0.3/xor_hill_depression_0.5_0.3_cat_invert.jpg)|

---

<a name="ex5"> <h2>Пример №5</h2> </a>

- #### Исходное изображение

    ![Original](original/cat2.jpg)

- #### Изображение с шумом и перцем

    ![With Salt](with_salt/with_salt_0.5_0.05_cat2.jpg)

### Задание

|**Эрозия (диск)**|**Разностное**|
|-----------------|--------------|
|![Eroded](res/cat2.jpg_svsp0.5_amount0.05/median_hill_0.5_0.05_cat2.jpg)|![Diff](res/cat2.jpg_svsp0.5_amount0.05/xor_hill_depression_0.5_0.05_cat2.jpg)|

---

<a name="ex6"> <h2>Пример №6</h2> </a>

- #### Исходное изображение

    ![Original](original/screen2.png)

- #### Изображение с шумом и перцем

    ![With Salt](with_salt/with_salt_0.5_0.09_screen2.png)

### Задание

|**Эрозия (диск)**|**Разностное**|
|-----------------|--------------|
|![Eroded](res/screen2.png_svsp0.5_amount0.09/median_hill_0.5_0.09_screen2.png)|![Diff](res/screen2.png_svsp0.5_amount0.09/xor_hill_depression_0.5_0.09_screen2.png)|

---

<a name="ex7"> <h2>Пример №7</h2> </a>

- #### Исходное изображение

    ![Original](original/spiral1.png)

- #### Изображение с шумом и перцем

    ![With Salt](with_salt/with_salt_0.5_0.1_spiral1.png)

### Задание

|**Эрозия (диск)**|**Разностное**|
|-----------------|--------------|
|![Eroded](res/spiral1.png_svsp0.5_amount0.1/median_hill_0.5_0.1_spiral1.png)|![Diff](res/spiral1.png_svsp0.5_amount0.1/xor_hill_depression_0.5_0.1_spiral1.png)|

---

<a name="ex8"> <h2>Пример №8</h2> </a>

- #### Исходное изображение

    ![Original](original/text1.jpg)

- #### Изображение с шумом и перцем

    ![With Salt](with_salt/with_salt_0.5_0.1_text1.jpg)

### Задание

|**Эрозия (диск)**|**Разностное**|
|-----------------|--------------|
|![Eroded](res/text1.jpg_svsp0.5_amount0.1/median_hill_0.5_0.1_text1.jpg)|![Diff](res/text1.jpg_svsp0.5_amount0.1/xor_hill_depression_0.5_0.1_text1.jpg)|

---

<a name="ex9"> <h2>Пример №9</h2> </a>

- #### Исходное изображение

    ![Original](original/pixel_art.jpg)

- #### Изображение с шумом и перцем

    ![With Salt](with_salt/with_salt_0.5_0.05_pixel_art.jpg)

### Задание

|**Эрозия (диск)**|**Разностное**|
|-----------------|--------------|
|![Eroded](res/pixel_art.jpg_svsp0.5_amount0.05/median_hill_0.5_0.05_pixel_art.jpg)|![Diff](res/pixel_art.jpg_svsp0.5_amount0.05/xor_hill_depression_0.5_0.05_pixel_art.jpg)|