from django.shortcuts import redirect
from functools import wraps
from .models import PersonalDetails , AddressDetails, BankDetails , LoanApplication
from django.core.exceptions import ObjectDoesNotExist

def first_check(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated :
            user = request.user
            personal_details = PersonalDetails.objects.get(user= user)
            address_details = AddressDetails.objects.get(user=user)
            bank_details = BankDetails.objects.get(user=user)
            if personal_details.first_time == True :
                if address_details.first_time == True:
                    if bank_details.first_time == True:
                        return redirect("dashboard-home")
                    else:
                        return redirect("bank")
                else:
                    return redirect("address")
            else :
                return redirect("registerCom")

            
            return func(request, *args, **kwargs)
        else:
            return redirect("dashboard:dashboard-home")
    return wrapper



def check_personal_detail(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        user = request.user
        personal_details = PersonalDetails.objects.get(user=user)
        
        if personal_details.first_time:
            return redirect("address")
        else:
            return func(request, *args, **kwargs)
    return wrapper
        
# def check_address_detail(func):
#     @wraps(func)
#     def wrapper(request, *args, **kwargs):
#         user = request.user
#         address_details = AddressDetails.objects.get(user=user)
#         if address_details.first_time:
#             return redirect("dashboard-home")
#         else:
#             return func(request, *args, **kwargs)
#     return wrapper

def check_address_detail(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        user = request.user
        try:
            address_details = AddressDetails.objects.get(user=user)
            if address_details.first_time:
                return redirect("bank")
            else:
                return func(request, *args, **kwargs)
        except AddressDetails.DoesNotExist:
            
            return func(request, *args, **kwargs)
    return wrapper
    
# def check_bank_detail(func):
#     @wraps(func)
#     def wrapper(request, *args, **kwargs):
#         user = request.user
#         bank_details = BankDetails.objects.get(user=user)
#         if bank_details.first_time:
#             return redirect("dashboard-home")
#         else:
#             return func(request, *args, **kwargs)
#     return wrapper

def check_bank_detail(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        user = request.user
        try:
            bank_details = BankDetails.objects.get(user=user)
            if bank_details.first_time:
                return redirect("dashboard-home")
            else:
                return func(request, *args, **kwargs)
        except BankDetails.DoesNotExist:
           
            return func(request, *args, **kwargs)
    return wrapper

# def check_all_detail(func):
#     @wraps(func)
#     def wrapper(request, *args, **kwargs):
#         if request.user.is_authenticated:
#             user = request.user
#             personal_details = PersonalDetails.objects.get(user=user)
#             address_details = AddressDetails.objects.get(user=user)
#             bank_details = BankDetails.objects.get(user=user)
#             if not personal_details.first_time:
#                 if not  address_details.first_time:
#                     if not bank_details.first_time:
#                         return redirect("dashboard-home")
#                     else:
#                         return redirect("bank")
#                 else:
#                     return redirect("address")
#             else:
#                 return redirect("registerCom")
#         else:
#             return redirect("dashboard-application")
#     return wrapper

# def check_all_detail(func):
#     @wraps(func)
#     def wrapper(request, *args, **kwargs):
#         user = request.user
#         try:
#             personal_details = PersonalDetails.objects.get(user=user)
#             address_details = AddressDetails.objects.get(user=user)
#             bank_details = BankDetails.objects.get(user=user)
#         except ObjectDoesNotExist:
           
#             return redirect("registerCom")
        
#         if not personal_details.first_time:
#             if not address_details.first_time:
#                 if not bank_details.first_time:
                    
#                     return redirect("dashboard-home")
#                 else:
                    
#                     return redirect("bank")
#             else:
                
#                 return redirect("address")
#         else:
           
#             return redirect("registerCom")
#     return wrapper