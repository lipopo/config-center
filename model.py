from peewee import MySQLDatabase, \
        Model, CharField, TextField, \
        SqliteDatabase

from config import config


db_url = config.get("database")
if db_url.startswith("sqlite://"):
    database = SqliteDatabase(db_url[9:])
else:
    database = MySQLDatabase(db_url)


class BaseModel(Model):
    class Meta:
        database = database


class Config(BaseModel):
    config_name = CharField(
       column_name="cnm", max_length=100, primary_key=True)
    config_type = CharField(column_name="ctp", max_length=100)
    config_value = TextField(column_name="cve")
