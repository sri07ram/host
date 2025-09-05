from django.urls import path
from .views import CreateHosView,GetHosView,UpdateHosView,DeleteHosView

urlpatterns=[
    path('hospital/',CreateHosView.as_view(),name='hospital'),
    path('hospital/update/',UpdateHosView.as_view(),name='hospital'),
    path('hospital/get/',GetHosView.as_view(),name='hospital'),
    path('hospital/delete/',DeleteHosView.as_view(),name='hospital')
]