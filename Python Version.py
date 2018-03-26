import pandas as pd
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


#######################################################################################################################
#### This thing poops out a lot of print statements. Kind of annoying now that I know how it works ####################
#### I would like to simplify this code so that it doesn't take so long to run. There is a lot of  ####################
#### dead code in this segment. I might rewrite this to just get the important stuff.              ####################
#######################################################################################################################
def populationByAge( ):
    df = pd.read_excel('Chopped_Sheet.xlsx', sheet_name='HH Records Data')

    df.set_index('Record Number', inplace=True)

    # Initialize lists.
    # First two contain all the ages that are in our sample HH records
    # i.e. if there is a male age 65, they are added to ageListMale
    ageListMale = []
    ageListFemale = []

    # These contain the list of ages in each care level. i.e. if there is a 65 year old man in care level 1,
    # the age 65 is added to careLevel1Men
    careLevel0Men = []
    careLevel1Men = []
    careLevel2Men = []
    careLevel3Men = []
    careLevel4Men = []
    careLevel0Women = []
    careLevel1Women = []
    careLevel2Women = []
    careLevel3Women = []
    careLevel4Women = []

    # Does the work of filling the previous lists. Loops through the rows of HH Records data.
    # Because there are up to 6 people in each household, 6 blocks of similar code are placed
    # only difference in the blocks is checking first person vs second person vs etc etc
    for i in range(1, 10000):
        # If gender is male, add to male gender
        if df.at[i, 'Gender1'] == 2:
            ageListMale.append(df.at[i, 'Age1'])
            # if they are above 64, they must also be counted in the appropriate care level
            if(df.at[i,'Age1']>64):
                careLevel = df.at[i,'HH1']
                if(careLevel == 1):
                    careLevel1Men.append(df.at[i,'Age1'])
                elif(careLevel == 2):
                    careLevel2Men.append(df.at[i,'Age1'])
                elif(careLevel == 3):
                    careLevel3Men.append(df.at[i,'Age1'])
                elif(careLevel == 4):
                    careLevel4Men.append(df.at[i,'Age1'])
                else:
                    careLevel0Men.append(df.at[i,'Age1'])

        # If they are female, do the same thing, but in female lists
        elif df.at[i, 'Gender1'] == 1:
            ageListFemale.append(df.at[i, 'Age1'])
            if(df.at[i,'Age1']>64):
                careLevel = df.at[i,'HH1']
                if(careLevel == 1):
                    careLevel1Women.append(df.at[i,'Age1'])
                elif(careLevel == 2):
                    careLevel2Women.append(df.at[i,'Age1'])
                elif(careLevel == 3):
                    careLevel3Women.append(df.at[i,'Age1'])
                elif(careLevel == 4):
                    careLevel4Women.append(df.at[i,'Age1'])
                else:
                    careLevel0Women.append(df.at[i,'Age1'])

        if df.at[i, 'Gender2'] == 2:
            ageListMale.append(df.at[i, 'Age2'])
            if(df.at[i,'Age2']>64):
                careLevel = df.at[i,'HH2']
                if(careLevel == 1):
                    careLevel1Men.append(df.at[i,'Age2'])
                elif(careLevel == 2):
                    careLevel2Men.append(df.at[i,'Age2'])
                elif(careLevel == 3):
                    careLevel3Men.append(df.at[i,'Age2'])
                elif(careLevel == 4):
                    careLevel4Men.append(df.at[i,'Age2'])
                else:
                    careLevel0Men.append(df.at[i,'Age2'])
        elif df.at[i, 'Gender2'] == 1:
            ageListFemale.append(df.at[i, 'Age2'])
            if(df.at[i,'Age2']>64):
                careLevel = df.at[i,'HH2']
                if(careLevel == 1):
                    careLevel1Women.append(df.at[i,'Age2'])
                elif(careLevel == 2):
                    careLevel2Women.append(df.at[i,'Age2'])
                elif(careLevel == 3):
                    careLevel3Women.append(df.at[i,'Age2'])
                elif(careLevel == 4):
                    careLevel4Women.append(df.at[i,'Age2'])
                else:
                    careLevel0Women.append(df.at[i,'Age2'])

        if df.at[i, 'Gender3'] == 2:
            ageListMale.append(df.at[i, 'Age3'])
            if(df.at[i,'Age3']>64):
                careLevel = df.at[i,'HH3']
                if(careLevel == 1):
                    careLevel1Men.append(df.at[i,'Age3'])
                elif(careLevel == 2):
                    careLevel2Men.append(df.at[i,'Age3'])
                elif(careLevel == 3):
                    careLevel3Men.append(df.at[i,'Age3'])
                elif(careLevel == 4):
                    careLevel4Men.append(df.at[i,'Age3'])
                else:
                    careLevel0Men.append(df.at[i,'Age3'])
        elif df.at[i, 'Gender3'] == 1:
            ageListFemale.append(df.at[i, 'Age3'])
            if(df.at[i,'Age3']>64):
                careLevel = df.at[i,'HH3']
                if(careLevel == 1):
                    careLevel1Women.append(df.at[i,'Age3'])
                elif(careLevel == 2):
                    careLevel2Women.append(df.at[i,'Age3'])
                elif(careLevel == 3):
                    careLevel3Women.append(df.at[i,'Age3'])
                elif(careLevel == 4):
                    careLevel4Women.append(df.at[i,'Age3'])
                else:
                    careLevel0Women.append(df.at[i,'Age3'])

        if df.at[i, 'Gender4'] == 2:
            ageListMale.append(df.at[i, 'Age4'])
            if(df.at[i,'Age4']>64):
                careLevel = df.at[i,'HH4']
                if(careLevel == 1):
                    careLevel1Men.append(df.at[i,'Age4'])
                elif(careLevel == 2):
                    careLevel2Men.append(df.at[i,'Age4'])
                elif(careLevel == 3):
                    careLevel3Men.append(df.at[i,'Age4'])
                elif(careLevel == 4):
                    careLevel4Men.append(df.at[i,'Age4'])
                else:
                    careLevel0Men.append(df.at[i,'Age4'])
        elif df.at[i, 'Gender4'] == 1:
            ageListFemale.append(df.at[i, 'Age4'])
            if(df.at[i,'Age4']>64):
                careLevel = df.at[i,'HH4']
                if(careLevel == 1):
                    careLevel1Women.append(df.at[i,'Age4'])
                elif(careLevel == 2):
                    careLevel2Women.append(df.at[i,'Age4'])
                elif(careLevel == 3):
                    careLevel3Women.append(df.at[i,'Age4'])
                elif(careLevel == 4):
                    careLevel4Women.append(df.at[i,'Age4'])
                else:
                    careLevel0Women.append(df.at[i,'Age4'])

        if df.at[i, 'Gender5'] == 2:
            ageListMale.append(df.at[i, 'Age5'])
            if(df.at[i,'Age5']>64):
                careLevel = df.at[i,'HH5']
                if(careLevel == 1):
                    careLevel1Men.append(df.at[i,'Age5'])
                elif(careLevel == 2):
                    careLevel2Men.append(df.at[i,'Age5'])
                elif(careLevel == 3):
                    careLevel3Men.append(df.at[i,'Age5'])
                elif(careLevel == 4):
                    careLevel4Men.append(df.at[i,'Age5'])
                else:
                    careLevel0Men.append(df.at[i,'Age5'])
        elif df.at[i, 'Gender5'] == 1:
            ageListFemale.append(df.at[i, 'Age5'])
            if(df.at[i,'Age5']>64):
                careLevel = df.at[i,'HH5']
                if(careLevel == 1):
                    careLevel1Women.append(df.at[i,'Age5'])
                elif(careLevel == 2):
                    careLevel2Women.append(df.at[i,'Age5'])
                elif(careLevel == 3):
                    careLevel3Women.append(df.at[i,'Age5'])
                elif(careLevel == 4):
                    careLevel4Women.append(df.at[i,'Age5'])
                else:
                    careLevel0Women.append(df.at[i,'Age5'])

        if df.at[i, 'Gender6'] == 2:
            ageListMale.append(df.at[i, 'Age6'])
            if(df.at[i,'Age6']>64):
                careLevel = df.at[i,'HH6']
                if(careLevel == 1):
                    careLevel1Men.append(df.at[i,'Age6'])
                elif(careLevel == 2):
                    careLevel2Men.append(df.at[i,'Age6'])
                elif(careLevel == 3):
                    careLevel3Men.append(df.at[i,'Age6'])
                elif(careLevel == 4):
                    careLevel4Men.append(df.at[i,'Age6'])
                else:
                    careLevel0Men.append(df.at[i,'Age6'])
        elif df.at[i, 'Gender6'] == 1:
            ageListFemale.append(df.at[i, 'Age6'])
            if(df.at[i,'Age6']>64):
                careLevel = df.at[i,'HH6']
                if(careLevel == 1):
                    careLevel1Women.append(df.at[i,'Age6'])
                elif(careLevel == 2):
                    careLevel2Women.append(df.at[i,'Age6'])
                elif(careLevel == 3):
                    careLevel3Women.append(df.at[i,'Age6'])
                elif(careLevel == 4):
                    careLevel4Women.append(df.at[i,'Age6'])
                else:
                    careLevel0Women.append(df.at[i,'Age6'])

    # Debugging purposes. Shows number of people in each care level / gender
