Spectral Energy Budget for Shallow Water 1-layer equations
==========================================================

These are notes for deriving the shallow water equation energy budget
which are more formally described in my `Ph.D.
thesis <https://urn.kb.se/resolve?urn=urn%3Anbn%3Ase%3Akth%3Adiva-256564>`_ and
implemented in
`FluidSim <https://fluidsim.readthedocs.io/en/latest/generated/fluidsim.solvers.sw1l.output.spect_energy_budget.html>`_.

Although originally intended for the classical shallow water equations, the
derivation was extended to examine energetics of a variant of it: a toy-model.

**Keywords**: *Helmholtz decomposition, normal mode decompositon, spectral energy budget, shallow water equations*

How to
------

Compile everything (figures + latex)::

  make

Clean the latex files::

  make clean

Clean everything (figures + latex)::

  make cleanall

Produce figure with Python::

  make pyfig

Display help messages::

  make help
