from django.shortcuts import render,redirect
from .models import StudentProfile
from .forms import StudentForm

# students = [
#     {'id':1,'name':'Juan Dela Cruz'},
#     {'id': 2, 'name': 'Henson Intila'},
#     {'id': 3, 'name': 'Gina Cole'}
# ]

# Create your views here.
def home(request):
    students = StudentProfile.objects.all()
    context = {'stud': students}
    return render(request,'base/home.html', context)

def profile(request,pk):
    student = StudentProfile.objects.get(id=pk)
    context = {'student':student}
    return render(request, 'base/profile.html', context)

def register(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'base/student_form.html',context)

def updateStudent(request,pk):
    student = StudentProfile.objects.get(id=pk)
    form = StudentForm(instance=student)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form':form}
    return render(request, 'base/student_form.html',context)

def deleteStudent(request,pk):
    student = StudentProfile.objects.get(id=pk)
    if request.method == "POST":
        student.delete()
        return redirect('home')
    context = {'student':student}
    return render(request, 'base/delete.html', context)