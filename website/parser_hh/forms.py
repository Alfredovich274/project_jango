from django import forms
from .models import Param, Schedule, Experience


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', widget=forms.TextInput(
                                    attrs={'placeholder': 'Ваше имя',
                                           'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(
                                    attrs={'placeholder': 'Ваш email адрес',
                                           'class': 'form-control'}))
    message = forms.CharField(label='Сообщение', widget=forms.Textarea(
                                    attrs={'placeholder': 'Текст сообщения',
                                           'class': 'form-control'}))


class CreateParams(forms.ModelForm):
    key_words = forms.CharField(label='Ключевые слова',
                                widget=forms.TextInput(
                                    attrs={'placeholder': 'Ключевые слова',
                                           'class': 'form-control'}))
    salary = forms.CharField(label='Заработная плата', required=False,
                             widget=forms.TextInput(
                                 attrs={'placeholder': 'Зарплата',
                                        'class': 'form-control'}))
    city = forms.CharField(label='Город', required=False,
                           widget=forms.TextInput(
                                 attrs={'placeholder': 'Город',
                                        'class': 'form-control'}))
    schedule = forms.ModelChoiceField(queryset=Schedule.objects.all(),
                                      label='Тип занятости', required=False,)
    experience = forms.ModelChoiceField(queryset=Experience.objects.all(),
                                        label='Опыт', required=False,)

    class Meta:
        model = Param
        fields = '__all__'
