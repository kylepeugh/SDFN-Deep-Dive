# 2. Pausing between printing descriptions
    # to add a delay to your message, the time module should be imported
import time
    # to use the delay, sleep method should be used like this
print("this will be printed with no delay....")
time.sleep(5) # the argument is the delay period by seconds 
print("this will be printed after 5 second delay....")
    # to make this more usable, you may think of creating a function
    # the function will be used anywhere in the game to add a message delay
    # you can try an aproach like this
def delay(period, msg):
    time.sleep(period)
    print(msg)
    # now, we can test it like this
delay(2, "this will be printed after 2 second delay....")