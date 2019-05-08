import pandas as pd
import numpy as np
import os

# read files (need to update to zip files on github)
os.chdir('C:/Users/mgow/Documents/UChicago/Courses/Data Mining/Group Project')
outcomes = pd.read_csv('Complications_and_Deaths_-_Hospital.csv')
survey = pd.read_csv('Patient_survey__HCAHPS__-_Hospital.csv')

print(pd.DataFrame.head(outcomes))
print(pd.DataFrame.head(survey))

print(str(outcomes))

# pivot outcomes data
outcomes_pivot = outcomes.pivot(index='Provider ID', columns='Measure ID', values='Score').reset_index()
print(outcomes_pivot)

# write to file for QA
# outcomes_pivot.to_csv(path_or_buf=
#                       'C:/Users/mgow/Documents/UChicago/Courses/Data Mining/Group Project/outcomesPivot2.csv')

# pivot survey data
survey_pivot = survey.pivot(index='Provider ID', columns='HCAHPS Measure ID',
                            values='HCAHPS Linear Mean Value').reset_index()
print(survey_pivot)

# write to file for QA
# survey_pivot.to_csv(path_or_buf='C:/Users/mgow/Documents/UChicago/Courses/Data Mining/Group Project/surveyPivot2.csv')

# drop all columns that are not linear mean scores
survey_pivot_trimmed = survey_pivot[['Provider ID', 'H_CLEAN_LINEAR_SCORE', 'H_COMP_1_LINEAR_SCORE',
                                     'H_COMP_2_LINEAR_SCORE', 'H_COMP_3_LINEAR_SCORE', 'H_COMP_5_LINEAR_SCORE',
                                     'H_COMP_6_LINEAR_SCORE', 'H_COMP_7_LINEAR_SCORE', 'H_HSP_RATING_LINEAR_SCORE',
                                     'H_QUIET_LINEAR_SCORE', 'H_RECMND_LINEAR_SCORE']]

# survey_pivot_trimmed.to_csv(path_or_buf='C:/Users/mgow/Documents/UChicago/Courses/Data Mining/Group Project/surveyPivotTrimmed.csv')

# merge dataframes together using Provider ID as join key
df = outcomes_pivot.merge(survey_pivot_trimmed, how='outer', on='Provider ID')
df.to_csv(path_or_buf='C:/Users/mgow/Documents/UChicago/Courses/Data Mining/Group Project/joinedData.csv')

# add back hospital metadata columns - location, number of survey responses


# get rid of 'Not Available' values and replace with blanks
