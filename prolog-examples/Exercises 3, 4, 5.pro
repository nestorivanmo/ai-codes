factorial(0,1).
factorial(X,R):-
    			X > 0,
    			A is X-1, 
    			factorial(A,R0), 
    			R is X*R0. 
            
reverse([X],[X]).
reverse([X|T],R):- reverse(T,R0), append(R0,[X], R).

ocurrences(_,0,[]).
ocurrences(X,N,[X|T]):- ocurrences(X,R0,T), N is R0+1.
ocurrences(X,N,[Y|T]):- dif(X,Y), ocurrences(X,N,T). 