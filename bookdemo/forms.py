from django.forms import ModelForm
from .models import Appointment


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ['parent_name', 'contact_no', 'email_id', 'child_name','child_age','course_time_date']


  
       