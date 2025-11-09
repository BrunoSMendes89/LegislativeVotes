from django.shortcuts import render
from django.db.models import Count, Q
from .models import Legislator, Bill, VoteResult

def home(request):
    context = {
        'legislator_data': None,
        'bill_data': None,
        'search_type': None
    }
    
    # Busca por Legislador
    legislator_search = request.GET.get('legislator_search', '').strip()
    if legislator_search:
        # Tenta buscar por ID ou nome
        try:
            legislator_id = int(legislator_search)
            legislator = Legislator.objects.filter(id=legislator_id).first()
        except ValueError:
            legislator = Legislator.objects.filter(name__icontains=legislator_search).first()
        
        if legislator:
            # Conta votos a favor (vote_type = 1) e contra (vote_type = 2)
            votes_for = VoteResult.objects.filter(
                legislator=legislator, 
                vote_type=1
            ).count()
            
            votes_against = VoteResult.objects.filter(
                legislator=legislator, 
                vote_type=2
            ).count()
            
            context['legislator_data'] = {
                'legislator': legislator,
                'votes_for': votes_for,
                'votes_against': votes_against
            }
            context['search_type'] = 'legislator'
        else:
            context['error'] = 'Legislador não encontrado'
    
    # Busca por Bill
    bill_search = request.GET.get('bill_search', '').strip()
    if bill_search:
        # Tenta buscar por ID ou título
        try:
            bill_id = int(bill_search)
            bill = Bill.objects.filter(id=bill_id).first()
        except ValueError:
            bill = Bill.objects.filter(title__icontains=bill_search).first()
        
        if bill:
            # Busca todos os votos relacionados a este bill
            from .models import Vote
            votes = Vote.objects.filter(bill=bill)
            
            # Conta apoiadores e opositores
            supporters = VoteResult.objects.filter(
                vote__in=votes,
                vote_type=1
            ).count()
            
            opponents = VoteResult.objects.filter(
                vote__in=votes,
                vote_type=2
            ).count()
            
            # Busca o nome do sponsor
            sponsor = Legislator.objects.filter(id=bill.sponsor_id).first()
            sponsor_name = sponsor.name if sponsor else "Desconhecido"
            
            context['bill_data'] = {
                'bill': bill,
                'supporters': supporters,
                'opponents': opponents,
                'sponsor_name': sponsor_name
            }
            context['search_type'] = 'bill'
        else:
            context['error'] = 'Projeto de lei não encontrado'
    
    return render(request, 'votes/home.html', context)