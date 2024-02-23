
text= """ Among 1485 patients (mean age, 34.0 [SD, 4.5] years), 1470 (99.0%) completed the trial (n = 735 in both randomization groups) 
and were included in the analysis. 
Trial-of-labor rates did not differ significantly between intervention and control groups (43.3% vs 46.2%, respectively; 
adjusted absolute risk difference, –2.78% [95% CI, –7.80% to 2.25%]; adjusted relative risk, 0.94 [95% CI, 0.84-1.05]). 
There were no statistically significant differences in vaginal birth rates (31.8% in both groups; 
adjusted absolute risk difference, –0.04% [95% CI, –4.80% to 4.71%]; adjusted relative risk, 1.00 [95% CI, 0.86-1.16]) 
or in any of the other 6 clinical maternal and neonatal secondary outcomes. 
There also were no significant differences between the intervention and control groups in the 5 decision quality measures 
(eg, mean decisional conflict scores were 17.2 and 17.5, respectively; adjusted mean difference, –0.38 [95% CI, –1.81 to 1.05]; 
scores >25 are considered clinically important).
"""


#confidence_interval = text.find("% CI")
#print(confidence_interval)

#### CONFIDENCE INTERVALS

def locations_of_substring(string, substring):

    substring_length = len(substring)    
    def recurse(locations_found, start):
        location = string.find(substring, start)
        if location != -1:
            return recurse(locations_found + [location], location+substring_length)
        else:
            return locations_found

    return recurse([], 0)

all_confidence_intervals = (locations_of_substring(text, '% CI'))

def Cloning(all_confidence_intervals):
    li_copy = []
    li_copy.extend(all_confidence_intervals)
    return li_copy

All_Measure_Value_Locations = Cloning(all_confidence_intervals)
All_Lower_Range_Value_Locations = Cloning(all_confidence_intervals)
All_Upper_Range_Value_Locations = Cloning(all_confidence_intervals)


for n, all_confidence_intervals in enumerate(all_confidence_intervals,1):
    globals()["CI_location%d"%n] = all_confidence_intervals
    

CI_1 = text[CI_location1-2:CI_location1+1]
CI_2 = text[CI_location2-2:CI_location2+1]
CI_3 = text[CI_location3-2:CI_location3+1]



#### ALL OUTCOME MEASURE VALUES
for i in range(len(All_Measure_Value_Locations)):
    All_Measure_Value_Locations[i] = All_Measure_Value_Locations[i] - 9

for n, All_Measure_Value_Locations in enumerate(All_Measure_Value_Locations,1):
    globals()["Measure_Value_Location%d"%n] = All_Measure_Value_Locations
    

Outcome_Value_1 = text[Measure_Value_Location1:Measure_Value_Location1+5]
Outcome_Value_2 = text[Measure_Value_Location2:Measure_Value_Location2+5]
Outcome_Value_3 = text[Measure_Value_Location3:Measure_Value_Location3+5]


#### LOWER RANGE OF MEASURE

for i in range(len(All_Lower_Range_Value_Locations)):
    All_Lower_Range_Value_Locations[i] = All_Lower_Range_Value_Locations[i] +6

for n, All_Lower_Range_Value_Locations in enumerate(All_Lower_Range_Value_Locations,1):
    globals()["Lower_Range_Value_Location%d"%n] = All_Lower_Range_Value_Locations
    

Lower_Range_Value_1 = text[Lower_Range_Value_Location1:Lower_Range_Value_Location1+5]
Lower_Range_Value_2 = text[Lower_Range_Value_Location2:Lower_Range_Value_Location2+6]
Lower_Range_Value_3 = text[Lower_Range_Value_Location3:Lower_Range_Value_Location3+6]

#### UPPER RANGE OF MEASURE

for i in range(len(All_Upper_Range_Value_Locations)):
    All_Upper_Range_Value_Locations[i] = All_Upper_Range_Value_Locations[i] +15

for n, All_Upper_Range_Value_Locations in enumerate(All_Upper_Range_Value_Locations,1):
    globals()["Upper_Range_Value_Location%d"%n] = All_Upper_Range_Value_Locations
    

Upper_Range_Value_1 = text[Upper_Range_Value_Location1:Upper_Range_Value_Location1+4]
Upper_Range_Value_2 = text[Upper_Range_Value_Location2:Upper_Range_Value_Location2+5]
Upper_Range_Value_3 = text[Upper_Range_Value_Location3+1:Upper_Range_Value_Location3+6]

"""
#### P-VALUES

all_p_values = (locations_of_substring(text, 'P ='))

for n, all_p_values in enumerate(all_p_values,1):
    globals()["P_value_location%d"%n] = all_p_values
    

P_Value_1 = text[P_value_location1+3:P_value_location1+7]
P_Value_2 = text[P_value_location2+3:P_value_location2+7]
P_Value_3 = text[P_value_location3+3:P_value_location3+7]
P_Value_4 = text[P_value_location4+3:P_value_location4+8]
"""
