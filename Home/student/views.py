from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def student_list(request):
    return render(request, "students/students.html")



def add_student(request):
    if request.method == "POST":
        # get all fields as you already do...
        # (keep your current code here...)

        # Check for duplicate
        if Student.objects.filter(student_id=student_id).exists():
            messages.error(request, f"A student with ID {student_id} already exists.")
            return render(request, "students/add-student.html")

        if not first_name or not last_name or not student_id:
            messages.error(request, "Please fill in all required fields.")
            return render(request, "students/add-student.html")

        parent = Parent.objects.create(
            father_name=father_name,
            father_occupation=father_occupation,
            father_mobile=father_mobile,
            father_email=father_email,
            mother_name=mother_name,
            mother_mobile=mother_mobile,
            mother_email=mother_email,
            present_address=present_address,
            permanent_address=permanent_address
        )

        student = Student(
            first_name=first_name,
            last_name=last_name,
            student_id=student_id,
            gender=gender,
            date_of_birth=date_of_birth,
            student_class=student_class,
            religion=religion,
            joining_date=joining_date,
            mobile_number=mobile_number,
            admission_number=admission_number,
            section=section,
            student_image=student_image,
            parent=parent
        )
        student.save()

        messages.success(request, "Student and parent info saved successfully!")
        return redirect('student_list')

    return render(request, "students/add-student.html")


def edit_student(request):
    return render(request, "students/edit-student.html")

def view_student(request, slug):
    student = get_object_or_404(Student, student_id = slug)
    context = {
        'student': student
    }
    return render(request, "students/student-details.html", context)

def student_list(request):
    student_list = Student.objects.select_related('parent').all()
    context = {
        'students': student_list  # ✅ must match the variable in template
    }
    return render(request, "students/students.html", context)
