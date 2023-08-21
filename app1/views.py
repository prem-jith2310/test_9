from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
from app1.models import tbl_user, tbl_cake
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import requests


# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    username = request.POST.get('uname')
    password = request.POST.get('pwd')
    p1 = authenticate(username = username, password = password)
    request.session['username'] = username
    if p1 is not None and p1.is_superuser == 1:
        return redirect('/admin_home/')
    elif p1 is not None and p1.is_superuser == 0:
        return redirect('/user_home/')
    else:
        return HttpResponse('invalid user')

def admin_home(request):
    p = request.session['username']
    return render(request, 'admin_home.html', {'x':p})

def signup(request):
    return render(request, 'signup.html')

def add_user(request):
    p = tbl_user()
    p1 = User()
    p.uname = request.POST.get('uname')
    p.fname = request.POST.get('fname')
    p.gender = request.POST.get('gender')
    p.phone = request.POST.get('phone')
    p.email = request.POST.get('email')
    p.place = request.POST.get('place')
    p.photo = request.POST.get('photo')
    p.address = request.POST.get('address')
    image = request.FILES['photo']
    fs = FileSystemStorage()
    filename = fs.save(image.name,image)
    file_url = fs.url(filename)
    p.photo = file_url
    p.save()
    p1.username = request.POST.get('uname')
    p1.first_name = request.POST.get('fname')
    p1.email = request.POST.get('email')
    password = request.POST.get('pwd')
    p1.set_password(password)
    p1.save()
    return redirect('/index.html/')

def user_home(request):
    p = request.session['username']
    p1= tbl_user.objects.get(uname = p)
    return render(request, 'user_home.html', {'x':p1})

def cakes(request):
    return render(request,'cakes.html')

def add_cakes(request):
    p = tbl_cake()
    p.name = request.POST.get('name')
    p.qty = request.POST.get('qty')
    p.flavour = request.POST.get('flavour')
    p.price = request.POST.get('price')
    image = request.FILES['photo']
    fs = FileSystemStorage()
    filename = fs.save(image.name,image)
    photo_url = fs.url(filename)
    p.photo = photo_url
    p.save()
    return render(request, 'cakes.html')

def view_users(request):
    p = tbl_user.objects.all()
    return render(request, 'view_users.html', {'data':p})

def del_user(request, id):
    p = tbl_user.objects.get(id = id)
    p.delete()
    p1 = User.objects.get(username = p.uname)
    p1.delete()
    return redirect('/view_users/')

def user_profile(request):
    p = request.session['username']
    p1 = tbl_user.objects.get(uname = p)
    return render(request, 'user_profile.html', {'x':p1})

def view_cakes(request):
    p = tbl_cake.objects.all()
    return render (request, 'view_cakes.html', {'data':p})

def update_cakes(request, id):
    p = tbl_cake.objects.get(id = id)
    return render(request, 'update_cakes.html', {'x':p})

def update_cakes2(request, id):
    p = tbl_cake.objects.get(id = id)
    try:
        p.name = request.POST.get('name')
        p.qty = request.POST.get('qty')
        p.flavour = request.POST.get('flavour')
        p.price = request.POST.get('price')
        image = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(image.name,image)
        photo_url = fs.url(filename)
        p.photo = photo_url
        p.save()
    except:
        p.name = request.POST.get('name')
        p.qty = request.POST.get('qty')
        p.flavour = request.POST.get('flavour')
        p.price = request.POST.get('price')
        p.save()
        return redirect('/view_cakes/')

def chocolate_cakes(request):
    p = tbl_cake.objects.filter(flavour = 'chocolate')
    return render(request, 'view_cakes.html', {'data':p})






