from ast import List
from urllib import request
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from .models import Post,Profile
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


# class homeView(View):

#     def get(self,request):
        
#         post_obj = Post.objects.all().order_by('-created')
#         other_profiles = Profile.objects.all().exclude(user=request.user)
#         return render(request,'home.html',{'Posts':post_obj,'other_profiles':other_profiles})
    
class homeListView(ListView,LoginRequiredMixin):
    model = Post
    template_name = 'home.html'
    context_object_name = 'Posts'
    ordering = ["-created"]

    

    
    

class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post 
    template_name = 'post_detail.html'



    
    
    
class profileView(LoginRequiredMixin,View):
    
    def get(self,request):
        return render(request,'profile.html')


# class NewPost(View):
#     def get(self,request):
#         post_form = CreatePostForm()
#         context = {
#             "post_form":post_form
#         }
#         return render(request,'create_post.html',context)
#     def post(self,request):
#         post_form = CreatePostForm(request.POST, instance=request.user)
#         if post_form.is_valid():
#             post_form.save()
#             messages.success(request, 'Post has Created Successfully!')
#             return redirect('home')
        
class NewPost(CreateView,LoginRequiredMixin,UserPassesTestMixin):
    model = Post
    fields = ['title','desc','catagory']
    template_name = 'create_post.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    
    
    
    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','desc','catagory']
    template_name = 'update_post.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user: 
            print(post.user)
            return True
        return False
    
    
   
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Post
    success_url='/'
    template_name='post_confirm_delete.html'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user: 
            print(post.user)
            return True
        return False



class ProfileUpdateView(LoginRequiredMixin,UserPassesTestMixin,View):
    
    def get(self,request):
        u_form = UserUpdateForm()
        p_form = ProfileUpdateForm()
        context = {
            'u_form':u_form,
            'p_form':p_form
        }
        return render(request,'profile_update.html',context)
    
    def post(self,request):
        
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid() and u_form.is_valid() :
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
        
        else:
            # Handle the case where the forms are invalid
            context = {
                'u_form': u_form,
                'p_form': p_form
            }
            return render(request, 'profile_update.html', context)

    def test_func(self):
        post = self.request
        if self.request.user == post.user: 
            print(post.user)
            return True
        return False
        
       
        
                
    
# class loginView(View):
#     def get(self,request):
#         form = UserRegisterForm()
#         context = {
#             'form':form
#             }
#         return render(request,'login.html',context)
    
#     def post(self,request):
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username,password=password)
#             # if user != None:
#             login(request,user)
#             return redirect('home')
#         return render(request,'login.html',{'form':form})

    
class logoutView(View):
    def get(self,request):
        logout(request)
        return render(request,'logout.html')

class registerView(View):
    def get(self,request):
        
        form = UserRegisterForm()
        context = {
            'form':form
            }
        return render(request,'register.html',context)
    
    def post(self,request):
        
        form = UserRegisterForm(request.POST)
        print(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account Successfully created for {username}')
            return redirect('login')
        return render(request,'register.html',{'form':form})
        
        
      

