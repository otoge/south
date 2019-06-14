from django.db import models

# Create your models here.


class Season(models.Model):

    season = models.CharField(
        verbose_name='シーズン',
        max_length=200,
    )


class Title(models.Model):

    season = models.ForeignKey(Season, on_delete=models.CASCADE)

    title = models.CharField(
        verbose_name='タイトル',
        max_length=200,
    )


class Item(models.Model):

    title = models.ForeignKey(Title, on_delete=models.CASCADE)

    progress = models.IntegerField(
        verbose_name='進行度',
        blank=True,
        null=True,
    )

    speaker = models.CharField(
        verbose_name='発話者',
        max_length=200,
    )

    script = models.TextField(
        verbose_name='セリフ',
        max_length=1000,
        blank=True,
        null=True,
    )
