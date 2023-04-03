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
    path('wish/<slug>',wish,name='wish'),
    path('my_wish', WishListView.as_view(),name ='my_wish'),
    path('delete_wish/<slug>', delete_wish, name='delete_wish'),
    path('contact',contact, name= 'contact'),
    path('checkout', CheckoutView.as_view(),name='checkout'),
    path('checker/<slug>', checker, name = 'checker'),
    path('billings', billing, name = 'billings'),
    path('thanks', thank, name = 'thanks'),


    # for password recovery
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),


]