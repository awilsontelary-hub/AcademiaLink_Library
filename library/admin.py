from django.contrib import admin
from .models import Category, BookDetails, BookFile, Recommendation

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(BookDetails)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'uploaded_by', 'created_at')
    search_fields = ('title', 'author')
    list_filter = ('category',)

@admin.register(BookFile)
class BookFileAdmin(admin.ModelAdmin):
    list_display = ('id','book', 'file', 'uploaded_at')
    search_fields = ('book','file')


@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ('book', 'recommended_by', 'created_at')
