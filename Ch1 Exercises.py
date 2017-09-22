#Jordan Breffle
#https://github.com/jtbreffle
#Theoretical Neuroscience Exercises, Dayan and Abbott, 2001
#Chapter 1: Neural Encoding I: Firing Rates and Spike Statistics


import scipy.io #use scipy.io.loadmat() for MAT files
import numpy as np #if loadmat() fails, then use numpy.loadtxt(), becuase it is a plain text file

import random
import matplotlib.pyplot as plt



# ------------------Helper Functions--------------------------------------
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



def pairedSTA(SSI, data): #interval between two spikes in 2x ms\
    '''
    returns the spike triggered average of pairs of spikes seperated by SSI (second spike interval)
    data contains rho (list of when spikes occured) and stim (intensity of stimulus)
    '''
    
    #list of preceding stims that led to spikes
    allSTs = []
    for i in range(len(data["rho"])):
        #break when i wili exceed length to find second spike
        if i > (len(data["rho"]) + SSI):
            break
        #for first 300ms, cannot compute 300ms STA of any spikes that occur
        elif i < 150:
            pass
        #if a spike occured at time point i AND a spike occures at time point i+SSI, add the preceding 300ms of stim data as a new list to the list allSTs
        elif data["rho"][i] == 1 and data["rho"][i+SSI] == 1:
            allSTs = allSTs + [data["stim"][(i-150+SSI):(i+SSI)]]
        #if no spike occured at time point i, do nothing
        else:
            pass
        
        #break prematurely for quick debugging
        #if i == 1000000:
            #break
        
    #allSTs is now a list of lists, where each list is the stim that lead to a single spike
    STA = []
    for i in range(len(allSTs[0])):
        sum = 0
        for j in range(len(allSTs)):
            sum = sum + allSTs[j][i]
        
        STA = STA + [float (sum / len(allSTs) )]  
        
    return STA


def extraSpike(i, SSI, data):
    
    #increment through rho from i to i+SSI
    j = i+1
    while j < (i + SSI):
        #if any spikes occur between i and i+SSI, return true
        if data["rho"][j] == 1:
            return True
        j = j + 1
    #if no spikes are found between i and i+SSI, return false
    return False


def pairedSTAExcl(SSI, data): #interval between two spikes in 2x ms\
    '''
    returns the spike triggered average of pairs of spikes seperated by SSI (second spike interval)
    data contains rho (list of when spikes occured) and stim (intensity of stimulus)
    
    same as pairedSTA(), except no extra spikes can occur between the two spikes of interest
    '''
    
    #list of preceding stims that led to spikes
    allSTs = []
    for i in range(len(data["rho"])):
        #break when i wili exceed length to find second spike
        if i > (len(data["rho"]) + SSI):
            break
        #for first 300ms, cannot compute 300ms STA of any spikes that occur
        elif i < 150:
            pass
        
        #if a spike occured at time point i AND a spike occures at time point i+SSI AND there are no spikes between i and i+SSI, add the preceding 300ms of stim data as a new list to the list allSTs
        elif data["rho"][i] == 1 and\
             data["rho"][i+SSI] == 1 and \
             not extraSpike(i, SSI, data):
                            
            allSTs = allSTs + [data["stim"][(i-150+SSI):(i+SSI)]]
        #if no spike occured at time point i, do nothing
        else:
            pass
        
        #break prematurely for quick debugging
        if i == 50000:
            break
        
    #allSTs is now a list of lists, where each list is the stim that lead to a single spike
    STA = []
    for i in range(len(allSTs[0])):
        sum = 0
        for j in range(len(allSTs)):
            sum = sum + allSTs[j][i]
        
        STA = STA + [float (sum / len(allSTs) )]  
        
    return STA






