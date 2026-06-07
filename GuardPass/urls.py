from django.urls import path
from . import views
urlpatterns=[
    path('add/',views.add_new_account),
    path('',views.show_accounts_list),
    path('account/<uuid:account_id>/',views.show_account,name= 'account'),
    path('delete/<uuid:account_id>/',views.delete, name= 'delete_account'),
]