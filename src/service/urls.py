
# Django
from django.urls import path

# Views 
from src.service.views import IsAuth

urlpatterns = [
    path('isauth/verification/', IsAuth.as_view(), name='isauth')        
]
