from pacient import Paciente

class Idoso(Paciente):
    def __init__(self, nome, idade, peso, altura, endereço):
        super().__init__(nome, idade, peso, altura, endereço)
        self.id = None
        self.comorbidades = []
        self.atividades = []
      
    def getID(self):
        return self.id
    
    def compareID(self, i):
        return (self.id == i)
    
    def getNome(self):
        return self.nome
    
    def setNome(self,nome):
        self.nome = nome
    
    def getIdade (self):
        return self.idade
    
    def setIdade(self,idade):
        self.idade = idade
    
    def getPeso(self):
        return self.peso
    
    def setPeso(self,peso):
        self.peso = peso
    
    def getAltura(self):
        return self.altura
    
    def setAltura(self,altura):
        self.altura = altura
    
    def getEndereco(self):
        return self.endereco
    
    def setEndereco(self,endereco):
        self.endereco = endereco
    
    
    def getComorbidades(self):
        return self.comorbidades
    
    def addComorbidade(self,comorbidade):
        if(comorbidade in TipoComorbidades.__members__):
            self.comorbidades.append(comorbidade)
        elif((isinstance (comorbidade,int))and (comorbidade <=(len(TipoComorbidades)))):
            tipo = TipoComorbidades(comorbidade).name
            self.comorbidades.append(tipo)
        else: 
            return -1
        #self.ordenaComorbidades()
    
    def hasComorbidade(self,comorbidade):
        return (comorbidade in self.comorbidades)
    
    def nComorbidades(self):
       return len(self.comorbidades)
   
    def ordenaComorbidades(self):
        self.comorbidades = sorted(self.comorbidades,key = lambda x: (x.tipo),reverse = False)
    
    def removeComorbidade(self,comorbidade):
        if(isinstance(comorbidade, int)):
            if(comorbidade<self.nComorbidades()):
                del self.comorbidades[comorbidade]
            #poderia fazer um else com excecao
        elif (isinstance(comorbidade, str)):
            if(self.temComorbidade(comorbidade)):
                self.comorbidades.remove(comorbidade)
            #poderia fazer um else com excecao
            

