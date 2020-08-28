from django.db import models
 
class Appointment(models.Model):
    parent_name = models.CharField(max_length=50 )
    contact_no = models.CharField(max_length=10)
    email_id = models.EmailField(max_length=50)
    child_name = models.CharField(max_length=50)
    child_age = models.IntegerField()
    course_time_date = models.CharField(max_length=50)
    
