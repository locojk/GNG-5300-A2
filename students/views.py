from django.shortcuts import render, get_object_or_404, redirect
from .models import Student

# View to list all students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

# View to display a single student's details
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})

# View to add a new student
def student_create(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        date_of_birth = request.POST['date_of_birth']
        enrollment_date = request.POST['enrollment_date']
        grade = request.POST['grade']
        
        # Create and save new student
        Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            date_of_birth=date_of_birth,
            enrollment_date=enrollment_date,
            grade=grade
        )
        return redirect('student_list')

    return render(request, 'students/student_form.html')

# View to edit an existing student's information
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    
    if request.method == 'POST':
        student.first_name = request.POST['first_name']
        student.last_name = request.POST['last_name']
        student.email = request.POST['email']
        student.date_of_birth = request.POST['date_of_birth']
        student.enrollment_date = request.POST['enrollment_date']
        student.grade = request.POST['grade']
        student.save()
        return redirect('student_detail', pk=student.pk)

    return render(request, 'students/student_form.html', {'student': student})



