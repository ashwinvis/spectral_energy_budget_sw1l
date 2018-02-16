import sympy
print(sympy.__version__)

from sympy import *
from sympy.vector import curl, divergence, gradient, Del
from sympy.abc import eta, psi, chi, theta, phi
init_printing()

global R
global transformation

u1, u2, u3 = symbols('u1:4', type='Function')
f1 = symbols('f_0', type='Function')
omega1 = symbols(r'\Omega', type='Function')
nabla = Del()
R.i = getattr(R, vec_names[0])
R.j = getattr(R, vec_names[1])
R.k = getattr(R, vec_names[2])
R.x = getattr(R, var_names[0])
R.y = getattr(R, var_names[1])
R.z = getattr(R, var_names[2])

u = u1(R.x, R.y, R.z) * R.i + u2(R.x, R.y, R.z) * R.j + u3(R.x, R.y, R.z) * R.k
e = eta(R.x, R.y, R.z)
if transformation == 'spherical':
    u_h = u2(R.x, R.y, R.z) * R.j + u3(R.x, R.y, R.z) * R.k
    stream = psi(R.y, R.z)
    pot = chi(R.y, R.z)
    u_r = -curl(R.i * stream).doit()
elif transformation == 'cartesian':
    u_h = u1(R.x, R.y, R.z) * R.i + u2(R.x, R.y, R.z) * R.j
    stream = psi(R.x, R.y)
    pot = chi(R.x, R.y)
    u_r = -curl(R.k * stream).doit()

u_d = gradient(pot).doit()
u_helm = u_r + u_d