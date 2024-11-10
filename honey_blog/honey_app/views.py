from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddCommentForm
from .models import Honey, Comment
from user_honey.models import UserHoney

def honey_list(request):
    honeys = Honey.objects.all()
    return render(request, "honey_list.html", {"honeys": honeys})

def honey_detail(request, honey_id):
    honey = get_object_or_404(Honey, pk=honey_id)
    comments = honey.comment_set.all() 

    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.honey = honey
            user_honey = UserHoney.objects.filter(user=request.user, honey=honey).first()
            if user_honey:
                comment.user = user_honey  
                comment.save()
                return redirect('honey_detail', honey_id=honey_id)
    else:
        form = AddCommentForm()

    return render(request, 'honey_detail.html', {'honey': honey, 'comments': comments, 'form': form})

@login_required
def add_comment(request, honey_id):
    honey = get_object_or_404(Honey, id=honey_id) 
    if request.method == "POST":
        form = AddCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            user_honey = UserHoney.objects.filter(user=request.user, honey=honey).first()
            if user_honey:
                comment.user = user_honey  
                comment.honey = honey  
                comment.save()
                return redirect('honey_detail', honey_id=honey_id)
    else:
        form = AddCommentForm()
    return render(request, "add_comment.html", {"form": form, "honey": honey})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')