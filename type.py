class Pokemon:
    def init(self, nom, points_de_vie, puissance_attaque, defense):
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.puissance_attaque = puissance_attaque
        self.defense = defense

    def get_nom(self):
        return self.nom

    def set_nom(self, nom):
        self.nom = nom

    def get_points_de_vie(self):
        return self.points_de_vie

    def set_points_de_vie(self, points_de_vie):
        self.points_de_vie = points_de_vie

    def get_puissance_attaque(self):
        return self.puissance_attaque

    def set_puissance_attaque(self, puissance_attaque):
        self.puissance_attaque = puissance_attaque

    def get_defense(self):
        return self.defense

    def set_defense(self, defense):
        self.defense = defense

    def attaquer(self, autre_pokemon):
        print(f"{self.nom} attaque {autre_pokemon.get_nom()} !")

    def est_ko(self):
        return self.points_de_vie <= 0

    def afficher_infos(self):
        print(f"{self.nom} - Points de vie : {self.points_de_vie}, Attaque : {self.puissance_attaque}, Defense : {self.defense}")


class PokemonNormal(Pokemon):
    def init(self, nom):
        super().init(nom, 100, 20, 20)


class PokemonFeu(Pokemon):
    def init(self, nom):
        super().init(nom, 80, 30, 10)


class PokemonEau(Pokemon):
    def init(self, nom):
        super().init(nom, 120, 10, 30)


class PokemonTerre(Pokemon):
    def init(self, nom):
        super().init(nom, 150, 10, 10)