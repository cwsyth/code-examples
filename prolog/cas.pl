:- op(300, xfy, ^).
d(X, X, D) :- atomic(X), !, D = 1.
d(C, _, D) :- atomic(C), !, D = 0.
d(U+V, X, DU+DV) :- d(U, X, DU), d(V, X, DV).
d(U-V, X, DU-DV) :- d(U, X, DU), d(V, X, DV).
d(U*V, X, DU*V+U*DV) :- d(U, X, DU), d(V, X, DV).
d(U^N, X, N*U^N1*DU) :- N1 is N-1, d(U, X, DU).
d(-U, X, -DU) :- d(U, X, DU).