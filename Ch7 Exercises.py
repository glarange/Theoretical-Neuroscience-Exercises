#Jordan Breffle
#https://github.com/jtbreffle
#Theoretical Neuroscience Exercises, Dayan and Abbott, 2001
#Chapter 7: Network models


import scipy.io #use scipy.io.loadmat() for MAT files
import numpy as np #if loadmat() fails, then use numpy.loadtxt(), becuase it is a plain text file



# ------------------Helper Functions--------------------------------------



#----------------------------Exercises------------------------------------
def Ex1():
    '''
    a) Consider network activities v(theta) that are steady-state solutions of
    equation 7.36, satisfying
    
    v(theta) = [ h(theta) + pi/2[integral]-pi/2 ( (dtheta'/pi) * (-gamma0 +
    gamma1*(cos(2(theta - theta')))*v(theta'))) ]
    
    in response to input h(theta) = Ac(1 - q + q cos(2theta)) as in equation
    7.37. Assuming that v(theta) is symmetric about theta = 0, show that
    v(theta) takes either the form
    
    v(theta) = alpha [cos(2theta) - cos(2thetaC)]+
    
    or the form
    
    v(theta) = alpha cos(2theta) + vtheta
    
    In the case of equation 2,which applieswhen thetaC < pi/2 and forwhich
    thetaC defines the width of the orientation tuning curve, by calculating
    the integral
    
    pi/2[integral]-pi/2 (dtheta'/pi) (-gamma0 + gamma1*(cos(2(theta - 
    theta')))*v(theta'))
    
    show that alpha and thetaC must satisfy the consistency conditions
    
    alpha = (A*c*epsilon) / (1 - lambda1 *(thetaC - sin(4thetaC))/pi
    
    cos(2thetaC) = (lambda0/pi) ( sin(2thetaC)) - 2thetaC(cos(2thetaC)) - ( 
    (1-epsilon) / epsilon) (1 - (lambda1/pi)(thetaC - ( (sin(4thetaC)) / 4))
    
    
    b) In the case of equation 3, calculate alpha and v0.
    
    c) For values lambda0 = 7.3, lambda1 = 11, c = 1, and A = 40 Hz, use the
    MATLAB® function fzero to find the value of thetaC that satisfies the
    consistency condition in equation 4 as a function of q for 0 < q =< 1.
    For q = 0.1 and c = 0.1, 0.2, 0.4, and 0.8, solve for alpha, and thereby
    reproduce figure 7.10B. Repeat the plots for lambda1 = 0. At what value
    of q does thetaC fall below pi/2. This corresponds to a model in which
    feedforward orientation tuning is sharpened only by inhibition, and
    the model lacks contrast invariant tuning.
    
    d) Numerically integrate equation 7.36 for the sets of parameters in 
    (c) to confirm your results. Use 100 neurons with preferred values
    evenly spaced between -pi/2 and pi/2.
    
    e) Plot thetaC - sin(4thetaC)/4 for 0 =< thetaC =< pi/2. What is its maximum
    value? As q -> 0 (so that (1 - q)/q -> infintity), calculate (from
    equation 4) a condition on lambda1 that ensures there will always be a
    solution with thetaC < pi/2. This defines a marginal phase in which the
    recurrent connections create a tuned output even from untuned input, and
    it constitutes what is called a continuous attractor.
    '''

def Ex2():
    '''
    A Hopfield associativememory network has activities for individual
    units, va for a = 1, 2, . . . ,N (or collectively v), that take values of 
    either +1 or -1, and are updated at every discrete time step of the network
    dynamics by the rule
    
    va(t + 1) = sgn( SIGMA(Maa' * va' (t)))
    
    where
    
    sgn(z) =  (+1 if z >= 0
               -1 if z < 0 
              
    Here M is a matrix constructed from P “memory” vectors vm (m =
    1, 2, . . .P), also composed of elements that are either +1 or -1, through
    the sum of outer products
    
    Maa' = (1 - Delta,a,a') SIGMA(VamVam)
    
    Note that the diagonal elements ofMare set to zero by this equation.
    Consider a 100-element network (N = 100). Construct P memory
    states by randomly assigning +1 and -1 values with equal probabilities
    to the N elements of each vm. Using these memory vectors, set
    the matrix of synaptic weights according to equation 6. Then, study
    the behavior of the network by iterating equation 5. Tomeasure how
    close the state of the network at time t, v(t), is to a particularmemory
    state, define the overlap function q(t) = v(t) * vm/N. This is equal to 1
    if v(t) = vm, is near zero if v(t) is unrelated to vm, and is equal to -1 if
    v(t) = -vm. Set the initial state v(0) so that it has a positive overlap,
    q(0),with memory state v1. Plot q(t) as the network evolves fromthis
    state according to equation 5. Final values of q(t) near one indicate
    successful recovery of the memory. Do the same starting from v(0)
    close to the inverse of the memory state -v1. What accounts for this
    behavior? Determine the range of q(0) values (about v1) that assures
    successfulmemory recovery for different values of P. Startwith P = 1
    and increase it untilmemory recovery fails even for q(0) = 1. Atwhat
    P value does this occur?
    '''
    
    
