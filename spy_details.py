from datetime import datetime


class Spy:

    def __init__(self,salutation,name, age, rating):
        self.salutation = salutation
        self.name = name
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None

spy=Spy('Mr.','Rohit',21,4.7)


friend_one=Spy('Miss.','Sunidhi',21,4.9)
friend_two=Spy('Mr.','Mukesh',4.5,22)
friend_three=Spy('Mr.','Gajanand',22,3.39)

friend_list =[friend_one,friend_two,friend_three]


class chatmess:
     def __init__(self,message,sent_by_me):
        self.message=message
        self.sent_by_me=sent_by_me
        self.time=datetime.now()