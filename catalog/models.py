from django.db import models

# Create your models here.
class Catalog(models.Model):
    name = models.CharField("Название",max_length=100)
    coast = models.CharField("Цена", max_length=10)
    image = models.ImageField("Фото товара", upload_to="media/img/")
    description = models.TextField("Описание",blank=True, null=True)
    category = models.CharField("Категории",
        max_length=50,
        choices=[
            ("console", "Приставки"),
            ("accessory", "Аксессуары"),
            ("subscription", "Подписки"),
        ],
        default="console"
    )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Order(models.Model):
    name = models.CharField("Имя", max_length=100)
    phone = models.CharField("Телефон", max_length=20)
    product = models.ForeignKey('Catalog', on_delete=models.CASCADE, verbose_name="Товар")
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.name} - {self.product.name}"