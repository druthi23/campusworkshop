"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaagg67avj5o48sep4g-a.oregon-postgres.render.com",
        database="todo_1j7o",
        user="todo_1j7o_user",
        password="jRknUYHntZIOPJHPnU89ALMHQWUVOagB")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
