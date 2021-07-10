from reporting_accident.models import Accident, Hospital
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


class Manager(models.Model):
    manager = models.OneToOneField(Employees, models.DO_NOTHING, db_column='Manager_ID', primary_key=True)  # Field name made lowercase.
    station = models.ForeignKey('Station', models.DO_NOTHING, db_column='Station_ID')  # Field name made lowercase.
    def __str__(self):
            return str(self.manager)
    class Meta:
        managed = False
        db_table = 'MANAGER'



class StationEmployees(models.Model):
    station_employee = models.OneToOneField(Employees, models.DO_NOTHING, db_column='Station_Employee_ID', primary_key=True)  # Field name made lowercase.
    station = models.ForeignKey('Station', models.DO_NOTHING, db_column='Station_ID')  # Field name made lowercase.
    crew = models.ForeignKey('Crew', models.DO_NOTHING, db_column='Crew_ID')  # Field name made lowercase.
    job_title = models.CharField(db_column='Job_Title', max_length=45)  # Field name made lowercase.
    number_of_accidents = models.IntegerField(db_column='Number_Of_Accidents', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
            return str(self.station_employee) +'  ____  '+ str(self.job_title)
    class Meta:
        managed = False
        db_table = 'STATION_EMPLOYEES'


class Station(models.Model):
    station_id = models.AutoField(db_column='Station_ID', primary_key=True)  # Field name made lowercase.
    hospital = models.ForeignKey(Hospital, models.DO_NOTHING, db_column='Hospital_ID', blank=True, null=True)  # Field name made lowercase.
    station_type = models.IntegerField(db_column='Station_Type')  # Field name made lowercase.
    place_long = models.FloatField(db_column='Place_Long')  # Field name made lowercase.
    place_lat = models.FloatField(db_column='Place_Lat')  # Field name made lowercase.
    governerate = models.CharField(db_column='Governerate', max_length=45)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=45)  # Field name made lowercase.
    available_cars = models.IntegerField(db_column='Available_Cars')  # Field name made lowercase.
    car_numbers = models.IntegerField(db_column='Car_Numbers')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'STATION'



class Crew(models.Model):
    crew_id = models.AutoField(db_column='Crew_ID', primary_key=True)  # Field name made lowercase.
    station = models.ForeignKey(Station, models.DO_NOTHING, db_column='Station_ID')  # Field name made lowercase.
    vehicle = models.ForeignKey('Vehicles', models.DO_NOTHING, db_column='Vehicle_ID')  # Field name made lowercase.
    crew_status = models.CharField(db_column='Crew_Status', max_length=45)  # Field name made lowercase.
    number_of_accidents = models.IntegerField(db_column='Number_Of_Accidents')  # Field name made lowercase.
    current_accident = models.IntegerField(db_column='Current_Accident', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CREW'


class Vehicles(models.Model):
    vehicle_id = models.IntegerField(db_column='Vehicle_ID', primary_key=True)  # Field name made lowercase.
    station = models.ForeignKey(Station, models.DO_NOTHING, db_column='Station_ID')  # Field name made lowercase.
    vehicle_status = models.CharField(db_column='Vehicle_Status', max_length=45)  # Field name made lowercase.
    vehicle_number = models.CharField(db_column='Vehicle_Number', max_length=24)  # Field name made lowercase.
    special_case = models.CharField(db_column='Special_Case', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VEHICLES'


class Casualties(models.Model):
    casualties_id = models.AutoField(db_column='Casualties_ID', primary_key=True)  # Field name made lowercase.
    accident = models.ForeignKey(Accident, models.DO_NOTHING, db_column='Accident_ID')  # Field name made lowercase.
    casualty_name = models.CharField(db_column='Casualty_Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='Age', max_length=45, blank=True, null=True)  # Field name made lowercase.
    gender = models.IntegerField(db_column='Gender')  # Field name made lowercase.
    weight = models.DecimalField(db_column='Weight', max_digits=4, decimal_places=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CASUALTIES'