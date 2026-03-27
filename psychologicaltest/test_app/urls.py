from django.urls import path

from test_app import views

urlpatterns=[
    path('testdemo/',views.testdemo)
]