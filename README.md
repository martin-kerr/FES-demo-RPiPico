# FES-demo-RPiPico
Code and circuit setup for Raspberry Pi Pico to demonstrates principle of operation of  FES (Functional Electrical Stimulation) 

## Background
Functional Electrical Stimulation (FES) is an assistive technology commonly used to help overcome ‘drop foot’ by stimulating the peroneal nerve though skin surface electrodes contracting the tibialis anterior and lifting the foot. A pressure sensing ‘footswitch’ is also worn under the patient’s heel so that the stimulation can be applied with correct timing as the patient walks.

 ![image](https://user-images.githubusercontent.com/50867224/209982204-18cdecd4-6fc2-4bc6-aff5-48d455cc58a8.png)


## Demo Circuit
This basic, low cost circuitry demonstrates the principle of operation of an FES device as it would function to alleviate 'drop foot'. It makes use of a Raspberry Pi Pico microcontroller programmed in Micropython. The demonstration simulation can be found on [Wokwi](https://wokwi.com/projects/352395885318022145) (https://wokwi.com/projects/352395885318022145)
 
![image](https://user-images.githubusercontent.com/50867224/209982222-928cc592-ebdf-4024-aaac-51fc3782ae9e.png)

Here, the footswitch is represented by a push button and
the foot is represented by a servo motor which is in a 
dropped position when unstimulated and lifts
to a dorsiflexed position when stimulated.

LED flashes as indicator that 'stimulation' is being applied to lift foot, triggered by 
releasing the load from the footswitch.


## Instructions for [Wokwi](https://wokwi.com/projects/352395885318022145) Simulation:

1. Start the Simulation

2. Press and then release footswitch

3. On RELEASE of the footswitch the foot lifts from a dropped 
   to a dorsiflexed position and the LED lights

4. On pressing footswitch again or leaving it unpressed for a specified
   timeout period (2.5s default), the 'stimulation' ends, LED switches off and
the foot returns to its dropped position

Next developments:

1. Introduce more timing parameters such as rising, 
   falling ramps and extension time.

2. Incorporate screen to enable visualisation of 
parameter settings, status of inputs/outputs etc
