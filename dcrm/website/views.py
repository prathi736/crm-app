from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    # Check to see if logging in 
    if request.method == 'POST':
        username = request.POST[ 'username' ]
        password = request.POST[ 'password' ]
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "YOU HAVE SUCCESSFULLY LOGGED IN!!")
            return redirect('home')
        else:
            messages.error(request, "THERE IS AN ERROR WHILE LOGGING IN, PLEASE TRY AGAIN!")
            return redirect('home')
    else:
        return render(request, "home.html", {})

def logout_user(request):
    logout(request)
    messages.info(request, "YOU HAVE BEEN LOGGED OUT!!")
    return redirect('home')