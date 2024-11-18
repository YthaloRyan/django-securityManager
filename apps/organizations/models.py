from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(User, related_name='organizations', blank=True)
    org_admin = models.ManyToManyField(User, related_name='org_admin', blank=True)
    
    class Meta:
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"
        ordering = ['name']
        
    def __str__(self):
        return self.name
    

# class Profiles(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#     description = models.TextField(blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     users = models.ManyToManyField(User, related_name='profiles', blank=True)
    
#     class Meta:
#         verbose_name = "Profile"
#         verbose_name_plural = "Profiles"
#         ordering = ['name']
        
#     def __str__(self):
#         return self.name