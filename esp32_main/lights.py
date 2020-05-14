from machine import Pin, PWM
import utime


# This is still in BETA testing. 
# The below light() function transtions between start value and stop values by increments as stated in the increase_X = variable. 
# Still need to develop all of the various transitions and write the MQTT stuff. 


r = PWM(Pin(16))
b = PWM(Pin(17))
ww = PWM(Pin(18)) 
cw = PWM(Pin(19))

def dark_sunrise():
    red = 0
    blue = 0
    cool = 0
    warm = 0

    increase_r = 1
    increase_b = 1
    increase_cw = 1
    increase_ww = 1
    
    while True:
        utime.sleep_ms(30)
        while r.duty(red) != (1000):
            if red > 150:
                print(str(r.duty()) + ' r.duty') # print() statements are for testing
                print(str(red) + ' red lights')
                break
            else:
                print(str(r.duty()) + ' r.duty') 
                print(str(red) + ' red lights') 
                red += increase_r
            break
        while b.duty(blue) != (1000):
            if blue > 75:
                print(str(b.duty()) + ' b.duty')
                print(str(blue) + ' blue lights')
            else:    
                print(str(b.duty()) + ' b.duty')
                print(str(blue) + ' blue lights')
                blue += increase_b
            break
        while cw.duty(cool) != (1000):
            if cool > 75:
                print(str(cw.duty()) + ' cw.duty') # print() statements are for testing
                print(str(cool) + ' Cool White')
                break
            else:
                print(str(cw.duty()) + ' cw.duty') 
                print(str(cool) + ' Cool White') 
                cool += increase_cw
            break
        while ww.duty(warm) != (1000):
            if warm > 200:
                print(str(ww.duty()) + ' ww.duty') # print() statements are for testing
                print(str(warm) + ' Warm White')
                break
            else:
                print(str(ww.duty()) + ' ww.duty') 
                print(str(warm) + ' Warm White') 
                warm += increase_ww
            break
        if red > 150 and blue > 75 and cool > 75 and warm > 200:
            break

def sunrise_morning():
    
    red = 150
    blue = 75
    cool = 75
    warm = 200

    increase_r = 1
    increase_b = 1
    increase_cw = 1
    increase_ww = 1
    
    while True:
        utime.sleep_ms(30)
        while r.duty(red) != (1000):
            if red > 700:
                print(str(r.duty()) + ' r.duty') # print() statements are for testing
                print(str(red) + ' red lights')
                break
            else:
                print(str(r.duty()) + ' r.duty') 
                print(str(red) + ' red lights') 
                red += increase_r
            break
        while b.duty(blue) != (1000):
            if blue > 600:
                print(str(b.duty()) + ' b.duty')
                print(str(blue) + ' blue lights')
            else:    
                print(str(b.duty()) + ' b.duty')
                print(str(blue) + ' blue lights')
                blue += increase_b
            break
        while cw.duty(cool) != (1000):
            if cool > 700:
                print(str(cw.duty()) + ' cw.duty') # print() statements are for testing
                print(str(cool) + ' Cool White')
                break
            else:
                print(str(cw.duty()) + ' cw.duty') 
                print(str(cool) + ' Cool White') 
                cool += increase_cw
            break
        while ww.duty(warm) != (1000):
            if warm > 700:
                print(str(ww.duty()) + ' ww.duty') # print() statements are for testing
                print(str(warm) + ' Warm White')
                break
            else:
                print(str(ww.duty()) + ' ww.duty') 
                print(str(warm) + ' Warm White') 
                warm += increase_ww
            break
        if red > 700 and blue > 600 and cool > 700 and warm > 700:
            break
def morning_highnoon():
    red = 0
    blue = 0
    cool = 0
    warm = 0

    increase_r = 1
    increase_b = 2
    increase_cw = 3
    increase_ww = 4
    
    while True:
        utime.sleep_ms(30)
        while r.duty(red) != (1000):
            if red > 300:
                print(str(r.duty()) + ' r.duty') # print() statements are for testing
                print(str(red) + ' red lights')
                break
            else:
                print(str(r.duty()) + ' r.duty') 
                print(str(red) + ' red lights') 
                red += increase_r
            break
        while b.duty(blue) != (1000):
            if blue > 300:
                print(str(b.duty()) + ' b.duty')
                print(str(blue) + ' blue lights')
            else:    
                print(str(b.duty()) + ' b.duty')
                print(str(blue) + ' blue lights')
                blue += increase_b
            break
        while cw.duty(cool) != (1000):
            if cool > 300:
                print(str(cw.duty()) + ' cw.duty') # print() statements are for testing
                print(str(cool) + ' Cool White')
                break
            else:
                print(str(cw.duty()) + ' cw.duty') 
                print(str(cool) + ' Cool White') 
                cool += increase_cw
            break
        while ww.duty(warm) != (1000):
            if warm > 600:
                print(str(ww.duty()) + ' ww.duty') # print() statements are for testing
                print(str(warm) + ' Warm White')
                break
            else:
                print(str(ww.duty()) + ' ww.duty') 
                print(str(warm) + ' Warm White') 
                warm += increase_ww
            break
        if red > 300 and blue > 300 and cool > 300 and warm > 600:
            break
