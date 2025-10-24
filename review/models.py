from django.db import models

# Create your models here.
class Reviews(models.Model):
    name = models.CharField("Имя клиента",max_length=100)
    count_stars = models.CharField("Количество звёзд",        choices=[
            ("★", "★"),
            ("★ ★", "★★"),
            ("★ ★ ★", "★★★"),
            ("★ ★ ★ ★", "★★★★"),
            ("★ ★ ★ ★ ★", "★★★★★"),
        ],default=5,max_length=15)
    image = models.ImageField("Фото товара", upload_to="media/img/rewiew/")
    text = models.TextField("Текст отзыва",blank=True, null=True)
    date = models.DateField("Дата написания отзыва",
        default="31.12.2021"
    )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

