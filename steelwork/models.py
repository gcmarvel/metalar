from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=500, verbose_name='Название')
    short_title = models.CharField(max_length=100, verbose_name='Короткое название')
    main_image = models.ImageField(null=True, verbose_name='Титульное изображение')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    active = models.BooleanField(verbose_name='Активно', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class ServiceImage(models.Model):
    image = models.ImageField(null=True, verbose_name='Изображение')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='images', verbose_name='Услуга')

    def __str__(self):
        return self.service.title

    class Meta:
        verbose_name = "Изображение услуги"
        verbose_name_plural = "Изображения услуги"
