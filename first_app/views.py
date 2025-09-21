from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from . import forms
from .forms import NewUserForm

# Create your views here.
# # Not Used
# def index(request):
#     my_dic = {"insert_me":"This is dynmic content coming from views"}
#     print(my_dic["insert_me"])
#     # text = "This is simple text from views.py"
#     return render(request,"first_app/index.html",context=my_dic)

# def index(request):
#     my_web_access = AccessRecord.objects.all().order_by('date')
#     my_dic = {"access_record":my_web_access}
#     # print(my_dic["access_record"])
#     # text = "This is simple text from views.py"
#     return render(request,"first_app/index.html",context=my_dic)

# # Not Used
# def user(request):
#     user_acc = User.objects.all()
#     user_info = {"user_info":user_acc}
#     return render(request,"first_app/user.html",context=user_info)

# def user(request):
#     form = NewUserForm()

#     if request.method == 'POST':
#         form = NewUserForm(request.POST)

#         if form.is_valid():
#             form.save(commit=True)
#             return index(request)
#         else:
#             print('Form is Invalid')
#     return render(request,"first_app/user.html",{'form':form})

# def form_name_view(request):
#     form = forms.FormName()

#     if request.method == "POST":
#         form = forms.FormName(request.POST)

#         if form.is_valid():
#             # DO SOMETHING CODE
#             print("VALIDATION SUCCESS!")
#             print("NAME: "+form.cleaned_data['name'])
#             print("EMAIL: "+form.cleaned_data['email'])
#             print("TEX: "+form.cleaned_data['text'])

#     return render(request,'first_app/form_page.html',{'form':form})


def index(request):
    context_dict = {'text':'hello world','number':100}
    return render(request,'first_app/index.html',context_dict)

def other(request):
    return render(request,'first_app/other.html')

def relative(request):
    return render(request,'first_app/relative_url_template.html')
