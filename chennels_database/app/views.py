from django.shortcuts import render
from .models import*


def index(request,group_name):
    group=Group.objects.filter(name=group_name).first()
    if group:
        chats=Chat.objects.filter(group=group)
    else:
        group=Group(name=group_name)
        group.save()
    return render(request, 'app/index.html',{'group_name':group_name,'chats':chats})