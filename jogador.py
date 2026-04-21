class Jogador:
    def __init__(self, nome, lvl=1, hpmaximo = 100):
        self.nome = nome
        self.__lvl = lvl #incializa com level 1
        self.__hp_maximo = hpmaximo
        self.__hp = self.__hp_maximo #incializa com o hp cheio

    #PROPRIEDADES


    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, valor):
        self.__hp = max(0, min(self.__hp_maximo, valor))  # entre 0 e hp_maximo

    @property
    def lvl(self):
        return self.__lvl

    @lvl.setter
    def lvl(self, valor):
        self.__lvl = max(0, valor)  # nível nunca negativo, >0

    #MEDODOS_PUBLICOS

    def estaVivo(self):
        if self.hp > 0:
            return True
        else: 
            return False
        
    def exibirStatus(self):
        if self.estaVivo():
            print(f"|NOME: {self.nome}|HP: {self.hp}/{self.__hp_maximo} |Level: {self.__lvl}|")
        else:
            print(f"|GAMEOVER: {self.nome} ESTÁ MORTO!|")

        
    def receberDano(self, dano):
        if self.estaVivo():
            self.hp -=dano #mexe no hp com setter, protegido
            print(f"{self.nome} recebeu {dano} de dano!\n")
        
    def curar(self, cura):
        if self.estaVivo():
            self.hp +=cura #mexe no hp com setter, protegido
            print(f"{self.nome} recebeu {cura} de cura!\n")