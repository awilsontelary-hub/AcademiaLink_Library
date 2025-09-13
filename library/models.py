from django.db import models
from apps.accounts.models import User

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Category"

    def __str__(self):
        return self.name

class BookDetails(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='books')
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='uploaded_books')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Book Details"
        verbose_name_plural = "Book Details"

    def __str__(self):
        return self.title

class BookFile(models.Model):
    book = models.ForeignKey(BookDetails, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='books/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Book Files"
        verbose_name_plural = "Book Files"

    def __str__(self):
        return f"{self.book.title} - {self.file.name}"

class Recommendation(models.Model):
    book = models.ForeignKey(BookDetails, on_delete=models.CASCADE, related_name='recommendations')
    recommended_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recommendations')
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.book.title} recommended by {self.recommended_by.username}"
