import pandas as pd
import os

# read files (need to update to zip files on github)
os.chdir('C:/Users/mgow/Documents/UChicago/Courses/Data Mining/Group Project')
outcomes = pd.read_csv('Complications_and_Deaths_-_Hospital.csv')
survey = pd.read_csv('Patient_survey__HCAHPS__-_Hospital.csv')

print(pd.DataFrame.head(outcomes))
print(pd.DataFrame.head(survey))

print(str(outcomes))

# pivot outcomes data
outcomes_pivot = outcomes.pivot(index='Provider ID', columns='Measure ID', values='Score')
print(outcomes_pivot)

# write to file for QA
# outcomes_pivot.to_csv(path_or_buf=
#                       'C:/Users/mgow/Documents/UChicago/Courses/Data Mining/Group Project/outcomesPivot2.csv')

# pivot survey data
survey_pivot = survey.pivot(index='Provider ID', columns='HCAHPS Measure ID',
                            values='HCAHPS Linear Mean Value')
print(survey_pivot)

# write to file for QA
survey_pivot.to_csv(path_or_buf='C:/Users/mgow/Documents/UChicago/Courses/Data Mining/Group Project/surveyPivot.csv')

# drop all columns that are not linear mean scores

# bind data together using Provider ID
# add back hospital metadata columns - location, number of survey responses