#Jordan Breffle
#https://github.com/jtbreffle
#Theoretical Neuroscience Exercises, Dayan and Abbott, 2001
#Chapter 6: Model neurons II: Conductances and morphology


import scipy.io #use scipy.io.loadmat() for MAT files
import numpy as np #if loadmat() fails, then use numpy.loadtxt(), becuase it is a plain text file



# ------------------Helper Functions--------------------------------------



#----------------------------Exercises------------------------------------
def Ex1():
    '''
    Build aConnor-Stevensmodel neuron by numerically integrating the
    equations for V, m, h, n, a, and b given in chapter 6 (see, in particular,
    equations 6.1, 6.4, and appendix A). Use cm = 10 nF/mm2, and as
    initial values take: V = -68 mV, m = 0.0101, h = 0.9659, n = 0.1559,
    a = 0.5404, and b = 0.2887. Use an integration time step of 0.1 ms.
    Use an external current with Ie/A = 200 nA/mm2 and plot V, m, h, n,
    a, and b as functions of time over a suitable interval. Plot the firing
    rate of the model as a function of Ie/A over the range from 0 to 500
    nA/mm2. How does this differ from what you got for the Hodgkin-
    Huxley model in exercise 8 of chapter 5. Finally, apply a pulse of
    negative current with Ie/A = -500 nA/mm2 for 5 ms followed by
    Ie/A = 200 nA/mm2and show what happens.
    '''

def Ex2():
    '''
    Construct aMorris-Lecarmodel neuron (Morris, C & Lecar, H (1981)
    Voltage oscillations in the barnacle giant muscle fiber. Biophysical
    Journal 35:193–213). Instead of simulating the fast sodium spikes
    of an action potential, this model describes slower calcium spikes.
    The model has just two active currents, an instantaneous voltagedependent
    Ca2+ current and a persistent K+ current, described by a
    single dynamical gating variable N:
    
    im = gL(V - EL) + gCaMinfinity(V)(V - ECa) + gKN(V - EK)
    
    with gL = 0.005mS/mm2, gCa = 0.01mS/mm2 and gK = 0.02mS/mm2,
    EL = -50mV, ECa = 100mV and EK = -70mV. Use cm = 10 nF/mm2.
    The function Minfinity(V) is given by
    
    Minfinity(V) = 1 / (1 + e**[-0.133(V+1)]
    
    and the gating variable N is given by
    
    tauN(V) (dN/dt) = Ninfinity(V) - N
    
    with
    
    tauN(V) = 3 / (cosh[0.345(V-10)]
    
    and
    
    Ninfinity(V) = 1 / (1 + e**[-0.138(V - 10)]
    
    Here, V is understood to be in mV units, and tauN is expressed in ms
    units. Determine the firing rate as a function of injected current and
    plot themembrane potential andN as a functions of time. Also, show
    a phase-plane trajectory, which is a plot of that path taken by these
    variables in the two-dimensional space described by the points (V,N), while the model is firing. In the phase plane, plot the nullclines
    for the V and N equations. These are lines in the V-N plane along
    which either dV/dt = 0 or dN/dt = 0. (Phase-plane descriptions and
    nullclines are described in chapter 7.)
    '''
    
    
def Ex3():
    '''
    The FitzHugh-Nagumo equations (see FitzHugh, R (1961) Impulses
    and physiological states in models of nerve membrane. Biophysical
    Journal 1:445–466) are given by
    
    dv/dt =  v(1 - v**2) - u + Ie
    
    and
    
    du/dt = epsilon * (v - 0.5u)
    
    Draw the nullclines for these equations for Ie = 0 and Ie = -1. These
    are the lines in the v-u plane where the right side of one or the other
    of these two equations is zero. In which case or cases do you think
    the model will produce oscillations? Next simulate the model to
    see what happens when these equations are integrated over time.
    Determine what happens for Ie = 0 with epsilon = 0.3, 0.1, and 1 and for
    Ie = -1 with epsilon = 0.3. (Phase-plane descriptions and nullclines are
    described in chapter 7.)
    '''
    
def Ex4():
    '''
    Show that solution of equation 6.19 satisfies the cable equation
    along an infinite cable in response to the injected current ie =
    Ie*taum*d(x)d(t)/(2pia).
    '''
    
def Ex5():
    '''
    Verify that the solution for an isolated junction given by equations
    6.21 and 6.22 satisfies the correct boundary conditions at the junction
    point: v1(0) = v2(0) = v3(0) and
    
    3[sigma]i=1 (ai**2 * (dvi/dx)x=0) = 0
    '''
    
def Ex6():
    '''
    Generalize the solution for an isolated junction of equation 6.21 to
    the time-dependent case when the injected current on segment 2 is
    ie = Ie*taum*delta(x2 - y)delta(t)/(2pia).
    '''
    
def Ex7():
    '''
    Show that the expression for v(x) given in figure 6.10,with R1 and R2
    given by equations 6.23 and 6.24, satisfies the cable equation and the
    boundary conditions, v(0) = vsoma and dv/dx = 0 when x = L.
    '''
    
def Ex8():
    '''
    Show that the expression for v(x) given in figure 6.12,with R3 and R4
    given by equations 6.26 and 6.27, satisfies the cable equation and the
    boundary conditions, v(0) = 0 and dv/dx = 0 when x = L.
    '''
    
def Ex9():
    '''
    Construct a non-branching axonal cable with conductances in each
    compartment described by the Connor-Stevens model (as in exercise
    1). Solve for the membrane potential using the methods of
    appendix B of chapter 6. Initiate action potential propagation at one
    end of the cable by injecting current into the terminal compartment
    of the cable. Plot the action potential propagation velocity as a function
    of the axon radius. Inject current into the middle of the cable
    to generate two, opposite-moving action potentials. Generate action
    potentials from each end of the cable and show that they annihilate
    each other when they collide.
    '''
    
def Ex10():
    '''
    Determine the numerical solution for a multi-compartment cable
    with a single branching node (where a single cable splits into two
    branches) analogous to the solution for a non-branching cable (equations
    6.53–6.56) given in appendix B of chapter 6.
    '''
    


def main():
    #loads data
    matc1p8 = scipy.io.loadmat(r'exercises\c2\data\c1p8.MAT')
    matc2p3 = scipy.io.loadmat(r'exercises\c2\data\c2p3.MAT')
    
    #Visualizes data parameters
    #for key in matc1p8:
        #print (key, ": ", len(matc1p8[key])     
    #print (len(matc10p1))

    #execute exercises here
    #Ex1()
    #Ex2()
    #Ex3()
    #Ex4()
    #Ex5()
    #Ex6()
    #Ex7()
    #Ex8()
    #Ex9()
    #Ex10()  


if __name__ == "__main__":
    main()