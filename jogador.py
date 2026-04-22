import copy
class Jogador:
    def __init__(self, nome, lvl=1, hpmaximo = 100):
        self.__nome = nome
        self.__lvl = lvl #incializa com level 1
        self.__xp = 0
        self.__xp_sobenivel = lvl*10 #cada nivel precisa de mais xp pra upar. ex: lvl 1 = 10xp, lvl 2 = 20xp, lvl 3 = 30xp
        self.__hp_maximo = hpmaximo
        self.__hp = self.__hp_maximo #incializa com o hp cheio
        
    # CONSTRUTORES
    @classmethod
    def criar_iniciante(cls, nome):
        return cls(nome, lvl=1, hpmaximo=100)

    @classmethod
    def criar_veterano(cls, nome):
        return cls(nome, lvl=10, hpmaximo=300)

    @classmethod
    def criar_copia(cls, outro_jogador):
        return copy.copy(outro_jogador)


    #PROPRIEDADES


    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def hp(self):
        return self.__hp
    
    @hp.setter
    def hp(self, valor):
        self.__hp = max(0, min(self.__hp_maximo, valor))  # entre 0 e hp_maximo

    @property
    def xp(self):
        return self.__xp
    
    @xp.setter
    def xp(self,xp):
        self.__xp = xp

    @property
    def lvl(self):
        return self.__lvl
    
    @lvl.setter
    def lvl(self, valor):
        self.__lvl = max(0, valor)  # nível nunca negativo, >0

    #MEDODOS_PUBLICOS

    def estaVivo(self): #verifica se o boneco está vivo
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

    def ganhaXp(self, qtdxp):
        self.__xp += qtdxp
        print(f"{self.__nome} recebeu {qtdxp} XP!")
        if self.__xp >= self.__xp_sobenivel:
            self.__lvl_up()

    def __lvl_up(self):
        #operando o xp
        xp_sobra = self.__xp - self.__xp_sobenivel #calcula o quanto de xp sobrou pra iniciar no proximo nivel.
        self.__lvl+=1 #sobe o nivel em 1
        self.__xp_sobenivel = self.__lvl*10 #atualiza a quantidade necessaria para upar de lvl
        self.__xp = xp_sobra #atualiza a quantidade de xp que jogador tem
        
        self.__hp_maximo +=10 #sobre o maximo do jogado
        print(f"O jogador {self.__nome} alcançou o Nivel: {self.__lvl}!")
        if self.__xp >= self.__xp_sobenivel: #encerral lvl_up
            self.__lvl_up() #chamada recursiva caso o jogador receba quantidade suficiente pra upar mais de um lvl

    def __del__(self):#destrutora do objeto Jogador .
        print(f"Jogador {self.__nome} removido.")