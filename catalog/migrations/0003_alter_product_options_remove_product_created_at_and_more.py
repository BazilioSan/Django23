# Generated by Django 5.1.2 on 2024-11-24 10:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_product_view_counter"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["title"],
                "permissions": [("can_unpublish_product", "can unpublish product")],
                "verbose_name": "продукт",
                "verbose_name_plural": "продукты",
            },
        ),
        migrations.RemoveField(
            model_name="product",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="product",
            name="updated_at",
        ),
        migrations.AddField(
            model_name="product",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="products",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Владелец",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="publish_status",
            field=models.BooleanField(
                default=False,
                help_text="Укажите статус публикации продукта",
                verbose_name="Статус публикации",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(
                blank=True,
                help_text="Введите описание продукта",
                null=True,
                verbose_name="Описание",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(
                blank=True,
                help_text="Загрузите фотографию продукта",
                null=True,
                upload_to="images/",
                verbose_name="Изображение",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.DecimalField(
                decimal_places=2,
                help_text="Введите цену продукта",
                max_digits=10,
                verbose_name="Цена",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="title",
            field=models.CharField(
                help_text="Введите название продукта",
                max_length=150,
                verbose_name="Название",
            ),
        ),
    ]
