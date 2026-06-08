from django.contrib import admin
from .models import ex_accounts
# Register your models here
@admin.register(ex_accounts)
class ex_accounts_admin(admin.ModelAdmin):
     list_display=('id','owner','UserName','Password','bio')
     readonly_fields=('decrypt_UserName','decrypt_Password','decrypt_bio')