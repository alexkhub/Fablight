from django.urls import path

from .views import *

urlpatterns = [
    path('register/', UserRegistrationCreateView.as_view(), name='register'),
    path('list_users/', UserListView.as_view(), name='list_users'),
    path('user_detail/<int:id>/', UserRetrieveUpdateDestroyView.as_view(), name='user_detail')

]