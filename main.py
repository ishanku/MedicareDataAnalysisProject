from matplotlib import pyplot as plt
from scipy.stats import linregress
import numpy as np
from sklearn import datasets
import pandas as pd
import boto3
import json
from pandas.io.json import json_normalize
import requests
from boto3 import session
import io
import logging
from botocore.exceptions import ClientError
from config import awskey
from config import secret
from config import bucketname
from config import googlekey

FileHospitalGeneralData="MedicareDataAnalysis/HospitalData/Hospital General Information.csv"
FileHosipitalSpendingStateData="MedicareDataAnalysis/HospitalData/Medicare Hospital Spending Per Patient - State.csv"
FilePhysicianData="MedicareDataAnalysis/HospitalData/Hospital General Information.csv"
FilePhysicianNationalData="MedicareDataAnalysis/PhysicianData/Physician_Compare_National_Downloadable_File.csv"
FilePhysicianGroupMIPSData="MedicareDataAnalysis/PhysicianData/Physician_Compare_2017_Group_Public_Reporting-Overall_MIPS_Performance.csv"
FilePhysicianIndivialMIPSData="MedicareDataAnalysis/PhysicianData/Physician_Compare_2017_Individual_EC_Public_Reporting_-_Overall_MIPS_Performance.csv"

OutputFilePhysicianData="MedicareDataAnalysis/Output/final_physician_data.csv"

class DataLoader():
	def LoadFile(file):
		s3 = boto3.client('s3',aws_access_key_id=awskey,aws_secret_access_key=secret)
		# Call S3 to list current buckets
		response = s3.list_buckets()
		Object_Read=s3.get_object(Bucket=bucketname,Key=file)
		output_data= pd.read_csv(Object_Read['Body'])
		return output_data

class DataHandler():
    def HospitalDataStarFilter(StarScore):
        if (StarScore<=5):
            Hospital_Data=pd.DataFrame(DataLoader.LoadFile(FileHospitalGeneralData))
            Lat =[]
            Lng =[]
            #print(len(Hospital_Data))
            HospitalStarsRated=Hospital_Data.loc[Hospital_Data["Hospital overall rating"] == str(StarScore)]
            #print(len(HospitalStarsRated))
            HospitalStarsRated=HospitalStarsRated[["Facility Name","Address","City","State","Hospital Ownership"]]
            HospitalStarsRated=HospitalStarsRated.dropna(how="any")
            #print(len(HospitalStarsRated))
            for index,Hospital in HospitalStarsRated.iterrows():
                #print(googleapi.getLatLon(Hospital["Address"]))
                if googleapi.getLatLon(Hospital["Address"])[0] == "Nan":
                    Lat.append(None)
                    Lng.append(None)
                else:
                    Lat.append(googleapi.getLatLon(Hospital["Address"])[0])
                    Lng.append(googleapi.getLatLon(Hospital["Address"])[1])
            HospitalStarsRated["Lat"]=Lat
            HospitalStarsRated["Lng"]=Lng
            HospitalStarsRated=HospitalStarsRated.dropna(how="any")
            #print(len(HospitalStarsRated))
        return HospitalStarsRated

class googleapi():
    def getLatLon(Address):
        loc =[]
        #Send request and receive json data by address
        target_url = ('https://maps.googleapis.com/maps/api/geocode/json?''address={0}&key={1}').format(Address, googlekey)
        geo_data = requests.get(target_url).json()
        if geo_data["status"] == 'OK':
            #lat = geo_data["results"][0]["geometry"]["location"]["lat"]
            #lng = geo_data["results"][0]["geometry"]["location"]["lng"]
            loc.append(geo_data["results"][0]["geometry"]["location"]["lat"])
            loc.append(geo_data["results"][0]["geometry"]["location"]["lng"])
        else:
            loc.append("NaN")
            loc.append("NaN")
        return loc

class npiapi():
    def GetAddress(SingleDF):
        npi=SingleDF["NPI"]
        url=f"https://npiregistry.cms.hhs.gov/api/?version=2.0&number={npi}"
        #print(url)
        response=requests.get(url).text
        response=json.loads(response)
        result=json_normalize(response["results"])
        getAddress=pd.DataFrame(json_normalize(result["addresses"][0]))
        getAddress=getAddress.loc[getAddress["address_purpose"]=='LOCATION']
        OutDF = pd.DataFrame({"NPI" : npi , 
                              "First Name" : SingleDF["First Name"],
                              "Last Name" : SingleDF["Last Name"],
                              "Address": getAddress["address_1"],
                             "City":getAddress["city"],
                             "State": getAddress["state"],
                              "PostalCode" : getAddress["postal_code"],
                              "Phone" : getAddress["telephone_number"]
                             })
        return OutDF