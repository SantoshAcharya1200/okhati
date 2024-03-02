# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OpeningHoursViewSet, ExceptionDayViewSet
from .views import CurrentWeekOpeningHours

router = DefaultRouter()
router.register(r'opening_hours', OpeningHoursViewSet)
router.register(r'exceptions', ExceptionDayViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('current_week_opening_hours/', CurrentWeekOpeningHours.as_view(), name='current_week_opening_hours'),

]
