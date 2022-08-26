# Проект YaCut

Это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Skrapivn/yacut.git
```

Cоздать и активировать виртуальное окружение:

```python
python -m venv venv
```

```python
 . venv/Scripts/activate
```

Обновить версию ```pip``` и установить зависимости из ```requirements.txt```:


```python
python -m pip install --upgrade pip
```

```python
pip install -r requirements.txt
```

Необходимо изменить ключи, при необходимости, в файле .env.example и переименовать файл в .env:

```
FLASK_APP=opinions_app
FLASK_ENV=development #  or production
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=you_secret_key # можно использовать в settings.py - os.urandom(20).hex() для случайного ключа
```

Используем функцию создания таблиц в БД:

```python
flask create_db  
```

Запустить проект:

```python
flask run
```

Также в проекте есть API, все endpoints можно посмотреть командой:

```python
flask routes
```

Документацию по API можно посмотреть в файле **openapi.yml**.

Для удобной работы с документом воспользуйтесь онлайн-редактором Swagger Editor <https://editor.swagger.io/>, в котором можно визуализировать спецификацию.

[Sergey K.](https://github.com/skrapivn/)
