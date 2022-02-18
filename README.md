# PhysicsM1
Инструкция по использованию
---
# parse_file.py
1) Установить необходимую конфигурацию:
```
2 L = [0.35, 0.3, 0.25, 0.2]  # Длина веревки в метрах 
3 filename = 'myfile.txt'  # Путь к текстовому файлу с измерениями
```
Структура файла с измерениями:
* Результаты экспериментов (1-4) записываются по принципу "каждый - на новой строке"
* Эксперименты отделяются ЛЮБОЙ НЕ ЦИФРОЙ

###### Пример
```
1.5
2,8
A
1.55
A
1,43
A
12
15.8
15.5
```

2) Запустить **parse_file.py**<br>
Результатом работы **parse_file.py** является файл **data.json**

---
# M1-plots.ipynb
Конфигурация:
~~~
PLOTNAME = "Experiment#"  # Название графикова, в данном случае: Experiment#1, Experiment#2, Experiment#3, Experiment#4
DIR = 'F:\Data\Kurs_1\sem2\physicsLABS\M1\plots' # Путь к директории,  в которую необходимо сохранить графики
JSON_PATH = 'F:\\Data\\Kurs_1\\sem2\\physicsLABS\M1\\data.json'  # Путь к файлу, выданному 1й программой (data.json)
DPI = 1200  # разрешение графика в формате .svg
~~~
Результатом работы **M1-plots.ipynb** является  графики в форматах PNG, SVG, расположенные в директории, указанной в переменной *DIR*
