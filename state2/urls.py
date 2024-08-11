from django.urls import path
from state2 import views

urlpatterns=[
    path('A',views.fest1),
    path('B',views.fest2),
    path('C',views.fest3)
]