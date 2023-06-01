from django.shortcuts import render
from .models import Chat
from django.db.models import Q
from users.models import CustomUser


def empty_chat(request):
    user_chats = Chat.objects.filter(Q(member_1=request.user) | Q(member_2=request.user))
    
    return render(request, "chat/chat.html", {
        "user_chats": user_chats
    })

def chat(request, id=None ):
    user_chats = Chat.objects.filter(Q(member_1=request.user) | Q(member_2=request.user))
    # if id == None:
    
    chat = Chat.objects.filter(Q(member_1=request.user.id, member_2=id) | Q(member_1=id, member_2=request.user.id)).first()
    if not(chat):
        new_chat = Chat.objects.create(member_1 = request.user, member_2 = CustomUser.objects.get(id = id) )
        chat = new_chat.id
    
    if request.method == "POST" and chat:
        message = request.POST.get("new_message")
        
        chat_send = Chat.objects.get(id = chat.id)
        chat_send.messages.create(sender = request.user, message = message)
        chat_send.save()
        
    return render(request, "chat/chat.html", {
        "chat": chat,
        "user_chats": user_chats
    })






