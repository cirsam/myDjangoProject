# Generated by Django 3.2.5 on 2021-08-29 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answers_name', models.CharField(max_length=200)),
                ('userId', models.CharField(default='1', editable=False, max_length=50)),
                ('pub_date', models.DateTimeField(default='', editable=False, verbose_name='date published')),
            ],
            options={
                'ordering': ['-answers_name'],
            },
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=200)),
                ('userId', models.CharField(default='1', editable=False, max_length=50)),
                ('pub_date', models.DateTimeField(default='', editable=False, verbose_name='date published')),
            ],
            options={
                'ordering': ['-class_name'],
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions_name', models.CharField(max_length=200)),
                ('courses_id', models.CharField(default='1', editable=False, max_length=20)),
                ('userId', models.CharField(default='1', editable=False, max_length=50)),
                ('correct_answer', models.CharField(default='1', editable=False, max_length=50)),
                ('pub_date', models.DateTimeField(default='', editable=False, verbose_name='date published')),
            ],
            options={
                'ordering': ['-questions_name'],
            },
        ),
        migrations.CreateModel(
            name='Schools',
            fields=[
                ('schools_id', models.AutoField(primary_key=True, serialize=False)),
                ('schools_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=60)),
                ('state_province', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=50)),
                ('userId', models.CharField(default='1', editable=False, max_length=50)),
                ('website', models.URLField()),
                ('pub_date', models.DateTimeField(default='', editable=False, verbose_name='date published')),
            ],
            options={
                'ordering': ['-schools_name'],
            },
        ),
        migrations.CreateModel(
            name='MyAnswers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_session', models.CharField(default='1', editable=False, max_length=50)),
                ('userId', models.CharField(default='1', editable=False, max_length=50)),
                ('pub_date', models.DateTimeField(default='', editable=False, verbose_name='date published')),
                ('answers', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='education.answers')),
                ('questions', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='education.questions')),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courses_name', models.CharField(max_length=200)),
                ('userId', models.CharField(default='1', editable=False, max_length=50)),
                ('pub_date', models.DateTimeField(default='', editable=False, verbose_name='date published')),
                ('classes', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='education.classes')),
                ('schools', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='education.schools')),
            ],
            options={
                'ordering': ['-courses_name'],
            },
        ),
        migrations.AddField(
            model_name='classes',
            name='schools',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='education.schools'),
        ),
        migrations.AddField(
            model_name='answers',
            name='questions',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='education.questions'),
        ),
    ]
