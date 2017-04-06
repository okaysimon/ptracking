from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from ProjectTracking.models import Requirement


class IndexView(generic.ListView):
    model = Requirement
    template_name = 'ProjectTracking/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['current_user'] = self.request.user
        return context


def add_view(request):
    if request.method == 'POST':
        name = request.POST['r_info_name'] if request.POST.get('r_info_name') else None
        submit_department = request.POST['r_info_submit_department'] if request.POST.get('r_info_submit_department') else None
        submit_person = request.POST['r_info_submit_person'] if request.POST.get('r_info_submit_person') else None
        value = request.POST['r_info_value'] if request.POST.get('r_info_value') else None
        print(name, submit_department, submit_person, value)
        return HttpResponseRedirect(reverse('ProjectTracking:index'))
    print(request.user.get_full_name())
    return render(request, 'ProjectTracking/add.html', {'current_user': request.user})


def change_view(request):
    print(request.POST)
    return render(request, 'ProjectTracking/change.html')


def login_view(request):
    errors = []
    if request.method == 'POST':
        username = request.POST['username'] if request.POST.get('username') else None
        password = request.POST['password'] if request.POST.get('password') else None
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('ProjectTracking:index'))
            else:
                errors.append('disabled account')
        else:
            errors.append('invalid user')
        print(username, password, user)
    return render(request, 'ProjectTracking/login.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('ProjectTracking:login'))
