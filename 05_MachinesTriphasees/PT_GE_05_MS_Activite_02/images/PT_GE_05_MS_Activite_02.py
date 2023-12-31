import math as m

phi = m.acos(0.8)

In = 200
Un = 2885
Ie = 32

A = In*In

B = -2*Un*In*m.sin(phi)

C = Un*Un - 100*100*Ie * Ie

Delta = B*B - 4*A*C

s1 = (-B-m.sqrt(Delta))/(2*A)
s2 = (-B+m.sqrt(Delta))/(2*A)
print(s1,s2)

