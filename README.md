### Пример файловой организационной структуры проекта

---

Краткая структура

project
├───.git
├───.idea
├───bin
├───data
│   ├───production
│   └───test
├───doc
├───log
├───src
│   ├───package1
│   └───package2
├───test
│   ├───package1
│   └───package2
└───venv
    ├───Lib
    └───Scripts

`bin` — исполняемые файлы

`data` — входные данные 

`doc` — документация

`log` — логи (выходные данные)

`src` — код

`test` — тесты компонентов

---

Развёрнутая структура

project
│   .gitignore
│   pyproject.toml
│   README.md
│
├───.git
│       HEAD
│       index
│       ...
│
├───.idea
│       project.iml
│       vcs.xml
│       workspace.xml
│       ...
│
├───bin
│
├───data
│   │   conf.json
│   │
│   ├───production
│   │
│   └───test
│
├───doc
│
├───log
│
├───src
│   │   main.py
│   │   __init__.py
│   │
│   ├───package1
│   │       module1.py
│   │       module2.py
│   │       __init__.py
│   │
│   └───package2
│           module3.py
│           module4.py
│           __init__.py
│
├───test
│   │   test_integration.py
│   │   __init__.py
│   │
│   ├───package1
│   │       test_module1.py
│   │       test_module2.py
│   │       __init__.py
│   │
│   └───package2
│           test_module3.py
│           test_module4.py
│           __init__.py
│
└───venv
    │   pyvenv.cfg
    │   ...
    │
    ├───Lib
    │       ...
    │
    └───Scripts
            ...


