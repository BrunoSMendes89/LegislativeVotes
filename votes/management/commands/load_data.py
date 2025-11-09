import pandas as pd
from django.core.management.base import BaseCommand
from votes.models import Legislator, Bill, Vote, VoteResult

class Command(BaseCommand):
    help = 'Carrega dados dos arquivos CSV para o banco de dados'

    def handle(self, *args, **kwargs):
        self.stdout.write('Iniciando carga de dados...')
        
        # Limpa dados existentes
        self.stdout.write('Limpando dados antigos...')
        VoteResult.objects.all().delete()
        Vote.objects.all().delete()
        Bill.objects.all().delete()
        Legislator.objects.all().delete()
        
        # Carrega Legislators
        self.stdout.write('Carregando legislators.csv...')
        df_legislators = pd.read_csv('legislators.csv')
        for _, row in df_legislators.iterrows():
            Legislator.objects.create(
                id=row['id'],
                name=row['name']
            )
        self.stdout.write(self.style.SUCCESS(f'✓ {len(df_legislators)} legisladores carregados'))
        
        # Carrega Bills
        self.stdout.write('Carregando bills.csv...')
        df_bills = pd.read_csv('bills.csv')
        for _, row in df_bills.iterrows():
            Bill.objects.create(
                id=row['id'],
                title=row['title'],
                sponsor_id=row['sponsor_id']
            )
        self.stdout.write(self.style.SUCCESS(f'✓ {len(df_bills)} projetos de lei carregados'))
        
        # Carrega Votes
        self.stdout.write('Carregando votes.csv...')
        df_votes = pd.read_csv('votes.csv')
        for _, row in df_votes.iterrows():
            bill = Bill.objects.get(id=row['bill_id'])
            Vote.objects.create(
                id=row['id'],
                bill=bill
            )
        self.stdout.write(self.style.SUCCESS(f'✓ {len(df_votes)} votações carregadas'))
        
        # Carrega Vote Results
        self.stdout.write('Carregando vote_results.csv...')
        df_results = pd.read_csv('vote_results.csv')
        for _, row in df_results.iterrows():
            legislator = Legislator.objects.get(id=row['legislator_id'])
            vote = Vote.objects.get(id=row['vote_id'])
            VoteResult.objects.create(
                id=row['id'],
                legislator=legislator,
                vote=vote,
                vote_type=row['vote_type']
            )
        self.stdout.write(self.style.SUCCESS(f'✓ {len(df_results)} resultados de votos carregados'))

        self.stdout.write(self.style.SUCCESS('🎉 Carga de dados concluída com sucesso!'))