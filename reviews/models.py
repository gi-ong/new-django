from django.db import models
from core import models as core_models


class Review(core_models.TimeStampedModel):

    """Review Model Definition"""

    review = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="user", on_delete=models.CASCADE
    )
    writing = models.ForeignKey(
        "writings.Writing", related_name="writing", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.review} - {self.writing}"
