from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from tasks.models import Position, Tag, Task, TaskType, Worker


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name",)


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("name", "task_type", "priority", "deadline", "is_completed", "created_at")
    list_filter = ("is_completed", "priority", "task_type")
    search_fields = ("name", "description")
    filter_horizontal = ("assignees", "tags")


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Company info", {"fields": ("position",)}),
    )
    list_display = UserAdmin.list_display + ("position",)
    list_filter = UserAdmin.list_filter + ("position",)
