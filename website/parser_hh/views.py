from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from .models import Vacancy
from .forms import ContactForm
from django.core.mail import send_mail
# Create your views here.


def main_view(request):
    return render(request, 'parser_hh/index.html', context={})


def results(request):
    vacancies = Vacancy.objects.all()  # 'data': vacancies
    return render(request, 'parser_hh/results.html', context={'data': vacancies})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']

            send_mail('Contact message',
                      f'Ваш сообщение {message} принято',
                      'from@example.com',
                      [email],
                      fail_silently=True,
                      )

            print('send message')
            # send_mail('Contact message',
            #           'Ваш сообщение принято',
            #           'from@example.com',
            #           ['email@email.com'],
            #           fail_silently=True,
            #           )
            return HttpResponseRedirect(reverse('parser:index'))
        else:
            return render(request, 'parser_hh/contacts.html',
                          context={'form': form})
    else:
        form = ContactForm()
        return render(request, 'parser_hh/contacts.html',
                      context={'form': form})


def vacancy(request):
    pass
#     return render(request, 'parser_hh/vacancy.html', context={})