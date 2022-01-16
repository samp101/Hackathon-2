import os


file_path = os.path.dirname(__file__)


class Config:

    SECRET_KEY = 'Youll-never-geuss'
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{file_path}/organizer.db'
