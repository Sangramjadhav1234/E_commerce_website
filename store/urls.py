from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='homepage'),  # Home page (product listing)
    path('store/', views.store, name='store'),  # Store page (filtered by category)
    path('login/', views.Login.as_view(), name='login'),  # Login page
    path('signup/', views.Signup.as_view(), name='signup'),  # Signup page
    path('cart/', views.CheckOut.as_view(), name='cart'),  # Cart page (checkout view)
    path('checkout/', views.CheckOut.as_view(), name='checkout'),  # Checkout page
    path('logout/', views.logout, name='logout'),  # Logout action
]
