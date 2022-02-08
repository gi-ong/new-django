from django.db import models
from core import models as core_models


class Category(core_models.TimeStampedModel):
    """Category Model Definition"""

    KIND_FREE = "free"
    KIND_MEMBER = "member"
    KIND_HUMOR = "humor"
    KIND_STUDY = "study"
    KIND_NOTICE = "notice"
    KIND_QA = "Q&A"

    KIND_CHOICES = (
        (KIND_FREE, "Free"),
        (KIND_MEMBER, "Member"),
        (KIND_HUMOR, "Humor"),
        (KIND_STUDY, "Study"),
        (KIND_NOTICE, "Notice"),
        (KIND_QA, "Q&A"),
    )
    name = models.CharField(max_length=20)
    kind = models.CharField(max_length=10, choices=KIND_CHOICES)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"
