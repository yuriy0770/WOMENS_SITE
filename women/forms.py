from django import forms
from women.models import Human

class FormHuman(forms.ModelForm):
    class Meta:
        model = Human
        fields = "__all__"
        widgets = {
            'name_h': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            'descriptions': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание женщины',
                'rows': 4
            }),
            'cat': forms.Select(attrs={
                'class': 'form-select'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Автоматически заполнится из имени'
            }),
        }
        labels = {
            'name_h': 'Имя',
            'descriptions': 'Описание',
            'cat': 'Категория',
            'image': 'Фотография',
            'slug': 'URL-адрес',
        }
        help_texts = {
            'slug': 'Оставьте пустым для автоматического заполнения',
            'image': 'Загрузите фотографию',
        }
