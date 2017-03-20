# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('answer_text', models.TextField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('course_name', models.TextField(max_length=100)),
                ('course_code', models.CharField(max_length=7)),
                ('course_duration', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('dept_name', models.TextField(max_length=100)),
                ('dept_description', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Exam_Session',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('exam_session', models.DateTimeField(default=django.utils.timezone.now, verbose_name='exam date')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('faculty_name', models.TextField(max_length=200)),
                ('fdescription', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('question_text', models.TextField(max_length=400)),
                ('weightage', models.CharField(max_length=10)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='published_date')),
            ],
        ),
        migrations.CreateModel(
            name='Question_Paper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('question_paper_text', models.CharField(max_length=200)),
                ('exam_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='exam date')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published')),
                ('exam_session', models.ForeignKey(to='Questiongeneration.Exam_Session')),
            ],
        ),
        migrations.CreateModel(
            name='Questions_Instruction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('question_instructions', models.TextField(max_length=200)),
                ('course_details', models.ForeignKey(to='Questiongeneration.Course')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='faculty',
            field=models.ForeignKey(to='Questiongeneration.Faculty'),
        ),
        migrations.AddField(
            model_name='course',
            name='dept',
            field=models.ForeignKey(to='Questiongeneration.Department'),
        ),
        migrations.AddField(
            model_name='course',
            name='facu',
            field=models.ForeignKey(to='Questiongeneration.Faculty'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question_ID',
            field=models.ForeignKey(to='Questiongeneration.Question'),
        ),
    ]
