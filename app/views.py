from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from app.models import BlogPost
from urllib.request import urlopen
from .forms import Register_User, Login_Form, Add_Post as Add_P
from django.contrib.auth.forms import AuthenticationForm
import json
from django.contrib import messages

# Create your views here.
""" url = 'http://127.0.0.1:8000/api/blogs/'
response = urlopen(url)
blogs = json.loads(response.read())
print(blogs) """


def Home(request):
    blogs = BlogPost.objects.all()
    catfood = BlogPost.objects.filter(category='food')
    cat1 = BlogPost.objects.filter(category='travel')
    catf = BlogPost.objects.filter(category='fashion')
    cats = BlogPost.objects.filter(category='study')
    catsc = BlogPost.objects.filter(category='science')
    catm = BlogPost.objects.filter(category='music')
    context = {
        'title': 'home',
        'blogs': blogs,
        'catfood': catfood,
        'cat': cat1,
        'catf': catf,
        'cats': cats,
        'catsc': catsc,
        'catm': catm,
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
    if request.method == 'POST':
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            username = fm.cleaned_data['username']
            userpassword = fm.cleaned_data['password']
            usr = authenticate(username=username, password=userpassword)
            if usr is not None:
                login(request, usr)
                messages.info(
                    request, f"You are now logged in as {username}.")
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid username or password.")

        else:
            messages.error(
                request, "Unsuccessful registration. Invalid information.")
    forms = AuthenticationForm()
    return render(request, 'auth.html', {'forms': forms})


def Register(request):
    if request.method == 'POST':
        form = Register_User(request.POST)
        if form.is_valid():
            form.save()
            """ username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user) """
            return redirect('home')
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


def Dashboard(request):
    blogs = BlogPost.objects.all()
    context = {
        'title': 'Dashboard',
        'blogs': blogs
    }
    template_name = 'dashboard.html'
    return render(request, template_name, context)


def Delete_Post(request, pk):
    BlogPost.objects.get(id=pk).delete()
    messages.success(request, 'Product Remove From Wishlist...')
    return redirect('dashboard')


def Add_Post(request):
    AddPost = Add_P()
    template_name = 'Add_Post.html'
    context = {
        'title': 'add-post',
        'addpost': AddPost
    }
    if request.method == 'POST':
        post = Add_P(data=request.POST)
        if post.is_valid():
            post.save()
    else:
        return render(request, 'Add_Post.html', {
            'title': 'add-post',
            'addpost': AddPost
        })
