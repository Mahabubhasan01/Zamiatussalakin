from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from app.models import BlogPost
from urllib.request import urlopen
from .forms import Register_User, Login_Form
import json
# Create your views here.
""" url = 'http://127.0.0.1:8000/api/blogs/'
response = urlopen(url)
blogs = json.loads(response.read())
print(blogs) """


def Home(request):
    blogs = BlogPost.objects.all()
    context = {
        'title': 'home',
        'blogs': blogs
    }
    print(blogs)
    template_name = 'home.html'
    return render(request, template_name, context)


def Blog_Detail(request, pk):
    blog = BlogPost.objects.get(id=pk)
    print(blog)
    template_name = 'blog_detail.html'
    return render(request, template_name, {'blog': blog})


def Auth(request):
    form = Login_Form(request=request, data=request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        userpassword = form.cleaned_data['password']
        usr = authenticate(username=username, password=userpassword)
        if usr is not None:
            login(request, usr)
            return redirect('/')
    else:
        forms = Login_Form()
    return render(request, 'auth.html', {'forms': forms})


def Register(request):
    if request.method == 'POST':
        form = Register_User(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            return redirect('/')
    else:
        forms = Register_User()
        template_name = 'register.html'
        return render(request, 'register.html', {'forms': forms})


def Calculater(request):
    template_name = 'calculater.html'
    return render(request, template_name)


def Category(request, cat):
    blogs = BlogPost.objects.filter(category=cat)
    template_name = 'category.html'
    return render(request, template_name, {'blogs': blogs})
