from django.db import models
from django.conf import settings

class Profile(models.Model):
    gender = [('m', 'Male'), ('f','Female')]

    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(null=True, blank=True, max_length=20)
    
    sex = models.TextField(choices=gender, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    dod = models.DateField(null=True, blank=True)
    job = models.TextField(null=True, blank=True)
    ethnicity = models.TextField(null=True, blank=True)
    location = models.TextField(null=True, blank=True)

    biography = models.TextField(null=True, blank=True)

    #Multiple
    stories = models.TextField(null=True, blank=True)
    link = models.TextField(null=True, blank=True)
    video= models.TextField(null=True, blank=True)
 
    number = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name



# class family (models.Model):

    # mother = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    # father = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    # mothers = models.ManyToManyField("Profile", blank=True)
    # fathers = models.ManyToManyField("Profile", blank=True)

#     friends 
#     mother
#     father
#     sister 
#     brother 
#     children 
