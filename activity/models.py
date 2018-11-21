from django.db import models
from user_info.models import CcpMember


# Create your models here.
class Activity(models.Model):
    pass


class AttendanceRecord(models.Model):
    ccp_member = models.ForeignKey(CcpMember, on_delete=models.CASCADE)
