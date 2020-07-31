from django.db import models
from django.contrib.auth.models import User
from scan_setting.models import ScanSettings
# Create your models here.


class ScanHistory(models.Model):
    org_file_name = models.CharField(max_length=200)
    cur_file_name = models.CharField(max_length=200)
    file_path = models.CharField(max_length=200)
    file_type = models.IntegerField(default=1)
    save_status = models.BooleanField(default=False)
    scan_date = models.DateTimeField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    scan_setting_id = models.ForeignKey(ScanSettings, on_delete=models.CASCADE)
