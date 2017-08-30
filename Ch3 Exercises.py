#Jordan Breffle
#https://github.com/jtbreffle
#Theoretical Neuroscience Exercises, Dayan and Abbott, 2001
#Chapter 3: Neural decoding


import scipy.io #use scipy.io.loadmat() for MAT files
import numpy as np #if loadmat() fails, then use numpy.loadtxt(), becuase it is a plain text file



# ------------------Helper Functions--------------------------------------



#----------------------------Exercises------------------------------------
def Ex1():
    '''
    Suppose that the probabilities that a neuron responds with a firing
    rate between r and r + deltar to two stimuli labeled plus and minus are
    p[r|±]deltar where
    
    p[r|±] = (1 / root(2PIsigma(r) ) * e**( -0.5 * ( (r-<r>) / sigma(r))**2 )
    
    Assume that the two mean rate parameters hri+ and hri- and the
    single variance sigma2r
    are chosen so that these distributions produce
    negative rates rarely enough that we can integrate over r values over
    the entire range -infinty < r < infinity. Suppose that you base discrimination
    of the plus and minus stimuli on whether the evoked firing rate is
    greater or less than a threshold z. Show that the size and power, alpha(z)
    and Beta(z) of this test are given by
    
    alpha(z) = -.5 * erfc( (z-<r>-)/ root(2sigma(r)))
    
    and 
    
    Beta(z) = -.5 * erfc( (z-<r>+)/ root(2sigma(r)))
    
    Show that the probability of a correct answer in the associated two alternative
    forced choice task involving discriminating between plusthen-
    minus and minus-then-plus presentations of the two stimuli is
    given by equation 3.10. Also, derive the result of equation 3.17. Plot
    ROC curves for different values of the discriminability
    
    d' = (<r>+ - <r>-) / sigma(r)
    
    By simulation, determine the fraction of correct discriminations that
    can be made in the two-alternative forced choice task. Show that the
    fractions of correct answer for different values of d' are equal to the
    areas under the corresponding ROC curves.
    '''

def Ex2():
    '''
    Simulate the random-dot discrimination experiment. Denote the
    stimulus by plus or minus, corresponding to the two directions of
    motion. On each trial, choose the stimulus randomly with equal
    probability for the two cases. When the minus stimulus is chosen,
    generate the responses of the neuron as 20 Hz plus a random Gaussian
    termwith a standard deviation of 10 Hz (set any rates that come
    out negative to zero). When the plus stimulus is chosen, generate
    the responses as 20 + 10d Hz plus a random Gaussian term with a
    standard deviation of 10 Hz, where d is the discriminability (again,
    set any rates that come out negative to zero). First, choose a threshold
    z = 20+5d,which is half-way between themeans of the two response
    distributions. Whenever r => z guess “plus”, otherwise guess “minus”.
    Over a large number of trials (1000, for example) determine
    how often you get the right answer for different d values. Plot the
    percent correct as a function of d over the range 0 =< d =< 10. Next, by
    allowing z to vary over a range, plot ROC curves for several values
    of d (starting with d = 2). To do this, determine how frequently the
    guess is “plus” when the stimulus is, in fact, plus (this is Beta), and how
    often the guess is “plus” when the real stimulus is minus (this is alpha).
    Then, plot Beta versus alpha for z over the range 0 =< z =< 140.
    '''
    
    
def Ex3():
    '''
    Simulate the responses of four interneurons in the cercal system of
    the cricket and check the accuracy of a vector decoding scheme. For a
    truewind direction theta, the average firing rates of the four interneurons
    should be generated as
    
    <ri> = [50 Hz cos(theta - thetai)]+
    
    where [ ]+ indicates half-wave rectification, and thetai = pi/4, 3pi/4, 5pi/4,
    7pi/4 for i = 1, 2, 3, 4. The actual rates, ri, are then obtained by adding
    to these mean rates a random number chosen from a Gaussian distribution
    with zero mean and a standard deviation of 5 Hz (set any
    rates the come out negative to zero). From these rates, construct the
    x and y components of the population vector

    x = 4[Sigma]i=1 (ri * cos(thetai))
    
    and 
    
    y = 4[Sigma]i=1 (ri * sin(thetai))
    
    and, from the direction of this vector, compute an estimate theta(est) of the
    wind direction. Average the squared difference (theta - theta(est))**2 over 1000
    trials. The square root of of this quantity is the error. Plot the error
    as a function of theta over the range -90degrees =< theta =< 90degrees.
    '''
    
def Ex4():
    '''
    Show that if an infinite number of unit vectors vec(Ca) is chosen uniformly
    froma probability distribution that is independent of direction,
    Sigma(vec(V) * vec(Ca) vec(Ca) proportionl to vec(V) for any vector vec(V). How does the sum approach this limit for
    a finite number of terms?
    '''
    
