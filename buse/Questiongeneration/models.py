from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.TextField(max_length=400)
    weightage = models.CharField(max_length=10)
    pub_date = models.DateTimeField('published_date', default=timezone.now)

    def __str__(self):
        return self.question_text


class Faculty(models.Model):
    faculty_name  = models.TextField(max_length=200)
    fdescription = models.TextField(max_length=200)

    def __str__(self):
        return self.faculty_name


class Department(models.Model):
    dept_name = models.TextField(max_length=100)
    dept_description =models.TextField(max_length=200)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    # faculty is a foreign key and the on delete function allows the user to delete the foreign key in a certain table and cascade helps not to delete any table dependent on t

    def __str__(self):
        return self.dept_name


class Exam_Session(models.Model):
    exam_session =models.DateTimeField('exam date', default=timezone.now)

    def __str__(self):
        return self.exam_session

class Course(models.Model):
    course_name = models.TextField(max_length=100)
    course_code = models.CharField(max_length=7)
    course_duration =models.CharField(max_length=20)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    facu = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name



class Question_Paper(models.Model):
    question_paper_text = models.CharField(max_length=200)
    exam_session = models.ForeignKey(Exam_Session, on_delete=models.CASCADE)
    exam_date = models.DateTimeField('exam date', default=timezone.now)
    pub_date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return self.question_paper_text
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Questions_Instruction(models.Model):
    question_instructions = models.TextField(max_length=200)
    course_details = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_instructions



class Answer(models.Model):
    answer_text =  models.TextField(max_length=400)
    question_ID = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer_text


    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
# Create your models here.
