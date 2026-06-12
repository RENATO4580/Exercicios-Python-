class Gato:
    def __init__(self,raca: str,cor: str,tipo__pelo: str,idade: int,nome:str):
        """
        Docstring for __init__
        
        :param self: Comando que faz os atributos e métodos olharem para a classe 
        :param raca: Digite a raça do gato
        :type raca: str
        :param cor: Digite a cor do gato
        :type cor: str
        :param tipo__pelo: Digite o tipo do pelo(Sem pelo, Pelo longo, Pelo curto)
        :type tipo__pelo: str
        :param idade: Digite a idade do gato com um número inteiro 
        :type idade: int
        :param nome: Digite o nome do gato
        :param str: Description
        """

        self.nome = nome
        self.idade = idade
        self.tipo__pelo = tipo__pelo
        self.cor = cor
        self.raca = raca
    def miar(self):
        print(f"O {self.nome} miou")


meu__gato = Gato("Angorá","Preto","pelo longo",7,"Dengoso")
meu__gato.miar()


    