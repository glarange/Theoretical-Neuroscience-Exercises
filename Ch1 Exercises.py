#Jordan Breffle
#https://github.com/jtbreffle
#Theoretical Neuroscience Exercises, Dayan and Abbott, 2001
#Chapter 1: Neural Encoding I: Firing Rates and Spike Statistics


import scipy.io #use scipy.io.loadmat() for MAT files
import numpy as np #if loadmat() fails, then use numpy.loadtxt(), becuase it is a plain text file

import random
import matplotlib.pyplot as plt



# ------------------Helper Functions-------------------------------------
def spikeCountWindow(input, window):
    '''for an input array of spikes, this returns an array of the number of 
    spikes that occur within each window '''

    op = []
    spikeCounter = 0
    windowCounter = 0
    for i in range(len(input)):
        if windowCounter == window:
            op = op + [spikeCounter]
            spikeCounter = 0
            windowCounter = 0
        else:
            windowCounter = windowCounter + 1
            if input[i] > 0:
                spikeCounter = spikeCounter + 1
    return op




#----------------------------Exercises------------------------------------
def Ex1():
    '''Generate spikes for 10 s (or longer if you want better statistics) using
    a Poisson spike generator with a constant rate of 100 Hz, and record
    their times of occurrence. Compute the coeÆcient of variation of the
    interspike intervals, and the Fano factor for spike counts obtained
    over counting intervals ranging from 1 to 100 ms. Plot the interspike
    interval histogram. '''
    
    #10s with points every 1ms
    x = np.linspace(0, 10, 1001)
    
    #samples drawn from a poisson distribution every 1ms for 10s, with probability corresponding to 100Hz
    y = np.random.poisson(0.1, 1001) 
    
    #a single ms timepoint can have >1 event so...
    #this for-loop rounds all events >1 to a single spike
    for i in range(len(y)):  
        if y[i] > 0:       
            y[i] = 1
            
    plt.figure(num='Exercise 1')
    plt.subplot(2, 1, 1)
    plt.title("Poisson Generated Spikes, 100Hz")
    plt.ylabel('Spikes')
    plt.xlabel('Time (S)')
    plt.plot(x, y)
    
    #list of all interspike-intervals of y
    ISI = [] 
    #current ISI in ms
    counter = 0 
    for i in range(len(y)):
        #if a spike does not occure at y[i], increment the counter and look for the next spike
        if y[i] == 0: 
            counter = counter + 1
        #if y[i] is a spike, add the counter to the list of ISIs and start counting the next ISI
        else: 
            ISI = ISI + [counter]
            counter = 1 #set to 1 because if there are two concurent spikes then the ISI is 1ms
    
    #coefficient of Variation of ISIs
    coefVar = ( np.std(ISI) / np.mean(ISI)) * 100
    
    spikes5ms = spikeCountWindow(y, window=5)
    #Fano Factor for number of spikes in 20ms windows
    fanoFactor5ms = (np.var(spikes5ms) / np.mean(spikes5ms) )
    
    spikes40ms = spikeCountWindow(y, window=40)
    #Fano Factor for number of spikes in 20ms windows
    fanoFactor40ms = (np.var(spikes40ms) / np.mean(spikes40ms) )
    
    spikes100ms = spikeCountWindow(y, window=100)
    #Fano Factor for number of spikes in 20ms windows
    fanoFactor100ms = (np.var(spikes100ms) / np.mean(spikes100ms) )
    
    plt.subplot(2, 1, 2)
    plt.hist(ISI)
    plt.title("Interspike Intervals")
    plt.xlabel("ISI (ms)\n \
                Coefficient of Variation of ISIs:" + str(np.round(coefVar)) \
                + "\n Fano Factor for 5ms Windows: " + str(fanoFactor5ms) \
                + "\n Fano Factor for 40ms Windows: " + str(fanoFactor40ms)\
                + "\n Fano Factor for 100ms Windows: " + str(fanoFactor100ms))
    plt.ylabel("Frequency")   
    plt.tight_layout()
    plt.show()





def main():
    #loads data
    matc1p8 = scipy.io.loadmat(r'exercises\c1\data\c1p8.MAT')
    matc10p1 = np.loadtxt(r'exercises\c1\data\c10p1.MAT')
    
    #Visualizes data parameters
    #for key in matc1p8:
        #print (key, ": ", len(matc1p8[key])     
    #print (len(matc10p1))
    
    Ex1()

if __name__ == "__main__":
    main()