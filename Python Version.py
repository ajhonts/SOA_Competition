import pandas as pd
import matplotlib.pyplot as plt;

plt.rcdefaults()
import numpy as np

def populationByAge():
    df = pd.read_excel('Chopped_Sheet.xlsx', sheet_name='HH Records Data')

    df.set_index('Record Number', inplace=True)

    ageListFemale = []
    ageListMale = []
    careLevel1Men = []
    careLevel2Men = []
    careLevel3Men = []
    careLevel4Men = []
    careLevel0Men = []
    careLevel1Women = []
    careLevel2Women = []
    careLevel3Women = []
    careLevel4Women = []
    careLevel0Women = []
    for i in range(1, 10000):
        if df.at[i, 'Gender1'] == 2:
            ageListMale.append(df.at[i, 'Age1'])
            if (df.at[i, 'Age1'] > 64):
                careLevel = df.at[i, 'HH1']
                if (careLevel == 1):
                    careLevel1Men.append(df.at[i, 'Age1'])
                elif (careLevel == 2):
                    careLevel2Men.append(df.at[i, 'Age1'])
                elif (careLevel == 3):
                    careLevel3Men.append(df.at[i, 'Age1'])
                elif (careLevel == 4):
                    careLevel4Men.append(df.at[i, 'Age1'])
                else:
                    careLevel0Men.append(df.at[i, 'Age1'])
        elif df.at[i, 'Gender1'] == 1:
            ageListFemale.append(df.at[i, 'Age1'])
            if (df.at[i, 'Age1'] > 64):
                careLevel = df.at[i, 'HH1']
                if (careLevel == 1):
                    careLevel1Women.append(df.at[i, 'Age1'])
                elif (careLevel == 2):
                    careLevel2Women.append(df.at[i, 'Age1'])
                elif (careLevel == 3):
                    careLevel3Women.append(df.at[i, 'Age1'])
                elif (careLevel == 4):
                    careLevel4Women.append(df.at[i, 'Age1'])
                else:
                    careLevel0Women.append(df.at[i, 'Age1'])

        if df.at[i, 'Gender2'] == 2:
            ageListMale.append(df.at[i, 'Age2'])
            if (df.at[i, 'Age2'] > 64):
                careLevel = df.at[i, 'HH2']
                if (careLevel == 1):
                    careLevel1Men.append(df.at[i, 'Age2'])
                elif (careLevel == 2):
                    careLevel2Men.append(df.at[i, 'Age2'])
                elif (careLevel == 3):
                    careLevel3Men.append(df.at[i, 'Age2'])
                elif (careLevel == 4):
                    careLevel4Men.append(df.at[i, 'Age2'])
                else:
                    careLevel0Men.append(df.at[i, 'Age2'])
        elif df.at[i, 'Gender2'] == 1:
            ageListFemale.append(df.at[i, 'Age2'])
            if (df.at[i, 'Age2'] > 64):
                careLevel = df.at[i, 'HH2']
                if (careLevel == 1):
                    careLevel1Women.append(df.at[i, 'Age2'])
                elif (careLevel == 2):
                    careLevel2Women.append(df.at[i, 'Age2'])
                elif (careLevel == 3):
                    careLevel3Women.append(df.at[i, 'Age2'])
                elif (careLevel == 4):
                    careLevel4Women.append(df.at[i, 'Age2'])
                else:
                    careLevel0Women.append(df.at[i, 'Age2'])

        if df.at[i, 'Gender3'] == 2:
            ageListMale.append(df.at[i, 'Age3'])
            if (df.at[i, 'Age3'] > 64):
                careLevel = df.at[i, 'HH3']
                if (careLevel == 1):
                    careLevel1Men.append(df.at[i, 'Age3'])
                elif (careLevel == 2):
                    careLevel2Men.append(df.at[i, 'Age3'])
                elif (careLevel == 3):
                    careLevel3Men.append(df.at[i, 'Age3'])
                elif (careLevel == 4):
                    careLevel4Men.append(df.at[i, 'Age3'])
                else:
                    careLevel0Men.append(df.at[i, 'Age3'])
        elif df.at[i, 'Gender3'] == 1:
            ageListFemale.append(df.at[i, 'Age3'])
            if (df.at[i, 'Age3'] > 64):
                careLevel = df.at[i, 'HH3']
                if (careLevel == 1):
                    careLevel1Women.append(df.at[i, 'Age3'])
                elif (careLevel == 2):
                    careLevel2Women.append(df.at[i, 'Age3'])
                elif (careLevel == 3):
                    careLevel3Women.append(df.at[i, 'Age3'])
                elif (careLevel == 4):
                    careLevel4Women.append(df.at[i, 'Age3'])
                else:
                    careLevel0Women.append(df.at[i, 'Age3'])

        if df.at[i, 'Gender4'] == 2:
            ageListMale.append(df.at[i, 'Age4'])
            if (df.at[i, 'Age4'] > 64):
                careLevel = df.at[i, 'HH4']
                if (careLevel == 1):
                    careLevel1Men.append(df.at[i, 'Age4'])
                elif (careLevel == 2):
                    careLevel2Men.append(df.at[i, 'Age4'])
                elif (careLevel == 3):
                    careLevel3Men.append(df.at[i, 'Age4'])
                elif (careLevel == 4):
                    careLevel4Men.append(df.at[i, 'Age4'])
                else:
                    careLevel0Men.append(df.at[i, 'Age4'])
        elif df.at[i, 'Gender4'] == 1:
            ageListFemale.append(df.at[i, 'Age4'])
            if (df.at[i, 'Age4'] > 64):
                careLevel = df.at[i, 'HH4']
                if (careLevel == 1):
                    careLevel1Women.append(df.at[i, 'Age4'])
                elif (careLevel == 2):
                    careLevel2Women.append(df.at[i, 'Age4'])
                elif (careLevel == 3):
                    careLevel3Women.append(df.at[i, 'Age4'])
                elif (careLevel == 4):
                    careLevel4Women.append(df.at[i, 'Age4'])
                else:
                    careLevel0Women.append(df.at[i, 'Age4'])

        if df.at[i, 'Gender5'] == 2:
            ageListMale.append(df.at[i, 'Age5'])
            if (df.at[i, 'Age5'] > 64):
                careLevel = df.at[i, 'HH5']
                if (careLevel == 1):
                    careLevel1Men.append(df.at[i, 'Age5'])
                elif (careLevel == 2):
                    careLevel2Men.append(df.at[i, 'Age5'])
                elif (careLevel == 3):
                    careLevel3Men.append(df.at[i, 'Age5'])
                elif (careLevel == 4):
                    careLevel4Men.append(df.at[i, 'Age5'])
                else:
                    careLevel0Men.append(df.at[i, 'Age5'])
        elif df.at[i, 'Gender5'] == 1:
            ageListFemale.append(df.at[i, 'Age5'])
            if (df.at[i, 'Age5'] > 64):
                careLevel = df.at[i, 'HH5']
                if (careLevel == 1):
                    careLevel1Women.append(df.at[i, 'Age5'])
                elif (careLevel == 2):
                    careLevel2Women.append(df.at[i, 'Age5'])
                elif (careLevel == 3):
                    careLevel3Women.append(df.at[i, 'Age5'])
                elif (careLevel == 4):
                    careLevel4Women.append(df.at[i, 'Age5'])
                else:
                    careLevel0Women.append(df.at[i, 'Age5'])

        if df.at[i, 'Gender6'] == 2:
            ageListMale.append(df.at[i, 'Age6'])
            if (df.at[i, 'Age6'] > 64):
                careLevel = df.at[i, 'HH6']
                if (careLevel == 1):
                    careLevel1Men.append(df.at[i, 'Age6'])
                elif (careLevel == 2):
                    careLevel2Men.append(df.at[i, 'Age6'])
                elif (careLevel == 3):
                    careLevel3Men.append(df.at[i, 'Age6'])
                elif (careLevel == 4):
                    careLevel4Men.append(df.at[i, 'Age6'])
                else:
                    careLevel0Men.append(df.at[i, 'Age6'])
        elif df.at[i, 'Gender6'] == 1:
            ageListFemale.append(df.at[i, 'Age6'])
            if (df.at[i, 'Age6'] > 64):
                careLevel = df.at[i, 'HH6']
                if (careLevel == 1):
                    careLevel1Women.append(df.at[i, 'Age6'])
                elif (careLevel == 2):
                    careLevel2Women.append(df.at[i, 'Age6'])
                elif (careLevel == 3):
                    careLevel3Women.append(df.at[i, 'Age6'])
                elif (careLevel == 4):
                    careLevel4Women.append(df.at[i, 'Age6'])
                else:
                    careLevel0Women.append(df.at[i, 'Age6'])

    print(ageListMale)
    print(ageListFemale)
    print("Care Level 0 Men")
    print(careLevel0Men)
    print("Care Level 1 Men")
    print(careLevel1Men)
    print("Care Level 2 Men")
    print(careLevel2Men)
    print("Care Level 3 Men")
    print(careLevel3Men)
    print("Care Level 4 Men")
    print(careLevel4Men)
    print("Care Level 0 Women")
    print(careLevel0Women)
    print("Care Level 1 Women")
    print(careLevel1Women)
    print("Care Level 2 Women")
    print(careLevel2Women)
    print("Care Level 3 Women")
    print(careLevel3Women)
    print("Care Level 4 Women")
    print(careLevel4Women)
    ageDistributionMale = []
    ageDistributionFemale = []
    for i in range(0, 118):
        ageDistributionMale.append(ageListMale.count(i))
        ageDistributionFemale.append(ageListFemale.count(i))

    print("Male Age Distributions at ages 0 thru 127")
    print(ageDistributionMale)
    print(min(ageListMale))
    print(max(ageListMale))
    print(len(ageDistributionMale))
    print("Female Age Distributions at ages 0 thru 127")
    print(ageDistributionFemale)
    print(min(ageListFemale))
    print(max(ageListFemale))
    print(len(ageDistributionFemale))
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
    for i in range(65, 118):
        print("number of men at level 0")
        print(careLevel0Men.count(i))
        print("total number of men at age ", i)
        print(ageDistributionMale[i])
        careLevel0MenDist.append(careLevel0Men.count(i) / ageDistributionMale[i])
        careLevel1MenDist.append(careLevel1Men.count(i) / ageDistributionMale[i])
        careLevel2MenDist.append(careLevel2Men.count(i) / ageDistributionMale[i])
        careLevel3MenDist.append(careLevel3Men.count(i) / ageDistributionMale[i])
        careLevel4MenDist.append(careLevel4Men.count(i) / ageDistributionMale[i])
        careLevel0WomenDist.append(careLevel0Women.count(i) / ageDistributionMale[i])
        careLevel1WomenDist.append(careLevel1Women.count(i) / ageDistributionMale[i])
        careLevel2WomenDist.append(careLevel2Women.count(i) / ageDistributionMale[i])
        careLevel3WomenDist.append(careLevel3Women.count(i) / ageDistributionMale[i])
        careLevel4WomenDist.append(careLevel4Women.count(i) / ageDistributionMale[i])
    numPeopleDistMale = 0
    numPeopleDistFemale = 0
    for i in range(0, 118):
        numPeopleDistMale = numPeopleDistMale + ageDistributionMale[i]
        numPeopleDistFemale = numPeopleDistFemale + ageDistributionFemale[i]

    print("Care Level 2 men distribution length", len(careLevel2MenDist))
    # print(numPeopleDistMale, len(ageListMale))
    # print(numPeopleDistFemale, len(ageListFemale))
    careLevelDists = [careLevel0MenDist, careLevel1MenDist, careLevel2MenDist, careLevel3MenDist, careLevel4MenDist,
                      careLevel0WomenDist, careLevel1WomenDist, careLevel2WomenDist, careLevel3WomenDist,
                      careLevel4WomenDist]
    return careLevelDists


