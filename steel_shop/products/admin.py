from django.contrib import admin

from . models import Category, Product, ProductSpecificationValue, Subcategory, Specification


class SpecificationInline(admin.TabularInline):
    model = ProductSpecificationValue
    min_num = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name_cat',)
    search_fields = ('name_cat',)
    # list_editable = ('name_cat',)
    empty_value_display = '-пусто-'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('base_price', 'discount', 'subcategory',)
    search_fields = ('subcategory',)
    # list_editable = ('base_price', 'discount',)
    empty_value_display = '-пусто-'
    inlines = (
        SpecificationInline,
    )


@admin.register(ProductSpecificationValue)
class ProductSpecificationValueAdmin(admin.ModelAdmin):
    list_display = ('product', 'specification', 'value',)
    search_fields = ('product',)
    # list_editable = ('value',)
    empty_value_display = '-пусто-'


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category',)
    search_fields = ('name',)
    # list_editable = ('slug',)
    empty_value_display = '-пусто-'


@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'subcategory',)
    search_fields = ('name',)
    # list_editable = ('name',)
    empty_value_display = '-пусто-'
