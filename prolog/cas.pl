:- op(300, xfy, ^).

d(X, X, D) :- atomic(X), !, D = 1.
d(C, _, D) :- atomic(C), !, D = 0.
d(U+V, X, DU+DV) :- d(U, X, DU), d(V, X, DV).
d(U-V, X, DU-DV) :- d(U, X, DU), d(V, X, DV).
d(U*V, X, DU*V+U*DV) :- d(U, X, DU), d(V, X, DV).
d(U^N, X, N*U^N1*DU) :- number(N), N1 is N-1, d(U, X, DU).
d(-U, X, -DU) :- d(U, X, DU).
d(sin(U),X,cos(U)*DU) :- d(U,X,DU).
d(cos(U),X,-sin(U)*DU) :- d(U,X,DU).

simplify(X+Y,Erg) :-   
				simplify(X,Z1), 
		    	simplify(Y,Z2),
		    	(not(X=Z1); not(Y=Z2)), 
		    	simplify(Z1+Z2, Erg).

simplify(X-Y,Erg) :-   
				simplify(X,Z1), 
		    	simplify(Y,Z2),
		    	(not(X=Z1); not(Y=Z2)), 
		    	simplify(Z1-Z2, Erg).

simplify(X*Y,Erg) :-   
				simplify(X,Z1), 
		    	simplify(Y,Z2),
		    	(not(X=Z1); not(Y=Z2)), 
		    	simplify(Z1*Z2, Erg).

simplify(A*(B*C^D), Z*C^D) :- number(A), number(B), Z is A * B.
simplify(A*(B*C), Z*C) :- number(A), number(B), Z is A * B.

simplify(X,X) :- atomic(X), !.
simplify(X^1,X) :- !. 
simplify(X^N,X^N) :- !. 

simplify(A*B,X) :- number(A), number(B), X is A*B.
simplify(A+B,X) :- number(A), number(B), X is A+B.
simplify(A-B,X) :- number(A), number(B), X is A-B.
simplify(X*N, N*X) :- number(N), not(number(X)).
simplify(A*(B*C), R) :- simplify(A*B*C, R).
simplify((A),A) :- atomic(A).
simplify((B*C)*A, B*C*A).

simplify(0*_,0) :- !.
simplify(1*X,X) :- !.
simplify(_*0,0) :- !.
simplify(X*1,X) :- !.
simplify(0+X,X) :- !.
simplify(X+0,X) :- !.
simplify(0-X,-X) :- !.
simplify(X-0,X) :- !.
simplify(X,X) :- !.