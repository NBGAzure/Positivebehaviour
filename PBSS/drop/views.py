from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Person, City
from .forms import PersonForm
from django.shortcuts import render

class PersonListView(ListView):
    model = Person
    context_object_name = 'people'

class PersonCreateView(CreateView):
    model = Person
    fields = ('name', 'birthdate', 'country', 'city')
    success_url = reverse_lazy('drop/person_changelist')

class PersonUpdateView(UpdateView):
    model = Person
    fields = ('name', 'birthdate', 'country', 'city')
    success_url = reverse_lazy('drop/person_changelist')
class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    success_url = reverse_lazy('person_changelist')

class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    success_url = reverse_lazy('person_changelist')
def load_cities(request):
    country_id = request.GET.get('country')
    cities = City.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'drop/city_dropdown_options.html', {'cities': cities})