
from django.urls import path, include
from . import views


urlpatterns = [

	path('dashboard/', views.get_dashboard, name='dashboard'),
	path('accounts/', include('django.contrib.auth.urls')),
	path('register/', views.register_user, name='register'),

]
