from rest_framework import serializers
from django.contrib.auth.models import User
from .models import FeedBackUser, Teacher, Program, Event, Student, Grade, Review, Testimonial

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class ProgramSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(read_only = True)
    teacher_name = serializers.PrimaryKeyRelatedField(queryset = Teacher.objects.all(),
    source = "teacher",write_only= True)
    reviews_count = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Program
        fields = '__all__'

    def get_reviews_count(self, obj):
        return obj.reviews.count()

    def get_average_rating(self, obj):
        reviews = obj.reviews.all()
        if reviews:
            total = sum([review.rating for review in reviews if hasattr(review, 'rating')])
            return total / len(reviews)
        return 0

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    user_details = UserSerializer(source='user', read_only=True)

    class Meta:
        model = Student
        fields = '__all__'


class GradeSerializer(serializers.ModelSerializer):
    user_details = UserSerializer(source='user', read_only=True)
    student_name = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Grade
        fields = '__all__'
class FeedBackUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBackUser
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    user_details = UserSerializer(source='user', read_only=True)
    user_name = serializers.CharField(source='user.username', read_only=True)
    program_title = serializers.CharField(source='program.title', read_only=True)

    class Meta:
        model = Review
        fields = '__all__'

class TestimonialSerializer(serializers.ModelSerializer):
    rating_stars = serializers.SerializerMethodField()
    
    class Meta:
        model = Testimonial
        fields = '__all__'
    
    
    def perform_create(self, serializer):
        
        serializer.save(user=self.request.user)
    

    def get_rating_stars(self, obj):
        return obj.get_rating_stars()

# Serializers pour les inscriptions/authentification
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirmation', 'first_name', 'last_name']

    def validate(self, data):
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError("Les mots de passe ne correspondent pas.")
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirmation')
        user = User.objects.create_user(**validated_data)
        return user

class StudentRegistrationSerializer(serializers.ModelSerializer):
    user = UserRegistrationSerializer()

    class Meta:
        model = Student
        fields = ['user', 'date_of_birth', 'grade_level']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserRegistrationSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        
        student = Student.objects.create(user=user, **validated_data)
        return student