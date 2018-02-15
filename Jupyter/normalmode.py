# coding: utf-8
from sympy import *
from sympy.abc import psi, phi, eta

init_printing()
sigma, kappa = symbols('\sigma \kappa', real=True)
f,ck,c = symbols('f ck c', real=True)
kx, ky=  symbols('kx ky')
u,v =  symbols('u v')

def subsigma(M):
    return M.subs(f**2 + ck**2,  sigma**2)
    
def simplifysigma(M):
    M = M.subs(sigma, sqrt(f**2 + ck**2) )
    M = simplify(M)
    return subsigma(M)
    
def subkappa(M):
    return M.subs(kx**2 + ky**2,  kappa**2)

def simplifykappa(M):
    M = M.subs(kappa, sqrt(kx**2 + ky**2) )
    M = simplify(M)
    return subkappa(M)
    
def subck(M):
    return M.subs(ck,c*kappa)

A = Matrix(( [0, 1j*f,0],[-1j*f, 0, -1j*ck],[0,1j*ck,0]))
L = A.eigenvals()
X = A.eigenvects()
print('Eigenvectors: ')
pprint(X)
#==============================================================================
# for j in xrange(2,-1,-1):
#     print j
#     pprint(X[j][2])
#     
#==============================================================================

XX = A.diagonalize()[0]
XX = subsigma(XX)
sig = sqrt(f**2 + ck**2)

NORM = eye(3)
NORM[0,0] = f/sig
NORM[1,1] = ck/(sig*sqrt(2))
NORM[2,2] = ck/(sig*sqrt(2))
XN = subsigma(XX*NORM)

CONJ = eye(3)
CONJ[1,1] = -1
XNCT = (CONJ*XN).transpose() 
XNCT = subsigma(XNCT)
 
#------------Check-----------#
ID = simplifysigma(XN*XNCT)
print 'Identity matrix:'
pprint(ID)
#---------------------------#
print 'Norm. Eigenvector matrix Xn:'
pprint(XN)

W = Matrix( [psi, -phi, c*eta/kappa] ) * kappa ** 2
# N = XNCT*W =  XNCT*P*U
U = Matrix( [u,v,eta] )
P = Matrix(( [-1j*ky, 1j*kx, 0],[1j*kx,1j*ky,0],[0,0,ck] ))

Pinv = simplifykappa(P.inv())
XNCTinv = simplifysigma(XNCT.inv())

Q = Pinv*(XNCTinv)
Q = simplifysigma(Q)
Q = simplifykappa(Q)
Q = subck(Q)

print 'inversion:'
pprint(U); print '=' ;  pprint(Q); pprint(W)
