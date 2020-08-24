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
    test = models.ForeignKey(
        "home.CustomText",
        on_delete=models.SET_DEFAULT,
        default=1,
        null=True,
        blank=True,
        related_name="customtext_test",
    )
    key2 = models.ForeignKey(
        "home.CustomText",
        on_delete=models.SET_DEFAULT,
        default=1,
        null=True,
        blank=True,
        related_name="customtext_key2",
    )
    key1 = models.ForeignKey(
        "home.CustomText",
        on_delete=models.SET_DEFAULT,
        default=2,
        null=True,
        blank=True,
        related_name="customtext_key1",
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
    key1 = models.ForeignKey(
        "users.User",
        on_delete=models.SET_DEFAULT,
        default=1,
        null=True,
        blank=True,
        related_name="homepage_key1",
    )
    key2 = models.ForeignKey(
        "home.CustomText",
        on_delete=models.SET_DEFAULT,
        default=2,
        null=True,
        blank=True,
        related_name="homepage_key2",
    )
    key3 = models.OneToOneField(
        "users.User",
        on_delete=models.SET_DEFAULT,
        default=1,
        null=True,
        blank=True,
        related_name="homepage_key3",
    )
    key4 = models.OneToOneField(
        "users.User",
        on_delete=models.SET_DEFAULT,
        default=4,
        null=True,
        blank=True,
        related_name="homepage_key4",
    )

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"
