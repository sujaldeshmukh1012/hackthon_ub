from rest_framework import serializers
from .models import Project,ProjectRecruit,Industry_Sector,Inquiry






class ProjectRecruitSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProjectRecruit
        fields = "__all__"



class InquirySerializers(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = "__all__"





class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
    
    
