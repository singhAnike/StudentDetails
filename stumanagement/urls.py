from django.urls import path
from .views import*

urlpatterns = [
         path('', welcome.as_view()),
    path('create/', CreateData.as_view()),

]
