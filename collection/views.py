from django.shortcuts import render_to_response
from random import randrange
from collection.models import Card, Collection, Team, User, UserCards

# Create your views here.
def index(request):
        
    # get card collection
    thisCollection = Collection.objects.get(collection_name='premier league')
    
    # get teams from this collection
    teams = Team.objects.filter(collection_id=thisCollection.id)
    
    # get all cards
    cards = Card.objects.filter(team_id__in=teams)
    
    #   *** GET A PACK OF CARDS ***  #    
    # generate random number between 1 and 1300
    cardRankIndex = randrange(0,1300)
    
    # identify range of cards to choose from
    cardPack = Card.objects.filter(card_rank__lte=cardRankIndex, team_id__in=teams).order_by('?')[:5]
    
    #  *** ASSIGN PACK CARDS TO USER ***  #
    
    # get card id list
    userCardList = []
    
    for assignCard in cardPack:
        uc = UserCards(cardid_id=assignCard.id,userid_id=1,count=1)
        UserCards.save(uc)
    
    # send data to the template
    context = {
               'cardlist': cardPack,
               'teams': teams,
               'cards': cards,
               'cardstoadd': userCardList
               }        
    
    return render_to_response('index.html', context)
