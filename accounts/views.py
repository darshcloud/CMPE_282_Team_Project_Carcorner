from django.shortcuts import render,redirect

# Create your views here.

def login(request):
    return render(request,'accounts/login.html')
    '''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')
'''
def register(request):
    return render(request,'accounts/register.html')

def dashboard(request):
    return render(request,'accounts/dashboard.html')

def logout(request):
    return redirect('home')