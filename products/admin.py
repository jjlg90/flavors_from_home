from django.contrib import admin
from .models import Product, Category, Reviews

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'upc',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('upc',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ReviewsAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'title',
        'user_profile',
        'user_rating',
        'created',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Reviews, ReviewsAdmin)