#    print(ageListMale)
#    print(ageListFemale)
#    print("Care Level 0 Men")
#    print(careLevel0Men)
#    print("Care Level 1 Men")
#    print(careLevel1Men)
#    print("Care Level 2 Men")
#    print(careLevel2Men)
#    print("Care Level 3 Men")
#    print(careLevel3Men)
#    print("Care Level 4 Men")
#    print(careLevel4Men)
#    print("Care Level 0 Women")
#    print(careLevel0Women)
#    print("Care Level 1 Women")
#    print(careLevel1Women)
#    print("Care Level 2 Women")
#    print(careLevel2Women)
#    print("Care Level 3 Women")
#    print(careLevel3Women)
#    print("Care Level 4 Women")
#    print(careLevel4Women)

    # Shows number of people in each age category. i.e. if the age 65 occurs 13 times in the above age list,
    # then the number 13 will appear in the 65th index of the list.
    ageDistributionMale = []
    ageDistributionFemale = []

    # Changed the bounds on these for loops in order to cut out people above age 110
    # People above 110 would simply die on the first time step, and would make our data structure worse to deal with.
    # Anyway, the loop fills the above lists.
    for i in range(0, 111):
        ageDistributionMale.append(ageListMale.count(i))
        ageDistributionFemale.append(ageListFemale.count(i))

    # debugs the above loop.
