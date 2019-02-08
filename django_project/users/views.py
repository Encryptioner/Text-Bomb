from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import os


from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage


def register(request):
    if request.user.is_authenticated:
        return redirect('profile')

    else:

        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()

                acc = account_activation_token.make_token(user)
                current_site = get_current_site(request)
                mail_subject = 'Activate your blog account.'
                message = render_to_string('users/acc_activation_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                    'token': account_activation_token.make_token(user),
                })

                uid = urlsafe_base64_encode(force_bytes(user.pk)).decode()
                token = account_activation_token.make_token(user)
                user.pk

                to_email = form.cleaned_data.get('email')
                email = EmailMessage(
                    mail_subject, message, to=[to_email]
                )

                email.send()
                return HttpResponse('Please confirm your email address to complete the registration')

                # form.save()
                # username = form.cleaned_data.get('username')
                # # messages.success(request, 'Account created for, {} !'.format(username))
                # messages.success(request, 'Your account has been created for, {} !'.format(username))
                # return redirect('login')
        else:
            form = UserRegisterForm()

        return render(request, 'users/register.html', {'form': form})


def activate(request, uidb64, token):
    try:
        # uidb64 = 'test7srt'
        uidb64
        uid = urlsafe_base64_decode(uidb64).decode()
        # uid = force_text(urlsafe_base64_decode(uidb64))
        uid
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    h = account_activation_token.check_token(user, token)
    # backk
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        login(request, user)
        messages.success(request, 'Your account has been created for, {} !'.format(user))
        return redirect('profile')

        # return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


@login_required
def profile(request):

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

            user = request.POST['username']
            user = User.objects.filter(username=user).first()
            pre_img = user.profile.image.url
            pre = BASE_DIR + pre_img

            # os.remove(pre)

            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'num_visits': num_visits
    }

    return render(request, 'users/profile.html', context)
