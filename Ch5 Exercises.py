#Jordan Breffle
#https://github.com/jtbreffle
#Theoretical Neuroscience Exercises, Dayan and Abbott, 2001
#Chapter 5: Model neurons I: Neuroelectronics


import scipy.io #use scipy.io.loadmat() for MAT files
import numpy as np #if loadmat() fails, then use numpy.loadtxt(), becuase it is a plain text file



# ------------------Helper Functions--------------------------------------



#----------------------------Exercises------------------------------------
def Ex1():
    '''
    The Nernst equation (equation 5.4) was derived in chapter 5 under
    the assumption that the membrane potential was negative and the
    ion being consideredwas positively charged. Rederive this result for
    a negatively charged ion and for the case when E is positive to verify
    that it applies in all these cases.
    '''

def Ex2():
    '''
    Verify that equation 5.47 is a solution of equation 5.46 when Vinfinity is
    independent of time. Then, solve equation 5.46 for the casewhen Vinfinity
    is an arbitrary function of time. In this solution, V(t) is expressed in
    terms of integrals involving Vinfinity(t).
    '''
    
    
def Ex3():
    '''
    Build a model integrate-and-fire neuron from equation 5.8. Use
    Vrest = -70 mV, Rm = 10 M
    , and taum = 10 ms. Initially set V = Vrest.
    When the membrane potential reaches Vth = -54 mV, make the neuron
    fire a spike and reset the potential to Vreset = -80 mV. Show
    sample voltage traces (with spikes) for a 300-ms-long current pulse
    (choose a reasonable current Ie) centered in a 500-ms-long simulation.
    Determine the firing rate of the model for various magnitudes
    of constant Ie and compare the results with equation 5.11.
    '''
    
def Ex4():
    '''
    Include an extra current in the integrate-and-firemodel to introduce
    spike-rate adaptation, as described in equations 5.13 and 5.14, and in
    the caption to figure 5.6.
    '''
    
def Ex5():
    '''
    Add an excitatory synaptic conductance to the integrate-and-fire neuron
    of exercise 3 by adding the extra synaptic conductance term in
    equation 5.43 with Es = 0. Set the external current to zero, Ie = 0, in
    this example, and assume that the probability of release on receipt
    of a presynaptic spike is 1. Use rmgs = 0.5 and describe Ps using the
    alpha function of equation 5.35 with taus = 10 ms and Pmax = 0.5. To
    incorporatemultiple presynaptic spikes, Ps should be described by a
    pair of differential equations,
    
    ts (dPs/dt) = e*Pmax*Z - Ps
    
    with e = exp(1), and
    
    taus (dz/dt) = -z
    
    with the additional rule that z is set to 1 whenever a presynaptic spike
    arrives. Plot V(t) in one graph and the synaptic current in another.
    Trigger synaptic events at times 50, 150, 190, 300, 320, 400, and 410
    ms. Explain what you see.
    '''
    
def Ex6():
    '''
    The equations in exercise 5 generate an alpha function response to a single
    input spike, but they do not prevent Ps from growing greater than 1
    when themodel synapse is driven bymultiple spikes at a sufficiently
    high frequency. In otherwords, this model synapse does not saturate.
    To introduce saturation, modify the equations of exercise 5 to
    
    ts (dPs/dt) = e*Pmax*Z(1 -Ps) - Ps
    
    with e = exp(1), and
    
    taus (dz/dt) = -z
    
    with the additional rule that z is set to 1 whenever a presynaptic
    spike arrives. Compare Ps(t) computed using these equations with
    Ps(t) computed using the equations of exercise 5 for constant rate,
    regular (periodic) presynaptic spike trains with frequencies ranging
    from 1 to 100 Hz. In both cases, use taus = 10 ms and Pmax = 0.5.
    '''
    
def Ex7():
    '''
    Construct a model of two coupled integrate-and-fire neurons similar
    to that of figure 5.20. Both model neurons obey equation 5.43
    with EL = -70 mV, Vth = -54 mV, Vreset = -80 mV, taum = 20 ms,
    rmgs = 0.15, and RmIe = 18 mV. Both synapses should be described
    as in exercise 5 with Pmax = 0.5 and taus = 10 ms. Consider cases
    where both synapses are excitatory, with Es = 0 mV, and both are
    inhibitory, with Es = -80 mV. Show how the pattern of firing for
    the two neurons depends on the type (excitatory or inhibitory) of the
    reciprocal synaptic connections. For these simulations, set the initial
    membrane voltages of the two neurons to slightly different values,
    randomly, and run the simulation until an equilibrium situation has
    been reached, which may take a few seconds of simulated run time.
    Start froma fewdifferent randominitial conditions to study whether
    the results are consistent. Investigate what happens if you change
    the strengths and time constants of the reciprocal synapses.
    '''

    
def Ex8():
    '''
    Build a Hodgkin-Huxley model neuron by numerically integrating
    the equations for V, m, h, and n given in chapter 5 (see, in particular
    equations 5.6, 5.17-5.19, 5.22, 5.24, and 5.25). Take cm = 10 nF/mm2,
    and as initial values take: V = -65 mV, m = 0.0529, h = 0.5961, and
    n = 0.3177. Use an integration time step of 0.1 ms. Use an external
    current with Ie/A = 200 nA/mm2 and plot V, m, h, and n as functions
    of time for a suitable interval. Also, plot the firing rate of the model
    as a function of Ie/A over the range from 0 to 500 nA/mm2. Show
    that the firing rate jumps discontinuously from zero to a finite value
    when the current passes through the minimum value required to
    produce sustained firing. Finally, apply a pulse of negative current
    with Ie/A = -50 nA/mm2 for 5 ms followed by Ie/A = 0 and show
    what happens.
    '''
    
def Ex9():
    '''
    Construct and simulate the K+ channel model of figure 5.12. Plot the
    mean squared deviation between the current produced by N such
    model channels and the Hodgkin-Huxley current as a function of N
    over the range 1 =< N =< 100, matching the amplitude of theHodgkin-
    Huxley model so that the mean currents are the same.
    '''
    
def Ex10():
    '''
    Compute analytically the value of the release probability Prel just before
    the time of each presynaptic spike for a regular (periodic rather
    than Poisson), constant-frequency presynaptic spike train as a function
    of the presynaptic firing rate. Do this for both the depression
    and facilitation models described by equation 5.37.
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