from django.shortcuts import render, redirect

from .forms import CreateUserForm, LoginForm

# - function from auth that allow us to log out

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from . models import Record


# - Homepage [author: Johnny Meninga]
def home(request):

    return render(request, 'portfolioApp/index.html')

# -  Register a user
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('my-login')

    context = {'form':form}
    return render(request, 'portfolioApp/register.html', context=context)


# - Login a user

def my_login(request):

    form = LoginForm(data=request.POST or None)
    #form = LoginForm()

    if request.method == 'POST':

        #form = LoginForm(request, data=request.POST or None)

        if form.is_valid():
            #username = request.POST.get('username')
            #password = request.POST.get('password')

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')


            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect('dashboard')

    context = {'form':form}

    return render(request, 'portfolioApp/my-login.html', context=context)




# - Dashboard

@login_required(login_url='my-login')
def dashboard(request):

    # - making a query to pull out all the objects records
    my_records = Record.objects.all()


    # - pass this throught the dashbourd in our context dictionary.
    context = {'records':my_records}


    return render(request, 'portfolioApp/dashboard.html', context=context)


# Create a record

@login_required(login_url='my-login')
def dashboard(request):

    pass



# - User logout

def user_logout(request):

    auth.logout(request)

    return redirect('my-login')