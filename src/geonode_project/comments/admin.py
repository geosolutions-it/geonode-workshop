from django.contrib import admin

from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "post_id", "name", "email")
    list_filter = ("post_id",)
    search_fields = ("name", "email", "body")
