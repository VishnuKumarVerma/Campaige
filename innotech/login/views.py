from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from login.models import data
from .forms import UploadImageForm
from .models import UploadedImage

# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        en = data(username=username, password=password)
        en.save()
        user = authenticate(username = username , password = password) 
    return render(request,"login.html")
        

def signout(request):
    logout(request)
    return redirect('login')

def afs(request):
    return render(request,"afs.html")

def profile(request):
    form=UploadImageForm()
    images=UploadedImage.objects.all()
    return render(request,"profile.html",{'images':images,'form':form})

def sign(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password = request.POST['comfirm_password']
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = username
        myuser.save() 
        if User.objects.filter(username=username):
            return redirect('afs')
        
        if User.objects.filter(email=email):
            return redirect('afs')
        
        return render(request,"login.html")
        
    return render(request,"sign.html")


def home_page(request):
    return render(request,"home.html")

def groups(request):
    return render(request,"groups.html")


def create_follow(request):
    if request.method == 'POST':
        form=UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        # else:
        #     form=UploadImageForm()
    return render(request,"create_follow.html")


def error_404(request,exception):
    return render(request,"404.html")
