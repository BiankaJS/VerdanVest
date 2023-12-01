from django.urls import path
from . import views

app_name='detail'
urlpatterns = [
    path('dashboard/', views.dashboardmarca_view, name='dashboard')
]