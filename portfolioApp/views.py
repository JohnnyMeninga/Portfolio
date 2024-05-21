from django.shortcuts import render, redirect

from . forms import CreateUserForm, loginForm

def home(request):

    return render(request, 'portfolioApp/index.html')

# -  Register a user
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            #return redirect('login/')

    context = {'form':form}
    return render(request, 'portfolioApp/register.html', context=context)
