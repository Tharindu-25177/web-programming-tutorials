from django.shortcuts import render, get_object_or_404
from .models import Student

def home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})

def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'student_detail.html', {'student': student})
