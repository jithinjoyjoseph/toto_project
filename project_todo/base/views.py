from django.contrib.auth.mixins import LoginRequiredMixin  #then go to settings and add login_url
from django.shortcuts import render,redirect
from django.http import  HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView,FormView
from django.views.generic.list import ListView
from .models import Task
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm #for  formview
from django.contrib.auth import login



# Create your views here.

def index(request):
    return render(request,'base/index.html')


class CustomLogin(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('task')


class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user =form.save()
        if user is not None:
            login(self.request , user)
        return super(RegisterPage,self).form_valid(form)

    #similar to the use of loginrequiredmmixin but in function way
    def get(self,  *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('login')
        return super(RegisterPage,self).get(*args,**kwargs)


class Tasklist(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = "tasks"
    template_name = 'base/task_list.html'

    # to user authenticated list(one can't see others )
    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user = self.request.user)
        context['count'] = context['tasks'].filter(complete = False).count()

        search_input = self.request.GET.get('search-area') or ''     #when we not search there should a empty
        if search_input:
            context['tasks'] = context['tasks'].filter(
                    title__startswith =search_input)
        context['search_input'] = search_input
        return context


class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'base/task.html'


class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
    fields = ['title','description','complete']                  #["__all__"]
    success_url =reverse_lazy('task')
    template_name = 'base/taskcreate.html'

    #in create.html there will be user selecting dropdown we should change it so that no dropdown to select user there
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate,self).form_valid(form)



class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    fields = ['title','description','complete']
    success_url = reverse_lazy('task')
    template_name = 'base/taskupdate.html'


class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    success_url = reverse_lazy('task')
    context_object_name = "tasks"
    template_name = 'base/task_confirm_delete.html'