#    print("Male Age Distributions at ages 0 thru 110")
#    print(ageDistributionMale)
#    print(min(ageListMale))
#    print(max(ageListMale))
#    print(len(ageDistributionMale))
#    print("Female Age Distributions at ages 0 thru 110")
#    print(ageDistributionFemale)
#    print(min(ageListFemale))
#    print(max(ageListFemale))
#    print(len(ageDistributionFemale))

    # creates lists for percentages. I.e. if 17 men are in care level 1 at age 78, and there are 100 total
    # 78 year old men, then .17 will appear in index 78 of careLevel1MenDist
    careLevel0MenDist = []
    careLevel1MenDist = []
    careLevel2MenDist = []
    careLevel3MenDist = []
    careLevel4MenDist = []
    careLevel0WomenDist = []
    careLevel1WomenDist = []
    careLevel2WomenDist = []
    careLevel3WomenDist = []
    careLevel4WomenDist = []

    # fills the first 65 indices of the distribution lists
    # Because care levels cannot occur until age 65, the first 64 entries of care level 0 should be 1,
    # and the first 64 entries of all other care levels should be 0.
    for i in range(0, 65):
        careLevel0MenDist.append(1)
        careLevel1MenDist.append(0)
        careLevel2MenDist.append(0)
        careLevel3MenDist.append(0)
        careLevel4MenDist.append(0)
        careLevel0WomenDist.append(1)
        careLevel1WomenDist.append(0)
        careLevel2WomenDist.append(0)
        careLevel3WomenDist.append(0)
        careLevel4WomenDist.append(0)

    # Fills in care levels for actually relevant age groups
    # # people in care level n at age m divided by people in age m total
    for i in range(65,111):
        print("number of men at level 0")
        print(careLevel0Men.count(i))
        print("total number of men at age ", i)
        print(ageDistributionMale[i])
        careLevel0MenDist.append(careLevel0Men.count(i)/ageDistributionMale[i])
        careLevel1MenDist.append(careLevel1Men.count(i)/ageDistributionMale[i])
        careLevel2MenDist.append(careLevel2Men.count(i)/ageDistributionMale[i])
        careLevel3MenDist.append(careLevel3Men.count(i)/ageDistributionMale[i])
        careLevel4MenDist.append(careLevel4Men.count(i)/ageDistributionMale[i])
        careLevel0WomenDist.append(careLevel0Women.count(i)/ageDistributionMale[i])
        careLevel1WomenDist.append(careLevel1Women.count(i)/ageDistributionMale[i])
        careLevel2WomenDist.append(careLevel2Women.count(i)/ageDistributionMale[i])
        careLevel3WomenDist.append(careLevel3Women.count(i)/ageDistributionMale[i])
        careLevel4WomenDist.append(careLevel4Women.count(i)/ageDistributionMale[i])

    # Total number of people in the population. Counted in following for loop.
    numPeopleDistMale = 0
    numPeopleDistFemale = 0
    for i in range(0, 111):
        numPeopleDistMale = numPeopleDistMale + ageDistributionMale[i]
        numPeopleDistFemale = numPeopleDistFemale + ageDistributionFemale[i]

    totalPopulation = numPeopleDistMale + numPeopleDistFemale

    # percentage of the population in each care level and gender. Should be
    # number of people in the age and care divided by number of people in age divided by total
    # number of people in population.
    # (# in care in age) / (# in population)
    percentPopMale0 = []
    percentPopMale1 = []
    percentPopMale2 = []
    percentPopMale3 = []
    percentPopMale4 = []

    percentPopFemale0 = []
    percentPopFemale1 = []
    percentPopFemale2 = []
    percentPopFemale3 = []
    percentPopFemale4 = []

    for i in range(0, 65):
        percentPopMale0.append(ageListMale.count(i) / totalPopulation)
        percentPopMale1.append(careLevel1Men.count(i) / totalPopulation)
        percentPopMale2.append(careLevel2Men.count(i) / totalPopulation)
        percentPopMale3.append(careLevel3Men.count(i) / totalPopulation)
        percentPopMale4.append(careLevel4Men.count(i) / totalPopulation)

        percentPopFemale0.append(ageListFemale.count(i) / totalPopulation)
        percentPopFemale1.append(careLevel1Women.count(i) / totalPopulation)
        percentPopFemale2.append(careLevel2Women.count(i) / totalPopulation)
        percentPopFemale3.append(careLevel3Women.count(i) / totalPopulation)
        percentPopFemale4.append(careLevel4Women.count(i) / totalPopulation)

    for i in range (65, 111):
        percentPopMale0.append(careLevel0Men.count(i) / totalPopulation)
        percentPopMale1.append(careLevel1Men.count(i) / totalPopulation)
        percentPopMale2.append(careLevel2Men.count(i) / totalPopulation)
        percentPopMale3.append(careLevel3Men.count(i) / totalPopulation)
        percentPopMale4.append(careLevel4Men.count(i) / totalPopulation)

        percentPopFemale0.append(careLevel0Women.count(i) / totalPopulation)
        percentPopFemale1.append(careLevel1Women.count(i) / totalPopulation)
        percentPopFemale2.append(careLevel2Women.count(i) / totalPopulation)
        percentPopFemale3.append(careLevel3Women.count(i) / totalPopulation)
        percentPopFemale4.append(careLevel4Women.count(i) / totalPopulation)

    ##################################### Debugging statements. #######################################################
   # print("Care Level 0 men distribution length", len(careLevel0MenDist))
   # print(careLevel0MenDist)
   # print(numPeopleDistMale, len(ageListMale))
   # print(numPeopleDistFemale, len(ageListFemale))

    ###################################################################################################################


    # This version is based on ratio between people in age level to care level. I have made a new version
    # careLevelDists = [careLevel0MenDist,careLevel1MenDist,careLevel2MenDist,careLevel3MenDist,careLevel4MenDist,careLevel0WomenDist,careLevel1WomenDist,careLevel2WomenDist,careLevel3WomenDist,careLevel4WomenDist]

    careLevelDists = [percentPopMale0, percentPopMale1, percentPopMale2, percentPopMale3, percentPopMale4, percentPopFemale0, percentPopFemale1, percentPopFemale2, percentPopFemale3, percentPopFemale4]
    return careLevelDists

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################


