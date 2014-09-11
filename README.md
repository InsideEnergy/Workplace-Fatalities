Workplace-Fatalities
====================

Data, methodology, and code behind our analysis of oil and gas worker fatal injuries

## Overview
This repository includes the raw data, analyzed data, and Python code Inside Energy used to calculate state-level oil and gas worker fatality rates (per 100,000 workers and per 100 rigs) for 2011 and 2012.

View the findings of this analysis, along with in-depth reporting on the topic, at InsideEnergy.org.

### Files in this repository
* **BLS_API_Download.py** - This is the Python code we used to download Census of Fatal Occupational Injuries (CFOI) data from the Bureau of Labor Statistics API. It retrieves all available years (2011 and 2012 when we first did this project) for [NAICS codes](http://www.census.gov/eos/www/naics/) 211, 212, 213, 213111 and 213112 and saves the data as a CSV file.
* **BLS_CFOI_data_states.csv** - This is the CFOI fatalities data we downloaded from the BLS API. The table structure is: BLS series ID, NAICS code, geography (state or US), year, number of fatalities.
* **CBP_Employment_data_states.csv** - This is the relevant state-level County Business Patterns data for 2011 and 2012 for NAICS codes 211, 212, 213, 213111 and 213112. See below for an explanation on how we filtered this data.
* **Rig_Count_data_states.csv** - This is the Baker Hughes active rotary rig count data at the state-level for data for 2011 and 2012. See below for information on how we downloaded and cleaned it.
* **State_Fatality_Rates_CALCULATED.csv** - This is the final output of our analysis.

### Methodology
How did we do this analysis? By following these steps, you'll be able to re-create the analysis. If you have any feedback, please contact jordanwb@insideenergy.org.
