len([], 0).
len([_|R], Res) :-
   len(R, Res1),
   Res is Res1 + 1.
   
has(K, [K|_]).
has(K, [_|R]) :- has(K, R).

% recursive copy
copy([], []).
copy([B|Rest], [B|ARest]) :- copy(R, ARest).
% alt: 
% copy([B|R], L) :- 
   % L = [B|AR],
   % copy(R, AR).

delete(K, [K|Rest], Rest).
delete(A, [B|Rest], [B|ARest]) :- delete(A, Rest, ARest).

insert(A, L, R) :- delete(A, R, L).  % Aufruf geht in delete(K, [K|Rest], Rest). -> Unifikation mittlere Variable
   % R = [A|L]

append([], L, L).
append([A|Rest], L, [A|CRest]) :- append(Rest, L, CRest).

nelem(1, [K|_], K).
nelem(N, [_|Rest], E) :- 
   N1 is N - 1,
   nelem(N1, Rest, E).