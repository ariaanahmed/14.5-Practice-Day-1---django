from django.shortcuts import render
from .forms import ContactForm
from .import models

# Create your views here.
def home (request):
    form = ContactForm()
    return render(request, 'home.html', {'form': form})

def model_form (request):
    student = models.Student.objects.all()
    print(student)
    return render(request, 'model_form.html', {'data': student})