from django.contrib import admin

from .models import EnvironmentalObservation


@admin.register(EnvironmentalObservation)
class EnvironmentalObservationAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "latitude", "longitude", "observed_at")
    list_filter = ("category", "observed_at")
    search_fields = ("title", "observer_name", "description")
