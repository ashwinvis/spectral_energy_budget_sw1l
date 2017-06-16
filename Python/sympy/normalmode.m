syms f ck 
sig = sqrt(f**2 + ck**2)
sig = 0
A = [-sig, 1j*f,0 ; -1j*f, -sig, -1j*ck ; 0,1j*ck,-sig]
d = eig(A)