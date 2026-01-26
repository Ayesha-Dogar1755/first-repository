class User:
    def __init__(self,name):
        self.name=name
class Message:
    def __init__(self,sender,text):
        self.sender=sender
        self.text=text
class ChatRoom:
    def __init__(self):
        self.users=[]
        self.messages=[]
    def join(self,user):
        self.users.append(user)
        print(f"{user.name} has joined the chat room.")
    def leave(self,user):
        self.users.remove(user)
        print(f"{user.name} has left the chat room.")
    def send_messages(self,user,text):
        msg=Message(user,text)
        self.messages.append(msg)
    def show_chat(self):
        for msg in self.messages:
            print(f"{msg.sender.name}: {msg.text}")
chatroom=ChatRoom()
user1=User("Alice")
user2=User("Bob")
chatroom.join(user1)
chatroom.join(user2)
chatroom.send_messages(user1,"Hello, everyone!")
chatroom.send_messages(user2,"Hi, Alice!")
chatroom.leave(user1)
chatroom.show_chat()