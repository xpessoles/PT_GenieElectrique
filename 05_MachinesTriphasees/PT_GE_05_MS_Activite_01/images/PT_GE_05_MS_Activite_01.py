import math as m

phi = m.acos(0.87)

V = 2880
R = 0.2
Icc = 200
Lom = 0.95

E = R*R *Icc*Icc+ V*V + Icc*Icc*Lom*Lom
E = E+ 2*V*Icc*(R*m.cos(phi)+Lom*m.sin(phi))

E = E**.5
print(E)