from spy_details import Spy,spy ,chatmess,friend_list

from termcolor import colored, cprint



def start_chat(spy):                                       #function to start the chat in both cases if new user or old user
    show_menu=True
    current_status_message = None
    print "So what's in your mind, "+spy.name
    while show_menu:
        menu_choice=int(raw_input("What do you want to do?\n1. Add Status Update.\n2. Add a friend\n3. Send a secret message.\n4. Read a secret message.\n5. Read older chats from spy friends.\n6. Close the Application"))
        if menu_choice==1:
            print "You choosed Status Update"
            add_status(current_status_message)                                     #add_status() function is called for adding status
        elif menu_choice==2:
            print 'You choosed adding a new friend.'
            add_friend()
        elif menu_choice==3:
            send_message()
        elif menu_choice==4:
            read_message()
        elif menu_choice==5:
            read_chat_history()
        elif menu_choice==6:
            show_menu=False



#this section contains some default status message anf a function add _status()

status_message=['Spies are cool','I\'m the best spy','My name is Rohit']




def add_status(current_status_message):
    updated_status_message = ''
    if current_status_message!=None:                                               #if a current status is there so it will print else not
        print "Your current status is"+current_status_message
    else:
        print "You don't have any status at this moment."
    default=raw_input("Do you want to select from older status,(Y/N).")            #selecting older status or not
    if default.upper()=="N":
        new_status_message=raw_input("Add your new status here.")
        if len(new_status_message)>0:
            status_message.append(new_status_message)                              #if not then new status is input,appended to list and print
            updated_status_message=new_status_message
            print "Your status is:"+ updated_status_message
           # current_status_message = updated_status_message
    elif default.upper()=="Y":
        item_position=1
        for message in status_message:
            print '%d. %s' % (item_position, message)                              #if yes then older status are printed and selected
            item_position=item_position+1
        message_selection=int(raw_input("Select the status you want."))
        if len(status_message)>=message_selection:
            updated_status_message=status_message[message_selection-1]
    else:
        print 'Please choose a valid option(Y/N)'

    if len(updated_status_message)>0:
        print 'Your updated status message is:'+" "+updated_status_message
    else:
        print 'You did not update your status message'
    return updated_status_message






#list for friend _details


def add_friend():                                                                      #function for friend details friend()
    new_friend=Spy('','',0,0.0)
    new_friend.name=raw_input("Please enter your friend's name.")
    new_friend.salutation=raw_input("Are they Mr. or Miss.")
    print "Seems a pretty name, "+new_friend.salutation+new_friend.name
    new_friend.age=int(raw_input("Enter your friend's age."))
    new_friend.rating=float(raw_input("Enter your friend's rating."))
    if len(new_friend.name)>0 and new_friend.age>12 and new_friend.rating>spy.rating:
        friend_list.append(new_friend)
        print new_friend.salutation+new_friend.name+" "+'Added as friend.'
    else:
        print "Sorry you are not eligible to be selected as a Spy."
    return len(friend_list)


def select_friend():
    print "Select a friend. "
    item_number=1
    for friends in friend_list:
        print '%d. %s %s'%(item_number,friends.salutation,friends.name)
        item_number=item_number+1
    friend_choice=raw_input("Choose from your friends.")
    friend_index=int(friend_choice)-1
    print "You choosed"+" "+friend_list[friend_index].salutation+" "+friend_list[friend_index].name
    return friend_index

from steganography.steganography import Steganography
from datetime import datetime
def send_message():
    friend_choice=select_friend()
    image_name=raw_input("What's the name of the image?")
    image_path='Output.jpg'
    text=raw_input("What do you want to say?")
    if len(text)==0:
        print "Please type a message to send."
        send_message()

    else:
        Steganography.encode(image_name,image_path,text)
        new_chat = chatmess(text, True)
        friend_list[friend_choice].chats.append(new_chat)
        print "Your secret message is ready to be sent."

def read_message():
    sender=select_friend()
    image_path=raw_input("What's the name of your file?")
    secret_text=Steganography.decode(image_path)
    if len(secret_text)<=100:
        if secret_text.upper()=="SOS" or secret_text.upper()=="SAVE ME":
            print friend_list[sender].salutation+friend_list[sender].name+" is in serious trouble. Go and help."
        else:
            print "Your message is:"+ secret_text
            new_chat = chatmess(secret_text,False)
            friend_list[sender].chats.append(new_chat)
            print "Your secret message has been saved."
    else:
        print friend_list[sender].salutation+friend_list[sender].name+" "+"is disturbing too much."
        delete=raw_input( "Do you want to delete this spy? (Y/N)")
        if delete.upper()=="Y":
            del friend_list[sender]
            print "Spy has been deleted."
            print "New updated friend list is:"
            item_number = 1
            for friends in friend_list:
                print '%d. %s %s' % (item_number, friends.salutation, friends.name)
                item_number = item_number + 1
        elif delete.upper()=="N":
            start_chat(spy)



def read_chat_history():
    read_for=select_friend()
    for chat in friend_list[read_for].chats:
        if chat.sent_by_me:
            print(colored('[%s]' % (chat.time.strftime("%d %B %Y")),'blue')+" "+colored('%s:' %('You said:'),'red')+" "+colored('%s'%(chat.message)))
        else:
            print(colored('[%s]'%(chat.time.strftime("%d %B %Y")),'blue')+" "+colored('%s:'%(friend_list[read_for].name),'red')+" "+colored('%s'%(chat.message)))

     #default spy_details are imported



print "Your Current Info:\n"+"Spy Name:"+spy.salutation+spy.name+"\n"+"Spy Age:"+str(spy.age)+"\n"+"Spy_rating:"+str(spy.rating)
print'Hey what\'s up'
question=raw_input('Welcome.Do you want to continue as '+spy.salutation+spy.name+'?\n'+"Enter your choice Y/N.")
if question=='Y'or question=='y':                                                 #continue as default spy
    print  'Glad to see you again '+spy.salutation+spy.name
    start_chat(spy)                  #starting app with start_chat() function
else:
    spy=Spy('','',0,0.0)
    spy.name = raw_input("Who's This?")

    if len(spy.name) > 0:                                                         #continue s new spy
        print 'Hi,Welcome ' + spy.name + '.How are you?'
        spy_salutation = raw_input("What should we call you (Mr. or Miss)")
        print 'Hello ' + spy_salutation+" " + spy.name
    else:
        print 'You should have a Proper Name'
    spy.age = int(raw_input("What's Your Age?"))
    if spy.age > 12 and spy.age < 50:
        spy.rating = float(raw_input("Enter Your Rating."))
        if spy.rating > 4.5:
            print"Great Ace"
        elif spy.rating > 3.5 and spy.rating <= 4.5:
            print"Have a Good job"
        elif spy.rating >= 2.5 and spy.rating <= 3.5:
            print"you can also do better"
        else:
            print"You can help others in office"
        spy_is_ofline = 'True'
        print'Authenticaion Complete!\nYour Age %s.\nYour Rating:%s \nAge:%s' % (spy.name, spy.rating, spy.age)
        start_chat(spy)
    else:                                                                         # starting chat with start_chat() fuction
        print"Sorry you are not eligible"


