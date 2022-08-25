import click

from . import app, db
# import os


@app.cli.command('create_db')
def create_db_command():
    """Функция для создания таблиц БД"""
    db.create_all()
    click.echo('Таблицы в БД созданы')
    # os.rename("./.env.example", "./.env")