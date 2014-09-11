Workplace-Fatalities
====================

Data, methodology, and code behind our analysis of oil and gas worker fatal injuries

## Overview
This repository includes the raw data, analyzed data, and Python code Inside Energy used to calculate state-level oil and gas worker fatality rates (per 100,000 workers and per 100 rigs) for 2011 and 2012.

View the findings of this analysis, along with in-depth reporting on the topic, at InsideEnergy.org.

If you have any feedback, please contact jordanwb@insideenergy.org.

### Files in this repository
* **BLS_API_Download.py** - This is the Python code we used to download Census of Fatal Occupational Injuries (CFOI) data from the Bureau of Labor Statistics API. It retrieves all available years (2011 and 2012 when we first did this project) for [NAICS codes](http://www.census.gov/eos/www/naics/) 211, 212, 213, 213111 and 213112 and saves the data as a CSV file.
* **BLS_CFOI_data_states.csv** - This is the CFOI fatalities data we downloaded from the BLS API. The table structure is: BLS series ID, NAICS code, geography (state or US), year, number of fatalities.
* **CBP_Employment_data_states.csv** - This is the relevant state-level County Business Patterns data for 2011 and 2012 for NAICS codes 211, 212, 213, 213111 and 213112. See below for an explanation on how we filtered this data.
* **Rig_Count_data_states.csv** - This is the Baker Hughes active rotary rig count data at the state-level for data for 2011 and 2012. See below for information on how we downloaded and cleaned it.
* **State_Fatality_Rates_CALCULATED.csv** - This is the final output of our analysis.

### Methodology
How did we do this analysis? By following these steps, you'll be able to re-create the analysis.

#### Data sources used in this analysis
* Number of fatalities (by state): Bureau of Labor Statistics [Census of Fatal Occupational Injuries](http://www.bls.gov/iif/oshcfoi1.htm), 2011 and 2012
* Number of workers (by state): United States Census Bureau [County Business Patterns](http://www.census.gov/econ/cbp/), 2011 and 2012
* Number of oil and gas rigs (by state): [Baker Hughes North America Rotary Rig Count](http://www.bakerhughes.com/rig-count), U.S. Annual Average by State, 2011 and 2012

#### A note on NAICS codes and data availability
In this analysis, we focused on the oil and gas industry, which is most accurately described using NAICS codes 211 (oil and gas extraction), 213111 (drilling for oil and gas) and 213112 (support activities for oil and gas). Some of the data (CFOI data at the state level) was not available for all relevant NAICS codes because it did not meet BLS publication standards. We spoke with BLS and confirmed that there is no way to know whether there were no fatalities in a given category (example: NAICS 213111 for Wyoming for 2012) of if there were fatalities that did not meet the BLS publication standards. Because of this, the state fatality numbers do not add up to the U.S. total. This means that the state fatality counts - and, by extension, the state fatality rates - are likely underestimates.