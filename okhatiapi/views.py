# views.py
from rest_framework import viewsets, permissions
from .models import OpeningHours, ExceptionDay
from .serializers import OpeningHoursSerializer, ExceptionDaySerializer
from .authentication import CustomAuthentication

from datetime import datetime, timedelta
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import OpeningHours, ExceptionDay

class OpeningHoursViewSet(viewsets.ModelViewSet):
    queryset = OpeningHours.objects.all()
    serializer_class = OpeningHoursSerializer
    # authentication_classes = [CustomAuthentication]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class ExceptionDayViewSet(viewsets.ModelViewSet):
    queryset = ExceptionDay.objects.all()
    serializer_class = ExceptionDaySerializer
    # authentication_classes = [CustomAuthentication]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CurrentWeekOpeningHours(APIView):
    def get(self, request):
        # Get the current date and the start of the current week
        today = datetime.now().date()
        start_of_week = today - timedelta(days=today.weekday())

        # Get the end of the current week
        end_of_week = start_of_week + timedelta(days=6)

        # Filter opening hours for the current week
        opening_hours = OpeningHours.objects.filter(
            day_of_week__range=[start_of_week.weekday(), end_of_week.weekday()]
        )

        # Get exception days for the current week
        exception_days = ExceptionDay.objects.filter(
            date__range=[start_of_week, end_of_week], is_closed=True
        )

        # Initialize dictionary to store opening hours for each day of the week
        week_schedule = {
            "Monday": None,
            "Tuesday": None,
            "Wednesday": None,
            "Thursday": None,
            "Friday": None,
            "Saturday": None,
            "Sunday": None,
        }

        # Iterate through the opening hours and exception days to update the schedule
        for hour in opening_hours:
            week_schedule[hour.get_day_of_week_display()] = {
                "opening_time": hour.opening_time.strftime("%H:%M"),
                "closing_time": hour.closing_time.strftime("%H:%M"),
            }

        for exception_day in exception_days:
            week_schedule[exception_day.date.strftime("%A")] = "Closed"

        return JsonResponse(week_schedule)
