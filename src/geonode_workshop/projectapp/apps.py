from django.apps import AppConfig


class ProjectappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'geonode_workshop.projectapp'

default_app_config = 'geonode_workshop.projectapp.AppConfig'