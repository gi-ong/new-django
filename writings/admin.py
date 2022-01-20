from django.contrib import admin
from . import models


@admin.register(models.Writing)
class WritingAdmin(admin.ModelAdmin):

    """Custom Writing Admin"""
