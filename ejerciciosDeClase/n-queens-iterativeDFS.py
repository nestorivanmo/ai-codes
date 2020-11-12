"""
N-Queens problem - BFS (Breath First Search)

Team members: 
- Carreón Guzmán Mariana Ivette
- Martínez Ostoa Néstor Iván
- Meza Ortega Fernando
- Pedraza Martínez José Alberto

N-Queens problem is a classic computer science problem could be stated as 
following: 

Description. Find (or count) all the possible ways to arrange n queens (1 <= n <
 inf) inside a nxn chess board in such that the queens must not attack each other.

Input. A integer n that represents the number of queens inside a nxn chess board.

Output. If n is relatively small (n < 8) then the problem should output all the 
possible chess board combinations where the queens cannot attack each other 
and enumerate each of them. Otherwise, just output the number of combinations 
inside the nxn chess board where the queens cannot attack each other.
"""
class Tablero():
    costo = 0
    def __init__(self, n):
        """
        La clase Tablero se define para guardar los atributos
        necesarios en este problema, lo que simplifica el trabajo
        al implementar breath first search (BFS)

        Parameters
        ----------
        n: int
            entero que representa la dimensión del tablero

        Attributes
        ----------
        costo: int
            la única variable de clase, encargada de almacenar el costo 
            de calcular todos los tableros pedidos

        dimension: int
            este entero almacena la dimensión del tablero

        reinas: set
            es un conjunto que almacena las posiciones de las reinas ya que es
            la única información que se necesita del tablero

        level: int
            se almacena el nivel del tablero y corresponde al número de reinas
            que tiene el tablero
        """
        self.dimension = n
        self.reinas = set()
        self.level = 0

    def __hash__(self):
        """Esta función sirve para poder guardar nuestros tableros en un conjunto
        se hace el hash del nivel y de las posiciones de las reinas, en este caso
        el método no es utilizado.
        ***Notar que no se puede aplicar hash a un conjunto de reinas, solo a tuplas
        
        Output
        ------
        int
            la salida es un entero generado por la función hash que Python define
        """
        return hash((self.level,tuple(self.reinas)))

    def set(self, fila, columna):
        """Esta funnción coloca una reina en la posición indicada por las cordenadas

        parameters
        ----------
        y : int
            la salida
        """
        item = fila,columna,
        if item not in self.reinas:
            self.reinas.add(item)
            self.level = self.level + 1  
        else:
            raise Exception("Reina ya existente")
            
    def __str__(self):
        cadena = ""
        for fila in range(0, self.dimension):
            for columna in range(0, self.dimension):
                temp = fila,columna,
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
    def validar(tablero, fila, columna):
        for reina in tablero.reinas:
            if columna == reina[1]:
                return False
        for fi,ci in tablero.reinas:
            diff = fila - fi
            difc = columna - ci
            if diff == difc or diff == -difc:
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
