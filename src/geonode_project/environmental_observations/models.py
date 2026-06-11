from django.db import models


class EnvironmentalObservation(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=80, db_index=True)
    observer_name = models.CharField(max_length=255)
    observer_email = models.EmailField()
    description = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    observed_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-observed_at", "title"]

    def __str__(self):
        return self.title

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "category": self.category,
            "observerName": self.observer_name,
            "observerEmail": self.observer_email,
            "description": self.description,
            "latitude": str(self.latitude),
            "longitude": str(self.longitude),
            "observedAt": self.observed_at.isoformat(),
        }
