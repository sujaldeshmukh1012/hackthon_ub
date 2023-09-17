from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    
    

class Skill(models.Model):
    skill_name = models.CharField(max_length=100)
    skill_desc = models.CharField(max_length=1000)
    skill_level = models.IntegerField(default=5)

    def __str__(self):
        return self.skill_name
    
    
    
    

class Industry_Sector(models.Model):
    industry_sector_name = models.CharField(max_length=100)
    industry_sector_desc = models.CharField(max_length=1000)
    industry_sector_level = models.IntegerField(default=5)

    def __str__(self):
        return self.industry_sector_name
    


    

class Work_Positions(models.Model):
    work_position_name = models.CharField(max_length=100)
    work_position_desc = models.CharField(max_length=1000)
    work_position_level = models.IntegerField(default=5)

    def __str__(self):
        return self.work_position_name
    


    


