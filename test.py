

@call_counter
def myfunction():
    myfunction.counter += 1
myfunction.counter = 0



myfunction()
myfunction()
print(myfunction.counter)
print(myfunction.calls)