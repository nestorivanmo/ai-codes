class Tablero():
    costo = 0
    def __init__(self, n):
        self.dimension = n
        self.reinas = set()
        self.level = 0

    def __hash__(self):
        return hash((self.level,tuple(self.reinas)))

    def __getitem__(self, key):
        return self.reinas[key]

    def set(self, y, x):
        item = y,x,
        if item not in self.reinas:
            self.reinas.add(item)
            self.level = self.level + 1  
        else:
            raise Exception("Reina ya existente")
            
    def __str__(self):
        cadena = ""
        for y in range(0, self.dimension):
            for x in range(0, self.dimension):
                temp = x,y,
                if temp not in self.reinas:
                    cadena += " - "
                else:
                    cadena += " Q "
            cadena += "\n"
        return cadena

    def __eq__(self, other):
        resultado = True
        for reina in self.reinas:
            if reina not in other.reinas:
                resultado = False
                break
        return resultado

    @staticmethod
    def copy(other):
        copia = Tablero(other.dimension)
        copia.reinas.clear()
        copia.level = other.level
        copia.dimension = other.dimension
        copia.reinas = {x for x in other.reinas}
        return copia
    
    @staticmethod
    def genLevel(tablero):
        for i in range(0, tablero.dimension):
            aux = Tablero.copy(tablero)
            if Tablero.validar(aux, aux.level, i):            
                aux.set(aux.level, i)
                yield aux
    
    @staticmethod
    def validar(tablero, x, y):
        for yi in tablero.reinas:
            if y == yi[1]:
                return False
        for xi,yi in tablero.reinas:
            difx = x - xi
            dify = y - yi
            if difx == dify or difx == -dify:
                return False    
        return True   
   

def breadth(inicial, generador, n_sols, verbose):
    hijos = []
    hijos.append(inicial)
    level = inicial.dimension
    contador = 0
    while hijos:
        if n_sols == 0:
            break                
        for hijo in generador(hijos.pop()):
            Tablero.costo = Tablero.costo + 1
            if hijo.level == level:
                if verbose:
                    print(hijo)
                contador = contador + 1
                n_sols = n_sols - 1
                if n_sols == 0:
                    break
            else:
                hijos.append(hijo)

    print(f"{contador} chessboards for {level} queens")
    print(f"cost: {Tablero.costo}")

def find_chessboards(n_queens, n_sols, verbose):
    breadth(Tablero(n_queens), Tablero.genLevel, n_sols, verbose)

if __name__ == '__main__':
    n_queens = int(input("N-queen problem. Insert the number of queens: "))
    verbose = int(input("Verbose? 0/1: "))
    n_sols = int(input("Insert the number of solutions: "))
    find_chessboards(n_queens, n_sols, verbose)  