def mortalityAnalysisByAge():
    mf = pd.read_excel('Chopped_Sheet.xlsx', sheet_name='Mortality Data')

    mf.set_index('Age', inplace=True)
    maleMortList = []
    femMortList = []
    for i in range(0, 111):
        maleMortList.append(mf.at[i, "MaleAvg"])
        femMortList.append(mf.at[i, "FemAvg"])

    print(maleMortList)
    print(femMortList)

    mortDists = [maleMortList, femMortList]
    return mortDists


def sim(numYears=1, initialPopulation=100000):
    # Set up matrices. Easiest to call popbyAge because it already has the correct structure (almost)
    # I need to append the Care level 0 ages 0-65 before the current info for it.
    curLiabiliy = populationByAge()
    frwLiability = populationByAge()

    # Ideally, I'll make another one of these to make transition Matrix (transM) in a useful way.
    mort = mortalityAnalysisByAge()

    # just debugging the curLiability information.
    print(len(curLiabiliy[0]))

    # SHOULD be filling in matrix
    # To my understanding, the matrix initially has just ratios of total population in each group, so this should allow
    # us to enter in a random size population and immediately start a sim.
    for i in range(0, 53):
        curLiabiliy[0][i] = curLiabiliy[0][i] * initialPopulation

    # How many times to run the simulation
    for i in range(0, numYears):
        # This loop fills in the trivial portion of the array (without age 0 population, see fertility)
        # [0] is male level 0, [5] is female level 0
        for j in range(0, 65):
            frwLiability[0][j + 1] = curLiabiliy[0][j] * (1 - mort[0][j])
            frwLiability[5][j + 1] = curLiabiliy[0][j] * (1 - mort[1][j])

        # Needs large amount of work. The higher care levels will have dropoffs due to mortality, and then
        # are filled in based on transitions between levels. Should be easily implemented, but need to fill out
        # care 0 before loop to avoid out of bounds exception. Maybe special case care level 4?
        # Regardless, [i][j] is a person in care level i travelling TO care level j.
        for j in range(66, 111):
            for k in range(0, 5):
                frwLiability[0][j][k] = 0

    # Should simply change pointer. Then, reassign the frwLiabilty to an empty matrix...
    # This is the very last command in the loop so that we can iterate again.
    curLiabiliy = frwLiability
