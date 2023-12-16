from django.urls import path
from .views import AnimalsView, LoginView


urlpatterns = [
    path('animals/', AnimalsView.as_view(), name='animals'),
    path('login/', LoginView.as_view(), name='login')
]
