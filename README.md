# Theoretical-Neuroscience-Exercises
Answers to the exercises in Theoretical Neuroscience, Dayan and Abbott (2001)


## Part I: Neural Encoding and Decoding
### Chapter 1: Neural Encoding I; Firing rates and spike statistics

<p align="center">
  <img src="https://raw.githubusercontent.com/jtbreffle/Theoretical-Neuroscience-Exercises/master/ReadMe_Figures/c1p1.png">
</p>

    1. Generate spikes for 10 s (or longer if you want better statistics) using
    a Poisson spike generator with a constant rate of 100 Hz, and record
    their times of occurrence. Compute the coeffcient of variation of the
    interspike intervals, and the Fano factor for spike counts obtained
    over counting intervals ranging from 1 to 100 ms. Plot the interspike
    interval histogram. 
<br />
<br />

![alt text](https://raw.githubusercontent.com/jtbreffle/Theoretical-Neuroscience-Exercises/master/ReadMe_Figures/c1p2.png)
    
    2. Add a refractory period to the Poisson spike generator by allowing
    the firing rate to depend on time. Initially, set the firing rate to a
    constant value, r(t) = r0. After every spike, set r(t) to 0, and then
    allow it to recover exponentially back to r0 with a time constant TauRef
    that controls the refractory recovery rate. In other words, have r(t)
    obey the equation 
    
    TauRef(dr/dt) = r0 - r
    
    except immediately after a spike, when it is set to 0. Plot the
    coeffcient of variation as a function of TauRef over the range 1 ms <=
    TauRef <= 20 ms, and plot interspike interval histograms for a few
    diferent values of TauRef in this range. Compute the Fano factor for
    spike counts obtained over counting intervals ranging from 1 to 100 ms
    for the case TauRef = 10 ms.
<br />
<br />

![alt text](https://raw.githubusercontent.com/jtbreffle/Theoretical-Neuroscience-Exercises/master/ReadMe_Figures/c1p8.png)

    8. MATLAB® file c1p8.mat contains data collected and provided by Rob
    de Ruyter van Steveninck from a fly H1 neuron responding to an approximate
    white-noise visual motion stimulus. Data were collected
    for 20minutes at a sampling rate of 500Hz. In the file, rho is a vector
    that gives the sequence of spiking events or nonevents at the sampled
    times (every 2 ms). When an element of rho is one, this indicates the
    presence of a spike at the corresponding time, whereas a zero value
    indicates no spike. The variable stim gives the sequence of stimulus
    values at the sampled times. 
    
    Calculate and plot the spike-triggered average from these data over the range 
    from 0 to 300 ms (150 time steps). (Based on a problem from Sebastian Seung.)
<br />
<br />

![alt text](https://raw.githubusercontent.com/jtbreffle/Theoretical-Neuroscience-Exercises/master/ReadMe_Figures/c1p9.png)

    9. Using the data of problem 8, calculate and plot stimulus averages
    triggered on events consisting of a pair of spikes (which need not necessarily
    be adjacent) separated by a given interval (as in figure 1.10).
    
    1) Plot these two-spike-triggered average stimuli for various separation
    intervals ranging from 2 to 100 ms. (Hint: in MATLAB® , use convolution
    for pattern matching: e.g. find(conv(rho,[1 0 1])==2) will
    contain the indices of all the events with two spikes separated by 4
    ms.) 
    
    2) Plot, as a function of the separation between the two spikes,
    the magnitude of the difference between the two-spike-triggered average
    and the sum of two single-spike-triggered averages (obtained
    in exercise 8) separated by the same time interval. 
    
    3)At what temporal separation does this difference become negligibly small. 
    (Based on a problem from Sebastian Seung.)
<br />
<br />

![alt text](https://raw.githubusercontent.com/jtbreffle/Theoretical-Neuroscience-Exercises/master/ReadMe_Figures/c1p10.png)

    10. Using the data of problem 8, find the spike-triggered average stimulus
    for events that contain exactly two adjacent spikes separated by
    various different intervals ranging from 2 to 100 ms (e.g. for 4 ms,
    the event [1 0 1] but not the event [1 1 1]). This is distinct from
    exercise 9 in which we only required two spikes separated by a given
    interval, but did not restrict what happened between the two spikes.
    Compare results of the exclusive case considered here with those of
    the inclusive two-spike-triggered average computed in exercise 9. In
    what ways and why are they different? (Based on a problem from
    Sebastian Seung.)
<br />
<br />
<br />
<br />

### Chapter 2: Neural Encoding II: Reverse correaltion abd visual receptive fields

### Chapter 3: Neural decoding

### Chapter 4: Information theory


## Part II: Neurons and Neural Circuits

### Chapter 5: Model neurons I: Neuroelectronics

### Chapter 6: Model neurons II: Conductances and morphology

### Chapter 7: Network models


## Part III: Adaptation and Learning

### Chapter 8: Plasticity and learning

### Chapter 9: Classical conditioning and reinforcement learning

### Chapter 10: Representational Learning
