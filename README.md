ds2-armor-optimizer
===================

A simple Dark Souls 2 Armor Optimizer, written in python, using linear programming.
Although the script is very simple, it outputs an OPTIMAL solution. 
That is, there's no better one for that given weight. 

The script doesn't account for weight reduction items, such as the prisioner's mask.


Dependencies
===================
- Python 3: The script is written in python.
- glpk: Gnu linear programming kit.
- pulp-py3: Python wrappers for glpk.


Instalation Guide (Arch Linux)
===================
- Install Python 3, pip for python 3 and glkp:

$ pacman -S python pip glpk

- Install pulp-py3
$ pip install pulp-py3

- Done! Now you can run the script with:
$ python ds2-armor-optimizer.py