def Ex5():
    '''
    Show that the Bayesian estimator that minimizes the expected average
    value of the the loss function L(s, sbayes) = (s - sbayes)**2 is the mean
    of the distribution p[s|r], given by equation 3.27. Also show that
    the estimate that arises from minimizing the expected loss function
    L(s, sbayes) = |s - sbayes| is the median of p[s|r].    
    '''
    
def Ex6():
    '''
    Show that the equations for the Fisher information in equation 3.42
    can also be written as in equation 3.43,

    IF(s) = <( (sigma ln p[r|s]) / sigma(s))**2> = integral (dr p[r|s] * ( (sigma ln p[r|s]) / sigma(s))**2
    
    or as

    IF(s) = integral (dr (1 / (p[r|s])) ( (sigma p[r|s]) / sigma(s))**2
    
    Use the fact that Integral(dr p[r|s]) = 1.
    '''
    
def Ex7():
    '''
    The discriminability for the variable Z defined in equation 3.19 is the
    difference between the average Z values for the two stimuli s + deltas
    and s divided by the standard deviation of Z. The average of the
    difference in Z values is
    
    <deltaZ> = ?
    
    Show that for small deltas, <deltaZ>  = IF(s)deltas. Also prove that the average value of Z,

    <Z> = ?
    
    is zero, and that the variance of Z is IF(s). Computing the ratio,
    we find from these results that d' = deltas * root(IF(s)) which matches the discriminability 3.49 of the ML estimator.
    '''
    
def Ex8():
    '''
    Extend equation 3.46 to the case of neurons encoding a Ddimensional
    vector stimulus vec(s) with tuning curves given by
    
    fa(vec(s)) = rmax * e ** ( - (|vec(s) - vec(sa)|)**2 / (2sigmar**2) )

    and perform the sum by approximating it as an integral over uniformly
    and densely distributed values of vec(sa) to derive the result in
    equation 3.48.
    '''
    
def Ex9():
    '''
    Derive equation 3.54 by minimizing the expression 3.53. Use the
    methods of appendix A of chapter 2.
    '''
    
def Ex10():
    '''
    MATLAB® program c3p10.m performs acausal decoding using signal
    processing techniques to construct an approximate solution of equation
    3.54, while suppressing unwanted effects of noise (for an illustration
    of these effects, see part (e) of this exercise). The program is
    called as [est,K,ind]=ch3ex10(stim,spk,nfft), where stim and
    spk are the stimulus and response respectively, nfft is the length of
    a discrete Fourier transform (suitable values are nfft= 210 = 1024
    or 211 = 2048), K is the acausal kernel, est is the resulting stimulus
    estimate, and ind is a vector of indices that specifies the range over
    which the estimate and stimulus should be compared. Specifically,
    est provides an estimate of stim(ind).
    
    a)Compute an estimated firing rate rest fromequation 2.1with r0 = 50
    Hz and
    
    D(tau) = -cos( (2pi(tau-20ms)) / 140ms) * e**( -tau / 60ms) Hz/ms
    
    in response to an approximate white noise stimulus (roughly 500
    seconds long) calculated by choosing at each time step (with deltat = 10
    ms) a stimulus value from a Gaussian distribution with mean 0 and
    variance 2. Generate a kernel and estimate for this stimulus using
    c3p10.m with rest playing the role of the argument spk. Verify that
    est and stim(ind) are closely related, and describe the relationship
    between the coding kernel D and the decoding kernel K.

    b) Repeat (a) with a rectification non-linearity, so that [rest]+ is used
    in place of rest. Measure the effect of the nonlinearity by comparing
    the average (over time) of the squared difference between est and
    stim(ind), divided by the variance of stim, for the rectified and
    nonrectified cases. What is the effect of rectification on the optimal
    decoding kernel K, and why? Assess the accuracy with which different
    frequency components in stim are captured in est by considering
    the power spectrum of the average squared difference between est
    and stim(ind).
    
    c) Generate a spike sequence spk from the rectified firing rate [rest]+
    using a Poisson generator. The sequence spk should consist of a one
    or a zero at each time step, depending on whether or not a spike
    occurred. Recompute the acausal kernel as in part (a), but using
    spk as the response rather than rest. How accurate is the resulting
    decoding, and what is the effect of using spikes rather than rates on
    the decoding kernel K?
    
    d) What happens to decoding accuracy as the value of deltat, which
    defines the approximation to a white noise stimulus, increases and
    why? In the general case, the approximate white noise should be
    generated by choosing a stimulus value at each time step from a
    Gaussian distribution with mean 0 and variance 20 ms/deltat.
    
    e) Attempt to repeat the decoding in (a) using the cross-correlation
    function xcorr and the fast Fourier transform fft to solve equation
    3.54. Why is the answer so noisy?
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