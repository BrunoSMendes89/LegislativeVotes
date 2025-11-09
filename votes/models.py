from django.db import models

class Legislator(models.Model):
    legislator_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'legislators'


class Bill(models.Model):
    bill_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=500)
    primary_sponsor = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'bills'


class Vote(models.Model):
    vote_id = models.IntegerField(unique=True)
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, to_field='bill_id')
    
    def __str__(self):
        return f"Vote {self.vote_id} on {self.bill.title}"
    
    class Meta:
        db_table = 'votes'


class VoteResult(models.Model):
    result_id = models.IntegerField(unique=True)
    legislator = models.ForeignKey(Legislator, on_delete=models.CASCADE, to_field='legislator_id')
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE, to_field='vote_id')
    vote_type = models.IntegerField()  # 1 = A favor, 2 = Contra
    
    def __str__(self):
        return f"{self.legislator.name} voted {self.vote_type} on vote {self.vote_id}"
    
    class Meta:
        db_table = 'vote_results'