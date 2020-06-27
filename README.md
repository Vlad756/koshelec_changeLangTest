# koshelec_changeLangTest
Test for switching languages

Для запуска теста необходимо в командной строке (или аналог) перейти в каталог с файлами (вместо перехода в необходимый каталог можно указать путь к файлу) и запустить его с помощью написания одной из следующих строк:
   1) python -m unittest main.ChangeLang.test_German (Запуск отдельного метода)
   2) python -m unittest main (Запуск модуля с тестами)
   3) python -m unittest -v main (С помощью флага -v можно получить более детальный отчёт)
   4) python main.py

Доступные методы класса теста: test_German, test_English, test_Spanish, test_Filipino, test_French, test_Arab, test_Italian, test_Japan, test_Korean, test_Portuguese, test_Russian, test_Turkish, test_Vietnamese, test_China1, test_China2.

В коде присутствуют разъяснительные комментарии в функции test_German. Функции одинаковы по своей структуре. Различия только элементах.
