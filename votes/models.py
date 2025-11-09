from django.db import models

class Legislator(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'legislators'


class Bill(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=500)
    sponsor_id = models.IntegerField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'bills'


class Vote(models.Model):
    id = models.IntegerField(primary_key=True)
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Vote {self.id} on {self.bill.title}"
    
    class Meta:
        db_table = 'votes'


class VoteResult(models.Model):
    id = models.IntegerField(primary_key=True)
    legislator = models.ForeignKey(Legislator, on_delete=models.CASCADE)
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)
    vote_type = models.IntegerField()  # 1 = A favor, 2 = Contra
    
    def __str__(self):
        return f"{self.legislator.name} voted {self.vote_type} on vote {self.id}"
    
    class Meta:
        db_table = 'vote_results'