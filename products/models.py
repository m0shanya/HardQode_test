from django.db import models
from django.conf import settings


class Product(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='ProductOwner',
        verbose_name="ProductOwner"
    )

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField(null=False, blank=True)
    duration = models.IntegerField(null=False, blank=True)

    def __str__(self):
        return self.name


class Status(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="UserStatus",
        verbose_name="UserStatus"
    )
    lesson = models.ForeignKey(
        Lesson,
        related_name="LessonStatus",
        verbose_name="LessonStatus",
        on_delete=models.CASCADE
    )
    time = models.IntegerField(null=False, blank=True)
    status = models.BooleanField(default=0)
    date = models.DateField(auto_now=True)


class Belonging(models.Model):
    lesson = models.ForeignKey(
        Lesson,
        related_name="LessonBelong",
        verbose_name="LessonBelong",
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        related_name="ProductBelong",
        verbose_name="ProductBelong",
        on_delete=models.CASCADE
    )


class Access(models.Model):
    product = models.ForeignKey(
        Product,
        related_name="ProdAccess",
        verbose_name="ProdAccess",
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='UserAccess',
        verbose_name="UserAccess"
    )
