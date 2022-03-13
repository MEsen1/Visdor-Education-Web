from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import ContactForm
from .models import Teacher
import random
# Create your views here.


def home(request):
    
    # items = list(Teacher.objects.all())
    # teachers = random.sample(items,1)
    
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form' : form,
        # 'teachers':teachers
    }
    return render(request, "home/index.html",context)


def about(request):
    return render(request, "home/about.html")


def teacher(request):
    teachers = Teacher.objects.all();
    context = {
        'teacher' : teachers
    }
    
    return render(request, "home/teacher.html",context)


