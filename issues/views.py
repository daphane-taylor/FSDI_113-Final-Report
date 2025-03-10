from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Issue, Status

class IssueListView(LoginRequiredMixin, ListView):
    model = Issue
    template_name = "issues/issue_list.html"
    context_object_name = "issues"
    
class IssueDetailView(LoginRequiredMixin, DetailView):
    model = Issue
    template_name = "issues/issue_detail.html"
    context_object_name = "issue"

class IssueCreateView(LoginRequiredMixin, CreateView):
    model = Issue
    template_name = "issues/issue_new.html"
    fields = ["name", "summary", "description", "assignee", "status"]
    
    def form_valid(self, form):
        form.instance.reporter = self.request.user
        return super().form_valid(form)

class IssueUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Issue
    template_name = "issues/issue_edit.html"
    fields = ["name", "summary", "description", "assignee", "status"]
    
    def test_func(self):
        issue = self.get_object()
        return self.request.user == issue.reporter or self.request.user.is_staff

class IssueDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Issue
    template_name = "issues/issue_delete.html"
    success_url = reverse_lazy("issue_list")
    
    def test_func(self):
        issue = self.get_object()
        return self.request.user == issue.reporter or self.request.user.is_staff