from django.contrib import admin

from products.models import Product, Access, Lesson, Belonging, Status


@admin.register(Access)
class AccessAdmin(admin.ModelAdmin):
    list_display = ("product", "user")


class BelongInline(admin.TabularInline):
    model = Belonging


class AccessInline(admin.TabularInline):
    model = Access


class StatusInline(admin.TabularInline):
    model = Status


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "owner")
    inlines = [
        AccessInline,
    ]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("name", "link", "duration")
    inlines = [
        BelongInline,
        StatusInline
    ]


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('user', 'lesson', 'time', 'status', 'date')


@admin.register(Belonging)
class BelongingAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'product')
