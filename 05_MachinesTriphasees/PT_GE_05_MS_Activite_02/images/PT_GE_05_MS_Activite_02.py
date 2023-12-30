import math as m

phi = m.acos(0.8)

In = 200
Un = 2885
Ie = 32

A = In*In

B = -2*Un*In*m.sin(phi)

C = Un*Un - 100*100*Ie * Ie