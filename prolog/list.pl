len([], 0).
len([_|R], Res) :-
   len(R, Res1),
   Res is Res1 + 1.
   
has(K, [K|_]).
has(K, [_|R]) :- has(K, R).

delete(K, [K|Rest], Rest).
delete(A, [B|Rest], [B|ARest]) :- delete(A, Rest, ARest).

insert(A, L, R) :- delete(A, R, L).

nelem(1, [K|_], K).
nelem(N, [_|Rest], E) :- 
   N1 is N - 1,
   nelem(N1, Rest, E).