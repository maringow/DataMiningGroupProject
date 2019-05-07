import pandas as pd
import os

os.chdir('C:/Users/mgow/Documents/UChicago/Courses/Data Mining/Group Project')
outcomes = pd.read_csv('Complications_and_Deaths_-_Hospital.csv')
survey = pd.read_csv('Patient_survey__HCAHPS__-_Hospital.csv')

print(pd.DataFrame.head(outcomes))
print(pd.DataFrame.head(survey))

