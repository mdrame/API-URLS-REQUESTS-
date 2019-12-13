from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# using django buildt in form to signUp user
from django.contrib import messages

# Create your views here.



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) # Create an instance of a form, and pass to template 
        if form.is_valid:
            form.save()
            userName = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {userName}!')
            # after getting clean render user to home destination
            return redirect('home')  
    else:
        # if form submission is not post return regular form
        form = UserCreationForm()
    return render(request, 'user/register.html', {'form': form})
