from django.db import models
import mongoengine
# Create your models here.

class tianqi(mongoengine.Document):
    city = mongoengine.StringField(max_length=20)
    wendu = mongoengine.StringField(max_length=20)
    kqzl = mongoengine.StringField(max_length=20)
    shidu = mongoengine.StringField(max_length=20)
    fengxiang = mongoengine.StringField(max_length=20)
    zwx = mongoengine.StringField(max_length=20)
    tianqi = mongoengine.StringField(max_length=20)
    wencha = mongoengine.StringField(max_length=20)