from django.db import models
from django.contrib.auth.models import AbstractUser


class AppUser(AbstractUser):
  
    profile_picture = models.ImageField(
        null=True,
        blank=True,
        upload_to="user_pics/",
        verbose_name="Изображение профиля"
    ) 

    desc = models.TextField(
        null=True,
        blank=True,
        verbose_name="Описание профиля"
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class UserLinks(models.Model):

    url = models.URLField(
        null=False,
        blank=False,
        verbose_name="Ссылка"
    )

    user = models.ForeignKey(
        AppUser, 
        on_delete=models.CASCADE, 
        null=False,
        blank=False,
        related_name="links", 
        verbose_name="Пользователь"
    )

    class Meta:
        verbose_name = "Ссылка"
        verbose_name_plural = "Ссыллки"