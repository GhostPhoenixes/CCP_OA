from django.db import models
from user_info.models import CcpMember


# Create your models here.
class CourseInfo(models.Model):
    # 存储了参加的党课信息
    ccp_member = models.ForeignKey(CcpMember, on_delete=models.CASCADE)


class DocumentInfo(models.Model):
    # 存储了提交的入党材料信息
    ccp_member = models.ForeignKey(CcpMember, on_delete=models.CASCADE)
