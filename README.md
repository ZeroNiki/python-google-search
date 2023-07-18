# Python google search (RU)
Библеотеки:
- iterfzf
- python-googlesearch 

Код выполняет поиск по запросу в терминале 

## Перед устоновкой 

Скачайте pyinstaller для того чтобы скомпилировать код в исходную программу


### Устоновка (GNU/Linux)

Скачайте репозиторий:

```bash
git clone https://github.com/ZeroNiki/python-google-search.git
cd python-google-search
```

Создайте виртуальное окружение(По желанию):

```bash
python3 -m venv venv && source venv/bin/activate
```

Устоновите зависимости:

```bash
pip install -r requirements.txt   
```

Запускаем:

```bash
python3 search.py
```

### Конфигурация
Скомпилируем файл:

```
pyinstaller --onefile search.py
```

переходим в деректорию dist/ и запускаем файл:
```bash
./search.py
```

### В случае возникновения ошибок 
Возможно будет вот такая ошибка:
[Error png](https://github.com/ZeroNiki/python-google-search/blob/main/content/error.png)

Просто перезапустите скрипт

----

# Python google search (EN)
Libraries:
- iterfzf
-python-googlesearch

The code does a search on demand in the terminal

## Before installation

Download pyinstaller to compile the code into source program


### Installation (GNU/Linux)

Download the repository:

```bash
git clone https://github.com/ZeroNiki/python-google-search.git
cd python-google-search
```

Create a virtual environment (Optional):

```bash
python3 -m venv venv && source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

We launch:

```bash
python3 search.py
```

### Configuration
Let's compile the file:

```
pyinstaller --onefilesearch.py
```

go to the dist/ directory and run the file:
```bash
./search.py
```

### In case of errors
Perhaps there will be an error like this:
[Error png](https://github.com/ZeroNiki/python-google-search/blob/main/content/error.png)

Just restart the script



