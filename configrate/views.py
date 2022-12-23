from django.shortcuts import render
from . models import UserR
# Create your views here.


def get_users(request):
    users = UserR.objects.all()
    context = {"user": users}
    return render(request, 'users.html', context)
