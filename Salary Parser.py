# Import pandas lib as pd
import pandas as pd

# Read excel holding base employee information
dataframe1 = pd.read_excel('EmployeeInformation.xlsx')

#print(dataframe1)
#print(dataframe1.columns.ravel())

# Create dictionaries to hold count of employees in each state and average tenure
stateCount = {}
timeOfEmployment = {}

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

# Loop through each entry in the Duration column of the excel sheet
# If that duration has not been seen before, create an entry for it
#   in the dictionary timeOfEmployment and set it's value to 1
#   If if has been seen before increment it's value by 1
for i in dataframe1['Duration']:
    if i in timeOfEmployment:
        x = timeOfEmployment[i]
        timeOfEmployment[i] = x+1
    else:
        timeOfEmployment[i] = 1

print(stateCount)
print(timeOfEmployment)