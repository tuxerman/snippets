import requests
import time
import pdb

def bombard(function, timesPerSecond, duration=1, uniform=False):
    count = 0
    keepGoing = True
    timeStart = time.time()

    results = []

    # if uniform:
        
    #     while(time.time() < timeStart + duration):

    #         timeStartFn = time.time()
    #         results.append( function() )
    #         timeEndFn = time.time()
    #         timeToExecute = timeEndFn - timeStartFn

    #         # calculate sleep time
    #         1 - now(): time left this second.
    #         1 - now() - (remaining count * time to execute): time left to sleep

    #         timeSleepTotal = 1 - (timesPerSecond * timeToExecute)
    #         timeSleepNow = timeSleepTotal / timesPerSecond

    #         time.sleep(timeSleepNow)

    if uniform: 

        while(time.time() < timeStart + duration):

            timeSecStart = time.time()
            count = 0

            while(time.time() < timeSecStart + 1 and count < timesPerSecond):
                timeStartFn = time.time()
                results.append(function())
                count = count + 1
                timeNow = time.time()
                timeToExecute =  timeNow - timeStartFn

                timeSlackLeft = 1 - timeNow + timeSecStart - (timesPerSecond - count) * timeToExecute
                sleepTime = ( timeSlackLeft / (timesPerSecond - count + 1) ) 

                time.sleep( max(0, sleepTime) )


    else:
        while (time.time() < timeStart + duration):

            timeSecStart = time.time()
            count = 0
            
            while (time.time() < timeSecStart + 1):

                if count >= timesPerSecond:
                    while (time.time() < timeSecStart + 1):
                        pass
                    break
                else:
                    results.append( function() )
                    count = count + 1

    return results

def dummyFunction():
    # print 'Inside function'
    time.sleep(0.001)
    return 0

if __name__ == '__main__':
    results = bombard(dummyFunction, 800, 1, uniform=True)

    # start = time.time()
    # results = []

    # while (time.time() < start + 3):
    #     results.append(dummyFunction())

    print len(results)