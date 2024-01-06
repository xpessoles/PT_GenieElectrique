import numpy as np
import matplotlib.pyplot as plt
import math as m
f = 50 #Hz
Veff = 230 # Veff = Vc/sqrt(2)
Vc = Veff * m.sqrt(2) # Tension de crête

Ieff = 150 #A

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


def plot_ui_condensateur():
    plt.close()
    les_t = np.linspace(0,.06,1000)
    f = 50 #Hz
    Eeff = 230 # Veff = Vc/sqrt(2)
    Ec = Eeff * m.sqrt(2) # Tension de crête

    #Ieff = 150 #A

    omega = 2*m.pi*f
    T = 1/f
    phi = 0 #0.8
    C = 1e-4
    les_e = Ec*np.cos(omega*les_t)
    les_i =-C*omega*Ec* np.sin(omega*les_t)
    plt.plot(les_t,les_v,label="Tension (V)")
    plt.plot(les_t,les_i,label="Courant (A)")
    #plt.plot(les_t,les_pi,label="Puissance instantanée (W)")
    plt.legend(loc='upper right')
    plt.grid()
    plt.show()



def plot_cos_sin():
    plt.close()
    les_t = np.linspace(0,.06,1000)
    f=50
    omega = 2*m.pi*f


    les_c = np.cos(omega*les_t)
    les_s = np.sin(omega*les_t)
    les_cs = les_c*les_s
    plt.plot(les_t,les_cs,label="cos x sin")
    plt.plot(les_t,les_c,label="cos")

    #plt.plot(les_t,les_pi,label="Puissance instantanée (W)")
    plt.legend(loc='upper right')
    plt.grid()
    plt.show()

def plot_V_tri():
    plt.close()
    les_t = np.linspace(0,.06,1000)
    f=50
    Ueff = 230
    omega = 2*m.pi*f
    les_v1 = Ueff*m.sqrt(2)*np.sin(omega*les_t)
    les_v2 = Ueff*m.sqrt(2)*np.sin(omega*les_t-2*m.pi/3)
    les_v3 = Ueff*m.sqrt(2)*np.sin(omega*les_t-4*m.pi/3)

    plt.plot(les_t,les_v1,label="$v_1(t)$")
    plt.plot(les_t,les_v2,label="$v_2(t)$")
    plt.plot(les_t,les_v3,label="$v_3(t)$")

    plt.legend(loc='upper right')
    plt.grid()
    plt.show()


def plot_U_tri():
    plt.close()
    les_t = np.linspace(0,.04,1000)
    f=50
    Ueff = 230
    omega = 2*m.pi*f
    les_v1 = Ueff*m.sqrt(2)*np.sin(omega*les_t)
    les_v2 = Ueff*m.sqrt(2)*np.sin(omega*les_t-2*m.pi/3)
    les_v3 = Ueff*m.sqrt(2)*np.sin(omega*les_t-4*m.pi/3)

    les_u_12 = les_v1-les_v2
    les_u_23 = les_v2-les_v3
    les_u_31 = les_v3-les_v1
    plt.plot(les_t,les_v1,linestyle='dashed', linewidth=1,label="$v_1(t)$")
    #plt.plot(les_t,les_v2,linestyle='dashed', linewidth=1,label="$v_2(t)$")
    #plt.plot(les_t,les_v3,linestyle='dashed', linewidth=1,label="$v_3(t)$")

    plt.plot(les_t,les_u_12,label="$u_{12}(t)$")
    plt.plot(les_t,les_u_23,label="$u_{23}(t)$")
    plt.plot(les_t,les_u_31,label="$u_{31}(t)$")

    plt.legend(loc='upper right')
    plt.grid()
    plt.show()
