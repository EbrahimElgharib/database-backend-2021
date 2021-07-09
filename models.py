# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Accident(models.Model):
    accident_id = models.AutoField(db_column='Accident_ID', primary_key=True)  # Field name made lowercase.
    accident_volume = models.CharField(db_column='Accident_Volume', max_length=45)  # Field name made lowercase.
    accident_description = models.CharField(db_column='Accident_Description', max_length=45)  # Field name made lowercase.
    place_long = models.FloatField(db_column='Place_Long')  # Field name made lowercase.
    place_lat = models.FloatField(db_column='Place_Lat')  # Field name made lowercase.
    special_case_1 = models.IntegerField(db_column='Special_Case_1', blank=True, null=True)  # Field name made lowercase.
    special_case_2 = models.IntegerField(db_column='Special_Case_2', blank=True, null=True)  # Field name made lowercase.
    special_case_3 = models.IntegerField(db_column='Special_Case_3', blank=True, null=True)  # Field name made lowercase.
    special_case_4 = models.IntegerField(db_column='Special_Case_4', blank=True, null=True)  # Field name made lowercase.
    hospital = models.ForeignKey('Hospital', models.DO_NOTHING, db_column='Hospital_ID', blank=True, null=True)  # Field name made lowercase.
    accident_time = models.DateTimeField(db_column='Accident_Time')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ACCIDENT'


class AccCrewT(models.Model):
    accident = models.OneToOneField(Accident, models.DO_NOTHING, db_column='Accident_ID', primary_key=True)  # Field name made lowercase.
    crew = models.ForeignKey('Crew', models.DO_NOTHING, db_column='Crew_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ACC_CREW_T'
        unique_together = (('accident', 'crew'),)


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


class Crew(models.Model):
    crew_id = models.AutoField(db_column='Crew_ID', primary_key=True)  # Field name made lowercase.
    station = models.ForeignKey('Station', models.DO_NOTHING, db_column='Station_ID')  # Field name made lowercase.
    vehicle = models.ForeignKey('Vehicles', models.DO_NOTHING, db_column='Vehicle_ID')  # Field name made lowercase.
    crew_status = models.CharField(db_column='Crew_Status', max_length=45)  # Field name made lowercase.
    number_of_accidents = models.IntegerField(db_column='Number_Of_Accidents')  # Field name made lowercase.
    current_accident = models.IntegerField(db_column='Current_Accident', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CREW'


class Employees(models.Model):
    employee = models.OneToOneField('AuthUser', models.DO_NOTHING, db_column='Employee_ID', primary_key=True)  # Field name made lowercase.
    employee_name = models.CharField(db_column='Employee_Name', max_length=45)  # Field name made lowercase.
    birth_date = models.DateField(db_column='Birth_Date')  # Field name made lowercase.
    phone_number = models.CharField(db_column='Phone_Number', max_length=11)  # Field name made lowercase.
    national_number = models.CharField(db_column='National_Number', max_length=14)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=45)  # Field name made lowercase.
    emp_type = models.IntegerField(db_column='Emp_Type')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EMPLOYEES'


class Hospital(models.Model):
    hospital_id = models.AutoField(db_column='Hospital_ID', primary_key=True)  # Field name made lowercase.
    hospital_name = models.CharField(db_column='Hospital_Name', max_length=45)  # Field name made lowercase.
    place_long = models.FloatField(db_column='Place_Long')  # Field name made lowercase.
    place_lat = models.FloatField(db_column='Place_Lat')  # Field name made lowercase.
    governerate = models.CharField(db_column='Governerate', max_length=45)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=45)  # Field name made lowercase.
    saturday = models.IntegerField(db_column='Saturday')  # Field name made lowercase.
    sunday = models.IntegerField(db_column='Sunday')  # Field name made lowercase.
    monday = models.IntegerField(db_column='Monday')  # Field name made lowercase.
    tuesday = models.IntegerField(db_column='Tuesday')  # Field name made lowercase.
    wednesday = models.IntegerField(db_column='Wednesday')  # Field name made lowercase.
    thursday = models.IntegerField(db_column='Thursday')  # Field name made lowercase.
    friday = models.IntegerField(db_column='Friday')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HOSPITAL'


class Manager(models.Model):
    manager = models.OneToOneField(Employees, models.DO_NOTHING, db_column='Manager_ID', primary_key=True)  # Field name made lowercase.
    station = models.ForeignKey('Station', models.DO_NOTHING, db_column='Station_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MANAGER'


class Reporter(models.Model):
    reporter_id = models.AutoField(db_column='Reporter_ID', primary_key=True)  # Field name made lowercase.
    phone_number = models.CharField(db_column='Phone_Number', max_length=11)  # Field name made lowercase.
    accident = models.ForeignKey(Accident, models.DO_NOTHING, db_column='Accident_ID')  # Field name made lowercase.
    reporter_name = models.CharField(db_column='Reporter_Name', max_length=45)  # Field name made lowercase.
    national_number = models.CharField(db_column='National_Number', max_length=14, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'REPORTER'


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


class StationEmployees(models.Model):
    station_employee = models.OneToOneField(Employees, models.DO_NOTHING, db_column='Station_Employee_ID', primary_key=True)  # Field name made lowercase.
    station = models.ForeignKey(Station, models.DO_NOTHING, db_column='Station_ID')  # Field name made lowercase.
    crew = models.ForeignKey(Crew, models.DO_NOTHING, db_column='Crew_ID')  # Field name made lowercase.
    job_title = models.CharField(db_column='Job_Title', max_length=45)  # Field name made lowercase.
    number_of_accidents = models.IntegerField(db_column='Number_Of_Accidents', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'STATION_EMPLOYEES'


class Vehicles(models.Model):
    vehicle_id = models.IntegerField(db_column='Vehicle_ID', primary_key=True)  # Field name made lowercase.
    station = models.ForeignKey(Station, models.DO_NOTHING, db_column='Station_ID')  # Field name made lowercase.
    vehicle_status = models.CharField(db_column='Vehicle_Status', max_length=45)  # Field name made lowercase.
    vehicle_number = models.CharField(db_column='Vehicle_Number', max_length=24)  # Field name made lowercase.
    special_case = models.CharField(db_column='Special_Case', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VEHICLES'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'
