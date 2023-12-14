from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

def home(request):

    records = Record.objects.all()

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
        return render(request, "home.html", {'records':records})

def logout_user(request):
    logout(request)
    messages.info(request, "YOU HAVE BEEN LOGGED OUT!!")
    return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "YOU HAVE SUCCESSFULLY REGISTERED! WELCOME!!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        # Look up records
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.error(request, "YOU MUST BE LOGGED IN TO VIEW THIS PAGE!!")
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.error(request, "RECORD HAS BEEN DELETED SUCCESSFULLY!")
        return redirect('home')
    else:
        messages.error(request, "YOU MUST BE LOGGED IN TO DO THAT OPERATION!!")
        return redirect('home')
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "RECORD ADDED SUCCESSFULLY!!")
                return redirect('home')
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.info(request, "YOU MUST BE LOGGED IN !!")
        return redirect('home')