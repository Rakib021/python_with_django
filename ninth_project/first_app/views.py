from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def home(request):
    return render(request,'home.html')
def signup(request):
    if request.method=='POST':
       form = RegisterForm(request.POST)
       if form.is_valid():
           messages.success(request,'Account created successfully')
           form.save()
           print(form.cleaned_data)
           return redirect('user_login')
    else:
        form = RegisterForm(request.POST)
        
    return render(request,"signup.html",{'form':form})


def user_login(request):
    # print("View function started")
    if request.method == 'POST':
        # print("POST request received")
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            # print("Form is valid")
            # ... your authentication logic ...
            if user is not None:
                # print("User authenticated")
                login(request, user)
                return redirect('profile')
            # else:
            #     print("Authentication failed")
            #     # ... handle invalid login ...
        # else:
        #     print("Form is not valid")
        #     # ... handle invalid form ...
    else:
        # print("GET request received")
        form = AuthenticationForm()
    # print("Rendering template")
    return render(request, 'login.html', {'form': form})

    
def profile(request):
    if request.user.is_authenticated:
        return render(request,'./profile.html',{'user':user})
    else:
        return redirect('user_login')
    
def userLogout(request):
    logout(request)
    return redirect('user_login')
                