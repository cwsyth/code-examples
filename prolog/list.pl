mylen([], 0).
mylen([_|R], Res) :-
	mylen(R, Res1),
	Res is Res1+1.
   
myhas([H|_], H).
myhas([_|R], E) :-
    myhas(R, E).

mycopy([], []).
mycopy([H|R1], [H|R2]) :-
    mycopy(R1, R2).

mydelete(E, [E|R], R).
mydelete(E, [H|R1], [H|R2]) :- mydelete(E, R1, R2).

myinsert(E, L, Res) :- Res = [E|L].
% myinsert(E, L, Res) :- mydelete(E, Res, L).

myappend(E, [], E).
myappend(E, [H|R1], [H|R2]) :-
    myappend(E, R1, R2).

reverse([], T, T).
reverse([H|R1], T, Res) :- reverse(R1, [H|T], Res).
reverse(L, Res) :- reverse(L, [], Res).

perm([], []).
perm([A|Rest], L) :- delete(A, L, Z), perm(Rest, Z).

nelem(1, [K|_], K).
nelem(N, [_|Rest], E) :- 
   N1 is N - 1,
   nelem(N1, Rest, E).