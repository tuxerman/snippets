import random

switchDoors = True    # whether player changes his choice after host opens a door
sampleTries = 100   

timesWon, timesLost = 0,0
for iters in range (sampleTries):

	# put the car behind a random door
	car = (int)(random.uniform(0,3)) 			
	#print "Car is behind",car

	# pick one door out of the remaining doors to open
	iOpen = (int)(random.uniform(0,3)) 			
	#print "You initially choose",iOpen

	# host picks the other door and offers you the choice
	heOpens = 0
	while (heOpens == car or heOpens == iOpen):
		heOpens = heOpens + 1				
	#print "Host opens",heOpens

