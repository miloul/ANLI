from django.shortcuts import redirect, render, get_object_or_404
from .models import Room
from django.utils import timezone

def home(request):
    rooms = Room.objects.all()
    return render(request, 'home.html', {'rooms': rooms})

def detail(request, id):
    room = get_object_or_404(Room, pk=id)
    return render(request, 'detail.html', {'room': room})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_room = Room()
    new_room.image=request.FILES['image']
    new_room.title=request.POST['title']
    new_room.price=request.POST['price']
    new_room.select_home=request.POST['select_home']
    new_room.location=request.POST['location']
    new_room.smaller_period=request.POST['smaller_period']
    new_room.startDay=request.POST['startDay']
    new_room.lastDay=request.POST['lastDay']
    new_room.floor_space=request.POST['floor_space']
    new_room.bathroom=request.POST['bathroom']
    new_room.room=request.POST['room']
    new_room.bed=request.POST['bed']
    new_room.bed=request.POST['basic_info']
    new_room.option=request.POST['option']
    new_room.description=request.POST['description']
    new_room.registered_dttm=timezone.now()
    new_room.save()
    return redirect('detail', new_room.id)

#------
#템플릿들 연결

def deposit(request, id):
    room = get_object_or_404(Room, pk=id)
    return render(request, 'deposit.html', {'room': room})

def mypage(request):
    return render(request, 'mypage.html')

def payment(request, id):
    room = get_object_or_404(Room, pk=id)
    return render(request, 'payment.html', {'room': room})

def wishlist(request):
    return render(request, 'wishlist.html')

def message(request):
    return render(request, 'message.html')

def search(request):
    return render(request, 'search.html')