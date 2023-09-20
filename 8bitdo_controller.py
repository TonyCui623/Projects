from evdev import InputDevice, categorize, ecodes

#create object "controller" to store the data you can call it whatever you like
controller=InputDevice('/dev/input/event3')

#prints out device info at start
print(controller)

#evdev takes care of polling the conntroller in a loop
for event in controller.read_loop():
    #print(categorize(event))

    #filters by event type
    if event.type==ecodes.EV_KEY:
        print(event)
    if event.type==ecodes.EV_ABS:
        print(event)