#######################################################################################################################
#### This method runs quietly. We should all run like this method. ####################################################
#######################################################################################################################
def mortalityAnalysisByAge():

    mf = pd.read_excel('Chopped_Sheet.xlsx', sheet_name='Mortality Data')

    mf.set_index('Age', inplace=True)
    maleMortList = []
    maleLinReg = []
    femMortList = []
    femLinReg = []
    for i in range (0, 111):
        maleMortList.append(mf.at[i, "MaleAvg"])
        maleLinReg.append(mf.at[i, "MaleDAvg"])
        femMortList.append(mf.at[i, "FemAvg"])
        femLinReg.append(mf.at[i, "FemDAvg"])

    print(maleMortList)
    print(femMortList)

    mortDists = [maleMortList, maleLinReg, femMortList, femLinReg]
    return mortDists

#########################################################################################################
#########################################################################################################
#########################################################################################################

def transitionMatrix():
    transM = pd.read_excel('Chopped_Sheet.xlsx', sheet_name='Care Level Transition Matrix')
    transM.set_index('Index', inplace = True)

    # initialize transition matrices as lists
    transM0 = []
    transM1 = []
    transM2 = []
    transM3 = []
    transM4 = []

    # collect all of the probabilities in the correct lists
    for i in range(1, 6):
        transM0.append(transM.at[i + 5*0, 'Probability'])
        transM1.append(transM.at[i + 5*1, 'Probability'])
        transM2.append(transM.at[i + 5*2, 'Probability'])
        transM3.append(transM.at[i + 5*3, 'Probability'])
        transM4.append(transM.at[i + 5*4, 'Probability'])

    # format of this data structure is like this
    # from is vertical, to is horizontal. The intersection is the probablity of going from one to another
    #        0  1  2  3  4
    #       0
    #       1
    #       2
    #       3
    #       4
    #   format for use "transM[From][To]" will give the probability going from first index to second index.
    fullTransitionMatrix = [transM0, transM1, transM2, transM3, transM4]
    return fullTransitionMatrix

