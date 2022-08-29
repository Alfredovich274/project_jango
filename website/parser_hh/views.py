from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from .models import Vacancy, Param, Schedule, Experience, Skill, Specialization
from .forms import ContactForm, CreateParams
from django.core.mail import send_mail
from django.views.generic import ListView, CreateView, DetailView, DeleteView


# Create your views here.
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']

            send_mail('Contact message',
                      f'Ваш сообщение {message}, {name}, принято',
                      'from@example.com',
                      [email],
                      fail_silently=True,
                      )
            return HttpResponseRedirect(reverse('parser:index'))
        else:
            return render(request, 'parser_hh/contacts.html',
                          context={'form': form})
    else:
        form = ContactForm()
        return render(request, 'parser_hh/contacts.html',
                      context={'form': form})


class ParamsListView(ListView):
    model = Param
    template_name = 'parser_hh/index.html'


class VacancyListView(ListView):
    model = Vacancy
    template_name = 'parser_hh/results.html'


def create_params(request):
    if request.method == 'POST':
        form = CreateParams(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('parser:index'))
    else:
        form = CreateParams()
        return render(request, 'parser_hh/create-options.html',
                      context={'form': form})


# class CreateNewParams(CreateView):
#     fields = '__all__'
#     model = Param
#     success_url = reverse_lazy('parser:index')
#     template_name = 'parser_hh/create-options.html'
#
#     def form_valid(self, form):
#         """
#         Метод срабатывает после того как форма валидна
#         :param form:
#         :return:
#         """
#         return super().form_valid(form)


class ParamsDeleteView(DeleteView):
    template_name = 'parser_hh/delete-params.html'
    model = Param
    success_url = reverse_lazy('parser:index')


class VacancyDeleteView(DeleteView):
    template_name = 'parser_hh/delete-vacancy.html'
    model = Vacancy
    success_url = reverse_lazy('parser:results')


class VacancyDetailView(DetailView):
    model = Vacancy
    template_name = 'parser_hh/vacancy.html'

