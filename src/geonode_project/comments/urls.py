from django.urls import path

from . import views

app_name = "comments"

urlpatterns = [
    path("", views.comment_list, name="comment-list"),
    path("api/", views.comment_list_api, name="comment-list-api"),
    path("api/<int:pk>/", views.comment_detail_api, name="comment-detail-api"),
]
