from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import CreateUserForm, LoginForm, CreateTransferForm, UpdateTransferForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Transfer

# home
def home(request):
  return render(request, 'webapp/index.html')


# register a user
def register(request):
  form = CreateUserForm()

  if request.method == "POST":
    form = CreateUserForm(request.POST)

    if form.is_valid():
      form.save()

      return redirect('my-login')

  context = {'form':form}

  return render(request, 'webapp/register.html', context=context)


# login a user
def my_login(request):
  form = LoginForm()

  if request.method == "POST":
    form = LoginForm(request, data=request.POST)

    if form.is_valid():
      username = request.POST.get('username')
      password = request.POST.get('password')
      user = authenticate(request, username=username, password=password)

      if user is not None:
        auth.login(request, user)
        return redirect('dashboard')
  context = {'form': form}
  return render(request, 'webapp/my-login.html', context=context)


# dashboard
@login_required(login_url='my-login')
def dashboard(request):
  my_transfers = Transfer.objects.all()
  context = {'transfers': my_transfers}
  return render(request, 'webapp/dashboard.html', context=context)


# create a transfer
@login_required(login_url='my-login')
def create_transfer(request):
  form = CreateTransferForm()

  if request.method == "POST":
    form = CreateTransferForm(request.POST)

    if form.is_valid():
      form.save()
      return redirect("dashboard")
    
  context = {'form': form}
  return render(request, 'webapp/create-transfer.html', context=context)


# update a transfer
@login_required(login_url='my-login')
def update_transfer(request, pk):
  transfer = Transfer.objects.get(id=pk)

  form = UpdateTransferForm(instance=transfer)

  if request.method == 'POST':
    form = UpdateTransferForm(request.POST, instance=transfer)

    if form.is_valid():
      form.save()
      return redirect("dashboard")
    
  context = {'form': form}

  return render(request, 'webapp/update-transfer.html', context=context)


# read/view a singular transfer
@login_required(login_url='my-login')
def singular_transfer(request, pk):
  all_transfers = Transfer.objects.get(id=pk)

  context = {'transfer': all_transfers}

  return render(request, 'webapp/view-transfer.html', context=context)


# delete a singular transfer
@login_required(login_url='my_login')
def delete_transfer(request, pk):
  transfer = Transfer.objects.get(id=pk)
  transfer.delete()

  return redirect("dashboard")

# user logout
def user_logout(request):
  auth.logout(request)
  return redirect("my-login")