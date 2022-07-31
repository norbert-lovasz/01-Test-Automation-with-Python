from abc import ABC, abstractmethod



class FormaGeometrica(ABC):
    PI = 3.14
    
    @abstractmethod #decorator = element care schimba comportamentul unei metode
    def aria(self):
        raise NotImplementedError
    
    @abstractmethod
    def descrie(self):
        print('Cel mai probabil am colturi')
    

class Patrat(FormaGeometrica): #Inheritance
    __latura = 30              #Encapsulation, private memeber
    def __init__(self, latura):
        self.__latura = latura
        
    def aria(self): #Contine metode abstracta Aria
        aria = self.__latura**2
        return aria
    
    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        print(f'Getter: Latura este {self.__latura}')
        return self.__latura

    @latura.setter
    def latura(self, latura):
        self.__latura = latura
        print(f'Setter: Noua latura este {latura}')

    @latura.deleter
    def latura(self):
        print(f'Deleter: Am sters latura')
        self.__latura = None
        

class Cerc(FormaGeometrica):
    
    __raza = 10
    
    def __init__(self, raza):
        self.__raza = raza
        
        
    def aria(self): #Contine metode abstracta Aria
        aria = self.__raza*self.__raza*self.PI
        print(f"Aria este {aria}")
        return aria
    
    def descrie(self):
        print('Cel mai probabil nu am colturi')
        
    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print(f'Getter: Raza este {self.__raza}')
        return self.__raza

    @raza.setter
    def latura(self, raza):
        self.__raza = raza
        print(f'Setter: Noua raza este {raza}')

    @latura.deleter
    def raza(self):
        print(f'Deleter: Am sters raza')
        self.__raza = None
        
    
        


# figura = Patrat(30)
# figura.aria()
# figura.descrie()
# figura.latura=45
# figura.latura=20

figura2 = Cerc(10)
figura2.aria()
figura2.descrie()
figura2.raza=45
figura2.raza=20




    