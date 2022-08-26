import click

from . import app, db
import os


@app.cli.command('create_db')
def create_db_command():
    """Функция для создания таблиц БД
    и переименовывания файла .env"""
    db.create_all()
    click.echo('Таблицы в БД созданы')
    if os.path.exists("./.env.example"):
        os.rename("./.env.example", "./.env1")
        click.echo('Файл .env.example переименован в .env')
    else:
        click.echo('Файл .env.example не существует или уже переименован')