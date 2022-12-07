/* Haus des Nikolaus */

kante(a, b).
kante(a, c).
kante(a, d).
kante(b, c).
kante(b, d).
kante(c, d).
kante(c, e).
kante(d, e).

enthalten(A, B, [A,B|_]).
enthalten(B, A, [B,A|_]).
enthalten(A, B, [_|Rest]) :- enthalten(A, B, Rest).

// laufen(X, Y, Z) :- kante(X, Y), kante(Y, Z).
nikolaus([_], [_]).
nikolaus([A,B|Rest]) :- (kante(A, B) ; kante(B, A)),
    					not(enthalten(A, B, Rest)),
    					nikolaus([B|Rest]).
    					