import random

class Combat:
    def init(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def est_termine(self):
        return self.pokemon1.est_ko() or self.pokemon2.est_ko()

    def obtenir_vainqueur(self):
        if not self.est_termine():
            return None

        if self.pokemon1.est_ko():
            return self.pokemon2.get_nom()
        else:
            return self.pokemon1.get_nom()

    def lancer_attaque(self, pokemon_attaquant, pokemon_defenseur):
        if random.randint(0, 1) == 0:
            print(f"{pokemon_attaquant.get_nom()} loupe son attaque !")
            return

        type_defenseur = type(pokemon_defenseur).name
        if type_defenseur == "PokemonNormal":
            multiplicateur = 1
        elif type_defenseur == "PokemonFeu":
            multiplicateur = 2 if type(pokemon_attaquant).name == "PokemonEau" else 0.5
        elif type_defenseur == "PokemonEau":
            multiplicateur = 2 if type(pokemon_attaquant).name == "PokemonTerre" else 0.5
        elif type_defenseur == "PokemonTerre":
            multiplicateur = 2 if type(pokemon_attaquant).name == "PokemonFeu" else 0.5
        else:
            raise ValueError("Type de Pokémon inconnu !")

        puissance_attaque = pokemon_attaquant.get_puissance_attaque() * multiplicateur
        pokemon_defenseur.set_points_de_vie(pokemon_defenseur.get_points_de_vie() - puissance_attaque)
        print(f"{pokemon_attaquant.get_nom()} attaque {pokemon_defenseur.get_nom()} ! {puissance_attaque} points de vie en moins.")

    def tour(self):
        self.lancer_attaque(self.pokemon1, self.pokemon2)
        if not self.est_termine():
            self.lancer_attaque(self.pokemon2, self.__pokemon1)
def combat(self):
        print(f"Combat entre {self.pokemon1.get_nom()} et {self.pokemon2.get_nom()} !")
        while not self.est_termine():
            self.tour()

        print(f"Le vainqueur est : {self.obtenir_vainqueur()} !")