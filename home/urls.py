from .views import *
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns =[
    path('', HomeView.as_view(),name='home'),
    path('category/<slug>', CategoryView.as_view(),name='category'),
    path('search', SearchView.as_view(),name='search'),
    path('details/<slug>', ProductDetailView.as_view(),name='details'),
    path('signup', signup,name='signup'),
    path('product_review/<slug>', product_review, name = 'product_review'),
    path('cart/<slug>', cart, name='cart'),
    path('my_cart', CartView.as_view(), name ='my_cart'),
    path('reduce_cart/<slug>', decrease_quantity, name='reduce_cart'),
    path('delete_cart/<slug>', delete_cart, name = 'delete_cart'),

    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),






]