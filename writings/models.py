from django.db import models
from core import models as core_models


class Photo(core_models.TimeStampedModel):

    """Photo Model Definition"""

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    writing = models.ForeignKey("Writing", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Writing(core_models.TimeStampedModel):

    """Writing Model Definition"""

    title = models.CharField(max_length=100)
    text = models.TextField()
    category = models.ForeignKey("categories.Category", on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
