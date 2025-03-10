from django.db.models.signals import post_save
from django.dispatch import receiver
from threading import Timer
from .models import StudentModel

def delete_record_after_one_minute(roll_no):

    object = StudentModel.objects.get(roll_no=roll_no)
    object.delete()

@receiver(post_save,sender=StudentModel)

def schedule_deletion(sender, instance, **kwargs):
    time = 1 * 60
    Timer(time, delete_record_after_one_minute,[instance.roll_no]).start()