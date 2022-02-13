from django.db import models
from django.urls import reverse


class Review(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    content = models.TextField(max_length=1000, verbose_name="Контент")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Фото")
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    views = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ["-created_at"]

    def get_absolute_url(self):
        return reverse('DetailReview', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name="Имя услуги")

    def __str__(self):
        return self.title