def highnoon_sunset():
    red = 0
    blue = 0
    cool = 0
    warm = 0

    increase_r = 1
    increase_b = 2
    increase_cw = 3
    increase_ww = 4
    
    while True:
        utime.sleep_ms(30)
        while r.duty(red) != (1000):
            if red > 300:
                print(str(r.duty()) + ' r.duty') # print() statements are for testing
                print(str(red) + ' red lights')
                break
            else:
                print(str(r.duty()) + ' r.duty') 
                print(str(red) + ' red lights') 
                red += increase_r
            break
        while b.duty(blue) != (1000):
            if blue > 300:
                print(str(b.duty()) + ' b.duty')
                print(str(blue) + ' blue lights')
            else:    
                print(str(b.duty()) + ' b.duty')
                print(str(blue) + ' blue lights')
                blue += increase_b
            break
        while cw.duty(cool) != (1000):
            if cool > 300:
                print(str(cw.duty()) + ' cw.duty') # print() statements are for testing
                print(str(cool) + ' Cool White')
                break
            else:
                print(str(cw.duty()) + ' cw.duty') 
                print(str(cool) + ' Cool White') 
                cool += increase_cw
            break
        while ww.duty(warm) != (1000):
            if warm > 600:
                print(str(ww.duty()) + ' ww.duty') # print() statements are for testing
                print(str(warm) + ' Warm White')
                break
            else:
                print(str(ww.duty()) + ' ww.duty') 
                print(str(warm) + ' Warm White') 
                warm += increase_ww
            break
        if red > 300 and blue > 300 and cool > 300 and warm > 600:
            break
def sunset_dusk():
    red = 0
    blue = 0
    cool = 0
    warm = 0

    increase_r = 1
    increase_b = 2
    increase_cw = 3
    increase_ww = 4
    
    while True:
        utime.sleep_ms(30)
        while r.duty(red) != (1000):
            if red > 300:
                print(str(r.duty()) + ' r.duty') # print() statements are for testing
                print(str(red) + ' red lights')
                break
            else:
                print(str(r.duty()) + ' r.duty') 
                print(str(red) + ' red lights') 
                red += increase_r
            break
        while b.duty(blue) != (1000):
            if blue > 300:
                print(str(b.duty()) + ' b.duty')
                print(str(blue) + ' blue lights')
            else:    
                print(str(b.duty()) + ' b.duty')
                print(str(blue) + ' blue lights')
                blue += increase_b
            break
        while cw.duty(cool) != (1000):
            if cool > 300:
                print(str(cw.duty()) + ' cw.duty') # print() statements are for testing
                print(str(cool) + ' Cool White')
                break
            else:
                print(str(cw.duty()) + ' cw.duty') 
                print(str(cool) + ' Cool White') 
                cool += increase_cw
            break
        while ww.duty(warm) != (1000):
            if warm > 600:
                print(str(ww.duty()) + ' ww.duty') # print() statements are for testing
                print(str(warm) + ' Warm White')
                break
            else:
                print(str(ww.duty()) + ' ww.duty') 
                print(str(warm) + ' Warm White') 
                warm += increase_ww
            break
        if red > 300 and blue > 300 and cool > 300 and warm > 600:
            break
def dusk_dark():
    red = 0
    blue = 0
    cool = 0
    warm = 0

    increase_r = 1
    increase_b = 2
    increase_cw = 3
    increase_ww = 4
    
    while True:
        utime.sleep_ms(30)
        while r.duty(red) != (1000):
            if red > 300:
                print(str(r.duty()) + ' r.duty') # print() statements are for testing
                print(str(red) + ' red lights')
                break
            else:
                print(str(r.duty()) + ' r.duty') 
                print(str(red) + ' red lights') 
                red += increase_r
            break
        while b.duty(blue) != (1000):
            if blue > 300:
                print(str(b.duty()) + ' b.duty')
                print(str(blue) + ' blue lights')
            else:    
                print(str(b.duty()) + ' b.duty')
                print(str(blue) + ' blue lights')
                blue += increase_b
            break
        while cw.duty(cool) != (1000):
            if cool > 300:
                print(str(cw.duty()) + ' cw.duty') # print() statements are for testing
                print(str(cool) + ' Cool White')
                break
            else:
                print(str(cw.duty()) + ' cw.duty') 
                print(str(cool) + ' Cool White') 
                cool += increase_cw
            break
        while ww.duty(warm) != (1000):
            if warm > 600:
                print(str(ww.duty()) + ' ww.duty') # print() statements are for testing
                print(str(warm) + ' Warm White')
                break
            else:
                print(str(ww.duty()) + ' ww.duty') 
                print(str(warm) + ' Warm White') 
                warm += increase_ww
            break
        if red > 300 and blue > 300 and cool > 300 and warm > 600:
            break
