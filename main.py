import machine
import time

# set up a pin as footswitch input
footswitch  = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)

#set up a servo output
servo = machine.Pin(27)             #assigns pin 17 as servo signal
servo_pwm = machine.PWM(servo)      #declares servo pin as Pulse Width Modulation
servo_pwm.freq(50)

#Setup the external LED  as an output 
LED = machine.Pin(16,machine.Pin.OUT) 

#select duty_u16 values for 'foot_up' and 'foot_down' servo positions

foot_down = 4000   #4000/65535 = 6% duty cycle
foot_up = 6000     #9000/65535 = 9% duty cycle

#timing parameters (ms)
timeout=2500 #time foot will be lifted for if uninterupted by footswitch

#code ('IRQhandler') to run when main code interrupted by falling edge (footswitch release)
def footswitchIRQHandler_unload(pin):
    if pin == footswitch:
        start=time.ticks_ms()#start timer at point stimulation is started
        print('foot up until timeout or footswitch loaded')

        #while timer is less then specified timeout period and footswitch is unloaded
        while (time.ticks_ms()-start)<timeout and footswitch.value()==0: 
            LED.value(1)                   #LED is on
            servo_pwm.duty_u16(foot_up)    #foot set to lifted position
            time.sleep_ms(1) #this momentary sleep avoids the simulation slowing down in wokwi simulator

#assign the trigger and IRQhandler to run when loaded footswitch becomes unloaded
footswitch.irq(trigger = machine.Pin.IRQ_FALLING,
           handler =  footswitchIRQHandler_unload)


while True: #Main code which runs unless interrupted
    LED.value(0)                           #LED is off
    servo_pwm.duty_u16(foot_down)          #foot set to dropped position
    print('foot down')                     #print statements to communicate what's happening in the program
    print('footswitch value:',footswitch.value(),"\n")
    time.sleep(1)                          #cycles main loop at 1Hz

    


