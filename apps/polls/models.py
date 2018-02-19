from django.db import models


class District(models.Model):
    district_name = models.CharField(max_length=100)

    def __str__(self):
        return self.district_name


class Candidate(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    candidate_name = models.CharField(max_length=100)
    candidate_no = models.CharField(max_length=100)
    party = models.CharField(max_length=100)
    remarks = models.TextField()
    img_link = models.TextField()
    no_of_vote = models.IntegerField(default=0)


    def __str__(self):
        return self.candidate_name

class Voter(models.Model):
    candidate = models.ForeignKey(Candidate , on_delete=models.CASCADE)
    voter_name = models.CharField(max_length=100, blank=True)
    voter_text = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.voter_name
