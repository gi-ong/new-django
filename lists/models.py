from django.db import models
from core import models as core_models


class List(core_models.TimeStampedModel):

    """List Model Definition"""

    name = models.CharField(max_length=80)
    user = models.ForeignKey(
        "users.User", related_name="user", on_delete=models.CASCADE
    )
    writings = models.ManyToManyField(
        "writings.Writing", related_name="writings", blank=True
    )

    def __str__(self):
        return self.name
