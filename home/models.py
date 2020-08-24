from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)
    tests = models.OneToOneField(
        "home.CustomText",
        on_delete=models.SET_DEFAULT,
        default=1,
        null=True,
        blank=True,
        related_name="customtext_tests",
    )
    user = models.OneToOneField(
        "home.CustomText",
        on_delete=models.SET_DEFAULT,
        default=2,
        null=True,
        blank=True,
        related_name="customtext_user",
    )
    new = models.OneToOneField(
        "home.CustomText",
        on_delete=models.SET_DEFAULT,
        default=1,
        null=True,
        blank=True,
        related_name="customtext_new",
    )

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"