def Ex3():
    '''
    Repeat exercise 2 with the matrixM replaced by
    Maa' = (1 - deltaaa' )

    Maa' = (1 - deltaaa') Sigma(Vam * Cmm' * Va'm')

    where Cmm' is the m,m' element of the inverse of the matrix
    
    Sigma(Vam*Vam')
    
    Compare the performance and capacity of the associative memory
    constructed using this matrix with that of the associative memory in
    exercise 2.
    '''
    
def Ex4():
    '''
    Build and study a simple model of oscillations arising from the interaction
    of excitatory and inhibitory populations of neurons. The
    firing rate of the excitatory neurons is rE, and that of the inhibitory
    neurons is rI and these are characterized by equations 7.50 and 7.51.
    Set MEE = 1.25, MIE = 1, MII = 0, MEI = -1, gammaE = -10 Hz, gammaI = 10
    Hz, tauE = 10 ms, and vary the value of tauI. The negative value of gammaE
    means that this parameter serves as a source of background activity
    (activity in the absence of excitatory input) rather than as a threshold.
    Show what happens for tauI = 30ms and for tauI = 50 ms. Find the value
    of tauI for which there is a transition between fixed-point and oscillatory
    behavior, thereby verifying the results obtained analytically in
    chapter 7 on the basis of equation 7.53.
    '''
    
def Ex5():
    '''MATLAB files c7p5.m and c7p5sub.m perform a numerical integration
    of a two-unit, nonlinear, symmetric recurrent network with a
    threshold linear activation function F(I) = beta[I]+ and plot the results.
    Here, the dynamics come from
    
    dv/dt = -v + F(M * v + h)
    
    with v = (v1, v2) and h1 = h2 = 1. The weight matrix in this example
    isM = [0 -1 ; -1 0],which tends tomake v1 and v2 compete. Execute
    c7p5.m to see the consequences of regimes of high (beta = 2) and low
    (beta = 0.5) activation (which is equivalent to large and small recurrent
    weights). For these two values of beta, plot the nullclines (the locations
    in the v1-v2 phase planewhere dv1/dt = 0 and dv2/dt = 0). You should
    find one fixed point for beta = 0.5 and three for beta = 2. Linearize the
    network about the fixed point with v1 = v2 and derive a condition on
    beta for this fixed point to be stable. (Based on a problem from Dawei
    Dong.)
    '''
    
def Ex6():
    '''
    Plot the results of exercise 5 for the inputs h = (0.75, 1.25) and h =
    (0.5, 1.5). By plotting nullclines for these values of h, explain the
    resulting behavior. (Based on a problem from Dawei Dong.)
    '''
    
def Ex7():
    '''
    Use the expression
    
    fu(s - epsilon, g - mu) = A * e** ( -(s-epsilon)**2 / 2sigmas**2) N ( (g
    - gamma) / sigmag)
    
    where A, epsilon, sigmas, mu, and sigmag are parameters and N is the
    (sigmoidal) cumulative normal function
    
    N(z) = integral[z, -infinity] (dx (1/root(2pi)) e**(-x**2 / 2 ) = 1 -
    (-1/2) erfc (z / root(2) )
    
    Plot fu(s - epsilon, g - mu) and find values of the parameters that make it
    roughly match the gain-modulated response of figure 7.6B. Using
    w(epsilon, mu) = exp(-(epsilon + ,mu)2/2sigma2
    w), evaluate the integral in equation 7.15
    in terms of a single cumulative normal function to show that the
    resulting tuning curves are functions of s + g, and assess how the
    tuning width depends on sigmas, sigmag and sigmaw.
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


if __name__ == "__main__":
    main()