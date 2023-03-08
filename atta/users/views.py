from django.shortcuts import render, redirect # redirect lets us redirect the user to a certain html file / url.
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def register(request):
    # we dont need to create our own user form, we can simply import it
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # this line gets the username from the form, if the user has not yet created an account with us.
            username = form.cleaned_data.get('username')
            messages.success(request, f' Your account has been created! You are now able to Log In')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form' : form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')
