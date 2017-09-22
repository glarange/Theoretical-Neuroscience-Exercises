# Theoretical-Neuroscience-Exercises
Answers to the exercises in Theoretical Neuroscience, Dayan and Abbott (2001)


## Part I: Neural Encoding and Decoding
### Chapter 1: Neural Encoding I; Firing rates and spike statistics

<p align="center">
  <img src="https://raw.githubusercontent.com/jtbreffle/Theoretical-Neuroscience-Exercises/master/ReadMe_Figures/c1p1.png">
</p>

    1) Generate spikes for 10 s (or longer if you want better statistics) using
    a Poisson spike generator with a constant rate of 100 Hz, and record
    their times of occurrence. Compute the coeffcient of variation of the
    interspike intervals, and the Fano factor for spike counts obtained
    over counting intervals ranging from 1 to 100 ms. Plot the interspike
    interval histogram. 
<br />
<br />

![alt text](https://raw.githubusercontent.com/jtbreffle/Theoretical-Neuroscience-Exercises/master/ReadMe_Figures/c1p2.png)
    
    2) Add a refractory period to the Poisson spike generator by allowing
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

<br />
<br />

![alt text](https://raw.githubusercontent.com/jtbreffle/Theoretical-Neuroscience-Exercises/master/ReadMe_Figures/c1p9.png)

<br />
<br />

![alt text](https://raw.githubusercontent.com/jtbreffle/Theoretical-Neuroscience-Exercises/master/ReadMe_Figures/c1p10.png)

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
