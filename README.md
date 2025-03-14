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

---

<a name="ex1"> <h2>Пример №1</h2> </a>

- #### Исходное изображение

    ![Original](original/cat.jpg)

- #### Изображение с шумом и перцем

    ![With Salt](with_salt/with_salt_0.5_0.05_cat.jpg)

### Задание

|**С шумом**|**Эрозия**|**Разностное**|
|-----------|----------|--------------|
|![With Salt](with_salt/with_salt_0.5_0.05_cat.jpg)|![Eroded](results/eroded/with_salt_0.5_0.05_cat_eroded.jpg)|![Diff](results/diff/with_salt_0.5_0.05_cat_diff.jpg)|

---

<a name="ex2"> <h2>Пример №2</h2> </a>

- #### Исходное изображение

    ![Original](original/cat.jpg)

- #### Изображение с шумом и перцем

    ![With Salt](with_salt/with_salt_0.5_0.3_cat.jpg)

### Задание

|**С шумом**|**Эрозия**|**Разностное**|
|-----------|----------|--------------|
|![With Salt](with_salt/with_salt_0.5_0.3_cat.jpg)|![Eroded](results/eroded/with_salt_0.5_0.3_cat_eroded.jpg)|![Diff](results/diff/with_salt_0.5_0.3_cat_diff.jpg)|

---

<a name="ex3"> <h2>Пример №3</h2> </a>

- #### Исходное изображение

    ![Original](original/cat_invert.jpg)

- #### Изображение с шумом и перцем

    ![With Salt](with_salt/with_salt_0.5_0.05_cat_invert.jpg)

### Задание

|**С шумом**|**Эрозия**|**Разностное**|
|-----------|----------|--------------|
|![With Salt](with_salt/with_salt_0.5_0.05_cat_invert.jpg)|![Eroded](results/eroded/with_salt_0.5_0.05_cat_invert_eroded.jpg)|![Diff](results/diff/with_salt_0.5_0.05_cat_invert_diff.jpg)|

---

<a name="ex4"> <h2>Пример №4</h2> </a>

- #### Исходное изображение

    ![Original](original/cat_invert.jpg)

- #### Изображение с шумом и перцем

    ![With Salt](with_salt/with_salt_0.5_0.3_cat_invert.jpg)

### Задание

|**С шумом**|**Эрозия**|**Разностное**|
|-----------|----------|--------------|
|![With Salt](with_salt/with_salt_0.5_0.3_cat_invert.jpg)|![Eroded](results/eroded/with_salt_0.5_0.3_cat_invert_eroded.jpg)|![Diff](results/diff/with_salt_0.5_0.3_cat_invert_diff.jpg)|

---

<a name="ex5"> <h2>Пример №5</h2> </a>

- #### Исходное изображение

    ![Original](original/cat2.jpg)

- #### Изображение с шумом и перцем

    ![With Salt](with_salt/with_salt_0.5_0.05_cat2.jpg)

### Задание

|**С шумом**|**Эрозия**|**Разностное**|
|-----------|----------|--------------|
|![With Salt](with_salt/with_salt_0.5_0.05_cat2.jpg)|![Eroded](results/eroded/with_salt_0.5_0.05_cat2_eroded.jpg)|![Diff](results/diff/with_salt_0.5_0.05_cat2_diff.jpg)|

---

<a name="ex6"> <h2>Пример №6</h2> </a>

- #### Исходное изображение

    ![Original](original/screen2.png)

- #### Изображение с шумом и перцем

    ![With Salt](with_salt/with_salt_0.5_0.09_screen2.png)

### Задание

|**С шумом**|**Эрозия**|**Разностное**|
|-----------|----------|--------------|
|![With Salt](with_salt/with_salt_0.5_0.09_screen2.png)|![Eroded](results/eroded/with_salt_0.5_0.09_screen2_eroded.jpg)|![Diff](results/diff/with_salt_0.5_0.09_screen2_diff.jpg)|

---

<a name="ex7"> <h2>Пример №7</h2> </a>

- #### Исходное изображение

    ![Original](original/spiral1.png)

- #### Изображение с шумом и перцем

    ![With Salt](with_salt/with_salt_0.5_0.1_spiral1.png)

### Задание

|**С шумом**|**Эрозия**|**Разностное**|
|-----------|----------|--------------|
|![With Salt](with_salt/with_salt_0.5_0.1_spiral1.png)|![Eroded](results/eroded/with_salt_0.5_0.1_spiral1_eroded.jpg)|![Diff](results/diff/with_salt_0.5_0.1_spiral1_diff.jpg)|

---

<a name="ex8"> <h2>Пример №8</h2> </a>

- #### Исходное изображение

    ![Original](original/text1.jpg)

- #### Изображение с шумом и перцем

    ![With Salt](with_salt/with_salt_0.5_0.1_text1.jpg)

### Задание

|**С шумом**|**Эрозия**|**Разностное**|
|-----------|----------|--------------|
|![With Salt](with_salt/with_salt_0.5_0.1_text1.jpg)|![Eroded](results/eroded/with_salt_0.5_0.1_text1_eroded.jpg)|![Diff](results/diff/with_salt_0.5_0.1_text1_diff.jpg)|

---

<a name="ex9"> <h2>Пример №9</h2> </a>

- #### Исходное изображение

    ![Original](original/pixel_art.jpg)

- #### Изображение с шумом и перцем

    ![With Salt](with_salt/with_salt_0.5_0.05_pixel_art.jpg)

### Задание

|**С шумом**|**Эрозия**|**Разностное**|
|-----------|----------|--------------|
|![With Salt](with_salt/with_salt_0.5_0.05_pixel_art.jpg)|![Eroded](results/eroded/with_salt_0.5_0.05_pixel_art_eroded.jpg)|![Diff](results/diff/with_salt_0.5_0.05_pixel_art_diff.jpg)|