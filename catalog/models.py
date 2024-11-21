from django.db import models
from users import User

class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["title"]


class Product(models.Model):
    title = models.CharField(
        max_length=150, verbose_name="Название", help_text="Введите название продукта"
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True,
        help_text="Введите описание продукта",
    )
    image = models.ImageField(
        upload_to="images/",
        verbose_name="Изображение",
        blank=True,
        null=True,
        help_text="Загрузите фотографию продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Категория",
    )
    publish_status = models.BooleanField(default=False, help_text= 'Укажите статус публикации продукта', verbose_name='Статус публикации')
    owner = models.ForeignKey(User, verbose_name='Владелец', on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    publish_status = models.BooleanField(
        default=False,
        help_text="Укажите статус публикации продукта",
        verbose_name="Статус публикации",
    )
    owner = models.ForeignKey(
        User,
        verbose_name="Владелец",
        on_delete=models.CASCADE,
        related_name="products",
        null=True,
        blank=True,
    )

    view_counter = models.PositiveIntegerField(
        default=0, verbose_name="Количество просмотров"
    )

    def __str__(self):
        return f"{self.title} {self.price}"


    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["title"]
        permissions = [
            ("can_unpublish_product", "can unpublish product"),
        ]
