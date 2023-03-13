class Pokemon:
    def init(self, nom, points_de_vie):
        self.nom = nom
        self.points_de_vie = points_de_vie

    def get_nom(self):
        return self.nom

    def set_nom(self, nom):
        self.nom = nom

    def get_points_de_vie(self):
        return self.points_de_vie

    def set_points_de_vie(self, points_de_vie):
        self.points_de_vie = points_de_vie

    def attaquer(self, autre_pokemon):
        print(f"{self.nom} attaque {autre_pokemon.get_nom()} !")

    def est_ko(self):
        return self.points_de_vie <= 0