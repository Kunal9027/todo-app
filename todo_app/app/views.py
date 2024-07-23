from django.shortcuts import render , redirect , HttpResponse
from django.contrib.auth import authenticate , login , logout
from app.models import Task

# Create your views here.

def home(request):
    
    status = {'success':False}
    
    if request.method == "POST":        
        Title = request.POST['title']  # "title" is the Id , name from forms.html
        desc = request.POST['desc']    # "desc" is the Id , name from forms.html
        print("Title :" + Title, "Description :" + desc)

          
        # ins instace
        ins = Task(title = Title , Desc = desc)
        ins.save()
        
        status = {'success':True}
        
        
    return render(request ,"index.html" , status)

def tasks(request):
    allTasks = Task.objects.all()
    context = {"tasks": allTasks,}
    
    if request.method == "POST":
        if "delete" in request.POST:
            pk = request.POST.get('delete') #id or pk primary of the data
            deleteTask = Task.objects.get(id=pk)
            deleteTask.delete()
    
        
    
    
    return render(request ,"tasks.html" , context)


def login_view(request):
    
    if request.method =="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('home')
        
        else:
            return redirect('login')
        
        
    return render(request , "auth/login.html")
 
def logout_view(request):
    logout(request  )
    
    return redirect('home')
    
