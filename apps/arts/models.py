from django.db import models

# ---------------------------------------------------------------------------------------
class ArtCoords(models.Model):
    long = models.FloatField(
        null=False,
        blank=False,
        verbose_name="Широта"
    )

    lant = models.FloatField(
        null=False,
        blank=False,
        verbose_name="Долгота"
    )

    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    class Meta:
        verbose_name = "Координаты художества"
        verbose_name_plural = "Координаты художества"


# ---------------------------------------------------------------------------------------
class Art(models.Model):
    
    ART_STATE = [
        ("BUF","Закрашенно"),
        ("NEW","В процессе"),
    ]

    is_archive = models.BooleanField(
        null=False,
        blank=False,
        default=False,
        verbose_name="Архивировано ли"
    )

    author = models.ForeignKey(
        "users.AppUser", 
        models.CASCADE, 
        null=False,
        blank=False, 
        verbose_name="Пользователь"
    )

    preview_image = models.ImageField(
        null=False,
        blank=False,
        upload_to="arts/preview/",
        verbose_name="Изображение превью"
    )

    state = models.CharField(
        null=True,
        blank=True,
        max_length=3,
        choices=ART_STATE,
        verbose_name="Состояния художества"
    )

    desc = models.TextField(
        null=True,
        blank=True,
        verbose_name="Описание"
    )

    coords = models.OneToOneField(
        ArtCoords, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Координаты"
    )

    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    class Meta:
        verbose_name = "Художество"
        verbose_name_plural = "Художества"


# ---------------------------------------------------------------------------------------
class ArtImage(models.Model):

    art = models.ForeignKey(
        Art, 
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="Художество"
    )

    image = models.ImageField(
        null=False,
        blank=False,
        upload_to="arts/preview/",
        verbose_name="Координаты"
    )

    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    
    class Meta:
        verbose_name = "Изображение художества"
        verbose_name_plural = "Изображения художеств"


# ---------------------------------------------------------------------------------------
class ArtComment(models.Model):

    art = models.ForeignKey(
        Art, 
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="Художество"
    )

    user = models.ForeignKey(
        "users.AppUser", 
        models.CASCADE, 
        null=False,
        blank=False, 
        verbose_name="Пользователь"
    )

    content = models.TextField(
        null=False,
        blank=False,
        verbose_name="Комментарий"
    )

    is_moderate = models.BooleanField(
        null=False,
        blank=False,
        verbose_name="Прошел ли модерацию"
    )

    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    
    class Meta:
        verbose_name = "Коментарий"
        verbose_name_plural = "Коментарии"