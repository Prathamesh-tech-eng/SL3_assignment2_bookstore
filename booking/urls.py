# # from django.urls import path
# # from . import views

# # urlpatterns = [
# #     path('register/', views.RegisterView.as_view(), name='register'),
# #     path('login/', views.CustomLoginView.as_view(), name='login'),
# #     path('logout/', views.LogoutView.as_view(), name='logout'),
# # ]

# # from django.contrib import admin
# # from django.urls import path, include

# # urlpatterns += [
# #     path('admin/', admin.site.urls),
# #     # path('accounts/', include('booking.urls')),  # Add this line for authentication URLs
    
# # ]

# # from django.urls import path
# # from . import views

# # urlpatterns += [
# #     path('register/', views.RegisterView.as_view(), name='register'),
# #     path('login/', views.CustomLoginView.as_view(), name='login'),
# #     path('logout/', views.LogoutView.as_view(), name='logout'),
# # ]

# # from django.urls import path
# # from booking.views import HomeView, BookingView  # Assuming BookingView is created

# # urlpatterns += [
# #     path('admin/', admin.site.urls),
# #     path('accounts/', include('booking.urls')),  # Authentication URLs
# #     path('', HomeView.as_view(), name='home'),   # Home page route
# #     path('booking/', BookingView.as_view(), name='booking'),  # Add a route for booking page
# # ]
# # booking/urls.py

# from django.urls import path
# from .views import CustomLoginView, RegisterView, LogoutView, BookingView

# urlpatterns = [
#     path('login/', CustomLoginView.as_view(), name='login'),
#     path('register/', RegisterView.as_view(), name='register'),
#     path('logout/', LogoutView, name='logout'),
#     path('booking/', BookingView.as_view(), name='booking'),
# ]

from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('shows/', ShowListView.as_view(), name='show_list'),
    path('book/<int:show_id>/', BookingView.as_view(), name='book_show'),
    path('history/', BookingHistoryView.as_view(), name='booking_history'),
    path('admin/shows/', ShowManageView.as_view(), name='admin_shows'),
    path('admin/shows/add/', ShowCreateView.as_view(), name='add_show'),
    path('admin/shows/edit/<int:pk>/', ShowUpdateView.as_view(), name='edit_show'),
    path('admin/shows/delete/<int:pk>/', ShowDeleteView.as_view(), name='delete_show'),
    path('cancel/<int:pk>/', CancelBookingView.as_view(), name='cancel_booking'),

]
