from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ScanSettings(models.Model):
    scan_language = models.IntegerField(default=1)
    initial_language = models.IntegerField(default=1)
    file_type = models.CharField(max_length=200)
    display_scan_level = models.IntegerField(default=1)
    write_output_file = models.IntegerField(default=1)
    java_finalization_check = models.BooleanField(default=False)
    nested_java_classes_check = models.BooleanField(default=False)
    java_android_check = models.BooleanField(default=False)
    cobol_first_code_col_pos = models.IntegerField()
    export_mode = models.BooleanField(default=False)
    result_filter_option = models.IntegerField()
    display_option = models.IntegerField()
    sign_comparison = models.BooleanField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)