from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Evenement
from .forms import AdminForm,UpdateAdminForm,LoginAdminForm,EventForm,User


def visu_event(request):
    all_event = Evenement.objects.all()
    return render(request, 'client/visu_event.html', {'all_event' : all_event, 'user': request.user})

def visu_detail(request, even_id):
    event = get_object_or_404(Evenement, pk = even_id)
    return render(request, 'client/visu_detail.html', {"event" : event, 'user': request.user})

def crea_compte(request):
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = AdminForm()

    return render(request, 'admin/crea_compte.html', {'form': form, 'user': request.user})

def cre_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = EventForm()

    return render (request, 'admin/crea_event.html',{'form':form, 'user': request.user})


def modif_compte(request,admin_id):
    admin = get_object_or_404(User, pk = admin_id)
    if request.method == 'POST':
        form = UpdateAdminForm(request.POST,instance=admin)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:

        form = UpdateAdminForm(instance=admin)
    return render(request,'admin/modif_compte.html',{'form':form,'admin' : admin, 'user': request.user})

# def archiver_compte(request,admin_id):
#     admin = Admin.objects.filter(id=admin_id)[0]
#     admin.admin_is_archived = True
#     admin.save()
#     return visu_event(request) # l'url pue la merde en faisant ca

@login_required
def admin_display(request):
    all_admins = User.objects.all()
    return render(request, 'admin/afficher_admin.html', {'all_admins': all_admins, 'user': request.user})


def admin_login(request):
    if request.method == 'POST':
        form = LoginAdminForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=request.POST['email'], password=request.POST['password'])
            if user is not None and user.is_active:
                login(request=request, user=user)
                return HttpResponseRedirect('/')
    else:
        form = LoginAdminForm()
    return render(request, 'admin/connection.html', {'form': form, 'user': request.user})

@login_required
def admin_logout(request):
    logout(request)
    return HttpResponseRedirect('/')