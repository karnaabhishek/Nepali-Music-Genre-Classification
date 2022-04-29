from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import logout, authenticate, login
from login.predict import predict_gen

from login.savemfcc import save_mfcc
from .forms import CreateUserForm, AudioForm
from django.contrib import messages

# Create your views here.
def index(request):
    import numpy as np
    print("form")
    if request.user.is_anonymous:
        return redirect("/login")
    if request.method=="POST":
        if len(request.FILES) == 0:
            messages.error(request,'Upload a file')
            return redirect("login:index")
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            uploadfile = request.FILES['record']
            if not uploadfile.name.endswith('.wav'):
                messages.error(request,'Only .wav file type is allowed')
                return redirect("predictor:index")
            meta = save_mfcc(uploadfile)
            X = np.array(meta["mfcc"])
            X = X[..., np.newaxis]
            Genre = {0:"Rock", 1:"Rap", 2:"Aadhunik", 3:"Deuda", 4:"Lok Dohori", 5:"Pop", 6:"Tamang Selo", 7:"Purbeli Bhaka"}
            genre = predict_gen(X)
            context = {'genre': Genre[genre]}
            print("form validated successfully")
            
            return render(request,'result.html',context)
            
    else:
        form = AudioForm()
    return render(request, 'index.html', {'form': form})

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")

def registration(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {"form":form}

    return render(request, 'registration.html', context)