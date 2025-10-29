from django.contrib import admin
from django.utils.safestring import mark_safe
# Register your models here.
from django.contrib import admin
from .models import FeedBackUser, Teacher, Program, Event, Student, Grade, Review,Testimonial

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'description_preview')
    search_fields = ('name',)
    list_per_page = 20
    
    def description_preview(self, obj):
        return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description
    description_preview.short_description = 'Description'

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'teacher', 'price', 'seats', 'lessons', 'hours')
    list_filter = ('teacher', 'price', 'seats')
    search_fields = ('title', 'description')
    list_editable = ('price', 'seats', 'lessons', 'hours')
    list_per_page = 20

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time_from', 'time_to', 'location')
    list_filter = ('date', 'location')
    search_fields = ('title', 'description', 'location')
    date_hierarchy = 'date'
    list_per_page = 20

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject','image', 'grade_level')
    list_filter = ('grade_level', 'name')
    search_fields = ('name','grade_level')
    list_per_page = 20

 
@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('user', 'mark')
    list_filter = ('mark',)
    search_fields = ('user__username', 'user__first_name', 'user__last_name')
    list_editable = ('mark',)
    list_per_page = 20

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'program', 'created_at', 'comment_preview')
    list_filter = ('program', 'created_at')
    search_fields = ('user__username', 'program__title', 'comment')
    date_hierarchy = 'created_at'
    list_per_page = 20
    
    def comment_preview(self, obj):
        return obj.comment[:50] + '...' if len(obj.comment) > 50 else obj.comment
    comment_preview.short_description = 'Comment'
    


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'created_at')


@admin.register(FeedBackUser)
class FeedBackUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')
  

