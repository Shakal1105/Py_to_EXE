# Py_to_EXE
Use Code in SHELL

` python pytoexe.py build `


Виправити на Windows
Зміни в keyboardпакеті pynput
Перейдіть до "\Lib\site-packages\pynput\keyboard".
Відкрийте файл « init .py».
На початку файлу додайте такий імпорт:from pynput.keyboard import _win32
Знайдіть рядок: backend = backend(__name__)і замініть його рядком:backend = _win32
Зміни в mouseпакеті pynput
Перейдіть до "\Lib\site-packages\pynput\mouse".
Відкрийте файл « init .py».
На початку файлу додайте такий імпорт:from pynput.mouse import _win32
Знайдіть рядок: backend = backend(__name__)і замініть його рядком:backend = _win32
