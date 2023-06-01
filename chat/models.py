from django.db import models
from users.models import CustomUser

class ChatMessage(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete = models.DO_NOTHING)
    message = models.TextField("Message")
    
    def __str__(self) -> str:
        return f"{self.id} {self.sender.username}"


class Chat(models.Model):
    member_1 = models.ForeignKey(CustomUser, related_name = "member1", on_delete = models.DO_NOTHING)
    member_2 = models.ForeignKey(CustomUser, related_name = "member2", on_delete = models.DO_NOTHING)
    
    messages = models.ManyToManyField(ChatMessage, related_name = "chat_messages", blank = True)  
      
    def __str__(self) -> str:
        return f"{self.id} | {self.member_1} <-> {self.member_2}"