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

"""
# In sheet of Voter information, combine first and last names into a new column
voterHistoryNames['Full Name'] = voterHistoryNames["First Name"] + " " + voterHistoryNames["Last Name"]

# Loop through newly created column in the Voter sheet and make a list of names
for i in voterHistoryNames["Full Name"]:
    if i not in voterNames:
        voterNames.append(i)
"""

# Loop through the voter information sheet and parse dates of birth, then convert to strings instead of time stamps
for i in voterHistoryNames["Date of Birth"]:
    x = i.strftime('%m/%d/%Y')
    if x not in voterBirthDateList:
        voterBirthDateList.append(x)
    else:
        dupVoterBirthDateList.append(x)

# Create new column in the insurance sheet to combine DOB and ZIP of patient
insuranceClaims["Date of Birth"] = insuranceClaims["Date of Birth"].dt.strftime('%m/%d/%Y')
insuranceClaims["Zip"] = insuranceClaims["Zip"].map(str)
insuranceClaims['DOB ZIP'] = insuranceClaims["Date of Birth"] + " " + insuranceClaims["Zip"]

# Loop through the insurance claim information sheet and parse dates of birth, then convert to strings instead of
# time stamps. Combine this with the zipcode to create a potentially identifiable string
for i in insuranceClaims["DOB ZIP"]:
    if i not in insuranceClaimDOBZIP:
        insuranceClaimDOBZIP.append(i)
    else:
        dupInsuranceClaimDOBZIP.append(i)

print("Voter DOBs")
print(voterBirthDateList)
print(dupVoterBirthDateList)
print()
print("Insurance DOBs")
print(insuranceClaimDOBZIP)
print(dupInsuranceClaimDOBZIP)

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