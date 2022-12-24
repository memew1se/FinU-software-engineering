from django.db import models


class Project(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    start = models.DateTimeField(verbose_name="Дата начала", null=True, blank=True)
    end = models.DateTimeField(verbose_name="Дата окончания", null=True, blank=True)

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return self.title
