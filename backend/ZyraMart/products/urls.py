
from django.urls import path
from .views import *

urlpatterns = [
    path('add_category/', AddCategoryAPIView.as_view()),
    path('add-brand/', AddBrandAPIVew.as_view()),
    path('add-products/', AddProductAPIViw.as_view()),
]