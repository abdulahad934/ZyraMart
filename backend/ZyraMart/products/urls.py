
from django.urls import path
from .views import *

urlpatterns = [
    path('add_category/', add_category),
    path('add-brand/', add_brand),
    path('add-products/', AddProductAPIView.as_view()),
]