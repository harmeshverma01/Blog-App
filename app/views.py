from django.http import HttpResponse 
from django.shortcuts import render, reverse
from .models import PostModel, CommentModel, ContactModel
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login,  logout
from django.views import View
from django.utils.decorators import method_decorator

# def homepage(request):
#     posts = PostModel.objects.all().order_by('-id')
#     return render(request, 'app/homepage.html', {"posts" : posts})

class HomePageView(View):
    template_name = "app/homepage.html"
    def get(self, request):
        posts = PostModel.objects.all().order_by('-id')
        context = {
            "posts" : posts
            }
        return render(request, self.template_name, context)



# def single_post(request,id):
#     post = PostModel.objects.get(id=id)
#     comments = CommentModel.objects.filter(post=post).order_by("-id")
#     context={
#        "post" : post,
#        "comments" : comments
#     }
#     return render(request, 'app/single_page.html', context)
#     return HttpResponse("Single post with id : {}".format(id))

class SinglePostView(View):
    template_name = "app/single_page.html"
    def get(self, request, id):
        post = PostModel.objects.get(id=id)
        comments = CommentModel.objects.filter(post=post).order_by("-id")
        context={
            "post" : post,
            "comments" : comments
        }
        return render(request, self.template_name, context)
        
    def post(self, request, id=None):
        pass

# @login_required
# @require_http_methods(["POST"])
# def add_comment(request,post_id):
#     post_obj = PostModel.objects.get(id=post_id)
#     comment_obj = CommentModel(post=post_obj, owner=request.user, comment_body=request.POST["msg"])
#     comment_obj.save()
#     return HttpResponseRedirect(reverse("blog_app:single_post", args=(post_id)))

@method_decorator(login_required, name="dispatch")
class AddCommentView(View):
    
    def post(self, request, post_id):
        post_obj = PostModel.objects.get(id=post_id)
        comment_obj = CommentModel(post=post_obj, owner=request.user, comment_body=request.POST["msg"])
        comment_obj.save()
        return HttpResponseRedirect(reverse("blog_app:single_post", args=(post_id)))


@require_http_methods(["POST","GET"])    
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if not username or not password:
            return render(request, 'app/login.html',{"msg" : "Both Username and Password require to Login."})
        else:
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("blog_app:homepage"))
            else:
                return render(request, 'app/login.html',{"msg" : "Invalid Username and Password Conbination."})
    elif request.method == "GET":
        msg = request.GET.get("msg")
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("blog_app:homepage"))
        return render(request, 'app/login.html',{"msg":msg})


@require_http_methods(["GET","POST"])
def Signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")
        if not username or not email or not password or not password_confirm:
            return render(request, "app/signup.html", {"msg" : "All Fields are madetory for signup."})
        elif password != password_confirm:
            return render(request, "app/signup.html", {"msg" : "Password and Corfirm password is not matching."})
        elif User.objects.filter(username=username).exists():
            return render(request, "app/signup.html", {"msg" : "Username already exists. Please use a different username."})
        elif User.objects.filter(email=email).exists():
            return render(request, "app/signup.html", {"msg" : "Email id already exists. Please use a different Email id."})
        else:
            user = User.objects.create_user(username,email,password)
            return HttpResponseRedirect(reverse("blog_app:login_user") + "?msg=User Created Successfully. Please Login ")        
    else:
        return render(request, "app/signup.html",{})
    

def logout_user(request): 
    logout(request)
    return HttpResponseRedirect(reverse("blog_app:login_user"))
 
def about_page(request):
    return render(request, 'app/about.html')    


@require_http_methods(["POST" , "GET"])
@login_required
def add_contact(request):
    if request.method == "POST":
        Name = request.POST.get("name")
        email = request.POST.get("email")
        phone_number = request.POST.get("mobile")
        contact_body = request.POST.get("Msg")
        contact_obj = ContactModel.objects.create(Name=Name, email=email, phone_number=phone_number, contact_body=contact_body)
        contact_obj.save()
        return HttpResponseRedirect(reverse("blog_app:add_contact"))
    else:
        return render(request, "app/contact.html", {}) 