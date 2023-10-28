from django.urls import path
from . import views

urlpatterns = [
    path('get_user_owner/', views.get_user_owner, name='get_user_owner'),
    path('branches/', views.branches, name='branches'),
    path('category/', views.category, name='category'),
    path('commision/', views.commision, name='commision'),
    path('surfacepursant/', views.surfacePursant, name='surfacepursant'),
    path('sellingpursant/', views.sellingPursant, name='sellingpursant'),
    path('premium/', views.premium, name='premium'),
    path('compress/', views.compress, name='compress')
]