#----------------------------Exercises------------------------------------
def Ex1():
    '''Generate spikes for 10 s (or longer if you want better statistics) using
    a Poisson spike generator with a constant rate of 100 Hz, and record
    their times of occurrence. Compute the coe∆cient of variation of the
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



def Ex2():
    '''
    Add a refractory period to the Poisson spike generator by allowing
    the firing rate to depend on time. Initially, set the firing rate to a
    constant value, r(t) = r0. After every spike, set r(t) to 0, and then
    allow it to recover exponentially back to r0 with a time constant TauRef
    that controls the refractory recovery rate. In other words, have r(t)
    obey the equation 
    
    TauRef(dr/dt) =r0 - r
    
    except immediately after a spike, when it is set to 0. Plot the coe∆-
    cient of variation as a function of TauRef over the range 1 ms <= TauRef <= 20 ms, and plot interspike interval histograms for a few diferent values of TauRef in this range. Compute the Fano factor for spike counts obtained over counting intervals ranging from 1 to 100 ms for the case TauRef =10 ms.
    '''
    
    
    #10s with points every 1ms
    x = np.linspace(0, 10, 1001)
    
    #samples drawn from a poisson distribution every 1ms for 10s, with probability reseting and then increasing exponentially after each spike
    y = []
    prob = 0.1
    #probability of a spike is set to 100Hz initially, if a spike occurs it is reset to 0, each ms that passes without a spike increases the probability of a spike by 1Hz
    for i in range(len(x)):
        y = y + [np.random.poisson(prob, 1)]
        if y[i] > 0:
            prob = 0
        else:
            prob = prob + 0.01
    
    #a single ms timepoint can have >1 event so...
    #this for-loop rounds all events >1 to a single spike
    for i in range(len(y)):  
        if y[i] > 0:       
            y[i] = 1
            
    plt.figure(num='Exercise 2')
    plt.subplot(2, 1, 1)
    plt.title("Poisson Generated Spikes with Refractory Period \n (Spike frequency increases by 1Hz per ms that passes without a spike)")
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
    
    
    
def Ex3():
    '''
    Compute autocorrelation histograms of spike trains generated by 
    1) a Poisson generator with a constant firing rate of 100 Hz
    2) a constant firing rate of 100 Hz together with a refractory period modeled as in exercise 2 with Tauref = 10 ms
    3) a variable firing rate r(t) = 100(1 + cos(2PIt/25 ms)) Hz. 
    Plot the histograms over a range from 0 to 100 ms.
    '''
    
    #10s with points every 1ms
    x = np.linspace(0, 10, 1001)
    
    
    #samples drawn from a poisson distribution every 1ms for 10s, with probability corresponding to 100Hz
    yNoRefPer = np.random.poisson(0.1, 1001)    
    
    
    #samples drawn from a poisson distribution every 1ms for 10s, with probability reseting and then increasing exponentially after each spike
    yRefPer = []
    prob = 0.1
    #probability of a spike is set to 100Hz initially, if a spike occurs it is reset to 0, each ms that passes without a spike increases the probability of a spike by 1Hz
    for i in range(len(x)):
        yRefPer = yRefPer + [np.random.poisson(prob, 1)]
        if yRefPer[i] > 0:
            prob = 0
        else:
            prob = prob + 0.01
    
    
    
    #variable firing rate r(t) = 100(1 + cos(2PIt/25 ms))
    yVarFir = []
    for i in range(len(x)):
        t = i / 2 #time t in ms 
        prob = 100 * (1 + np.cos(2 * np.pi * (t / 25) ) )
        yVarFir = yVarFir + [np.random.poisson(prob, 1)]
   
            
            
    
    #a single ms timepoint can have >1 event so...
    #this for-loop rounds all events >1 to a single spike
    for i in range(len(yNoRefPer)):  
        if yNoRefPer[i] > 0:       
            yNoRefPer[i] = 1
            
    #a single ms timepoint can have >1 event so...
    #this for-loop rounds all events >1 to a single spike
    for i in range(len(yRefPer)):  
        if yRefPer[i] > 0:       
            yRefPer[i] = 1 
        else:
            yRefPer[i] = 0
            
    #a single ms timepoint can have >1 event so...
    #this for-loop rounds all events >1 to a single spike
    for i in range(len(yVarFir)):  
        if yVarFir[i] > 0:       
            yVarFir[i] = 1   
            
            
    plt.figure(num='Exercise 3')
    plt.subplot(3, 1, 1)
    plt.title("Poisson Generated Spikes, 100Hz")
    plt.ylabel('Spikes')
    plt.xlabel('Time (S)')
    plt.plot(x, yNoRefPer)  
    
    plt.subplot(3, 1, 2)
    plt.title("Poisson Generated Spikes with Refractory Period \n (Spike frequency increases by 1Hz per ms that passes without a spike)")
    plt.ylabel('Spikes')
    plt.xlabel('Time (S)')
    plt.plot(x, yRefPer)     
    
    
    plt.subplot(3, 1, 3)
    #plt.hist(ISI)
    plt.title("Variable fire rate")
    plt.ylabel('Spikes')
    plt.xlabel('Time (S)')
    plt.plot(x, yVarFir)  
    
    plt.tight_layout()
    plt.show()    
    
    
    
    
def Ex4():
    '''
    Generate a Poisson spike train with a time-dependent firing rate
    r(t) = 100(1+ cos(2PIt/300 ms)) Hz. Approximate the firing rate from
    this spike train using a variable rapprox that satisfies 

    Tauapprox * (drapprox / dt) = -rapprox ,
    
    except that rapprox -> rapprox + 1/Tauapprox every time a spike occurs.
    
    *Make plots of the true rate, the spike sequence generated, and the
    estimated rate. 
    *Experiment with a few different values of Tauapprox in the range of 1 to
    100 ms. 
    *Determine the best value of Tauapprox by computing the average squared
    error of the estimate, INTEGRAL: dt(r(t) - rapprox(t))2, for different
    values of Tauapprox, and finding the value of Tauapprox that minimizes
    this error.
    '''
    
    
    #10s with points every 1ms
    x = np.linspace(0, 10, 1001)
    
    
    #samples drawn from a poisson distribution every 1ms for 10s, with probability corresponding to 100Hz
    yNoRefPer = np.random.poisson(0.1, 1001)    
    
    
    #samples drawn from a poisson distribution every 1ms for 10s, with probability reseting and then increasing exponentially after each spike
    yRefPer = []
    prob = 0.1
    #probability of a spike is set to 100Hz initially, if a spike occurs it is reset to 0, each ms that passes without a spike increases the probability of a spike by 1Hz
    for i in range(len(x)):
        yRefPer = yRefPer + [np.random.poisson(prob, 1)]
        if yRefPer[i] > 0:
            prob = 0
        else:
            prob = prob + 0.01
    
    
    #variable firing rate r(t) = 100(1+ cos(2PIt/300 ms))
    yVarFir = []
    for i in range(len(x)):
        t = i / 2 #time t in ms 
        prob = 100 * (1 + np.cos(2 * np.pi * (t / 300) ) )
        yVarFir = yVarFir + [np.random.poisson(prob, 1)]
   
            
            
    
    #a single ms timepoint can have >1 event so...
    #this for-loop rounds all events >1 to a single spike
    for i in range(len(yNoRefPer)):  
        if yNoRefPer[i] > 0:       
            yNoRefPer[i] = 1
            
    #a single ms timepoint can have >1 event so...
    #this for-loop rounds all events >1 to a single spike
    for i in range(len(yRefPer)):  
        if yRefPer[i] > 0:       
            yRefPer[i] = 1 
        else:
            yRefPer[i] = 0
            
    #a single ms timepoint can have >1 event so...
    #this for-loop rounds all events >1 to a single spike
    for i in range(len(yVarFir)):  
        if yVarFir[i] > 0:       
            yVarFir[i] = 1   
            
           
    plt.figure(num='Exercise 4')
    plt.subplot(3, 1, 1)
    #plt.hist(ISI)
    plt.title("Variable fire rate")
    plt.ylabel('Spikes')
    plt.xlabel('Time (S)')
    plt.plot(x, yVarFir)  
    
    #plt.subplot(3, 1, 2)
    #plt.title("Poisson Generated Spikes, 100Hz")
    #plt.ylabel('Spikes')
    #plt.xlabel('Time (S)')
    #plt.plot(x, yNoRefPer)  
    
    #plt.subplot(3, 1, 3)
    #plt.title("Poisson Generated Spikes with Refractory Period \n (Spike frequency increases by 1Hz per ms that passes without a spike)")
    #plt.ylabel('Spikes')
    #plt.xlabel('Time (S)')
    #plt.plot(x, yRefPer)     
    
    
    plt.tight_layout()
    plt.show()    
    
    
    
    
def Ex5():
    '''
    For a constant rate Poisson process, every specific (up to a finite
    resolution) sequence of N spikes occurring over a given time interval
    is equally likely. This seems paradoxical because we certainly do not
    expect to see all N spikes appearing within the first 1% of the time
    interval. Resolve this paradox.
    '''
    

    print ( "\
    We do not expect to see all N spikes appearing within the first 1% of the\
    \n time interval because the set of all possible sequences of N spikes \
    \n occurring within the first 1% of the time interval is a very small \
    \n subset of the total possible sequences of N spikes occuring withing the \
    \n first 100% of the time interval. \
    \n    Although any give sequence from either set is equally likely, the \
    \n first set has many fewer possible members and therefore the chance of \
    \n some individual member of the set occuring is very small.\
    ")
    
    #TODO: what is the exact probability?
    
    
    
def Ex6():
    '''
    Build an approximatewhite-noise stimulus by choosing randomvalues
    at discrete times separated by a time-step interval deltat. Plot its
    autocorrelation function and power spectrum(use theMATLABÆ function
    spectrum or psd). Discuss how well this stimulus matches an
    ideal white-noise stimulus given the value of deltat you used.
    '''
    
    
    
def Ex7():
    '''
    Consider a modelwith a firing rate determined in terms of a stimulus
    s(t) by integrating the equation
    
    Taur (drest(t) / dt) = [r0 + s]+ - rest(t),
    
    where r0 is a constant that determines the background firing rate and
    Taur = 20 ms. Drive the model with an approximate white-noise stimulus.
    Adjust the amplitude of the white-noise and the parameter r0
    so that rectification is not a big effect (i.e. r0 + s > 0 most of the time).
    Fromthe responses of themodel, compute the stimulus-response correlation
    function, Qrs. Next, generate spikes from this model using a
    Poisson generatorwith a rate rest(t), and compute the spike-triggered
    average stimulus from the spike trains produced by the white-noise
    stimulus. By comparing the stimulus-response correlation function
    with the spike-triggered average, verify that equation 1.22 is satisfied.
    Examine what happens if you set r0 = 0, so that the white-noise
    stimulus becomes half-wave rectified.
    '''
    
def Ex8(data):
    '''
    MATLABÆ file c1p8.mat contains data collected and provided by Rob
    de Ruyter van Steveninck from a fly H1 neuron responding to an approximate
    white-noise visual motion stimulus. Data were collected
    for 20minutes at a sampling rate of 500Hz. In the file, rho is a vector
    that gives the sequence of spiking events or nonevents at the sampled
    times (every 2 ms). When an element of rho is one, this indicates the
    presence of a spike at the corresponding time, whereas a zero value
    indicates no spike. The variable stim gives the sequence of stimulus
    values at the sampled times. 
    
    **Calculate and plot the spike-triggered average from these data over the range from 0 to 300 ms (150 time steps). (Based on a problem from Sebastian Seung.)**
    '''
    #linear space 300ms before a spike, point every 2 ms
    x = np.linspace(-298, 0, 150)
    
    #list of preceding stims that led to spikes
    allSTs = []
    for i in range(len(data["rho"])):
        #for first 300ms, cannot compute 300ms STA of any spikes that occur
        if i < 150:
            pass
        #if a spike occured at time point i, add the preceding 300ms of stim data as a new list to the list allSTs
        elif data["rho"][i] == 1:
            allSTs = allSTs + [data["stim"][(i-150):i]]
        #if no spike occured at time point i, do nothing
        else:
            pass
        
        #break prematurely for quick debugging
        #if i == 5000:
            #break
        
    #allSTs is now a list of lists, where each list is the stim that lead to a single spike
    STA = []
    for i in range(len(allSTs[0])):
        sum = 0
        for j in range(len(allSTs)):
            sum = sum + allSTs[j][i]
        
        STA = STA + [float (sum / len(allSTs) )]
        
    plt.figure(num='Exercise 8')       
    plt.plot(x, STA)
    plt.title("Spike-Triggered Average of a Fly H1 Neuron")
    plt.xlabel("Time (ms)")
    plt.ylabel("Stimulus")   
    plt.tight_layout()    
    plt.show()
        
    
    
def Ex9(data):
    '''
    Using the data of problem 8, calculate and plot stimulus averages
    triggered on events consisting of a pair of spikes (which need not necessarily
    be adjacent) separated by a given interval (as in figure 1.10).
    
    1) Plot these two-spike-triggered average stimuli for various separation
    intervals ranging from 2 to 100 ms. (Hint: in MATLABÆ , use convolution
    for pattern matching: e.g. find(conv(rho,[1 0 1])==2) will
    contain the indices of all the events with two spikes separated by 4
    ms.) 
    
    2) Plot, as a function of the separation between the two spikes,
    the magnitude of the difference between the two-spike-triggered average
    and the sum of two single-spike-triggered averages (obtained
    in exercise 8) separated by the same time interval. 
    
    3)At what temporal separation does this difference become negligibly small. (Based on a problem from Sebastian Seung.)
    '''
    
    #linear space 300ms before a spike, point every 2 ms
    x = np.linspace(-298, 0, 150)    
    
    ssi2ms = pairedSTA(SSI=1, data=data) #STA for spikes sepearted by 2ms
    ssi4ms = pairedSTA(SSI=2, data=data) #STA for spikes sepearted by 4ms
    ssi6ms = pairedSTA(SSI=3, data=data) #STA for spikes sepearted by 6ms
    ssi10ms = pairedSTA(SSI=5, data=data) #STA for spikes sepearted by 10ms
    ssi50ms = pairedSTA(SSI=25, data=data) #STA for spikes sepearted by 50ms
    ssi100ms = pairedSTA(SSI=50, data=data) #STA for spikes sepearted by 100ms
    
    STAMax = 29.472907029165032 #maximum stim amplitude for single spike STA from exercise 8
        
    plt.figure(num='Exercise 9')
    plt.subplot(2, 1, 1)    
    plt.plot(x, ssi100ms, label="100ms")
    plt.plot(x, ssi50ms, label="50ms")
    plt.plot(x, ssi10ms, label="10ms")
    plt.plot(x, ssi6ms, label="6ms")
    plt.plot(x, ssi4ms, label="4ms")
    plt.plot(x, ssi2ms, label="2ms")
    plt.title("STA's for pairs of spikes")
    plt.xlabel("Time (ms)")
    plt.ylabel("Stimulus") 
    plt.legend(loc='best', ncol=2, fancybox=True, shadow=True)
    
    plt.subplot(2, 1, 2)    
    plt.xlabel("Interval between spikes")
    plt.ylabel("Peak stim - single spike peak") 
    plt.plot(2, (max(ssi2ms) - (STAMax)), 'bo')
    plt.plot(50, (max(ssi50ms) - (STAMax)), 'bo')
    plt.plot(10, (max(ssi10ms) - (STAMax)), 'bo')
    plt.plot(100, (max(ssi100ms) - (STAMax)), 'bo') 
    plt.plot(4, (max(ssi4ms) - (STAMax)), 'bo')
    plt.plot(6, (max(ssi6ms) - (STAMax)), 'bo')
    
    plt.tight_layout()    
    plt.show()    
    
    
    
    
def Ex10(data):
    '''
    Using the data of problem 8, find the spike-triggered average stimulus
    for events that contain exactly two adjacent spikes separated by
    various different intervals ranging from 2 to 100 ms (e.g. for 4 ms,
    the event [1 0 1] but not the event [1 1 1]). This is distinct from
    exercise 9 in which we only required two spikes separated by a given
    interval, but did not restrict what happened between the two spikes.
    Compare results of the exclusive case considered here with those of
    the inclusive two-spike-triggered average computed in exercise 9. In
    what ways and why are they different? (Based on a problem from
    Sebastian Seung.)
    '''

    #linear space 300ms before a spike, point every 2 ms
    x = np.linspace(-298, 0, 150)    
    
    ssi2ms = pairedSTAExcl(SSI=1, data=data) #STA for spikes sepearted by 2ms
    ssi4ms = pairedSTAExcl(SSI=2, data=data) #STA for spikes sepearted by 4ms
    ssi6ms = pairedSTAExcl(SSI=3, data=data) #STA for spikes sepearted by 6ms
    ssi10ms = pairedSTAExcl(SSI=5, data=data) #STA for spikes sepearted by 10ms
    ssi50ms = pairedSTAExcl(SSI=25, data=data) #STA for spikes sepearted by 50ms
    ssi100ms = pairedSTAExcl(SSI=50, data=data) #STA for spikes sepearted by 100ms
    
    STAMax = 29.472907029165032 #maximum stim amplitude for single spike STA from exercise 8
        
    plt.figure(num='Exercise 10')
    plt.subplot(2, 1, 1)    
    plt.plot(x, ssi100ms, label="100ms")
    plt.plot(x, ssi50ms, label="50ms")
    plt.plot(x, ssi10ms, label="10ms")
    plt.plot(x, ssi6ms, label="6ms")
    plt.plot(x, ssi4ms, label="4ms")
    plt.plot(x, ssi2ms, label="2ms")
    plt.title("STA's for pairs of spikes, no between-spike spikes")
    plt.xlabel("Time (ms)")
    plt.ylabel("Stimulus") 
    plt.legend(loc='best', ncol=3, fancybox=True, shadow=True, prop={'size': 11})
    
    plt.subplot(2, 1, 2)    
    plt.xlabel("Interval between spikes")
    plt.ylabel("Peak stim - single spike peak") 
    plt.plot(2, (max(ssi2ms) - (STAMax)), 'bo')
    plt.plot(50, (max(ssi50ms) - (STAMax)), 'bo')
    plt.plot(10, (max(ssi10ms) - (STAMax)), 'bo')
    plt.plot(100, (max(ssi100ms) - (STAMax)), 'bo') 
    plt.plot(4, (max(ssi4ms) - (STAMax)), 'bo')
    plt.plot(6, (max(ssi6ms) - (STAMax)), 'bo')
    
    plt.tight_layout()    
    plt.show()    



def main():
    #loads data
    c1p8 = scipy.io.loadmat(r'exercises\c1\data\c1p8.MAT')
    c10p1 = np.loadtxt(r'exercises\c1\data\c10p1.MAT')
    
    #Visualizes data parameters
    #for key in matc1p8:
        #print (key, ": ", len(matc1p8[key])     
    #print (len(matc10p1))

    #execute exercises here
    #Ex1()
    #Ex2()
    #Ex3() #not finished
    #Ex4() #not finished
    #Ex5() #not finished
    #Ex6() #not finished
    #Ex7() #not finished
    #Ex8(data = c1p8)
    #Ex9(data = c1p8)
    #Ex10(data = c1p8)
    

if __name__ == "__main__":
    main()