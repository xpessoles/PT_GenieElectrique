import numpy as np
import matplotlib.pyplot as plt
import math as m
f = 50 #Hz
Veff = 230 # Veff = Vc/sqrt(2)
Vc = Veff * m.sqrt(2) # Tension de crête

Ieff = 200 #A

omega = 2*m.pi*f
T = 1/f
phi = 0 #0.8

les_t = np.linspace(0,.06,1000)

les_i = Ieff * m.sqrt(2) * np.sin(omega*les_t)
les_v = Veff * m.sqrt(2) * np.sin(omega*les_t+phi)

les_pi = les_i*les_v

def plot_ui():
    plt.close()
    plt.plot(les_t,les_v,label="Tension (V)")
    plt.plot(les_t,les_i,label="Courant (A)")
    #plt.plot(les_t,les_pi,label="Puissance instantanée (W)")
    plt.legend(loc='upper right')
    plt.grid()
    plt.show()

def plot_uip():
    plt.close()
    plt.plot(les_t,les_v,label="Tension (V)")
    plt.plot(les_t,les_i,label="Courant (A)")
    plt.plot(les_t,les_pi,label="Puissance instantanée (W)")
    plt.legend(loc='upper right')
    plt.grid()
    plt.show()