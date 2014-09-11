import requests
import json
import prettytable
import csv

# This code uses a list of NAICS industry codes and a list of state-level geographics to generate series IDs for BLS CFOI data.
# It then retrieves data (for all available years) via the BLS API and stores that data in a CSV.


# These are the NAICS codes you will be retrieving data for. If you want other NAICS codes, modify this list.
NAICs_list = ['211XXX','212XXX','213XXX','213111','213112']


def create_data_list(mylist):    #read CSV file into a list
    with open(mylist, 'rU') as f:
        list_data = []
        reader = csv.reader(f)
        reader.next()
        for row in reader:
            list_data.append(row)
    for i in list_data:
        i[1] = i[1].translate(None, "\xca")
    #print list_data
    return list_data


def generateIDList(geo_list, NAICs):  # Generates the series IDs you want to query the BLS API for Census of Workplace Fatal Occupational Injuries
    ID_list = []
    for i in geo_list:
        for j in NAICs:            
            ID_list.append("FWU00X" + str(j) + "80" + str(i[3]))
    return ID_list

   

def getBLSdata(IDs_list, geo_IDs, file_name):    # Takes a list of series IDs and returns the data, for all available years, from the BLS API in comma-separated format
    headers = {'Content-type': 'application/json'}
    output_list = []
    out = csv.writer(open(file_name,"w"), delimiter=",",quoting=csv.QUOTE_ALL)
    for i in range(0,len(IDs_list)):
        data = json.dumps({"seriesid": [IDs_list[i]],"startyear":"2011", "endyear":"2014"}) 
        p = requests.post('http://api.bls.gov/publicAPI/v1/timeseries/data/', data=data, headers=headers) 
        json_data = json.loads(p.text) 
        for series in json_data['Results']['series']:
    #        x=prettytable.PrettyTable(["series id","year","period","value","footnotes"])
            seriesId = series['seriesID']
            NAICS = seriesId[6:12]
            #print NAICS
            for item in series['data']:
                year = item['year']
                period = item['period']
                value = item['value']
                footnotes=""
                geo = ""
                for i in geo_IDs:
                    #print seriesId[-3:]
                    #print i[0]
                    if seriesId[-3:] == i[3]:                       
                        geo = str(i[0])
                        #print geo
    
                # print seriesId + ", " + year + ", " + geo + ", " + value
                output_list.append(seriesId + ", " + NAICS + ", " + geo + ", " + year + ", " + value)
    #print output_list
    out.writerow(output_list)
    return output_list



#states_list = generateStatesList()
#IDList = generateIDList(states_list, NAICs_list)
#print IDList

#newIDs = generateID_list_new(states_list, NAICs_list)
#print newIDs

geo_IDs_list = create_data_list('master_geo_lookup.csv') #master_geo_lookup.csv is a file that contains state names, FIPS codes, postal abbreviations, and BLS location codes
#print geo_IDs_list

IDs = generateIDList(geo_IDs_list, NAICs_list)
#print IDs


#data_output = getBLSdata(IDs, geo_IDs_list, "BLS_output.csv")
#print data_output

getBLSdata(IDs, geo_IDs_list, "BLS_output_3.csv") #You can modify the file name
