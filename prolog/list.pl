mylen([], 0).
mylen([_|R], Res) :-
	mylen(R, Res1),
	Res is Res1+1.

len_rr([], Z, Z).
len_rr([_|R], Z, E) :-
    Z1 is Z+1,
    len(R, Z1, E).
len_rr(L, E) :- len(L, 0, E).
   
myhas([H|_], H).
myhas([_|R], E) :-
    myhas(R, E).

mycopy([], []).
mycopy([H|R1], [H|R2]) :-
    mycopy(R1, R2).

mydelete(E, [E|R], R).
mydelete(E, [H|R1], [H|R2]) :- mydelete(E, R1, R2).

delete_all([], _, []).
delete_all([E|R1], E, R2) :- delete(R1, E, R2).
delete_all([K|R1], E, [K|R2]) :- delete(R1, E, R2)

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