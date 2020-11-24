father(juan, pedro).
father(juan, maria).
father(jose, juan).
mother(petra, pedro).
parent(X,Y) :- father(X,Y).
parent(X,Y) :- mother(X,Y).
grandparent(X,Y) :- parent(X,Y), 
    				parent(X,Y).

sumlist([],0).
sumlist([H|T],R) :- sumlist(T,R0), R is H+R0.

find(X,[X|_]).
find(X, [_|T]) :- find(X,T).



unir([], L, L).
unir([H], L, [H|L]).
unir([H|T], L, [H|L1]) :- unir(T, L, L1).

cp([_], [], []).
cp([H1], [H2|T2], [[H1,H2]|[T3]]) :- 
    cp([H1], T2, T3).
cp([H1|T1], L2, L3) :-
    cp([H1],L2,L31),
    cp(T1,L2,L32),
    unir(L31,L32,L3),!.
