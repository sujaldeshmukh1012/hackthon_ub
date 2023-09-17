from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from authorization.models import Skill,Industry_Sector,Work_Positions,UserProfile
# Create your models here.




class Project(models.Model):
    title=models.CharField(max_length=300,blank=False)
    created_on = models.DateTimeField(
        blank=True, editable=False, default=timezone.now
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    skills_used = models.ManyToManyField(Skill,blank=True)
    banner = models.ImageField(upload_to="project-banners/",blank=True)
    description = models.TextField()
    team_members = models.ManyToManyField(UserProfile,blank=True)
    industry = models.ForeignKey(Industry_Sector,blank=True,on_delete=models.CASCADE)
    contact_email = models.EmailField(max_length=200,blank=False)
    purpose = models.CharField(max_length=400,blank=True)
    want_to_expand = models.BooleanField(default=False)
    

    def __str__(self):
        return self.title + " by " + self.user

    def save(self, *args, **kwargs):
        self.created_on = timezone.now()
        super(Project, self).save(*args, **kwargs)




class ProjectRecruit(models.Model):
    title=models.CharField(max_length=300,blank=False)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    position = models.ManyToManyField(Work_Positions,blank=True)
    created_on = models.DateTimeField(
        blank=True, editable=False, default=timezone.now
    )
    open_till = models.DateTimeField(
        blank=True, editable=False, default=timezone.now
    )
    description = models.CharField(max_length=500,blank=False)
    paid = models.BooleanField(default=False)
    pay = models.CharField(max_length=200)

    def __str__(self):
        return self.title + " at " + self.project
    
    def save(self, *args, **kwargs):
        self.created_on = timezone.now()
        super(ProjectRecruit, self).save(*args, **kwargs)


    
    
class Inquiry(models.Model):
    created_on = models.DateTimeField(
        blank=True, editable=False, default=timezone.now
    )
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.TextField()
    
    

    
    
    # user profile attribute addition
    # serialize
    #  api