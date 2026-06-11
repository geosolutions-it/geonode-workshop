from django.urls import path

from . import views

app_name = "environmental_observations"

urlpatterns = [
    path("", views.observation_list, name="observation-list"),
    path("api/", views.observation_list_api, name="observation-list-api"),
    path("api/<int:pk>/", views.observation_detail_api, name="observation-detail-api"),
]
