import pyfirmata
comport = 'COM4'
board = pyfirmata.Arduino(comport)
in1 = board.get_pin('d:4:o')
in2 = board.get_pin('d:5:o')
in3 = board.get_pin('d:6:o')
in4 = board.get_pin('d:7:o')
ena = board.get_pin('d:9:o')
enb = board.get_pin('d:3:o')
led = board.get_pin('d:8:o')
ena.write(1)
enb.write(1)


def ins(val):
    if val == 1:
        in1.write(1)
        in2.write(0)
        in3.write(0)
        in4.write(1)
    elif val == 2:
        in1.write(0)
        in2.write(1)
        in3.write(1)
        in4.write(0)  
    elif val == 0:
        in1.write(1)
        in2.write(1)
        in3.write(1)
        in4.write(1)
    elif val == 3:
        led.write(1)
           