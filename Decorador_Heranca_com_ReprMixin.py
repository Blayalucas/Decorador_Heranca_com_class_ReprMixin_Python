# Decoração com Classe - Class MyReprMixin

"""
Decorador com class MyReprMixin em MINHA PERCEPÇÃO faz com que: 
A Herança entre classe seja realizada de uma forma " fácil de compreender
usando o repr e fazendo o comando Basico de atributos do Dunder __Repr__


"""
# Passo 1 - Criar um ReprMixin - com comando básico de atributos do Dunder __ Repr__
class MyReprMixin: 
    def __repr__(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f"{class_name}({class_dict})"
        return class_repr

# Passo 2 - Class "Mãe" 
class SuperVeiculo:
    ...

# Passo 3 - Class "Filha"
class Veiculo  (SuperVeiculo,MyReprMixin): # class "Filha" herda Classe Mãe e o repr
    def __init__(self, nome):
        self.nome = nome
        
        
# Passo 4 - Class Neta 
class Moto (MyReprMixin): # Classe "Neta" herda o repr
    def __init__(self, nome):
        self.nome = nome

# Passo 5 - Instancia por modelos de automoveis 
hb20 = Veiculo ( "HB20")
onix = Veiculo ("Onix")

hornet = Moto ("Hornet")
xj6 = Moto ("XJ6")

# Passo 6 - print na tela em forma de Biblioteca com tupas
print(hb20)
print(onix)
print(hornet)
print(xj6)
