% fib recursive
fib(0, 1) :- !.
fib(N, Res) :- 
    N1 is N-1,
    N2 is N-2,
    fib(N1, Res1),
    fib(N2, Res2),
    Res is Res1 + Res2.

% fib recursive repetitive
fib_rr(0, P1, _, Res) :- Res is P1.
% fib_rr(0, Res, _, Res) :- !.
fib_rr(N, P1, P2, Res) :-
    PN is P1 + P2,
    NN is N-1,
 	fib_rr(NN, PN, P1, Res).
fib_h(N, Res) :- fib_rr(N, 1, 0, Res).
