import pandas as pd


def populationByAge( ):
    df = pd.read_excel('Chopped_Sheet.xlsx', sheet_name='HH Records Data')

    df.set_index('Record Number', inplace=True)

    ageListFemale = []
    ageListMale = []
    for i in range(1, 10000):
        if df.at[i, 'Gender1'] == 2:
            ageListMale.append(df.at[i, 'Age1'])
        elif df.at[i, 'Gender1'] == 1:
            ageListFemale.append(df.at[i, 'Age1'])

        if df.at[i, 'Gender2'] == 2:
            ageListMale.append(df.at[i, 'Age2'])
        elif df.at[i, 'Gender2'] == 1:
            ageListFemale.append(df.at[i, 'Age2'])

        if df.at[i, 'Gender3'] == 2:
            ageListMale.append(df.at[i, 'Age3'])
        elif df.at[i, 'Gender3'] == 1:
            ageListFemale.append(df.at[i, 'Age3'])

        if df.at[i, 'Gender4'] == 2:
            ageListMale.append(df.at[i, 'Age4'])
        elif df.at[i, 'Gender4'] == 1:
            ageListFemale.append(df.at[i, 'Age4'])

        if df.at[i, 'Gender5'] == 2:
            ageListMale.append(df.at[i, 'Age5'])
        elif df.at[i, 'Gender5'] == 1:
            ageListFemale.append(df.at[i, 'Age5'])

        if df.at[i, 'Gender6'] == 2:
            ageListMale.append(df.at[i, 'Age6'])
        elif df.at[i, 'Gender6'] == 1:
            ageListFemale.append(df.at[i, 'Age6'])

    print(ageListMale)
    print(ageListFemale)

    ageDistributionMale = []
    ageDistributionFemale = []
    for i in range(0, 127):
        ageDistributionMale.append(ageListMale.count(i))
        ageDistributionFemale.append(ageListFemale.count(i))

    print(ageDistributionMale)
    print(ageDistributionFemale)

    numPeopleDistMale = 0
    numPeopleDistFemale = 0
    for i in range(0, 127):
        numPeopleDistMale = numPeopleDistMale + ageDistributionMale[i]
        numPeopleDistFemale = numPeopleDistFemale + ageDistributionFemale[i]

    print(numPeopleDistMale, len(ageListMale))
    print(numPeopleDistFemale, len(ageListFemale))

def mortalityAnalysisByAge():

    mf = pd.read_excel('Chopped_Sheet.xlsx', sheet_name='Mortality Data')

    mf.set_index('Age', inplace=True)

    mf_fem05 = pd.DataFrame(mf, columns = ['Age', '2005']).cumsum()

    print(mf_fem05)
########################################################################################################################

mortalityAnalysisByAge()