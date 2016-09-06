from peewee import *

db_user = input("Please enter your database username:\n")
db = PostgresqlDatabase('story_manager', user=db_user)

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
db.create_table(Story,safe=True)