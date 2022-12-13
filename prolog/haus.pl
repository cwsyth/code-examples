# Haus des Nikolaus

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

# überprüft nur Lösungen ob richtig/falsch
gehe([A, B|R]) :- 
    				(kante(A, B) ; kante(B, A)),
    				not(enthalten(A, B, [B|R])),
    				gehe([B|R]).
gehe([_]).