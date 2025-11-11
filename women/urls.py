from django.urls import path
from . import views

app_name = 'women'

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('category/<slug:cat_slug>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('human/<slug:human_slug>/', views.HumanDetailView.as_view(), name='human_detail'),
    path('all-humans/', views.AllHumansView.as_view(), name='all_humans'),
    path('create/', views.CreateHuman.as_view(), name='create'),
    path('update/<int:pk>/', views.UpdateHuman.as_view(), name='update'),
    path('update/<slug:slug>/', views.UpdateHuman.as_view(), name='update_by_slug'),
    path('about/', views.AboutView.as_view(), name='about'),
]