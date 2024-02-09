from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm, PersonalDetailForm
from users.models import User

def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        personal_detail_form = PersonalDetailForm(request.POST)
        print(f"\n\n User form: {user_form.is_valid()} Personal detail form: {personal_detail_form.is_valid()} \n\n")
        if user_form.is_valid() and personal_detail_form.is_valid():

            # Save the User instance and get the created user
            user = user_form.save()

            my_user = User.objects.get(phone=user.phone)

            if my_user is None:
                return HttpResponse("<h1>User not found</h1>")

            # Set the user of the PersonalDetail instance and save it
            personal_detail = personal_detail_form.save(commit=False)
            personal_detail.user = my_user
            personal_detail.save()
            return HttpResponse("<h1>User created successfully</h1>")
        print(user_form.cleaned_data)
        # print(user_form.errors, personal_detail_form.errors)
    else:
        user_form = UserForm()
        personal_detail_form = PersonalDetailForm()
    return render(request, 'app/registration/register.html', {'user_form': user_form, 'personal_detail_form': personal_detail_form})
