from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from ProjectTracking.forms import RequirementForm
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
        form = RequirementForm(request.POST, request.FILES)
        if form.is_valid():
            requirement = form.save(commit=False)
            requirement.i_submit_time = timezone.now()
            requirement.i_submit_user = request.user
            if requirement.i_file:
                extension = requirement.i_file.name.split('.')[-1]
                requirement.i_file.name = requirement.i_name+'.V0.1.'+extension
            requirement.save()
            return HttpResponseRedirect(reverse('ProjectTracking:index'))
    else:
        form = RequirementForm()
    return render(request, 'ProjectTracking/add.html', {'current_user': request.user,
                                                        'form': form})


def filename_update(filename, requirement_name, value):
    tmp = filename.split('.')
    version = float('.'.join(tmp[-3:-1])[1:]) + value
    version = 'V' + str(version)
    extension = tmp[-1]
    return '.'.join([requirement_name, version, extension])


def change_view(request, r_id):
    requirement = Requirement.objects.get(r_id=r_id)
    name_old = requirement.i_file.name
    if request.method == 'POST':
        form = RequirementForm(request.POST, request.FILES, instance=requirement)
        if form.is_valid():
            requirement = form.save(commit=False)
            if name_old != requirement.i_file.name:
                requirement.i_file.name = filename_update(name_old, requirement.i_name, 0.1)
                print(requirement.i_file.name)
            requirement.save()
            return HttpResponseRedirect(reverse('ProjectTracking:index'))
    else:
        form = RequirementForm(instance=requirement)
    return render(request, 'ProjectTracking/change.html', {'current_user': request.user,
                                                           'requirement': requirement,
                                                           'form': form})


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
    return render(request, 'ProjectTracking/login.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('ProjectTracking:login'))
