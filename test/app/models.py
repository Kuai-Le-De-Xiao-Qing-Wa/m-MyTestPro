
from django.db import models

# Create your models here.


class User(models.Model):
    id = models.AutoField(max_length=11,primary_key=True,null=False)
    username = models.CharField(max_length=255,null=False)
    pwd = models.CharField(max_length=255,null=False)
    create_time = models.DateTimeField(auto_now_add=True,null=False)

    class Meta:
        db_table = 'tb_user'