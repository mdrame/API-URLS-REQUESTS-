from django.shortcuts import render, redirect
# using django buildt in form to signUp user
from django.contrib import messages
from .form import UserRegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) # Create an instance of a form, and pass to template 
        if form.is_valid:
            form.save()
            userName = form.cleaned_data.get('username')
            messages.success(request, f'Account created: Pls log in {userName}!')
            # after getting clean render user to home destination
            return redirect('login')  
    else:
        # if form submission is not post return regular form
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'user/profile.html')