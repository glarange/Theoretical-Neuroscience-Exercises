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
    Performthe integrals in equations 2.31 and 2.32 for the case sigmax =
    sigmay = sigma to obtain the results
    
    (A/2) * e**(- (sigma**2 (k**2 + k**2)) / 2) * (cos(phi - psi) * e**(sigma**2 * k * K * cos(sigma)) + cos(phi - psi) * e**(-simga**2 * k * K * cos(sigma)))
    
    and 
    
    Lt(t) = ( (alpha**6 * |w| * root(w**2 + 4alpha**2) / (w**2 + alpha**2)**4) ) * cos(w*t - delta)
    
    with
    
    delta = 8 * arctan (w / alpha) + arctan (2alpha/w) - PI
    
    From these results, verify the selectivity curves in figures 2.15 and
    2.16. In addition, plot delta as a function of w.
    '''
    
def Ex7():
    '''
    Numerically compute the spatial part of the linear response of a
    simple cellwith a separable space-time receptive field to a sinusoidal
    grating, as given by equation 2.31. Use a stimulus oriented with
    Phi = 0. For the spatial receptive field kernel, use equation 2.27 with
    sigma*x = sigma*y = 1degrees, phi = 0, and 1/k = 0.5degrees. Plot Ls as a
    function of K taking Phi = 0 and A = 50. This determines the 
    frequency selectivity of the cell. What is its preferred spatial
    frequency? Plot Ls as a function of Phi taking 1/K = 0.5degrees and A = 50. This determines the spatial phase selectivity of the cell. What is its 
    preferred spatial phase?
    '''
    
def Ex8():
    '''
    Consider a complex cell with the spatial part of its response given by
    L2,1 + L2,2, where L1 and L2 are linear responses determined by equation
    2.31 with kernels given by equation 2.27 with sigmax = sigmay = 
    1degrees, and 1/k = 0.5degrees; and with phi = 0 for L1 and phi =
    -PI/2 for L2. Use a stimulus oriented with Phi = 0. Compute and plot
    L2,1 + L2,2 as a function of K taking Phi = 0 and A = 5. This
    determines the spatial frequency selectivity of the cell. Compute and
    plot L2,1 + L2,2 as a function of Phi taking 1/K = 0.5degrees and A =
    5. This determines the spatial phase selectivity of the cell. Does the
    spatial phase selectivity match what you expect for a complex cell?
    '''    

    
def Ex9():
    '''
    Consider the linear temporal response for a simple or complex cell
    given by equation 2.32with a temporal kernel given by equation 2.29
    with 1/alpha = 15 ms. Compute and plot Lt(t) for w = 6PI/s. This
    determines the temporal response of the simple cell. Do not plot the
    negative part of Lt(t) because the cell cannot fire at a negative rate.
    Compute and plot L2t(t) for w = 6PI/s. This determines the temporal
    response of a complex cell. What are the differences between the
    temporal responses of the simple and complex cells?
    '''
    
def Ex10():
    '''
    Compute the response of amodel simple cellwith a separable spacetime
    receptive field to a moving grating

    s(x, y, t) = cos(Kx - w*t) .
    
    For Ds, use equation 2.27with sigmax = sigmay = 1degrees, Phi = 0, and 1/k = 0.5degrees. For
    Dt, use equation 2.29 with 1/alpha = 15 ms. Compute the linear estimate
    of the response given by equation 2.24 and assume that the actual
    response is proportional to a rectified version of this linear response
    estimate. Plot the response as a function of time for 1/K = 1/k = 0.5degrees
    and w = 8PI/s. Plot the response amplitude as a function of w for
    1/K = 1/k = 0.5degrees and as a function of K for w = 8PI/s.
    '''
    
def Ex11():
    '''
    Compute the response of a model complex cell to the moving grating

    s(x, y, t) = cos(Kx - w*t)

    The complex cell should be modeled by squaring the unrectified
    linear response estimate of a simple cells with a spatial receptive
    field given by equation 2.27 with sigmax = sigmay = 1degrees, Phi = 0, and 1/k = 0.5degrees,
    and adding this to the square of the unrectified linear response of
    a second simple cell with identical properties except that its spatial
    phase preference is Phi = -PI/2 instead of Phi = 0. Both linear responses
    are computed fromequation 2.24. For both of these, use equation 2.29
    with 1/alpha = 15 ms for the temporal receptive field. Plot the complex
    cell response as a function of time for 1/K = 1/k = 0.5degrees and w = 8PI/s.
    Plot the response amplitude as a function of w for 1/K = 1/k = 0.5degrees
    and as a function of K for w = 8PI/s.
    '''
    
def Ex12():
    '''
    Construct a model simple cell with the nonseparable space-time receptive
    field described in the caption of figure 2.21B. Compute its
    response to the moving grating

    s(x, y, t) = cos(Kx - w*t) .
    
    Plot the amplitude of the response as a function of the velocity of the
    grating, w/K, using w = 8PI/s and varying K to obtain a range of both
    positive and negative velocity values (use negative K values for this).
    Show that the response is directionally selective.
    '''
    
def Ex13():
    '''
    Construct amodel complex cell that is disparity tuned but insensitive
    to the absolute position of a grating. The complex cell is constructed
    by summing the squares of the unrectified linear responses of two
    simple cells, but disparity effects are now included. For this exercise,
    we ignore temporal factors and only consider the spatial dependence
    of the response. Each simple cell response is composed of two terms
    that correspond to inputs coming from the left and right eyes. Because
    of disparity, the spatial phases of the image of a grating in the
    two eyes, PhiL and PhiR, may be different. We write the spatial part of
    the linear response estimate for a grating with the preferred spatial
    frequency (k = K) and orientation (Psi = theta = 0) as
    
    L1 = A/2 * (cos(PhiL) + cos(PhiR)) ,
    
    assuming that phi = 0 (this equation is a generalization of equation
    2.34). Let the complex cell response be proportional to L2,1 + L2,2,
    where L2 is similar to L1 but with the cosine functions replaced by
    sine functions. Show that the response of this neuron is tuned to the
    disparity, PhiL - PhiR, but is independent of the absolute spatial phase
    of the grating, PhiL + PhiR. Plot the response tuning curve as a function
    of disparity. (See DeAngelis, GC, Ohzawa, I, & Freeman, RD (1991)
    Depth is encoded in the visual cortex by a specialized receptive field
    structure. Nature 352:156–159.)
    '''
    
def Ex14():
    '''
    Determine the selectivity of the LGN receptive field of equation 2.45
    to spatial frequency by computing its integrals when multiplied by
    the stimulus
    
    s = cos(Kx)
    
    for a range of K values. Use sigmac = 0.3degrees, sigmas = 1.5degrees, B = 5, 1/alpha = 16
    ms, and 1/Beta = 64 ms, and plot the resulting spatial frequency tuning
    curve.
    '''
    
def Ex15():
    '''
    Construct the Hubel-Wiesel model of a simple-cell spatial receptive
    field, as depicted in figure 2.27A. Use difference-of-Gaussian functions
    (equation 2.45) to model the LGN receptive fields. Plot the
    spatial receptive field of the simple cell constructed by summing
    the spatial receptive fields of the LGN cells that provide its input.
    Compare the result of summing appropriately placed LGN centersurround
    receptive fields (figure 2.27A) with the results of an appropriately
    adjusted Gabor filter model of the simple cell that uses the
    spatial kernel of equation 2.27.
    '''
    
def Ex16():
    '''
    Construct the Hubel-Wiesel model of a complex cell, as depicted in
    figure 2.27B. UseGabor functions (equation 2.27) to model the simple
    cell responses, which should be rectified before being summed. Plot
    the spatial receptive field of the complex cell constructed by summing
    the different simple cell responses. Compare the responses of a complex
    cell constructed by linearly summing the outputs of simple cells
    (figure 2.27B) with different spatial phase preferences with the complex
    cell model obtained by squaring and summing two unrectified
    simple cell responses with spatial phases 90degrees apart as in exercise 8.
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