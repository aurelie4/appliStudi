import random
from django.db import transaction
from monappli_gl.models import Categorie, Produit, Client, Vente

CATEGORIES = [
    "Alimentation",
    "Maison",
    "Mode",
    "Beauté",
    "High-Tech",
]

N_PRODUCTS = 50
N_CLIENTS = 100
N_VENTES = 1000

@transaction.atomic
def create_random_data():
    # Création des catégories
    categories = []
    for cat_name in CATEGORIES:
        cat = Categorie.objects.create(nom=cat_name)
        categories.append(cat)

    # Création des produits
    produits = []
    for i in range(N_PRODUCTS):
        nom_produit = f"Produit {i}"
        prix = random.uniform(1, 1000)
        categorie = random.choice(categories)
        produit = Produit.objects.create(nom=nom_produit, prix=prix, categorie=categorie)
        produits.append(produit)

    # Création des clients
    clients = []
    for i in range(N_CLIENTS):
        nom_client = f"Client {i}"
        profession = random.choice(["Etudiant", "Salarié", "Indépendant", "Retraité"])
        client = Client.objects.create(nom=nom_client, profession=profession)
        clients.append(client)

    # Création des ventes
    ventes = []
    for i in range(N_VENTES):
        produit = random.choice(produits)
        client = random.choice(clients)
        quantite = random.randint(1, 10)
        vente = Vente.objects.create(produit=produit, client=client, quantite=quantite)
        ventes.append(vente)

    print(f"{N_PRODUCTS} produits, {N_CLIENTS} clients, {N_VENTES} ventes créés.")