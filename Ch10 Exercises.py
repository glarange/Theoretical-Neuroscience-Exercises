#Jordan Breffle
#https://github.com/jtbreffle
#Theoretical Neuroscience Exercises, Dayan and Abbott, 2001
#Chapter 10: Representational learning


import scipy.io #use scipy.io.loadmat() for MAT files
import numpy as np #if loadmat() fails, then use numpy.loadtxt(), becuase it is a plain text file



# ------------------Helper Functions--------------------------------------



#----------------------------Exercises------------------------------------
def Ex1():
    '''
    Data file c10p1.mat contains 100 data points drawn from the same
    two-dimensional distribution as those in figure 10.1. Fit a mixture
    of two circular Gaussian distributions to these data using EM, as in
    equation 10.4. Do not allow the variance of either of the Gaussians
    to become smaller than a minimal value of 0.0001.
    '''

def Ex2():
    '''
    Explore what happens to the fit of the mixture of Gaussians model
    from exercise 1 as the number of data points from each Gaussian
    is reduced and the number of potential Gaussians is increased. If
    you set the minimal variance given in exercise 1 to 0, a Gaussian
    distribution can settle around a single sample point and then have
    its variance shrink to 0. Why does this pathological behavior occur?
    '''
    
    
def Ex3():
    '''
    Modify your code from exercise 1 to calculate function F of equation
    10.14 during each E and M step of EM. Check that F changes
    monotonically. Explicitly calculate the true log likelihood of the data
    from equation 10.7 at the end of each M phase. Is it equal to F ?
    '''
    
def Ex4():
    '''
    Modify the code in exercise 1 to fit a K-means model rather than a
    mixture of Gaussians. Can you see any practical differences in the
    solutions that arise?
    '''
    
def Ex5():
    '''
    Consider the factor analysis model of figure 10.3 (discussed in more
    generality later in the chapter). Using the joint probability over v and
    u given in equation 10.15, derive an expression for F , and thus the
    learning rules of equation 10.5.
    '''
    
def Ex6():
    '''
    Using the EM version of factor analysis (see the appendix of chapter
    10), reproduce figure 10.4. MATLAB file c10p6.m shows how to
    generate data u1 for figure 10.4A and B, and u2 for C and D. First
    perform factor analysis on these data and reproduce figures 10.4A
    and C. Next, use the eig function to perform principal components
    analysis on u1 and u2, and thereby produce the rest of the figures. For
    some initial conditions, the cloud of points in the figuresmight slope
    downwards instead of upwards. Why? Calculate the expression for
    F derived in exercise 5 as factor analysis progresses and show that
    it changes monotonically.
    '''
    
def Ex7():
    '''
    Apply a rotationmatrix to the data set u2 fromexercise 6 (an example
    rotation matrix is given as rot in MATLAB file c10p6.m). Performfactor
    analysis and principal components analysis on the rotated data.
    How do the results compare with those for the unrotated data (remember
    to rotate your results back, if necessary, so that appropriate
    comparisons can be made)?
    '''
    
def Ex8():
    '''
    Construct a data set u from a set of independent, heavy-tailed,
    “sources” v through the relation u = G * v. Both u and v should
    be four-dimensional vectors. Choose the components of v independently
    and randomly from a double exponential distribution,
    for which the probability of getting the value v is proportional to
    exp(-|v|) (note that a one-sided exponentially distributed random
    variable can be generated using either exprnd(*) or -log(rand(*))).
    Choose a randommatrix G and generate the corresponding u values
    as u = G * v. Use 2000 randomly chosen v's and their corresponding
    u's. Then, use independent components analysis, as in equation
    10.40, to learn generative sources from the inputs u. How well
    do the values of the extracted sources match those of the original
    sources?
    '''
    
def Ex9():
    '''
    Compare the actual G you used to generate the data in problem 8
    with the G that is recovered by independent components analysis.
    Plot the six two-dimensional projections of the input data (u1 versus
    u2; u1 versus u3; etc) together with the projections of the mixing axes
    coming fromG(it is good to usemore data points for this, say 10000).
    The mixing axes are lines parallel to vectors with components G1i,
    G2i, G3i, and G4i, for i = 1, 2, 3, 4. What relationship exists between
    thesemixing axes and the envelope of the data points, andwhy? Plot
    u generated in the same way when the components of v are chosen
    independently from identical Gaussian distributions, together with
    the mixing axes coming from G. What differences do you see?
    '''
    
def Ex10():
    '''
    Implement wake-sleep learning for the Helmholtz machine with binary
    units when the input data is derived from a square “retina” of
    size ndim×ndim. The ndim columns of the input array are independently
    turned “on” with probability pbar. Each unit in a column that
    is “on” takes the value 1 with probability 1-pout and 0 with probability
    pout, and each unit in a column that is “off” takes the value 1
    with probability pout and 0 with probability 1-pout. MATLAB program
    c10p10.m is an example. In what way does the activity of the
    v units in the model capture the way that each input u was actually
    generated? What happens if there are not enough hidden units to
    represent each column separately?
    '''
    
def Ex11():
    '''
    Implementwake-sleep learning for the binaryHelmholtzmachine as
    in problem10, except nowmake a correlational structure between the
    columns - so that for half the input patterns, only columns 1 . . .ndim/2
    are eligible to be turned on (with probability pbar), and for the other
    half, only the other columns ndim/2+ 1 . . .ndim are eligible. Program
    c10p11.m shows oneway to generate such inputs. Train aHelmholtz
    machine with two representational layers (v and z), the top layer (z)
    having just one unit, the middle layer (v) with ndim+1 units. Does
    this build a generative model that captures the hierarchical way in
    which each input pattern is generated?
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
 

if __name__ == "__main__":
    main()