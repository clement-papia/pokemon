import json

class Pokedex:
    def init(self):
        self.pokemons = {}
        self.charger_pokemons()

    def charger_pokemons(self):
        try:
            with open("pokedex.json", "r") as f:
                self.pokemons = json.load(f)
        except FileNotFoundError:
            pass

    def sauvegarder_pokemons(self):
        with open("pokedex.json", "w") as f:
            json.dump(self.pokemons, f, indent=4)

    def ajouter_pokemon(self, pokemon):
        nom = pokemon.get_nom()
        if nom in self.pokemons:
            print(f"Le Pokémon {nom} est déjà enregistré dans le Pokédex !")
            return

        self.pokemons[nom] = {
            "type": type(pokemon).name,
            "defense": pokemon.get_defense(),
            "puissance_attaque": pokemon.get_puissance_attaque(),
            "points_de_vie": pokemon.get_points_de_vie()
        }

        self.sauvegarder_pokemons()
        print(f"Le Pokémon {nom} a été ajouté au Pokédex !")

    def afficher_pokemons(self):
        nb_pokemons = len(self.pokemons)
        print(f"Il y a {nb_pokemons} Pokémon(s) dans le Pokédex):
        for nom, infos in self.__pokemons.items():
            print(f"- {nom} ({infos['type']}) : {infos['defense']} DEF, {infos['puissance_attaque']} ATK, {infos['points_de_vie']} PV") 