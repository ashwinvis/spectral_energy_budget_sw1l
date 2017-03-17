# coding: utf-8
from sympy import *
from normalmode import *


# init_session()
# get_ipython().magic(u'run normalmode.py')

init_printing()

A = Matrix(( [-sig, 1j*f,0],[-1j*f, -sig, -1j*ck],[0,1j*ck,-sig]))
pprint(A.eigenvects())

XnT = Matrix(( [-ck/f,0,1], [f,1j*sqrt(ck**2+f**2),ck], [f,-1j*sqrt(ck**2+f**2),ck] ))
sig = sqrt(f**2+ck**2)
sig2 = (sqrt(2)*sig)
Xn = Matrix(( [-ck/sig,0,f/sig], [f/sig2,-1j*sqrt(ck**2+f**2)/sig2,ck/sig2], [f/sig2,1j*sqrt(ck**2+f**2)/sig2,ck/sig2] ))
Xn = Xn.transpose()
print 'Xn='
pprint(Xn)

XnT = Matrix(( [-ck/sig,0,f/sig], [f/sig2,1j*sqrt(ck**2+f**2)/sig2,ck/sig2], [f/sig2,-1j*sqrt(ck**2+f**2)/sig2,ck/sig2] ))
print 'XnT*Xn='
pprint(XnT*Xn)
