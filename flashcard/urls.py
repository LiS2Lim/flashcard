from django.urls import path
from . import views

urlpatterns = [
    path('', views.FlashList.as_view(), name='FlashList'),
    path('flash/<int:pk>',views.FlashTest.as_view(),name='details')
]
