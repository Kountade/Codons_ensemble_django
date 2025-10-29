from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (FeedBackUserViewSet,TeacherViewSet, ProgramViewSet,EventViewSet,StudentViewSet,GradeViewSet,ReviewViewSet,TestimonialViewSet
)

router = DefaultRouter()
router.register(r'teachers', TeacherViewSet, basename='teacher')
router.register(r'programs', ProgramViewSet, basename='program')
router.register(r'events', EventViewSet, basename='event')
router.register(r'students', StudentViewSet, basename='student')
router.register(r'grades', GradeViewSet, basename='grade')
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'testimonials', TestimonialViewSet, basename='testimonial')
router.register(r'feedbacks', FeedBackUserViewSet, basename='feedback')

urlpatterns = [
    path('', include(router.urls)),
]
