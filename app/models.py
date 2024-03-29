from django.db import models
from django.conf import settings

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

    url = models.URLField(
        verbose_name='URL',
        max_length=200,
        default="",
    )

    @property
    def season_is(self):
        return self.season.season




class Item(models.Model):

    title = models.ForeignKey(Title, on_delete=models.CASCADE, blank=True, null=True)

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

    @property
    def title_is(self):
        return self.title.title


class User(models.Model):
    name = models.CharField(max_length=128)
    scripts = models.ManyToManyField(Item)

    def __str__(self):
        return self.name


class Profile(models.Model):
    name = models.CharField("名前", max_length=255)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    scripts = models.ManyToManyField(Item, blank=True, through='Quote')

    def __str__(self):
        return self.name

    def my_function(self):
        # Return some calculated value based on the entry
        my_value = "korede"
        return my_value


class Post(models.Model):
    title = models.CharField('タイトル', max_length=255)

    def __str__(self):
        return self.title


class Quote(models.Model):
        script = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True)
        owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
        date_joined = models.DateField(auto_now_add=True)

        def get_script(self):
            script = self.script.script
            return script

        def get_speaker(self):
            speaker = self.script.speaker
            return speaker

        def get_id(self):
            i_id = self.script.pk
            return i_id



