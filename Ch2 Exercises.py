#Jordan Breffle
#https://github.com/jtbreffle
#Theoretical Neuroscience Exercises, Dayan and Abbott, 2001
#Chapter 2: Neural Encoding I: Reverse correlation and visual receptive fields


import scipy.io #use scipy.io.loadmat() for MAT files
import numpy as np #if loadmat() fails, then use numpy.loadtxt(), becuase it is a plain text file



# ------------------Helper Functions--------------------------------------



#----------------------------Exercises------------------------------------
def Ex1():
    '''
    Use the rate given by equation 2.1 with r0 = 50 Hz and
    
    D(TAU) = -cos (( 2PI (TAU - 20ms) ) / 140ms) * e** ( -TAU / 60ms) Hz/ms
    
    to predict the response of a neuron of the electrosensory lateral-line
    lobe to a stimulus. The above equation is an approximation for
    the linear kernel obtained from the spike-triggered average shown
    in figure 1.9. Use an approximate Gaussian white noise stimulus
    constructed by choosing a stimulus value every 10 ms (deltat = 10 ms)
    from a Gaussian distribution with zero mean and variance sigma2s / deltat,
    with sigma2s = 10. Compute the firing rate over a 10 s period. From the
    results, compute the firing rate-stimulus correlation function Qrs(TAU).
    Using equation 2.6, compare Qrs(-TAU)/sigma2s with the kernel D(TAU)
    given above.
    '''

def Ex2():
    '''
    MATLAB® file c1p8.mat contains the data described in exercise 8 of
    chapter 1. Use the spike-triggered average (calculated in that exercise)
    to construct a linear kernel and use it in equation 2.1 to provide a
    model of the response of theH1 neuron. Choose r0 so that the average
    firing rate predicted by the model in response to the stimulus used
    for the data matches the actual average firing rate. Use a Poisson
    generator with the computed rate to generate a synthetic spike train
    fromthis linear estimate of the firing rate in response to the stimulus
    stim. Plot examples of the actual and synthetic spike trains. How
    are they similar and how do they differ? Plot the autocorrelation
    function of the actual and the synthetic spike trains over the range 0
    to 100ms. Why is there a dip at a lag of 2 ms in the autocorrelation of
    the actual spike train? Is there a dip for the synthetic train too? Plot
    the interspike interval histogramfor both spike trains. Why is there a
    dip below 6 ms in the histogram for the actual spike train? What are
    the coefficients of variation for the two spike trains and why might
    they differ? (Based on a problem from Sebastian Seung).
    '''
    
    
def Ex3():
    '''
    MATLAB® file c2p3.mat contains the responses of a cat LGN cell to
    two-dimensional visual images (these data are described in Kara, P,
    Reinagel, P, & Reid, RC (2000) Low response variability in simultaneously
    recorded retinal, thalamic, and cortical neurons. Neuron
    30:803-817 and were kindly provided by Clay Reid). In the file,
    counts is a vector containing the number of spikes in each 15.6 ms
    bin, and stim contains the 32767, 16 × 16 images that were presented
    at the corresponding times. Specifically, stim(x, y, t) is the stimulus
    presented at the coordinate (x,y) at time-step t. Note that
    stim is an int8 array that must to be converted into double using
    the command stim=double(stim)in order to bemanipulatedwithin
    MATLAB®. Calculate the spike-triggered average images for each of
    the 12 time steps before each spike and show them all (using the
    imagesc command). Note that in this example, the time bins can
    contain more than one spike, so the spike-triggered average must be
    computed by weighting each stimulus by the number of spikes in
    the corresponding time bin, rather than weighting it by either 1 or
    0 depending on whether a spike is present or not. In the averaged
    images, you should see a central receptive field that reverses sign
    over time. By summing up the images across one spatial dimension,
    produce a figure like that of figure 2.25C. (Based on a problem from
    Sebastian Seung.)
    '''
    
def Ex4():
    '''
    For a Gaussian random variable x with zero mean and standard
    deviation sigma, prove that

    <xF(alpha x)> = alpha sigma**2 <F'(alpha x)>
    
    where alpha is a constant, F is any function, F' is its derivative,
    
    <xF(alpha x)> = integral[ dx(1/root(2PISigma) * e**(-x**2 / 2Sigma**2) * xF(alphax) ],
    
    and similarly for hF'(alpha x)i. This is the basis of the identity 2.64,which
    can be derived by extending this basic result first to multivariate
    functions and then to functionals.
    '''
    
def Ex5():
    '''
    Using the inverses of equations 2.15 and 2.17
    
    epsilon = epsilon0 (e**(x/lambda) - 1) 
    
    and 
    
    a = -((180degrees (epsilon0 + epsilon) Upsilon) / (lambda * epsilon * PI))
    

    map from cortical coordinates back to visual coordinates and determine
    what various patterns of activity across the primary visual
    cortex would “look like”. Ermentrout and Cowan (Ermentrout, GB,
    & Cowan, J (1979)Amathematical theory of visual hallucination patterns.
    Biological Cybernetics 34:137–150)used these results as a basis of
    amathematical theory of visual hallucinations. The figure generated
    by the MATLAB® programc2p5.m shows an illustrative example. This
    program simulates a plane sine wave of activity across the primary
    visual cortex with a specified spatial frequency and direction, and
    then maps it back into retinal coordinates to see what visual pattern
    would be perceived due to this activity. Consider various other
    patterns of activity and show the visual hallucinations they would
    generate.
    '''
    
def Ex6():
    '''
    '''
    
def Ex7():
    '''
    '''
    
def Ex8():
    '''
    '''
    
def Ex9():
    '''
    '''
    
def Ex10():
    '''
    '''
    
def Ex11():
    '''
    '''
    
def Ex12():
    '''
    '''
    
def Ex13():
    '''
    '''
    
def Ex14():
    '''
    '''
    
def Ex15():
    '''
    '''
    
def Ex16():
    '''
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
    #Ex11() 
    #Ex12() 
    #Ex13() 
    #Ex14() 
    #Ex15() 
    #Ex16() 

if __name__ == "__main__":
    main()