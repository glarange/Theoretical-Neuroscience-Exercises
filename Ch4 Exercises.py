#Jordan Breffle
#https://github.com/jtbreffle
#Theoretical Neuroscience Exercises, Dayan and Abbott, 2001
#Chapter 4: Information theory


import scipy.io #use scipy.io.loadmat() for MAT files
import numpy as np #if loadmat() fails, then use numpy.loadtxt(), becuase it is a plain text file



# ------------------Helper Functions--------------------------------------



#----------------------------Exercises------------------------------------
def Ex1():
    '''
    Show that the firing-rate distribution that maximizes the entropy
    when the firing rate is constrained to lie in the range 0 =< r =< rmax
    is given by equation 4.22, and that its entropy for a fixed resolution
    deltar is given by equation 4.23. Use a Lagrange multiplier (see the
    Mathematical Appendix) to constrain the integral of p[r] to one.
    '''

def Ex2():
    '''
    Show that the firing-rate distribution that maximizes the entropy
    when the mean of the firing rate is held fixed is an exponential,
    and compute its entropy for a fixed resolution deltar. Assume that the
    firing rate can fall anywhere in the range from 0 to infinity. Use Lagrange
    multipliers (see theMathematicalAppendix) to constrain the integral
    of p[r] to 1 and the integral of p[r]r to the fixed average firing rate.
    '''
    
    
def Ex3():
    '''
    Show that the distribution that maximizes the entropy when the
    mean and variance of the firing rate are held fixed is a Gaussian,
    and compute its entropy for a fixed resolution deltar. To simplify the
    mathematics, allow the firing rate to take any value between -infinity and
    +infininty. Use Lagrange multipliers (see the Mathematical Appendix) to
    constrain the integral of p[r] to 1, the integral of p[r]r to the fixed
    average firing rate hri, and the integral of p[r](r - hri)**2 to the fixed
    variance.
    '''
    
def Ex4():
    '''
    Using Fourier transforms, solve equation 4.37, using equation 4.36,
    to obtain the result of equation 4.42.
    '''
    
def Ex5():
    '''
    Suppose the filter Ls(vec(a)) has a correlation function that satisfies equation
    4.37. Consider a new filter constructed in terms of this old one
    by writing
    
    L's(vec(a)) = ?
    
    Show that if U(vec(a), vec(c)) satisfies the condition of an orthogonal transformation,
    
    ? = ?
    
    the correlation function for this new filter also satisfies equation 4.37.
    '''
    
def Ex6():
    '''
    Consider a stimulus sr = ss +mu that is given by the sumof a true stimulus
    ss and a noise term mu. Values of the true stimulus ss are drawn
    from a Gaussian distribution with mean 0 and variance Qss. Values
    of the noise term mu are also obtained from a Gaussian distribution,
    with mean 0 and variance Qmumu. The two terms mu and ss are independent
    of each other. Using the formula for the continuous entropy of
    a Gaussian random variable calculated in problem 3, calculate the
    mutual information between sr and ss.
    '''
    
def Ex7():
    '''
    Consider amultivariate signal ss drawn fromaGaussian distribution
    with mean 0 and covariance matrix Qss. Compute the continuous
    entropy of s in terms of the eigenvalues of Qss, up to the usual
    resolution term for a continuous entropy.
    '''
    
def Ex8():
    '''
    Suppose that a stimulus at one point on the retina, and at a given
    time, sr = ss + mu, is the sum of a true stimulus ss and a noise term mu, as
    in exercise 6. Model the retinal processing at this particular location
    as producing a signal at the thalamus
    
    sl = Dssr + mul ,
    
    where Ds is a parameter called the transfer constant, and mul represents
    an additional, independent source of noise that can be modeled as
    being drawn froma Gaussian distribution with mean 0 and variance
    Qmulmul . Calculate the mutual information Il between sl and ss as a
    function of Ds. The power of the signal produced by the retina is
    defined as Pr = h(Dssr)2i. By maximizing
    
    Il - kPr
    
    as a function of Ds, find the transfer constant that maximizes the
    mutual information for a given value of k (with k > 0), a parameter
    that controls the trade-off between information and power. What
    happens when Qss, describing the visual signal, gets much smaller
    than Qmumu? (Based on a problem from Dawei Dong.)
    '''
    
def Ex9():
    '''
    Consider two independent inputs s and s' drawn from Gaussian
    distributions with means 0 andwith different variances Qss and Qs's' .
    These generate two thalamic signals, as in exercise 8.
    
    sl = Dss + mu and s'l = Ds' s' + mu' ,
    
    defined by two separate transfer constants, Ds and Ds' , and two
    independent noise terms with variances Qmumu and Qmu'mu' . Find the
    transfer constants that maximize the total mutual information Il + I'l
    for a fixed total power Pr + P'r, where the non-primes and primes
    denote the information and power for sl and s'l , respectively.
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


if __name__ == "__main__":
    main()