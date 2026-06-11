from django.db import models


class Comment(models.Model):
    post_id = models.PositiveIntegerField(db_index=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["post_id", "id"]

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            "id": self.id,
            "postId": self.post_id,
            "name": self.name,
            "email": self.email,
            "body": self.body,
        }
