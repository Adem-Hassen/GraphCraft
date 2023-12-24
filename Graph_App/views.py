from django.shortcuts import render,redirect
from django.contrib import messages
from .models import function
from .graph import function_graph
# Create your views here.


def home(request):  
    return render(request,'home.html')




def user_login(request):
    
       functions=function.objects.all()
       return render(request,'graph_interface.html',{"functions":functions})
   
       
def plot(request):
    functions=function.objects.all()
    selected_function=request.POST['selected_function']

    graphic=function_graph(selected_function)
    if graphic==False:
         messages.success(request,"Please Select a Function.")
         return redirect("user_login")
    else:
         return render(request, 'graph_interface.html', {"functions":functions,'graphic': graphic})
    
