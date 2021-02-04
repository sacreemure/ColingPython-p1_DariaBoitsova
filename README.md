## Задание 1:

Реализуйте класс ```python OneIndexedList```, который имитирует поведение списка, использующего индексацию начинающуюся с 1 (а не с 0, как в стандартном списке). Используйте магические методы init, setattr, getattr

```python
a = OneIndexedList([1,2,3])
a[1]
>>> 1
```

NB!: 
При инициализации класса без аргумента 
```python
OneIndexedList()
```
класс должен использовать пустой список по умолчанию, поддерживающий такую индексацию

Подсказка:
[] or items

Пример:

```python
a = OneIndexedList()
a.items.append(0)
a[1]

>>> 0
```

Потестируйте на случайных списках, не берите ==[1,2,3,4]==


Задание 2:

Вам необходимо написать скрипт, в котором реализован класс ==FileReader()==

Конструктор этого класса принимает один параметр: путь до файла на диске. 

В классе ```python FileReader()``` должен быть реализован метод ```python read()```, возвращающий строку - содержимое файла, путь к которому был указан при создании экземпляра класса, а так же метод write, который записывает некоторое содержимое в файл. 

Python модуль должен быть написан таким образом, чтобы импорт класса ```python FileReader()``` из него не вызвал ошибок. Например, при написании реализации метода read, вам нужно учитывать случай, когда при инициализации был передан путь к несуществующему файлу. Требуется обработать возникающее при этом исключение ==FileNotFoundError== и вернуть из метода read пустую строку.

Также в классе должен реализован метод count, который возвращает количество строк и слов в файле (для токенизации используйте NLTK), а также записывает информацию в соответствующие атрибуты ```python line_count``` и ```python word_count```.

Кроме того в классе необходимо переопределять следующие магические методы:
a) ```python __add__()```: склеивает содержимое двух файлов, записывает в текущую директорию, возвращает объект класса FileReader
b) ```python __str__()```: выводит путь до файла (или же использовать ```python __repr__()```)

Базовый пример:
```python
>>> from solution import FileReader
>>> reader = FileReader('not_exist_file.txt')
>>> text = reader.read()
>>> text
''
>>> with open('some_file.txt', 'w') as file:
...     file.write('some text')
...
9
>>> reader = FileReader('some_file.txt')
>>> text = reader.read()
>>> text
'some text'
>>> type(reader)
<class 'solution.FileReader'>
```


Задание 3:

В этом задании вам необходимо реализовать свой униграммный морфологический анализатор. В классе UnigramMorphAnalyzer должны быть реализованы следующие методы:

 a) train: считывает слова из размеченного корпуса и накапливает частеречную статистику в соответствии с  окончаниями слов (4, 3, 2, 1 последних символа)

Частеречная статистика по окончаниям должна иметь следующий вид:
{
     "end_1": 
          {"pos_1": "count", 
           "pos_2": "count"},
     "end_2": 
          {"pos_1": "count", 
           "pos_2": "count"},
 }
Назвать словарь можно endings_stat
 b) predict: выводит список вероятностей различных частей речи для данного токена 
 
 c) save: сохраняет модель с помощью библиотеки pickle

 d) load: загружает модель
 
 e) При вызове  UnigramMorphAnalyzer[‘ending’] должна выводиться частеречная статистика по указанному окончанию
 
 f) eval: должна выводить точность анализатора на тестовых данных open corpora (для загрузки датасета используете библиотеку Corus https://nbviewer.jupyter.org/github/natasha/corus/blob/master/docs.ipynb#load_corpora)
(Разбейте заранее данные на train-test в пропорции 0.8 / 0.2 без перемешивания)



# !wget 'http://opencorpora.org/files/export/annot/annot.opcorpora.xml.byfile.zip'
# !pip install tqdm, corus

from corus import load_corpora
import tqdm

path = 'annot.opcorpora.xml.byfile.zip'
records = load_corpora(path)

with open('pos_data.txt', 'w', encoding='utf8') as f:
    for rec in tqdm.tqdm(records):
        for par in rec.pars:
            for sent in par.sents:
                for token in sent.tokens:
                    f.write(f'{token.text} {token.forms[0].grams[0]}\n')
