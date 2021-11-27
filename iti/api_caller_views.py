from django.shortcuts import redirect, render
import requests


def get_api_students(request):
    r=requests.get("http://localhost:8000/api/v1/students",params=request.GET)
    stds= r.json()
    print(stds[0])
    return render(request,"home.html",{'students':stds})


def add_api_student(request):
    if request.POST:
        payload=dict(student_name=request.POST["sname"],student_age=request.POST["age"],track=request.POST["track"])
        print(payload)
        r=requests.post("http://localhost:8000/api/v1/students/new",data=payload)
        print(r)
        return redirect("callstudents")
    else:

        return render(request, "calleraddstudent.html")