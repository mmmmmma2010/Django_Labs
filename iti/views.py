from django.db.models.base import Model
from django.shortcuts import redirect, render ,get_object_or_404
from iti.models import Track, Course, Student
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from .forms import AddStudent
from django.contrib.auth.decorators import login_required


#########################################################3

class StudentList(ListView):
    model= Student
@login_required(login_url='login')
def addstudent(request):
    if request.POST:
        s = Student(student_name=request.POST["sname"],
                    student_age=request.POST["age"], track_id=request.POST["track_id"])
        try:           
            s.save()
            return HttpResponseRedirect("students")
        except Exception as e :
            return e.__str__
        
    else:

        return render(request, "addstudent.html")

@login_required(login_url='login')
def get_students(request):

    students = Student.objects.all()
    return render(request, "students.html", {"students": students})


def get_student(request, sid):
    instance = get_object_or_404(Student, id=sid)
    form = AddStudent(request.POST or None , instance=instance)
    if request.POST:
        print("entered")
        if form.is_valid():
            print("")
            form.save()
            return HttpResponseRedirect("/students")

    return render(request, 'studentdetails.html', {'form': form})
    # student =AddStudent()
    # return render(request, "studentdetails.html", {"students": student})


def delete_student(request, sid):
    student = Student.objects.filter(id=sid).delete()
    return HttpResponseRedirect("/students")


def update_student(request, sid,*args):
    student = Student.objects.filter(id=sid).update(stutdent_name=args[0],student_age=args[1],track_id=args[2])
    return HttpResponseRedirect("/iti/students")
    




####################################################

def addcourse(request):
    c = Course(course_name="javascript", duration="2 weeks")
    c.save()
    return HttpResponse("done")


def get_courses(request):
    courses = Course.objects.all()
    return HttpResponse(courses)


def index(request):
    students = Student.objects.all()
    tracks = Track.objects.all()
    return render(request, "welcome.html", {"students": students, "tracks": tracks})


def addtrack(request):
    t = Track(track_name="opensource")
    c = Course(course_name="css", duration="1 weeks")
    c.save()
    t.save()
    t.courses.add(c)
    return HttpResponse("done")


def get_tracks(request):
    tracks = Track.objects.all()
    return HttpResponse(tracks)