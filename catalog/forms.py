from django import forms
from .models import Product
from django.core.exceptions import ValidationError


STOP_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'image', 'price', 'category']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите описание продукта'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите описание продукта'})
        self.fields['image'].widget.attrs.update({'class': 'form-control-file', 'placeholder': 'Загрузите изображение'})
        self.fields['price'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите цену продукта'})
        self.fields['category'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Выберите категорию продукта'})

        def clean_price(self):
            price = self.cleaned_data['price']
            if price < 0:
                raise ValidationError('Цена не может быть отрицательной')
            return price

        def clean(self):
            clean_data = super().clean()
            title = clean_data.get('title')
            description = clean_data.get('description')
            if any(word in title.lower() for word in STOP_WORDS) or any(word in description.lower() for word in STOP_WORDS):
                raise ValidationError('Предложение содержит запрещенные слова')
