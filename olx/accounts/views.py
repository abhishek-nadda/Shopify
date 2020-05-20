from django.shortcuts import render,redirect
from django.contrib.auth import logout as ls
from .forms import SignUpForm
from django.contrib import auth
from django.contrib.auth.models import User
from .models import User
from django.core.mail import send_mail
from .tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
# Create your views here.
def logout(request):    
    ls(request)
    return redirect('product:product_list')

def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        #form.save()
        user = form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        email = form.cleaned_data.get('email')
        

        site_name = get_current_site(request)
        domain = site_name.domain

        message = {
            'domain': domain,
            'site_name': site_name,
            'token': account_activation_token.make_token(user),
            
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'user': user,
        }
        message = render_to_string("registration/account_activate.html",{
            'domain': domain,
            'site_name': site_name,
            'token': account_activation_token.make_token(user),
            
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'user': user,
        })

        send_mail(
             'Activate your account',
             f'your {message}',
             'EMAIL_HOST_USER',
             [email],
             fail_silently=False,
         )
        messages.success(request, ('account confirmation link has been sent to your mail.'))
        return redirect('accounts:login')
    return render(request, 'registration/signup.html', {'form': form})
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     password1 = request.POST['confirmpassword']
    #     if password == password1:
    #         if Users.objects.filter(username=username).exists():
    #             messages.info(request, '*Username taken')
    #             return redirect('register')
    #         elif Users.objects.filter(email=email).exists():
    #             messages.info(request, '*Email taken')
    #             return redirect('register')
    #         else:
    #             user1 = Users.objects.create_user( email=email, password=password,
    #                                     username=username
    #                                     )
    #             user1.is_active=False
    #             user1.save()
    # # form = SignUpForm(request.POST)
    # # if form.is_valid():
    #     #form.save()
    #     # user = form.save()
    #     # username = form.cleaned_data.get('username')
    #     # email = request.POST['email']
    #     # password = form.cleaned_data.get('password1')
        

    #     site_name = get_current_site(request)
    #     domain = site_name.domain

    #     message = {
    #         'domain': domain,
    #         'site_name': site_name,
    #         'token': account_activation_token.make_token(user1),
            
    #         'uid': urlsafe_base64_encode(force_bytes(user1.pk)),
    #         'user': user1,
    #     }
    #     message = render_to_string("registration/account_activate.html",{
    #         'domain': domain,
    #         'site_name': site_name,
    #         'token': account_activation_token.make_token(user1),
            
    #         'uid': urlsafe_base64_encode(force_bytes(user1.pk)),
    #         'user': user1,
    #     })
        


    #     send_mail(
    #         'Activate your account',
    #         f'your {message}',
    #         'EMAIL_HOST_USER',
    #         [email],
    #         fail_silently=False,
    #     )
    # else:
       
    #     messages.info(request, '*Password not matching')
    #     return redirect('accounts:signup')
    # messages.success(request, ('account confirmation link has been sent to your mail.'))
    # return redirect('accounts:login')
    # # return render(request, 'registration/signup.html', {'form': form})




def activateAccount(request,uidb64,token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk = uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user,token):
        user.is_active = True
        user.save()
        messages.success(request, ('Your account have been confirmed.'))
        return redirect('accounts:login')
        # return redirect('product:product_list')
    else:
        print("Invalid Link")
        return HttpResponse("<h3>Invalid Link</h3>")