from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm

# Create your views here.

# registration page view
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()  # save form data
            username = form.cleaned_data.get('username') # username for registration
            messages.success(request, f'Hey {username} your registration is successful, you can now login !!')
            return redirect('login')
    else:     
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


#this view is only accesible for logged in users. If the user is not logged in then the user is not able to access the page.

@login_required
def profilepage(request):
    return render(request, 'users/profile.html')