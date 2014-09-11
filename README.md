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
* **master_geo_lookup.csv** - Lookup table for state names and codes. Table structure: name, 2-digit postal code, 2-digit FIPS code, 3-digit BLS geographic area code.
### Methodology
How did we do this analysis? By following these steps, you'll be able to re-create the analysis.

#### Data sources used in this analysis
* Number of fatalities (by state): Bureau of Labor Statistics [Census of Fatal Occupational Injuries](http://www.bls.gov/iif/oshcfoi1.htm), 2011 and 2012
* Number of workers (by state): United States Census Bureau [County Business Patterns](http://www.census.gov/econ/cbp/), 2011 and 2012
* Number of oil and gas rigs (by state): [Baker Hughes North America Rotary Rig Count](http://www.bakerhughes.com/rig-count), U.S. Annual Average by State, 2011 and 2012

#### A note on NAICS codes and data availability
In this analysis, we focused on the oil and gas industry, which is most accurately described using NAICS codes 211 (oil and gas extraction), 213111 (drilling for oil and gas) and 213112 (support activities for oil and gas). Some of the data (CFOI data at the state level) was not available for all relevant NAICS codes because it did not meet [BLS publication standards](http://www.bls.gov/opub/hom/pdf/homch9.pdf). We confirmed with BLS that there is no way to know whether there were no fatalities in a given category (example: NAICS 213111 for Wyoming for 2012) of if there were fatalities that did not meet the BLS publication standards. Because of this, the state fatality numbers do not add up to the U.S. total. This means that the state fatality counts - and, by extension, the state fatality rates - are likely underestimates.

#### Step 1: Downloaded CFOI data using the BLS API
We wrote Python code that queries the BLS API for all states for NAICS codes 211, 212, 213, 213111 and 213112.
(Note on inputs and outputs?)

#### Step 2: Download CBP employment data for 2011 and 2012
Download:
* 2011 and 2012 state data as zip files (add links)
* 2011 and 2012 U.S. data as zip files
Once you've downloaded the files, filter out the relevant NAICS codes. We did this in Excel, but you can do it in whatever data-wrangling tool you like best.
The data identifies states by FIPS code, so you'll need to convert it to a state name. You can do this using our lookup table (master_geo_lookup.csv). We did this in Google Fusion Tables, but you can do it in Access, MySQL, or whatever database tool you prefer.
(Link to the data dictionary)

#### Step 3: Download rig count data
Download the [file-name](link) from the Baker Hughes website.
Filter out state totals and the relevant years (2011 and 2012). Again, we did this in Excel, but you can use your favorite data-wrangling tool.

#### Step 4: Merge all the data together
We used Excel and pivot tables to aggregate and merge the data, but again, use your favorite data-wrangling tool. Once we had the data in one-spot, we:
* Added the 211, 212 and 213 NAICS code data (for employees, fatalities) together to get mining data

#### Step 5: Calculate a two-year average
For all the data types (fatality count, employees, fatalities), we compiled 2011 and 2012 data together to get a two-year average.

#### Step 6: Calculate fatality rates
We calculated fatality rates (deaths per 100,000 workers) for the entire mining industry and the oil and gas sub-industry. We also calculated rig-count fatality rates (deaths per 100 active rigs).

#### Step 7: Filter out states with small oil and gas industries
Because we are working with rates, very small numbers can throw off the analysis. So we included only states that had at least 5,000 oil and gas workers _and_ at least 10 active oil rigs in 2011 and 2012. This limited our analysis to 13 states (Arkansas, California, Colorado, Kansas, Louisiana, New Mexico, North Dakota, Oklahoma, Pennsylvania, Texas, Utah, West Virginia, Wyoming). We also did the same analysis nationally.

#### Step 8: 
Our final analysis is in State_Fatality_Rates_CALCULATED.csv, which has a table structure: 