#########################################################################################################
#########################################################################################################
#########################################################################################################

def sim(numYears = 1, initialPopulation = 80000000):
    # Set up matrices. Easiest to call popbyAge because it already has the correct structure (almost)
    # These are simply percentages. We have two seperate lists that have percentages of population in each location.
    curLiability = populationByAge()
    frwLiability = [[], [], [], [], [], [], [], [], [], []]
    for i in range(0, 111):
        for j in range(0, 10):
            frwLiability[j].append(0)

    # Ideally, I'll make another one of these to make transition Matrix (transM) in a useful way.
    # I did the previous thing. See comments for mort and transM in order to know how to use them.
    mort = mortalityAnalysisByAge()
    transM = transitionMatrix()

    print("######################### SIMULATION START ############################")

    # just debugging the curLiability information.
    print(curLiability[0])

    # SHOULD be filling in matrix
    # To my understanding, the matrix initially has just ratios of total population in each group, so this should allow
    # us to enter in a random size population and immediately start a sim.
    for i in range(0, 10):
        for j in range (0, 111):
            curLiability[i][j] = int(curLiability[i][j] * initialPopulation)

    print(curLiability[0])

    # Initial conditions are completed. Now, run the simulation a number of times equal to the input
    # number of years
    for y in (0, numYears):
        print("Time step number ", y+1)
        # This loop fills in the trivial portion of the array (without age 0 population, see fertility)
        # [0] is male level 0, [5] is female level 0
        for i in range(0, 110):
            frwLiability[0][i+1] = curLiability[0][i] * (1 - mort[0][i])
            frwLiability[5][i+1] = curLiability[0][i] * (1 - mort[1][i])
        # OKAY so I found an error. After the above loop on time step 1, the entire array NaN's out. So we have
        # no working code for more than 1 time step. I probably just have to be wasteful and make the curLiability a
        # copy of frwLiability.... gonna be dumb.
        print("Frw of 0 after deaths", frwLiability[0])

        # This fills in the survival of people in care levels. Since mortality rate is tripled for
        # care level > 0, this gets its own loop. Two of these so that Female also happens
        for i in range(1, 5):
            for j in range(65, 110):
                frwLiability[i][j + 1] = curLiability[i][j] * (1 - (3 * mort[0][j]))
        for i in range(6, 10):
            for j in range(65, 110):
                frwLiability[i][j + 1] = curLiability[i][j] * (1 - (3 * mort[1][j]))

        # temporary array. Will hold the values of the care levels while tMatrix is being applied
        tmpArray = [0, 0, 0, 0, 0]

        # This will be the transition matrix location. transM[i][j] is going from [i] to [j]. Since we are traveling horizontally
        # and transitioning between vertical locations in the matrix, we need to have our outer loop be the age, and our inner loop
        # be the care level.
        for j in range(65, 111):
            for i in range(0, 5):
                tmpArray[i] = frwLiability[i][j]
            for i in range(0, 5):
                frwLiability[i][j] = tmpArray[0] * transM[0][i] + tmpArray[1] * transM[1][i] + tmpArray[2] * transM[2][i] + tmpArray[3] * transM[3][i] + tmpArray[4] * transM[4][i]

            for i in range(5, 10):
                tmpArray[i - 5] = frwLiability[i][j]
            for i in range(5, 10):
                j = i - 5
                frwLiability[i][j] = tmpArray[0] * transM[0][j] + tmpArray[1] * transM[1][j] + tmpArray[2] * transM[2][j] + tmpArray[3] * transM[3][j] + tmpArray[4] * transM[4][j]


        # Update cur pointer to frw. Next time step, frw is obviously the cur.
        # frw now becomes an empty array of the proper size.
        for i in range(0, 10):
            for j in range(0, 111):
                curLiability[i][j] = int(frwLiability[i][j])
      #  curLiability = frwLiability
       # frwLiability = [[], [], [], [], [], [], [], [], [], []]
      #  for i in range(0, 111):
       #     for j in range(0, 10):
        #        frwLiability[j].append(0)

        print("\n\n")

        # update the values of the mortality lists. Odd entries are the linear regression slope
        for i in range(0, 111):
            mort[0][i] = mort[0][i] + mort[1][i]
            mort[2][i] = mort[2][i] + mort[3][i]
