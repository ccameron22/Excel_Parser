# Import pandas lib as pd
import pandas as pd

# Read excel with medical and voter information
medicalTreatment = pd.read_excel('MedicalHistory.xlsx', sheet_name="Medical History")
voterHistoryNames = pd.read_excel('MedicalHistory.xlsx', sheet_name="Voter Registration")
insuranceClaims = pd.read_excel('MedicalHistory.xlsx', sheet_name="Insurance Claims")

# Create lists to hold parsed columns
voterNames = []
voterBirthDateList = []
dupVoterBirthDateList = []
insuranceClaimDOBZIP = []
dupInsuranceClaimDOBZIP = []
insuranceDates = {}
voterInfo = {}
answerList = []

# In sheet of Voter information, combine first and last names into a new column
voterHistoryNames['Full Name'] = voterHistoryNames["First Name"] + " " + voterHistoryNames["Last Name"]

# Format Procedure list in Medical sheet as strings
medicalTreatment["Procedure"] = medicalTreatment["Procedure"].map(str)

# Create new column in the voter history sheet to combine DOB and ZIP of voter
voterHistoryNames["Date of Birth"] = voterHistoryNames["Date of Birth"].dt.strftime('%m/%d/%Y')
voterHistoryNames["Zip"] = voterHistoryNames["Zip"].map(str)
voterHistoryNames['DOB ZIP'] = voterHistoryNames["Date of Birth"] + " " + voterHistoryNames["Zip"]

# Create new column in the insurance sheet to combine DOB and ZIP of patient
insuranceClaims["Date of Birth"] = insuranceClaims["Date of Birth"].dt.strftime('%m/%d/%Y')
insuranceClaims["Zip"] = insuranceClaims["Zip"].map(str)
insuranceClaims['DOB ZIP'] = insuranceClaims["Date of Birth"] + " " + insuranceClaims["Zip"]

# Format date of service in Medical record and Insurance record
medicalTreatment["Date of Service"] = medicalTreatment["Date of Service"].dt.strftime('%m/%d/%Y')
insuranceClaims["Date of Service"] = insuranceClaims["Date of Service"].dt.strftime('%m/%d/%Y')

# Create dictionary with Date of Service as key and DOB-ZIP as value
index = 0
for i in insuranceClaims["Date of Service"]:
    insuranceDates[i] = insuranceClaims.loc[index, "DOB ZIP"]
    index += 1

# Create dictionary with DOB-Zip as key and Full Name as value
index = 0
for i in voterHistoryNames["DOB ZIP"]:
    voterInfo[i] = voterHistoryNames.loc[index, "ID"]
    index += 1

# Loop through each entry in the Date of Service column
# of the Medical Treatment record and check if a matching date of treatment
index = 0
for i in medicalTreatment["Date of Service"]:
    medCode = medicalTreatment.loc[index, "Procedure"]
    index += 1
    if i in insuranceDates:
        x = insuranceDates[i]
        if x in voterInfo:
            y = voterInfo[x]
            y = y + "_" + medCode
            answerList.append(y)

print(answerList)