from django.contrib import admin
from .models import (Question, Faculty, Questions_Instruction, Question_Paper, Answer, Course, Exam_Session, Department)


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
admin.site.register(Question, QuestionAdmin)
admin.site.register(Question_Paper)
admin.site.register(Questions_Instruction)
admin.site.register(Answer)
admin.site.register(Exam_Session)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Faculty)
