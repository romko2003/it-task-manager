from django.contrib.auth.models import AbstractUser
from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ("name",)

    def __str__(self) -> str:
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position,
        on_delete=models.PROTECT,
        related_name="workers",
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ("username",)

    def __str__(self) -> str:
        full = f"{self.first_name} {self.last_name}".strip()
        return full or self.username

