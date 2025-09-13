from django.shortcuts import render, get_object_or_404
from django.http import FileResponse
from apps.accounts.decorators import teacher_required, student_required
from .models import BookDetails, BookFile
from django.http import HttpResponseForbidden

# Students can view all books
@student_required
def student_book_list(request):
    books = BookDetails.objects.all()
    return render(request, "library/student_book_list.html", {"books": books})

# Teachers can view all books
@teacher_required
def teacher_book_list(request):
    books = BookDetails.objects.all()
    return render(request, "library/teacher_book_list.html", {"books": books})

# Book download (for both roles)
def download_book_file(request, file_id):
    book_file = get_object_or_404(BookFile, id=file_id)
    
    # Restrict access: only authenticated teachers or students
    if not request.user.is_authenticated:
        return HttpResponseForbidden("You must be logged in.")
    
    return FileResponse(book_file.file, as_attachment=True)

# Create your views here.
