# Create your views here.
from email import message
from django.http import HttpResponse
from django.contrib import messages

from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .forms import LinkForm, LoginForm, ProfileCreateForm, ProfileEditForm, UserRegitrationForm
from .models import ProfileModel
from .filters import StoryFilter, BookFilter
from stories.models import Book

@login_required
def dashboard(request):
    return render(request, 'social/dashboard.html', {'dashboard':'dashboard'})


def profile_create_view(request):
    context = {}
    form = ProfileCreateForm(request.POST or None)
    form2 = LinkForm(request.POST or None)
    if form.is_valid():
        form.save()
        form2.save()
        try:
            return redirect('/users/profile_list_view/')
        except:
            pass
    context = {
        'form': form,
        'form2': form2,
    }
    return render(request, "views/profile_create_view.html", context)


def profile_list_view(request):
    story_list = ProfileModel.objects.order_by('name')
    story_filter = StoryFilter(request.GET, queryset=story_list)

    paginator = Paginator(story_filter.qs, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = { "page_obj": page_obj, "filter": story_filter,}

    return render(request, "views/profile_list_view.html", context)


def profile_detail_view(request, id):
    about = Book.objects.filter(about__in=id)
    authors = Book.objects.filter(authors__in=id)

    story_filter = BookFilter(request.GET, queryset=Book.objects.all())
    context_404 = { "data": get_object_or_404(ProfileModel,id=id), "filter": story_filter, "about":about, "authors":authors}
    return render(request, "views/profile_detail_view.html", context_404)

       
def profile_update_view(request, id):
    context = {}
    obj = get_object_or_404(ProfileModel,id=id)
    form = ProfileEditForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        try:
            return redirect('/users/profile_list_view/'+id)
        except:
            pass
    context['form'] = form
    return render(request, "views/profile_update_view.html", context)

def profile_delete_view(request, id):
    context = {}
    obj = get_object_or_404(ProfileModel,id=id)
    form = ProfileEditForm(request.POST or None, instance=obj)
    if request.method=="POST":
        obj.delete()
        try:
            return redirect('/users/profile_list_view')
        except:
            pass
    context['form'] = form
    return render(request, "views/profile_delete_view.html", context)


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username = cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.info(request,'Authenticated successfully')
                    return redirect('home')
                else:
                    messages.info(request,'Disabled account')
                    return redirect('/users/login/')

            else:
                messages.info(request,'Invalid account')
                return redirect('/users/login/')

    else:
        form = LoginForm()
    return render(request, 'social/login.html', {'form':form})

def register(request):
    if request.method == "POST":
        user_form = UserRegitrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'social/registered.html', {'new_user':new_user})
    else:
        user_form = UserRegitrationForm()
    return render(request, 'social/register.html', {'user_form':user_form})


def user_logout(request):
    logout(request)
    return redirect('home')