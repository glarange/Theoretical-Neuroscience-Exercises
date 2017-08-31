#Jordan Breffle
#https://github.com/jtbreffle
#Theoretical Neuroscience Exercises, Dayan and Abbott, 2001
#Chapter 8: Plasticity and learning


import scipy.io #use scipy.io.loadmat() for MAT files
import numpy as np #if loadmat() fails, then use numpy.loadtxt(), becuase it is a plain text file



# ------------------Helper Functions--------------------------------------



#----------------------------Exercises------------------------------------
def Ex1():
    '''
    Simulate the course of Hebbian learning for the case of figure 8.3.
    Find the ranges of initial weight values, (w1,w2), that lead to saturation
    at (1, 1). Can you predict the result analytically? If the
    off-diagonal term in the correlation matrix is -2 instead of -0.4 and
    there are no saturation boundaries, what happens to the sum of the
    weights? Could this be used as a way of normalizing the weights?
    '''

def Ex2():
    '''
    Show that the averaged form of the single-trial Oja rule in equation
    8.16 is given by

    tauw (dw/dt) = Q * w - alpha (w * Q * w)w

    Prove that if it converges, the averaged learning rule produces a set
    of weights proportional to an eigenvector of the correlation matrix
    Q, normalized so that |w|2=1/alpha.
    '''
    
    
def Ex3():
    '''
    Simulate the ocular dominance model of figure 8.7 using a subtractively
    normalized version of equation 8.31 (i.e. equation 8.14) with
    saturation limits at 0 and 1, and cortical interactions generated as in
    figure 8.8 from
    
    Kaa' = e**( - (a - a')**2 / 2sigma**2) - (1/9) e**( - (a - a')**2 / 18sigma**2)
    
    where sigma = 0.066 mm. Use 512 cortical cells with locations a spread
    evenly over a nominal 10 mm of cortex, and periodic boundary conditions
    (this means that you can use Fourier transforms to calculate
    the effect of the cortical interactions). Also use the discrete form of
    equation 8.31
    
    W -> W+ qK * W * Q
    
    with a learning rate of q = 0.01. Plot w- as it evolves from near 0
    to the final form of ocular dominance. Calculate the magnitude of
    the discrete Fourier transform of w-. Repeat this around 100 times,
    work out the average of the magnitudes of the Fourier transforms,
    and compare this to the Fourier transform of K.
    '''
    
def Ex4():
    '''
    Construct two-dimensional input data sets similar to those shown
    in figure 8.4 and use them to train a two-input, one output linear
    network using correlation- and covariance-based Hebbian learning
    rules with multiplicative normalization. Compare the final outcome
    for the weights with the principal components of the data when the
    mean of the input distribution is zero and when it is nonzero.
    '''
    
def Ex5():
    '''
    Repeat exercise 4 for a data set with zero mean, but with subtractive
    normalization and saturation. Startwith initial values for theweights
    that are chosen randomly over the full range from0 to their saturation
    limit. When does this algorithm produce a weight vector aligned
    with the principal component axis of the input data set, and when
    does it fail to do so. Why does the weight vector sometimes fail to
    align with the principal component axis?
    '''
    
def Ex6():
    '''
    Consider minimizing the function E(w) = (w - 2)**2 using the gradient
    descent rule for w,
    
    w -> w - epsilon (dE/dw)
    
    Plot E(w) together with the trajectories of w starting from w = 5 for
    q = 0.01, 0.1, 1, 2, 3. Why does learning diverge as q gets large?
    '''
    
def Ex7():
    '''
    Consider E(w) proportional to <(h(s) - w * f(s))**2>, as in equation 8.52,
    in the case that matrix hf(s)f(s)i is invertible. An extended delta rule
    can be written as
    
    w -> w + h(h(s) - w * f(s))H * f(s)i ,
    
    where H is amatrix that generalizes the learning rate q of the standard
    delta rule. For what matrix H does this rule go from any initial value
    w to the optimal weights in one single step. This amounts to a form
    of the Newton-Raphson method.
    '''
    
def Ex8():
    '''
    Train the feedforward network of figure 8.13 to produce the output
    v = cos(0.6s)when the input tuning curves are given as in the caption
    to figure 8.14. Train the network by using the stochastic delta learning
    rule (equation 8.61) with s values chosen randomly in the range
    between -10 and 10.
    '''
    
def Ex9():
    '''
    Construct a perceptron (equation 8.46) that classifies 10 binary inputs
    according to whether their sum(ua) is positive or negative. Use a
    randomset of binary inputs during training and compare the performance
    (both the learning rate and the final accuracy) of the Hebbian
    (equation 8.47), delta, and perceptron learning rules. Repeat this
    training protocol, but this time attempt to make the output of the
    perceptron classify according to the parity of the inputs, which is the
    sign of their product PI(ua). Why is this example so much harder than
    the first case?
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