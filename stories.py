import peewee
import psycopg2
from peewee import *
import os.path
import os

def connect_data():
    try:
        filename = os.path.join(os.path.dirname(__file__), 'user.txt')
        with open(filename) as f:
            data = f.read()
            return data.strip("\n")
    except FileNotFoundError:
        print("""Please create a "user.txt" file before starting the application(see:readme.md)""")
        quit()
try:
    db_user = connect_data()
    db = PostgresqlDatabase('story_manager', user=db_user)
except psycopg2.OperationalError:
    print("jj")

class BaseModel(Model):
    """A base model that will use our Postgresql database"""

    class Meta():
        database = db

class Story(BaseModel):
    story_title = CharField()
    user_story = CharField()
    acceptance_criteria = CharField()
    business_value = IntegerField()
    estimation = FloatField()
    status = CharField()

db.connect()
db.create_table(Story, safe=True)