'''
        Spanav 0.1v
        Copyright (C) 2020 SpanavEdTech.private.limited
        
        Created By : NayanRaj Adhikary  (github : https://github.com/nayanraj210401)
                     Sameer Kasivajhula (github : https://github.com/sameerkousik)

'''

from django.contrib import admin
from .models import ExperimentDevelopment,Stream,Branch,JobRole
# Register your models here.

admin.site.register(ExperimentDevelopment)  
admin.site.register(Stream)
admin.site.register(Branch)
admin.site.register(JobRole)