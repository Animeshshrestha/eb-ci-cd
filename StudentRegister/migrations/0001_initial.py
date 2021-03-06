# Generated by Django 3.2.6 on 2021-08-25 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Admission_Number', models.CharField(max_length=50, verbose_name='Admission Number')),
                ('First_Name', models.CharField(max_length=50, verbose_name='First Name')),
                ('Last_Name', models.CharField(max_length=50, verbose_name='Lat Name')),
                ('Date_Of_Birth', models.DateField(max_length=50, null=True, verbose_name='Date Of Birth')),
                ('Date_Joined', models.DateField(null=True, verbose_name='Date Joined')),
                ('Faculty', models.CharField(max_length=50, verbose_name='Faculty')),
                ('Department', models.CharField(max_length=50, verbose_name='Department')),
                ('Course_Name', models.CharField(max_length=50, verbose_name='Course Name')),
                ('Year_Of_Study', models.CharField(max_length=50, verbose_name='Year of Study')),
                ('Unit_Name', models.CharField(max_length=50, verbose_name='Unit Name')),
                ('Grade', models.CharField(max_length=50, verbose_name='Grade')),
            ],
        ),
    ]
