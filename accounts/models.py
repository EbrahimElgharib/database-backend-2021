from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Employees(models.Model):
    employee = models.OneToOneField(User, models.DO_NOTHING, db_column='Employee_ID', primary_key=True)  # Field name made lowercase.
    employee_name = models.CharField(db_column='Employee_Name', max_length=45)  # Field name made lowercase.
    birth_date = models.DateField(db_column='Birth_Date')  # Field name made lowercase.
    phone_number = models.CharField(db_column='Phone_Number', max_length=11)  # Field name made lowercase.
    national_number = models.CharField(db_column='National_Number', max_length=14)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=45)  # Field name made lowercase.
    emp_type = models.IntegerField(db_column='Emp_Type')  # Field name made lowercase.
    def __str__(self):
            return str(self.employee_name) + ' ' + str(self.employee)
    class Meta:
        managed = False
        db_table = 'EMPLOYEES'


### Signals
# create profile when Sign-Up
@receiver(post_save, sender=User)
def create_user_Employees(sender, instance, created, **kwargs):
    if created:
        Employees.objects.create(employee=instance)


# class Manager(models.Model):
#     manager = models.OneToOneField(Employees, models.DO_NOTHING, db_column='Manager_ID', primary_key=True)  # Field name made lowercase.
#     station = models.ForeignKey('Station', models.DO_NOTHING, db_column='Station_ID')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'MANAGER'



# class StationEmployees(models.Model):
#     station_employee = models.OneToOneField(Employees, models.DO_NOTHING, db_column='Station_Employee_ID', primary_key=True)  # Field name made lowercase.
#     station = models.ForeignKey(Station, models.DO_NOTHING, db_column='Station_ID')  # Field name made lowercase.
#     crew = models.ForeignKey(Crew, models.DO_NOTHING, db_column='Crew_ID')  # Field name made lowercase.
#     job_title = models.CharField(db_column='Job_Title', max_length=45)  # Field name made lowercase.
#     number_of_accidents = models.IntegerField(db_column='Number_Of_Accidents', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'STATION_EMPLOYEES'