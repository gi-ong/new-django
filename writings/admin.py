from django.contrib import admin
from . import models


@admin.register(models.Writing)
class WritingAdmin(admin.ModelAdmin):

    """Writing Admin Definition"""

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Photo Admin Definition"""

    pass
