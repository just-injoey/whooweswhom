from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import User
# ,room,room_members,transaction,debt,final_transactions,Personal_income,Personal_expense
# Register your models here.

admin.site.register(User, UserAdmin)