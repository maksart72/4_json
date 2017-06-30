# Prettify JSON

Задача состоит в том, чтобы написать скрипт, который на вход принимает путь до файла, в котором хранится json и выводит его содержимое в консоль в удобном для чтения виде. 

Описание.

Путь до файла с содержимым JSON получаем через переменную filepath и функцию sys.argv
Функция load_data(filepath) - загружает содержимое файла
Функция pretty_print_json(data) - преобразует данные с помощью функции json.dumps в удобный вид
Результат преобразования выводится в консоль через print 

# Quickstart

Example of script launch on Linux, Python 3.5:

```#!bash

$ python pprint_json.py <path to file>
# TODO add output example

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
