from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import logout, authenticate, login
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm 

def logout_view(request):
    """Log out user"""
    logout(request)
    return HttpResponseRedirect(reverse('blogs:index'))

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        #Init new form for user enter data.
        form = UserCreationForm()
    else:
        #Submitted, process data.
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            #Log user in and then redirect to home page
            authenticated_user = authenticate(username=new_user.username,
                password=request.POST['password1'])
            login(request, authenticated_user)

            return HttpResponseRedirect(reverse('blogs:index'))
    
    context = {'form':form}

    return render(request, 'users/register.html', context)

        
        
    
