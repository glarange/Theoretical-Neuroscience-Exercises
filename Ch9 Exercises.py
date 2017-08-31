#Jordan Breffle
#https://github.com/jtbreffle
#Theoretical Neuroscience Exercises, Dayan and Abbott, 2001
#Chapter 9: Classical conditioning and reinforcement learing


import scipy.io #use scipy.io.loadmat() for MAT files
import numpy as np #if loadmat() fails, then use numpy.loadtxt(), becuase it is a plain text file



# ------------------Helper Functions--------------------------------------



#----------------------------Exercises------------------------------------
def Ex1():
    '''
    Implement acquisition and extinction as in figure 9.1 using the
    Rescorla-Wagner (delta) rule (equation 9.2).
    '''

def Ex2():
    '''
    Add a second stimulus and demonstrate that the delta rule can describe
    blocking, but that it fails to exhibit secondary conditioning.
    '''
    
def Ex3():
    '''
    Consider the case of partial reinforcement (studied in figure 9.1) in
    which reward r = 1 is provided randomly with probability p on any
    given trial. Assume that there is a single stimulus with u = 1, so that
    qdeltau, with Delta = r - v = r - wu, is equal to q(r - w). By considering
    the expected value hw + q(r - w)i and the expected square value
    h(w + q(r - w))2i of the new weights, calculate the self-consistent
    equilibrium values of the mean and variance of the weight w. What
    happens to your expression for the variance if q = 2 or q > 2? To
    what features of the learning rule do these effects correspond?
    '''
    
def Ex4():
    '''
    The original application of temporal difference learning to conditioning
    (Sutton & Barto, 1990) considered the use of stimulus traces (as a
    preliminary to the linear filter of equation 9.5). That is, the prediction
    of sum future reward at time t is v(t) = w * u(t) where ui(t), with
    predictionweight is wi, marks the presence (when ui(t) = 1) or
    absence(when ui(t) = 0) of stimulus i at time t. Also, the temporal 
    differencelearning rule of equation 9.10 is replaced by
    
    wi -> wi + qdelta(t)ui(t) ,
    
    where
    
    ui(t) = gammaui(t - 1) + (1 - gamma)ui(t)
    
    is the stimulus trace for stimulus i, and delta(t) is as in equation 9.10. Here
    gamma is the trace parameter which governs the length of the memory of
    the past occurrence of stimuli (see equation 9.30). Construct a trace
    learning model for a case similar to that of figure 9.2, but taking
    r(t) to be the hat-function r(t) = 1/5, 200 =< t =< 210 and r(t) = 0
    otherwise. Note that to match figure 9.2, you must use deltat = 5 for
    each time step rather than deltat = 1. Show the signals as in figure 9.2B
    for gamma = 0.5, 0.9, 0.99, using q = 0.2. Could this model account for the
    data on the activity of the dopamine cells? Would it show secondary
    conditioning?
    '''
    
def Ex5():
    '''
    Use the prediction model of equation 9.5 and the standard temporal
    difference learning rule of equation 9.10 to reproduce figure 9.2. Take
    r(t) to be the hat-function r(t) = 1/5, 200 =< t =< 210 and r(t) = 0
    otherwise. In this figure, the increments of time are in steps of deltat = 5,
    and q = 0.4. Considerwhat happens if the time between the stimulus
    and the reward is stochastic, drawn from a uniform distribution
    between 50 and 150. Show the average prediction error signal delta(t)
    time-locked to the stimulus and the reward. How does this differ
    from those in figure 9.2.
    '''
    
def Ex6():
    '''
    Implement a stochastic three-armed bandit using the indirect actor
    and the action choice softmax rule 9.12. Let arm a produce a reward
    of pa, with p1 = 1/4, p2 = 1/2, p3 = 3/4, and use a learning rate of
    q = 0.01, 0.1, 0.5 and beta = 1, 10, 100. Consider what happens if after
    every 250 trials, the arms swap their reward probabilities at random.
    Averaging over a long run, explore to see which values of q and beta
    lead to the greatest cumulative reward. Can you account for this
    behavior?
    '''
    
def Ex7():
    '''
    Repeat exercise 6 using the direct actor (with learning rule 9.22).
    For r, use a low-pass filtered version of the actual reward, which is
    obtained by using the update rule
    
    r -> gammar + (1 - gamma)r
    
    with gamma = 0.95. Study the effect of the different values of q and beta in
    controlling the average rate of rewards when the arms swap their
    reward probabilities at random every 250 trials.
    '''
    
def Ex8():
    '''
    Implement actor critic learning (equations 9.24 and 9.25) in the maze
    of figure 9.7, with learning rate q = 0.5 for both actor and critic, and
    beta = 1 for the critic. Starting from zero weights for both the actor and
    critic, plot learning curves as in figures 9.8 and 9.9. Start instead from
    a policy in which the agent is biased to go left at both B and C, with
    initial probability 0.99. How does this affect learning at A?
    '''
    
def Ex9():
    '''
    Implement actor critic learning for the maze, as in exercise 8, except
    using vectorial state representations as in equations 9.26, 9.27,
    and 9.28. If u(A) = (1, 0, 0), u(B) = (0, 1, 0) and u(C) = (0, 0, 1), then
    the result should be exactly as in exercise 8. What happens to the
    speed of leaning if u(A) = (1, a, a) (while retaining u(B) = (0, 1, 0) and
    u(C) = (0, 0, 1)) for a = +0.5 and a = -0.5, and why?
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