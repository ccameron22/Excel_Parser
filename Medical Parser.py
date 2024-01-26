# Import pandas lib as pd
import pandas as pd

# Read excel with medical and voter information
medicalTreatmentNames = pd.read_excel('MedicalHistory.xlsx', sheet_name="Medical History")
voterHistoryNames = pd.read_excel('MedicalHistory.xlsx', sheet_name="Voter Registration")

# Create lists to hold parsed columns
medNames = []
voterNames = []
birthDateList = []

# Loop through sheet of medical providers and strip names
for i in medicalTreatmentNames['Provider']:
    if i not in medNames:
        medNames.append(i)

# In sheet of Voter information, combine first and last names into a new column
voterHistoryNames['Full Name'] = voterHistoryNames["First Name"] + " " + voterHistoryNames["Last Name"]

# Loop through newly created column in the Voter sheet and make a list of names
for i in voterHistoryNames["Full Name"]:
    if i not in voterNames:
        voterNames.append(i)

# Loop through the voter information sheet and parse dates of birth, then convert to strings instead of time stamps
for i in voterHistoryNames["Date of Birth"]:
    x = i.strftime('%m/%d/%Y')
    if x not in birthDateList:
        birthDateList.append(x)

print(birthDateList)
"""
# Loop through each entry in the State column of the excel sheet
# If the state has not been seen before, create an entry for it
#   in the dictionary stateCount and set it's value to 1
#   If it has been seen before increment it's value by 1
for i in dataframe1['State']:
    if i in stateCount:
        x = stateCount[i]
        stateCount[i] = x+1
    else:
        stateCount[i] = 1
"""