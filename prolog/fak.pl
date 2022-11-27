fak(0, 1) :- !.
fak(N, Res) :- 
   	N1 is N-1,
    fak(N1, Res1),
    Res is N * Res1.

fak_rr(0, Z, Res) :- Res is Z.
fak_rr(N, Z, Res) :-
    N1 is N - 1,
    Z1 is Z * N,
    fak_rr(N1, Z1, Res).
fak_h(4, Res) :- fak_rr(7, 1, Res).
