from django import forms
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
from .models import User
from .models import PersonalDetails

class UserForm(forms.ModelForm):

    phone = forms.RegexField(
        regex=r'\d{9,15}$',
        help_text=_('Enter 10 digit phone number'),
        error_messages={'invalid': _('Invalid phone number')},
        widget=forms.TextInput(attrs={
            'placeholder': _(''),
            'class': 'block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer',
            'id': 'phone',
            'required': 'true',
            'type': 'tel',
        })
    )

    password1 = forms.RegexField(
        label=_('Password'),
        regex=r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d!@#$%^&*()_+]{8,}$',
        help_text=_('Minimum 8 characters with at least 1 letter and 1 number and one special character from !@#$%^&*()_+'),
        error_messages={'required': _('Password is required'), 'invalid': _('Invalid password')},
        widget=forms.PasswordInput(attrs={
            'placeholder': _(''),
            'class': 'block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer',
            'id': 'password',
            'required': 'true',
            'type': 'password',
        })
    )

    terms_accepted = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={
            'class': 'peer h-4 w-4 rounded border-2 translate-y-1 mr-1 border-gray-300 accent-blue-500 focus:ring-2 focus:ring-blue-500',
            'id': 'terms',
            'type': 'checkbox',
            'checked': True,
        }),
        required=False,
    )
    #  w-4 h-4  rounded-md accent-blue-500 focus:ring-2 focus:ring-blue-500
    # <input type="checkbox" id="terms" name="terms" checked class="">

    def clean_terms_accepted(self):
        terms_accepted = self.cleaned_data.get('terms_accepted')
        if not terms_accepted:
            raise forms.ValidationError(_('You must accept the terms and conditions.'))
        return True  # Set it to True if checkbox is checked

    def clean(self):
        cleaned_data = super().clean()
        # Add additional form-wide validation here if needed
        return cleaned_data

    class Meta:
        model = User
        fields = ['phone', 'password1',  'terms_accepted']

class PersonalDetailForm(forms.ModelForm):

    first_name = forms.CharField(
        label=_('First name'),
        widget=forms.TextInput(attrs={
            'placeholder': _(''),
            'class': 'block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer',
            'id': 'first_name',
            'required': 'true',
            'type': 'text',
        })
    )

    last_name = forms.CharField(
        label=_('Last name'),
        widget=forms.TextInput(attrs={
            'placeholder': _(''),
            'class': 'block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer',
            'id': 'last_name',
            'required': 'true',
            'type': 'text',
        })
    )
    class Meta:
        model = PersonalDetails
        fields = ['first_name', 'last_name']


# from django.shortcuts import render, redirect
# from .forms import RegistrationForm

# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             user_form = form.cleaned_data['user']
#             personal_detail_form = form.cleaned_data['personal_detail']

#             # Save the User instance and get the created user
#             user = user_form.save()

#             # Set the user of the PersonalDetail instance and save it
#             personal_detail = personal_detail_form.save(commit=False)
#             personal_detail.user = user
#             personal_detail.save()

#             return redirect('home')
#     else:
#         form = RegistrationForm()

#     return render(request, 'register.html', {'form': form})
    
# html ussage of the form
# <form method="post">
#     {% csrf_token %}
#     {{ form.user.phone }}
#     {{ form.user.password1 }}
#     {{ form.user.terms_accepted }}
#     {{ form.personal_detail.first_name }}
#     {{ form.personal_detail.last_name }}
#     <button type="submit">Register</button>
# </form>
    