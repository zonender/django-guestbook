from django.shortcuts import render, redirect
from .models import Comment
from .forms import CommentForm

# Create your views here.
# -date_added the minus infront of the field name means in reverse 
def index(request):
    comments = Comment.objects.order_by('-date_added')

    context = {'comments' : comments}

    return render(request, 'guestbook/index.html', context)

def sign(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = Comment(name=request.POST['name'], comment=request.POST['comment'])
            new_comment.save()
            return redirect('index')
    else:
        form = CommentForm()
    

    form = CommentForm() #instantiating the form, also must be imported on top.

    context = {'form' : form} #this enables us to pass the form to the template

    return render(request, 'guestbook/sign.html', context)