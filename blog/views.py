from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View, UpdateView,DeleteView
from .forms import PostCreateForm
from .models import Post
from django.urls import reverse_lazy

# Create your views here.

#Mostrar los objetos de la base de datos
class BlogListView(View): 
    def get(self, request, *args, **Kwargs):
        posts = Post.objects.all()
        context = {
            "posts":posts
        }
        return render(request, 'blog_list.html', context)

#Crear objetos y registrarlos en la base de datos
class BlogCreateView(View):
    def get(self, request, *args, **kwargs):
        form=PostCreateForm()
        context = {    
            'form':form
        }
        return render(request, 'blog_create.html', context)
    def post(self, request, *args, **kwargs):
        if request.method=="POST":
            form=PostCreateForm(request.POST)
            if form.is_valid():
                tittle= form.cleaned_data.get('tittle')
                content = form.cleaned_data.get('content')
                p, created = Post.objects.get_or_create(tittle=tittle, content=content)
                p.save()
                return redirect('blog:home')

        context = {    
        }
        return render(request, 'blog_create.html', context)

#Detalla mostrando los campos del objeto creado
class BlogDetailView(View):
    def get(self, request, pk,*args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        context = {
            "post":post
        }
        return render(request, 'blog_detail.html', context)

#Actualiza los campos de un objeto en la base de datos
class Update_view(UpdateView):
    model = Post
    fields = ['tittle','content']
    template_name='blog_update.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('blog:detail', kwargs={'pk':pk})

#Borra un objeto de la base de datos
class BlogDeleteView(DeleteView):
    model= Post
    template_name='blog_delete.html'
    success_url = reverse_lazy('blog:home')

