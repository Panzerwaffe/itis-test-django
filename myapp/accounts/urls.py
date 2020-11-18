from django.urls import path
from . import views as signup

urlpatterns = [
	path('account/', signup.account, name='account'),
	path('signup/', signup.SignUp.as_view(), name='signup'),
]
