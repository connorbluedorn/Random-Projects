#Deal or No Deal Test
#Written by Connor Bluedorn
#Last Updated 29 April 2022

#Written to disprove the idea that in Deal or No Deal, it is statistically favorable to switch your case for the last remaining case if
#the most valuable case is still in play, after encountering many people who argued that it is the same as a Monty Hall statistical problem.

import random #Random library used to generate random number guess to emulate random pick of case and eliminations. 

#################################
#Modifiable Variables
casecount = 20            #Modify the number of cases to select from. Win % of both the case you choose at the start and the last case that has not been eliminated should roughly equal 1/casecount
trialcount = 10000        #Number of trials run. Linear runtime increase, higher trail count will yield more accurate results. 1000+ should be satisfiable.
#################################
swapcase = 0    #
mycase = 0      # Counter Variables to track result of individual trials
losses = 0      #
numlist = []            #
i=0                     # Initializes the list of cases, with 0 being the most valuable, to allow for tests with different amounts
while i<casecount:      # of cases in play. Constructs an unmodified list of cases. 0 is always the most valuable to make win checking
    numlist.append(i)   # simpler to accomplish.
    i+=1                #
while trialcount>0:             #The trial, will run # of times equal to trial count.
    numstring = numlist.copy()#Copy over numlist so original list is not modified
    bound = len(numstring)-1#Establish bound for random integer guess
    mynumber = random.randint(0,bound);
    mypick = numstring[mynumber] #Pick a random case and remove it from the remaining cases
    numstring.pop(mynumber)
    n = bound-1 
    while (n>0): #While there is more than 1 case that is not eliminated or chosen by the 'player', randomly eliminate a case.
        numstring.pop(random.randint(0,n))
        n-=1
    dealerpick = numstring[0] #When all cases but one have been eliminated, establish the last case as the 'swappable' case.
    if(dealerpick == 0): #If the last case contains 0, mark it as a win for switching.
        swapcase += 1
    elif(mypick == 0): #If the case originally chosen contains 0, mark it as a win for the player's pick
        mycase += 1
    else:   #If neither case contains 0, mark it as a loss.
        losses +=1 
    trialcount -=1 #Remove 1 from the trial count and iterate.

###################################
#Print results to terminal
print("Losses")
print(losses)
print("My Case Wins")
print(mycase)
print("Dealers Case Wins")
print(swapcase)
###################################