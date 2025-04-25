# from django.shortcuts import render

# # Create your views here.
# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.views import View
# from django.contrib.auth import login

# class RegisterView(View):
#     def get(self, request):
#         form = UserCreationForm()
#         return render(request, 'registration/register.html', {'form': form})
    
#     def post(self, request):
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)  # Automatically log in the user after registration
#             return redirect('home')  # Redirect to home page after successful registration
#         return render(request, 'registration/register.html', {'form': form})

# from django.contrib.auth.views import LoginView

# class CustomLoginView(LoginView):
#     template_name = 'registration/login.html'

# from django.contrib.auth import logout
# from django.shortcuts import redirect

# class LogoutView(View):
#     def get(self, request):
#         logout(request)
#         return redirect('login')

# from django.shortcuts import render, redirect
# from django.views import View
# from django.contrib.auth.decorators import login_required

# # from django.shortcuts import render, redirect
# # from django.views import View
# # from django.contrib.auth.mixins import LoginRequiredMixin

# # class HomeView(View):
# #     def get(self, request):
# #         if request.user.is_authenticated:
# #             return redirect('booking')  # Redirect to the booking page or user dashboard
# #         return render(request, 'home.html')  # Show homepage if not authenticated

# # booking/views.py

# from django.views import View
# from django.shortcuts import render, redirect
# from django.contrib.auth.mixins import LoginRequiredMixin

# class HomeView(View):
#     def get(self, request):
#         if request.user.is_authenticated:
#             return redirect('booking')  # Be sure 'booking' is not the homepage
#         return render(request, 'home.html')

# class BookingView(LoginRequiredMixin, View):
#     def get(self, request):
#         return render(request, 'booking.html')


from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Show, Booking

class HomeView(View):
    def get(self, request):
        return render(request, 'booking/home.html')

class RegisterView(View):
    def get(self, request):
        return render(request, 'booking/register.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            return render(request, 'booking/register.html', {'error': 'Username exists'})
        User.objects.create_user(username=username, password=password)
        return redirect('login')

class LoginView(View):
    def get(self, request):
        return render(request, 'booking/login.html')

    def post(self, request):
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('show_list')
        return render(request, 'booking/login.html', {'error': 'Invalid credentials'})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')

class ShowListView(View):
    def get(self, request):
        shows = Show.objects.all()
        return render(request, 'booking/show_list.html', {'shows': shows})

class BookingView(LoginRequiredMixin, View):
    def get(self, request, show_id):
        show = get_object_or_404(Show, id=show_id)
        return render(request, 'booking/booking.html', {'show': show})

    def post(self, request, show_id):
        show = get_object_or_404(Show, id=show_id)
        seats = int(request.POST['seats'])
        if seats > 0 and seats <= show.total_seats:
            show.total_seats -= seats
            show.save()
            Booking.objects.create(user=request.user, show=show, seats=seats)
            return redirect('booking_history')
        return render(request, 'booking/booking.html', {'show': show, 'error': 'Invalid seat count'})

class BookingHistoryView(LoginRequiredMixin, View):
    def get(self, request):
        bookings = Booking.objects.filter(user=request.user)
        return render(request, 'booking/history.html', {'bookings': bookings})

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

class ShowManageView(AdminRequiredMixin, View):
    def get(self, request):
        shows = Show.objects.all()
        return render(request, 'booking/show_manage.html', {'shows': shows})

class ShowCreateView(AdminRequiredMixin, View):
    def get(self, request):
        return render(request, 'booking/show_form.html')

    def post(self, request):
        Show.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            date=request.POST['date'],
            time=request.POST['time'],
            total_seats=request.POST['total_seats']
        )
        return redirect('admin_shows')

class ShowUpdateView(AdminRequiredMixin, View):
    def get(self, request, pk):
        show = get_object_or_404(Show, pk=pk)
        return render(request, 'booking/show_form.html', {'show': show})

    def post(self, request, pk):
        show = get_object_or_404(Show, pk=pk)
        show.title = request.POST['title']
        show.description = request.POST['description']
        show.date = request.POST['date']
        show.time = request.POST['time']
        show.total_seats = request.POST['total_seats']
        show.save()
        return redirect('admin_shows')

class ShowDeleteView(AdminRequiredMixin, View):
    def get(self, request, pk):
        show = get_object_or_404(Show, pk=pk)
        show.delete()
        return redirect('admin_shows')

class CancelBookingView(LoginRequiredMixin, View):
    def get(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk, user=request.user)
        # Restore the seats
        booking.show.total_seats += booking.seats
        booking.show.save()
        booking.delete()
        return redirect('booking_history')
