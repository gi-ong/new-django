from django.contrib import admin
from . import models


@admin.register(models.Writing)
class WritingAdmin(admin.ModelAdmin):

    """Writing Admin Definition"""

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("title", "text", "category", "author")},
        ),
        (
            "Likes",
            {"fields": ("likes",)},
        ),
    )

    list_display = (
        "title",
        "category",
        "author",
        "count_likes",
    )

    ordering = ("title", "category", "author")

    list_filter = ("category", "author__gender")

    search_fields = ("=category__name", "^author__username")

    filter_horizontal = ("likes",)

    def count_likes(self, obj):
        return obj.likes.count()

    count_likes.short_description = "likes count"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Photo Admin Definition"""

    pass
