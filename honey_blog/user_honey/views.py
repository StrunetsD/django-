from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import HoneyForm, UpdateHoneyForm
from .models import UserHoney
from honey_app.models import Honey


@login_required
def account_detail(request):
    user = request.user
    user_honey = UserHoney.objects.filter(user=user)
    return render(request, 'account_detail.html', {'user':user, 'user_honey':user_honey})

@login_required
def delete_post_honey(request, honey_id):
    user = request.user
    user_honey = get_object_or_404(UserHoney, pk=honey_id, user=user)
    honey = user_honey.honey
    if request.method == 'POST':
       user_honey.delete()
       if not UserHoney.objects.filter(honey=honey).exists():
           honey.delete()
       return redirect('account_detail')

    return render(request, 'account_detail.html')


@login_required
def add_honey(request):
    if request.method == 'POST':
        form = HoneyForm(request.POST, request.FILES)
        if form.is_valid():
            honey = form.save()
            UserHoney.objects.create(user=request.user, honey=honey)
            return redirect('account_detail')
    else:
        form = HoneyForm()
    return render(request, 'add_honey.html', {'form': form})


@login_required
def update_honey_article(request, honey_id):
    honey = get_object_or_404(Honey, pk= honey_id)
    if request.method == "POST":
        form = UpdateHoneyForm(request.POST, instance=honey)
        if form.is_valid():
            form.save()
            return redirect('account_detail')
    else:
        form = UpdateHoneyForm(instance=honey)

    return render(request, 'update.html', {"form":form, "honey": honey})        