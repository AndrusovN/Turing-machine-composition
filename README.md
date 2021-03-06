# Turing-machine-composition
Это скрипт на python, созданный для композиции двух машин Тьюринга, созданных в симуляторе машины Тьюринга К. Полякова.
Если у вас есть две программы МТ, которые вы хотите выполнить последовательно, то данный скрипт позволит создать новую программу машины Тьюринга, 
которая последовательно выполняет данные две.

Чтобы использовать эту программу, необходимо, чтобы на компьютере был установлен python 3.x, и, если вы работаете на Windows, то python должен быть добавлен в PATH.

[Скачать Python](https://www.python.org/downloads/)

Сначала скачайте  исходный код программы с github (здесь должна быть кнопка `download zip`)

Если вы работаете на windows, то попробуйте такие три метода запуска программы:
  1. Двойной клик по файлу `main.py`
  2. Правой кнопкой мыши по `main.py` -> `открыть с помощью` -> `Python.exe`
  3. Открыть командную строку, перейти в директорию, куда скачан `main.py`, выполнить команду `py main.py` или `python main.py`

Если же вы работаете на Ubuntu/MacOS, откройте терминал, перейдите в директорию, в которой сохранен `main.py` и выполните команду `python main.py`

Если ни один из методов не сработал, скорее всего, у вас не установлен python на компьютере.

Если же вам удалось запустить программу, прочтите инструкцию далее, чтобы объединить программы машины тьюринга:

Сначала вам надо убедиться, что вторая программа машины Тьюринга готова запускаться ровно на выходе первой программы 
(ничто не будет очищено, головка машины Тьюринга никуда не будет сдвинута).

Затем экспортируйте обе программы машины Тьюринга в `.txt` файлы, как показано на рисунке.
![Turing machine export](https://downloader.disk.yandex.ru/preview/ea6cc5990b0b4adb61f66cf1fc7c32380ee524e28f877ef0887561fc57943e87/60ba3059/Y0DAdtvSCm3w5Yfw9-eW2Q-CY4ZElHI046jitHQ-WK6YDowtGgMhACfcsWvPrIqczHIrnKLSjjGhrXzzZ0m8Ng%3D%3D?uid=0&filename=2021-06-04_12-49-56%20%282%29.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)
Программа попросит вас ввести пути к файлам программ МТ - введите пути к экспортированным `.txt` файлам.

По итогу работы программы будет сохранен `.txt` файл, который можно импортировать (см. рис.)
![Turing machine import](https://downloader.disk.yandex.ru/preview/4efae2a4f2f7e46d85f7cdf8ec363cea3c1a7f91bccf4e7afedf865474c3d5db/60ba37ee/J9N-7bKZEhgC_JeZ0thIweDIAXmAlOgVbPFQ3rPzPv-t3fLTVOx1e0xjflvookSuJDhoYoVteLn6FeFfAXJmwQ%3D%3D?uid=0&filename=2021-06-04_13-25-15.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)

После импорта программы МТ не забудьте ее сохранить в отдельный `.tur` файл.

По всем дополнительным вопросам пишите в телеграм или ВК @n_andrusov
