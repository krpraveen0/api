from django.urls import path
from api.views import StudentCRUDCBV
urlpatterns = [
    path('api/',StudentCRUDCBV.as_view()),

]
