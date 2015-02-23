from django.db import models

# Create your models here.

class Collection(models.Model):
    collection_name = models.CharField(max_length=256)   
    
    def __str__(self):
        return self.collection_name
    
class Team(models.Model):
    team_name = models.CharField(max_length=256)
    team_image = models.ImageField(blank=True)
    collection_id = models.ForeignKey(Collection)

    def __str__(self):
        return self.team_name

class Card(models.Model):
    card_name = models.CharField(max_length=256)
    card_image = models.ImageField(blank=True)
    card_rank = models.IntegerField(default=10)
    team_id = models.ForeignKey(Team)
    
    def __str__(self):
        return self.card_name
    
class User(models.Model):
    user_firstname = models.CharField(max_length=256)
    user_lastname = models.CharField(max_length=256)
    user_cards = models.ManyToManyField(Card, through='UserCards')
    
class UserCards(models.Model):
    cardid = models.ForeignKey(Card)
    userid = models.ForeignKey(User)
    count = models.IntegerField()        