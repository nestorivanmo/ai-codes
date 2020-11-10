class Tablero():
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
                    cadena += "-"
                else:
                    cadena += "Q"
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
   

def breadth(inicial, generador):
    hijos = []
    hijos.append(inicial)
    soluciones = set()
    level = inicial.dimension
    while hijos:                
        for hijo in generador(hijos.pop()):
            if hijo.level == level:
                soluciones.add(hijo)
            hijos.append(hijo)
    return soluciones 

def find_chessboards(n_queens, n_sols, verbose):
    boards = breadth(Tablero(n_queens), Tablero.genLevel)
    if verbose:
        i = 0
        for b in boards:
            if i < n_sols:
                print(b)
            else:
                break 
            i += 1
    print(f"{len(boards)} chessboards for {n_queens} queens")
    

if __name__ == '__main__':
    n_queens = int(input("N-queen problem. Insert the number of queens: "))
    verbose = int(input("Verbose? 0/1: "))
    n_sols = None
    if verbose:
        n_sols = int(input("Insert the number of solutions to print: "))
    find_chessboards(n_queens, n_sols, verbose)  