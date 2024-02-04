from django.contrib import admin
from .models import PersonalDetails, AddressDetails, BankDetails, LoanApplication

admin.site.register(PersonalDetails)
admin.site.register(AddressDetails)
admin.site.register(BankDetails)
admin.site.register(LoanApplication)
