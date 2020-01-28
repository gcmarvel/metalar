from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=500, verbose_name='Название', default='Новая услуга')
    image = models.ImageField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

