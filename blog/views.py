from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.core.mail import send_mail

from blog.forms import EmailPostForm
from blog.models import Post


# Create your views here.

def post_list(request):
    object_list = Post.objects.filter(status='published')
    paginator = Paginator(object_list, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver first page
        posts = paginator.page(1)
    except EmptyPage:
        # If age is out of range deliver the list of results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/index.html', {'page':page, 'posts':posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                               publish__day=day)
    return render(request, 'blog/detatil.html', {'post':post})

class PostListView(ListView):
    queryset = Post.objects.filter(status='published')
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/index.html'

def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status = 'published')

    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form Fields passed validation
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(
                post.get_absolute_url()
            )
            subject = '{} ({}) recommends you reading "{}"'.\
                format(cd['name'], cd['email'], post.Title)
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.\
                format(post.Title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'aetos.anatole@gmailcom', [cd['to']])
            sent = True

    else:
        form = EmailPostForm()
    return render(request, 'blog/share.html', {'post': post,
                                               'form': form})


def home_page(request):
    # post = get_object_or_404()
    return render(request, 'blog/Homepage.html')