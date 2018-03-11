import pandas as pd


def populationByAge( ):
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
    for i in range(65,118):
        print("count")
        print(careLevel0Men.count(i))
        print("Number of men at age i")
        print(ageDistributionMale[i])
        careLevel0MenDist.append(careLevel0Men.count(i)/ageDistributionMale[i])
        careLevel1MenDist.append(careLevel1Men.count(i)/ageDistributionMale[i])
        careLevel2MenDist.append(careLevel2Men.count(i)/ageDistributionMale[i])
        careLevel3MenDist.append(careLevel3Men.count(i)/ageDistributionMale[i])
        careLevel4MenDist.append(careLevel4Men.count(i)/ageDistributionMale[i])
        careLevel0WomenDist.append(careLevel0Women.count(i)/ageDistributionMale[i])
        careLevel0WomenDist.append(careLevel1Women.count(i)/ageDistributionMale[i])
        careLevel0WomenDist.append(careLevel2Women.count(i)/ageDistributionMale[i])
        careLevel0WomenDist.append(careLevel3Women.count(i)/ageDistributionMale[i])
        careLevel0WomenDist.append(careLevel4Women.count(i)/ageDistributionMale[i])
    numPeopleDistMale = 0
    numPeopleDistFemale = 0
    for i in range(0, 118):
        numPeopleDistMale = numPeopleDistMale + ageDistributionMale[i]
        numPeopleDistFemale = numPeopleDistFemale + ageDistributionFemale[i]

    print(numPeopleDistMale, len(ageListMale))
    print(numPeopleDistFemale, len(ageListFemale))
    careLevelDists = [careLevel0MenDist,careLevel1MenDist,careLevel2MenDist,careLevel3MenDist,careLevel4MenDist,careLevel0WomenDist,careLevel1WomenDist,careLevel2WomenDist,careLevel3WomenDist,careLevel4WomenDist]
    return careLevelDists

def mortalityAnalysisByAge():

    mf = pd.read_excel('Chopped_Sheet.xlsx', sheet_name='Mortality Data')

    mf.set_index('Age', inplace=True)

    mf_fem05 = pd.DataFrame(mf, columns = ['Age', '2005'])

    print(mf_fem05)
########################################################################################################################

mortalityAnalysisByAge()