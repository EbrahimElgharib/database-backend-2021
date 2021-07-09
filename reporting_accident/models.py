from django.db import models

# Create your models here.

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



class Reporter(models.Model):
    reporter_id = models.AutoField(db_column='Reporter_ID', primary_key=True)  # Field name made lowercase.
    phone_number = models.CharField(db_column='Phone_Number', max_length=11)  # Field name made lowercase.
    accident = models.ForeignKey(Accident, models.DO_NOTHING, db_column='Accident_ID')  # Field name made lowercase.
    reporter_name = models.CharField(db_column='Reporter_Name', max_length=45)  # Field name made lowercase.
    national_number = models.CharField(db_column='National_Number', max_length=14, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'REPORTER'