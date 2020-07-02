from django.urls import path

from . import views

app_name = 'stocks'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'), # instead of <int:pk> should be stock ticker
]
