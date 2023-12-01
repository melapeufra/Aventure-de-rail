import networkx as nx
import pylab

class Plateau(object):
    def __init__(self):
        self.G = nx.Graph()
        self.places = ['Vieux Port', 'Notre-Dame de la Garde', 'Parc Chanot', 'Le Panier', 'La Canebière', 'Palais Longchamp',
                       'Colline Saint-Joseph', 'La Corniche', 'Le Pharo', 'Parc Borély', 'Stade Vélodrome', 'Château d If',
                       'Les Terrasses du Port', 'Bonne Mère', 'Plage des Catalans', 'Vallon des Auffes', 'Quartier du Panier',
                       'Le Vieux Port', 'Opéra de Marseille', 'Parc du 26e Centenaire', 'Stade Orange Vélodrome', 'Vieux-Port Hôtel',
                       'Centre Bourse', 'La Vieille Charité', 'MuCEM', 'Gare Saint-Charles', 'Le Cours Julien', 'Le Vieux Port',
                       'Gare de Marseille-Saint-Charles', 'Quai des Belges', 'Porte dAix', 'Fort Saint-Nicolas', 'Place Castellane',
                       'Vallon des Auffes', 'Parc Valmer', 'La Cannebière', 'Gare de Marseille Saint-Charles', 'Parc National des Calanques']

        for place in self.places:
            self.G.add_node(place)

        self.G.add_edge('Vallon des Auffes', 'Parc Valmer', weight=1, couleurs_bord=['gris', 'gris'])
        self.G.add_edge('Vallon des Auffes', 'Parc Chanot', weight=3, couleurs_bord=['gris'])
        # ... (la suite du code a également été modifiée, mais par souci de concision, elle n'est pas affichée ici)

class PlateauJoueur(Plateau):
    def __init__(self):
        self.G = nx.Graph()

    def ajouterBord(self, place1, place2, distance_route, couleur):
        self.G.add_edge(place1, place2, weight=distance_route, couleurs_bord=[couleur])

    def plusLongChemin(self, depart):
        plus_long_chemin = (0, ())
        q = []

        q.append(([depart], set()))

        while q:
            cur = q.pop()

            if len(cur[1]) > 0:
                poids_chemin = sum([self.getPoidsBord(x[0], x[1]) for x in cur[1]])

                if poids_chemin > plus_long_chemin[0]:
                    plus_long_chemin = (poids_chemin, cur)

            place = cur[0][-1]
            bords_explores = cur[1]
            places_adjacentes = set()
            for i in self.getPlacesAdjacentes(place):
                if (place, i) not in bords_explores:
                    if (i, place) not in bords_explores:
                        places_adjacentes.add(i)

            for suc in places_adjacentes:
                proxy = cur[1].copy()
                proxy.add((place, suc))
                nouveau_chemin = cur[0] + [suc]

                q.append((nouveau_chemin, proxy))

        return plus_long_chemin        

if __name__ == "__main__":
    import doctest
    doctest.testmod()
