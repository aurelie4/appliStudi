# Create your views here.
from django.shortcuts import render
from django.db.models import Sum
from .models import Client, Panier, LignePanier

def expenses_by_category(request):
    # récupérer les dépenses par catégorie et catégorie socioprofessionnelle
    expenses = LignePanier.objects.values('panier__client__categorie_socio', 'produit__categorie')\
                .annotate(total_depense=Sum('prix_unitaire'))

    # construire un dictionnaire pour stocker les dépenses par catégorie
    categories_expenses = {}
    for expense in expenses:
        categorie_socio = expense['panier__client__categorie_socio']
        categorie_produit = expense['produit__categorie']
        total_depense = expense['total_depense']
        if categorie_socio not in categories_expenses:
            categories_expenses[categorie_socio] = {}
        categories_expenses[categorie_socio][categorie_produit] = total_depense


    # préparer les données pour le graphique
    data = {
        'categories': [],
        'datasets': []
    }
    for categorie_socio, expenses in categories_expenses.items():
        data['categories'].append(categorie_socio)
        dataset = {
            'label': categorie_socio,
            'data': [],
            'backgroundColor': []
        }
        for categorie_produit, total_depense in expenses.items():
            dataset['data'].append(total_depense)
            dataset['backgroundColor'].append(get_random_color())
        data['datasets'].append(dataset)

    return render(request, 'expenses_by_category.html', {'data': data})
