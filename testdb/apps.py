from django.apps import AppConfig
from django.db import models

class TestdbConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'testdb'

