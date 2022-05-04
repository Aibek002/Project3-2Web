from django.contrib import messages
from django.shortcuts import get_object_or_404

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import UpdateView

from rest_framework import generics

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import WomenSerializer
from .forms import *
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
def index(request):
    return render(request,"BonusTask_app/index.html")
def index1(request):
    return render(request,"BonusTask_app/index1.html")
def index2(request):
    return render(request,"BonusTask_app/index2.html")
def index3(request):
    return render(request,"BonusTask_app/index3.html")
def index4(request):
    return render(request,"BonusTask_app/index4.html")