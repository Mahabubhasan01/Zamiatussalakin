from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from app.models import BlogPost, Notice, UserComment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import Register_User, Login_Form, Add_Post
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


def Home(request):
    blogs = BlogPost.objects.all().order_by('-date')[:3]
    blogsd = BlogPost.objects.all().order_by('date')
    catfood = BlogPost.objects.filter(category='food')
    cat1 = BlogPost.objects.filter(category='travel')
    catf = BlogPost.objects.filter(category='fashion')
    cats = BlogPost.objects.filter(category='study')
    catsc = BlogPost.objects.filter(category='science')
    catm = BlogPost.objects.filter(category='music')
    notices = Notice.objects.all().order_by('-date')
    totalnotify = Notice.objects.all().count()
    context = {
        'title': 'home',
        'blogs': blogs,
        'blogsd': blogsd,
        'catfood': catfood,
        'cat': cat1,
        'catf': catf,
        'cats': cats,
        'catsc': catsc,
        'catm': catm,
        'notices': notices,
        'totalnotify': totalnotify
    }
    print(blogs)
    template_name = 'home.html'
    return render(request, template_name, context)


def Blog_Detail(request, pk):
    post = get_object_or_404(BlogPost, id=pk)

    # Update the view count on each visit to this post.
    if post:
        post.views += 0
        post.save()

        # Or
        post.update_views()
    context = {
        'blog': post,
        'title': post.title
    }

    return render(request, "blog_detail.html", context)


def Notice_Details(request, pk):
    blog = get_object_or_404(Notice, id=pk)
    template_name = 'Notice_detail.html'
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
        """ firstname = request.POST['firstname']
        lastname = request.POST['lastname'] """
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()
                return redirect('auth')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('register')
    else:
        return render(request, 'register.html',)


def Calculater(request):
    template_name = 'calculater.html'
    return render(request, template_name)


def Category(request, cat):
    blogs = BlogPost.objects.filter(category=cat)
    template_name = 'category.html'
    return render(request, template_name, {'blogs': blogs})
def Inbox_chatting(request):
    return render(request,'inbox_chat.html')

@login_required(login_url='auth')
def Dashboard(request):
    blogs = BlogPost.objects.all().order_by('-date')
    context = {
        'title': 'Dashboard',
        'blogs': blogs
    }
    template_name = 'dashboard.html'
    return render(request, template_name, context)


@login_required(login_url='auth')
def Delete_Post(request, pk):
    BlogPost.objects.get(id=pk).delete()
    messages.success(request, 'Product Remove From Wishlist...')
    return redirect('dashboard')


@login_required(login_url='auth')
def Add_New_Post(request):
    if request.method == 'POST':
        post = Add_Post(request.POST)
        if post.is_valid():
            post.save()
    else:
        AddPost = Add_Post()
        return render(request, 'Add_Post.html', {'addpost': AddPost})


def NoticeWithNotifications(request):
    notices = Notice.objects.all()
    context = {
        'title': 'Notices',
        'blogs': notices
    }
    template_name = 'Notice.html'
    return render(request, template_name, context)


@login_required(login_url='auth')
def Users(request):
    users = User.objects.all().order_by('-id')
    template_name = 'users.html'
    context = {
        'users': users}
    return render(request, template_name, context)


@login_required(login_url='auth')
def Super_User(request, pk):
    user = User.objects.get(id=pk)
    user.is_superuser = True
    user.is_staff = True
    user.save()
    messages.success(request, 'successfully admin done')
    return redirect('users')


@login_required(login_url='auth')
def Delete_User(request, pk):
    User.objects.get(id=pk).delete()
    print(User)
    messages.success(request, 'Product Remove From Wishlist...')
    return redirect('users')


@login_required(login_url='auth')
def Dashboard_Home(request):
    blogs = BlogPost.objects.all().order_by('-date')
    blog = BlogPost.objects.all().first()
    blogg = BlogPost.objects.all().last()
    if blog:
        blog.views += 0
        blog.save()

        # Or
        blog.update_views()
        context = {
            'blogs': blogs,
            'blog': blog,
            'blogg': blogg,
            'title': 'Dashboard home'
        }
        return render(request, 'dashboard_home.html', context)


def Total_Blog_Post(request):
    blogs = BlogPost.objects.all().order_by('-date')
    blog = BlogPost.objects.all().first()
    blogg = BlogPost.objects.all().last()
    context = {
        'blogs': blogs,
        'blog': blog,
        'blogg': blogg,
        'title': 'Blogs'
    }
    return render(request, 'total_post.html', context)


@login_required(login_url='auth')
def User_logout(request):
    logout(request)
    return redirect('auth')
