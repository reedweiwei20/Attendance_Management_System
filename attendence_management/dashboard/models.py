from django.db import models

# Create your models here.

class EmployeeInfo(models.Model):
    # personal information
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=False)
    photo = models.ImageField(null=True, blank= True, upload_to='pics')
    adharno = models.BigIntegerField(blank=False)
    phoneno = models.BigIntegerField(blank=False)
    role = models.TextField(blank=False)
    sallery = models.FloatField(blank=False)
    dob = models.DateField(blank=False)
    education = models.TextField(blank=True)
    workexperience = models.IntegerField(blank=False)
    recuritmentdate = models.DateField(blank=False)
    medicalhistory = models.TextField(blank=True)


class DailyAttendenceInfor(models.Model):
    adharno = models.ForeignKey(EmployeeInfo, on_delete=models.CASCADE)
    date = models.DateField()
    intime = models.TimeField()
    outtime = models.TimeField()
    '''
    #daily Attendence Information
    #adharno no Foreign key
    #presentdays = models.IntegerField()
    #absentdays = models.IntegerField()
    #overtimehrs = models.TimeField()

    sallery report attendence information
    adhar number foreign key
    
    


    # Sallery Infromation
    adharno foreign key
    rate = models.FloatField()
    totalpayment = models.FloatField()
    advancesallery = models.FloatField()
    netTotal = models.FloatField()
    paymentmode = models.TextField()
    sallery = models.FloatField()'''




