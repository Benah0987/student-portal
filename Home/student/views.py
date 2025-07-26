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


def edit_student(request, slug):
    student = get_object_or_404(Student, student_id=slug)
    parent = student.parent

    if request.method == "POST":
        # Get all POST data
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        student_id = request.POST.get("student_id")
        gender = request.POST.get("gender")
        date_of_birth = request.POST.get("date_of_birth")
        student_class = request.POST.get("student_class")
        religion = request.POST.get("religion")
        joining_date = request.POST.get("joining_date")
        mobile_number = request.POST.get("mobile_number")
        admission_number = request.POST.get("admission_number")
        section = request.POST.get("section")
        student_image = request.FILES.get("student_image")

        father_name = request.POST.get("father_name")
        father_occupation = request.POST.get("father_occupation")
        father_mobile = request.POST.get("father_mobile")
        father_email = request.POST.get("father_email")
        mother_name = request.POST.get("mother_name")
        mother_mobile = request.POST.get("mother_mobile")
        mother_email = request.POST.get("mother_email")
        present_address = request.POST.get("present_address")
        permanent_address = request.POST.get("permanent_address")

        # Validation
        if not first_name or not last_name or not student_id:
            messages.error(request, "Please fill in all required fields.")
            return redirect("edit_student", slug=slug)

        if Student.objects.exclude(id=student.id).filter(student_id=student_id).exists():
            messages.error(request, f"A student with ID {student_id} already exists.")
            return redirect("edit_student", slug=slug)

        # Update student
        student.first_name = first_name
        student.last_name = last_name
        student.student_id = student_id
        student.gender = gender
        student.date_of_birth = date_of_birth
        student.student_class = student_class
        student.religion = religion
        student.joining_date = joining_date
        student.mobile_number = mobile_number
        student.admission_number = admission_number
        student.section = section
        if student_image:
            student.student_image = student_image
        student.save()

        # Update parent
        if parent:
            parent.father_name = father_name
            parent.father_occupation = father_occupation
            parent.father_mobile = father_mobile
            parent.father_email = father_email
            parent.mother_name = mother_name
            parent.mother_mobile = mother_mobile
            parent.mother_email = mother_email
            parent.present_address = present_address
            parent.permanent_address = permanent_address
            parent.save()

        messages.success(request, "Student and parent info updated successfully!")
        return redirect("student_list")

    context = {
        "student": student,
        "parent": parent
    }
    return render(request, "students/edit-student.html", context)

def view_student(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    context = {'student': student}
    return render(request, "students/student-details.html", context)


def student_list(request):
    student_list = Student.objects.select_related('parent').all()
    context = {
        'students': student_list  # ✅ must match the variable in template
    }
    return render(request, "students/students.html", context)

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

def delete_student(request, slug):
    student = get_object_or_404(Student, student_id=slug)
    
    if request.method == "POST":
        student.delete()  # This will also delete the parent if you have on_delete=models.CASCADE set
        messages.success(request, "Student record deleted successfully.")
        return redirect("student_list")

    context = {
        "student": student
    }
    return render(request, "students/confirm-delete.html", context)
