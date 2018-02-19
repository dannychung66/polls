from django.contrib import admin
from .models import District, Candidate, Voter

class DistrictModelAdmin(admin.ModelAdmin):
    list_display = ['district_name', ]

    class Meta:
        model = District

class CandidateModelAdmin(admin.ModelAdmin):
    list_display = ['candidate_name', 'candidate_no',]
    search_fields = ['candidate_name', ]
    list_filter = ['district',]
    class Meta:
        model = Candidate

class VoterModelAdmin(admin.ModelAdmin):
    list_display = ['voter_name', 'voter_text',]
    search_fields = ['voter_name', ]

    class Meta:
        model = Voter

admin.site.register(District, DistrictModelAdmin)
admin.site.register(Candidate, CandidateModelAdmin)
admin.site.register(Voter, VoterModelAdmin)
