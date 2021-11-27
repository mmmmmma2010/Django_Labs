from django.db import models
import json

class Course(models.Model) :
    course_name=models.CharField(max_length=50)
    duration=models.CharField(max_length=50)
    
    def __str__(self):
        return f"course_name: {self.course_name}, duration:{self.duration}\n"
    
class Track(models.Model) :
    track_name=models.CharField(max_length=50)
    courses=models.ManyToManyField(Course)
    def __str__(self):
        return f"{self.id}"

class Student (models.Model):
    student_name=models.CharField(max_length=50)
    student_age=models.IntegerField()
    track=models.ForeignKey(Track, on_delete=models.CASCADE)

    def __str__(self):
        return self.__dict__.__str__()
        # return f"sname: {self.student_name}, sAge:{self.student_age},strack:{self.track}\n"
    # def __dict__(self):
    #     dic={sname: self.student_name, sAge:self.student_age,strack:self.track}
    #     return dic
