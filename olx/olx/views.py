from django.shortcuts import render
from django.core.mail import send_mail
from accounts.models import Mailing

def home(request):
    return render(request, 'registration/home.html')

def about(request):
    return render(request,'registration/about.html')

def contact(request):
    if request.method=="POST":
        email2=request.POST['email1']
        name2=request.POST['name1']
        message2=request.POST['message1']
        subject2=request.POST['subject1']
        
        receiver=Mailing(email=email2,name=name2,subject=subject2,message=message2)
        receiver.save()
        subject="You got Message From"+ email2  +"and subject of mail is " + subject2
        message=message2
        send_mail(
            subject,
            message,
            email2,
            ['abhikohli221@gmail.com'],
            fail_silently=False



        )
        return render(request,'registration/home.html')
    else:
        return render(request,'registration/contact.html')    

def facebook(request):
    return render(request,'registration/facebook.html')