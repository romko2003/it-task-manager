from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.decorators.http import require_POST

from tasks.forms import TaskForm
from tasks.models import Position, Tag, Task, TaskType

Worker = get_user_model()


class IndexView(LoginRequiredMixin, generic.RedirectView):
    pattern_name = "tasks:task-list"


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    paginate_by = 10

    def get_queryset(self):
        qs = (
            super()
            .get_queryset()
            .select_related("task_type")
            .prefetch_related("assignees", "tags")
        )

        q = self.request.GET.get("q", "").strip()
        status = self.request.GET.get("status", "").strip()  # done / todo / ""
        task_type = self.request.GET.get("task_type", "").strip()
        priority = self.request.GET.get("priority", "").strip()
        assignee = self.request.GET.get("assignee", "").strip()

        if q:
            qs = qs.filter(Q(name__icontains=q) | Q(description__icontains=q))

        if status == "done":
            qs = qs.filter(is_completed=True)
        elif status == "todo":
            qs = qs.filter(is_completed=False)

        if task_type.isdigit():
            qs = qs.filter(task_type_id=int(task_type))

        if priority:
            qs = qs.filter(priority=priority)

        if assignee.isdigit():
            qs = qs.filter(assignees__id=int(assignee)).distinct()

        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["task_types"] = TaskType.objects.all()
        ctx["workers"] = Worker.objects.all()
        ctx["priorities"] = Task.Priority.choices

        # keep filters in templates
        ctx["q"] = self.request.GET.get("q", "")
        ctx["status"] = self.request.GET.get("status", "")
        ctx["task_type_selected"] = self.request.GET.get("task_type", "")
        ctx["priority_selected"] = self.request.GET.get("priority", "")
        ctx["assignee_selected"] = self.request.GET.get("assignee", "")
        return ctx


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm

    def get_success_url(self):
        return reverse("tasks:task-detail", kwargs={"pk": self.object.pk})


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm

    def get_success_url(self):
        return reverse("tasks:task-detail", kwargs={"pk": self.object.pk})


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:task-list")


@require_POST
def toggle_task_status(request, pk: int):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = not task.is_completed
    task.save(update_fields=["is_completed"])
    return HttpResponseRedirect(request.META.get("HTTP_REFERER", reverse("tasks:task-list")))


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    paginate_by = 10
    template_name = "tasks/worker_list.html"


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker
    template_name = "tasks/worker_detail.html"


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    fields = ("name",)
    success_url = reverse_lazy("tasks:position-list")


class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    fields = ("name",)
    success_url = reverse_lazy("tasks:position-list")


class PositionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    success_url = reverse_lazy("tasks:position-list")


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    fields = ("name",)
    success_url = reverse_lazy("tasks:tasktype-list")


class TaskTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    fields = ("name",)
    success_url = reverse_lazy("tasks:tasktype-list")


class TaskTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    success_url = reverse_lazy("tasks:tasktype-list")


class TagListView(LoginRequiredMixin, generic.ListView):
    model = Tag


class TagCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tag
    fields = ("name",)
    success_url = reverse_lazy("tasks:tag-list")


class TagUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tag
    fields = ("name",)
    success_url = reverse_lazy("tasks:tag-list")


class TagDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:tag-list")
