from django.urls import path
from . import views

app_name = "library"

urlpatterns = [
    path("student/books/", views.student_book_list, name="student_books"),
    path("teacher/books/", views.teacher_book_list, name="teacher_books"),
    path("download/<int:file_id>/", views.download_book_file, name="download_book"),
]
