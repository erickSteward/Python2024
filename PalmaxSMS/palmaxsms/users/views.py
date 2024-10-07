# from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Course, Attendance, Feedback
from .forms import CourseForm, AttendanceForm, FeedbackForm
from django.http import HttpResponse

# @login_required
# def dashboard(request):
#     if request.user.groups.filter(name='Admin').exists():
#         return render(request, 'users/dashboard_admin.html')
#     elif request.user.groups.filter(name='Teacher').exists():
#         return render(request, 'users/dashboard_teacher.html')
#     elif request.user.groups.filter(name='Student').exists():
#         return render(request, 'users/dashboard_student.html')
#     elif request.user.groups.filter(name='Front Office').exists():
#         return render(request, 'users/dashboard_front_office.html')
#     else:
#         return redirect('login')

# @login_required
# def course_list(request):
#     courses = Course.objects.all()
#     return render(request, 'users/course_list.html', {'courses': courses})

# @login_required
# def add_course(request):
#     if request.method == 'POST':
#         form = CourseForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('course_list')
#     else:
#         form = CourseForm()
#     return render(request, 'users/add_course.html', {'form': form})

# @login_required
# def view_attendance(request):
#     attendance_records = Attendance.objects.filter(user=request.user)
#     return render(request, 'users/view_attendance.html', {'attendance_records': attendance_records})

# @login_required
# def submit_feedback(request, course_id):
#     course = Course.objects.get(id=course_id)
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             feedback = form.save(commit=False)
#             feedback.user = request.user
#             feedback.course = course
#             feedback.save()
#             return redirect('course_list')
#     else:
#         form = FeedbackForm()
#     return render(request, 'users/submit_feedback.html', {'form': form, 'course': course})

def login(request):
    return render(request, 'users/login.html')
