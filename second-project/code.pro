:-op(1,fx,neg).
:-op(2,xfy,or).
:-op(2,xfy,and).
:-op(3,xfy,implies).
:-op(3,xfy,dimplies).

%Case

secuentes([A],[A]):-write(A),write(' |- '), writeln(A).

% Negation

secuentes(Gamma,[neg D|Delta]):-union([D],Gamma,U),secuentes(U,Delta),
    write(Gamma),write(' |- '),writeln([neg D|Delta]).

secuentes([neg D|Gamma],Delta):-union([D],Delta,U),secuentes(Gamma,U),
    write([neg D | Gamma]),write(' |- '),writeln(Delta).

% Disjunction

secuentes(Gamma,[C or D|Delta]):- union([C,D],Delta,U),secuentes(Gamma,U),
    write(Gamma),write(' |- '),writeln([C or D | Delta]).

secuentes([C or D | Gamma],Delta):-union([C],Gamma,U1),union([D],Gamma,U2),secuentes(U1,Delta),secuentes(U2,Delta),
    write([C or D | Gamma]), write(' |- '), writeln(Delta).

% Conjunction

secuentes([C and D|Gamma],Delta):-union([C,D],Gamma,U),secuentes(U,Delta),
    write([C and D|Gamma]), write(' |- '), writeln(Delta).

secuentes(Gamma,[C and D|Delta]):-union([C],Delta,U1),union([D],Delta,U2),secuentes(Gamma,U1),secuentes(Gamma,U2),
    write(Gamma), write(' |- '), writeln([C and D|Delta]).

%Implication

secuentes([C implies D|Gamma],Delta):-union([C],Delta,U1),union([D],Gamma,U2),secuentes(Gamma,U1),secuentes(U2,Delta),
    write([C implies D|Gamma]), write(' |- '), writeln(Delta).

secuentes(Gamma,[C implies D|Delta]):- union([C],Gamma,U1),union([D],Delta,U2),secuentes(U1,U2),
    write(Gamma), write(' |- '), writeln([C implies D|Delta]).


%Double implication

secuentes([C dimplies D|Gamma],Delta):-union([C,D],Delta,U1),union([C,D],Gamma,U2),secuentes(Gamma,U1),secuentes(U2,Delta),
    write([C dimplies D|Gamma]), write(' |- '), writeln(Delta).

secuentes(Gamma,[C dimplies D|Delta]):-union([C],Gamma,U1),union([D],Delta,U2),union([D],Gamma,U3),union([C],Delta,U4),secuentes(U1,U2),secuentes(U3,U4),
    write(Gamma), write(' |- '), writeln([C dimplies D|Delta]).

% Structural rules

%Exchange

secuentes(Gamma,[H|T]):-atom(H),buscarNA(T),union(T,[H],U),secuentes(Gamma,U), T \== [],
    write(Gamma),write('|-'),writeln([H|T]).

% Weakening

secuentes(Gamma,Delta):-not(buscarNA(Gamma)),not(buscarNA(Delta)),buscar(Gamma, Delta),
    write(Gamma),write(' |- '),writeln(Delta).

buscarNA([H|_]):-not(atom(H)).
buscarNA([_|T]):-buscarNA(T).

buscar([H|_],L):-[H]\==[],member(H,L).
buscar([_|T],L):-buscar(T,L).

