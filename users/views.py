from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm as UserForm
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from mainapp.models import News
from blog.models import Post
from catalog.models import BusTour, Cruise
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from blog.forms import BlogPostForm
from mainapp.forms import NewsPostForm
from catalog.forms import BusTourForm, CruiseForm
from .forms import UserUpdateForm, ClientUpdateForm, ManagerRegistrationForm
from .models import ClientProfile, CLIENT, MANAGER
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        # Create an instance of UserRegistrationForm filled in with new user's data
        form  = UserForm(data=request.POST)
        # Check the form for validation
        if form.is_valid():
            reg_f = form.save()
            reg_f.is_staff = False # the access to admin section denied
            reg_f.is_active = True
            reg_f.is_superuser = False
            reg_f.date_joined = datetime.now()
            reg_f.last_login = datetime.now()
            reg_f.save() # save changes
            # Retrieve username from the form
            username = form.cleaned_data.get('username')
            # Display message about successfull registration
            messages.success(request, f'Учётная запись пользователя {username} успешно создана.')
            return redirect('login')
        else:
            for message in form.error_messages:
                messages.error(request, f'{message}: {form.error_messages[message]}')
    else:
        # Create an instance of UserCreationForm as a blank form
        form  = UserForm()

    return render(request,
                  'users/register.html',
                  {'form': form,
                  'title': 'Регистрация'})


@login_required
def profile(request):
    if request.user.profile.status == CLIENT:
        client = ClientProfile.objects.get(user=request.user)

        if request.method == 'POST':
            u_form = UserUpdateForm(data=request.POST, instance=request.user)
            c_form = ClientUpdateForm(data=request.POST, instance=client)
            if u_form.is_valid() and c_form.is_valid():
                u_form.save()
                c_form.save()
                messages.success(request, 'Данные профиля успешно обновлены.')
                return redirect('profile')
        else:
            u_form = UserUpdateForm(instance=request.user)
            c_form = ClientUpdateForm(instance=client)

        context = {
            'u_form': u_form,
            'c_form': c_form
        }
    else:
        if request.method == 'POST':
            u_form = UserUpdateForm(data=request.POST, instance=request.user)
            if u_form.is_valid():
                u_form.save()
                messages.success(request, 'Данные профиля успешно обновлены.')
                return redirect('profile')
        else:
            u_form = UserUpdateForm(instance=request.user)

        context = {
                'u_form': u_form
            }
   
    return render(request, 'users/profile.html', context)


class NewsEditListView(ListView):
    model = News
    template_name = 'users/news-edit.html'
    paginate_by = 5


class BlogEditListView(ListView):
    model = Post
    template_name = 'users/blog-edit.html'
    paginate_by = 5


@login_required
def catalog_list(request):
    return render(request, 'catalog/catalog-list.html')


class BusTourEditListView(ListView):
    model  = BusTour
    template_name = 'users/bustours-edit.html'
    paginate_by = 5


class CruiseEditListView(ListView):
    model = Cruise
    template_name = 'users/cruises-edit.html'
    paginate_by = 5


def managers_list(request):
    managers = User.objects.filter(profile__status='M')
    return render(request, 'users/managers-edit.html', context={'managers': managers})


class NewsPostDeleteView(DeleteView):
    model = News
    success_url = reverse_lazy('news-edit') # redirect a user to the home page after deletion
    template_name = 'users/newspost_confirm_delete.html'


class BlogPostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog-edit') 
    template_name = 'users/blogpost_confirm_delete.html'


class BusTourDeleteView(DeleteView):
    model = BusTour
    success_url = reverse_lazy('bustours-edit')
    template_name = 'users/bustour_confirm_delete.html'


class CruiseDeleteView(DeleteView):
    model = Cruise
    success_url = reverse_lazy('cruises-edit')
    template_name = 'users/cruise_confirm_delete.html'


@login_required
def manager_confirm_delete(request, pk):
    manager = get_object_or_404(User, id=pk)
    if request.method == 'POST':
        manager.delete()
        return redirect('managers-edit')

    return render(request, 'users/manager_confirm_delete.html', {'object': manager})


@login_required
def blogpost_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            messages.success(request, f'Пост "{title}" успешно добавлен.')
            return redirect('blog-edit')
        else:
            for message in form.error_messages:
                messages.error(request, f'{message}: {form.error_messages[message]}')
    else:
        # create a blank form
        form = BlogPostForm()

    context = {
        'form': form,
        'title': 'Добавить пост'
    }

    return render(request,
                  'users/create-form.html',
                  context)


@login_required
def newspost_create(request):
    if request.method == 'POST':
        form = NewsPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            messages.success(request, f'Новость "{title}" успешно добавлена.')
            return redirect('news-edit')
        else:
            for message in form.error_messages:
                messages.error(request, f'{message}: {form.error_messages[message]}')
    else:
        # create a blank form
        form = NewsPostForm()

    context = {
        'form': form,
        'title': 'Добавить новость'
    }

    return render(request,
                  'users/create-form.html',
                  context)


@login_required
def bustour_create(request):
    if request.method == 'POST':
        form = BusTourForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            messages.success(request, f'Автобусный тур "{title}" успешно добавлен.')
            return redirect('bustours-edit')
        else:
            for message in form.error_messages:
                messages.error(request, f'{message}: {form.error_messages[message]}')
    else:
        # create a blank form
        form = BusTourForm()

    context = {
        'form': form,
        'title': 'Добавить автобусный тур'
    }

    return render(request,
                  'users/create-form.html',
                  context)


@login_required
def cruise_create(request):
    if request.method == 'POST':
        form = CruiseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            messages.success(request, f'Круиз "{title}" успешно добавлен.')
            return redirect('cruises-edit')
        else:
            for message in form.error_messages:
                messages.error(request, f'{message}: {form.error_messages[message]}')
    else:
        # create a blank form
        form = CruiseForm()

    context = {
        'form': form,
        'title': 'Добавить круиз'
    }

    return render(request,
                  'users/create-form.html',
                  context)

@login_required
def manager_create(request):
    if request.method == 'POST':
        form = ManagerRegistrationForm(data=request.POST)
        if form.is_valid():
            reg_f = form.save()
            reg_f.is_active = True
            reg_f.is_superuser = False
            reg_f.date_joined = datetime.now()
            reg_f.last_login = datetime.now()
            reg_f.save() # save changes
            username = form.cleaned_data.get('username')
            messages.success(request, f'Менеджер {username} успешно зарегистрирован.')
            return redirect('managers-edit')
        else:
            for message in form.error_messages:
                messages.error(request, f'{message}: {form.error_messages[message]}')
    else:
        form = ManagerRegistrationForm()

    return render(request, 'users/register-manager.html', {'form': form})
