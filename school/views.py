from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import FeedBackUser, Teacher, Program, Event, Student, Grade, Review, Testimonial
from .serializers import *

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['get'])
    def reviews(self, request, pk=None):
        program = self.get_object()
        reviews = program.reviews.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]

class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [permissions.IsAuthenticated]
    





class FeedBackUserViewSet(viewsets.ModelViewSet):
    queryset = FeedBackUser.objects.all()
    serializer_class = FeedBackUserSerializer
    permission_classes = [permissions.AllowAny]  # tout le monde peut envoyer un feedback

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all().order_by("-created_at")
    serializer_class = TestimonialSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

   