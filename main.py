from matplotlib import pyplot as plt
from scipy.stats import linregress
import numpy as np
from sklearn import datasets
import pandas as pd
import boto3
from boto3 import session
import io
import logging
from botocore.exceptions import ClientError
from config import awskey
from config import secret
from config import bucketname

FileHospitalGeneralData="MedicareDataAnalysis/HospitalData/Hospital General Information.csv"
FileHosipitalSpendingStateData="MedicareDataAnalysis/HospitalData/Medicare Hospital Spending Per Patient - State.csv"
FilePhysicianData="MedicareDataAnalysis/HospitalData/Hospital General Information.csv"
FilePhysicianNationalData="MedicareDataAnalysis/PhysicianData/Physician_Compare_National_Downloadable_File.csv"
FilePhysicianGroupMIPSData="MedicareDataAnalysis/PhysicianData/Physician_Compare_2017_Group_Public_Reporting-Overall_MIPS_Performance.csv"
FilePhysicianIndivialMIPSData="MedicareDataAnalysis/PhysicianData/Physician_Compare_2017_Individual_EC_Public_Reporting_-_Overall_MIPS_Performance.csv"

class DataLoader():
	def LoadFile(file):
		s3 = boto3.client('s3',aws_access_key_id=awskey,aws_secret_access_key=secret)
		# Call S3 to list current buckets
		response = s3.list_buckets()
		Object_Read=s3.get_object(Bucket=bucketname,Key=file)
		output_data= pd.read_csv(Object_Read['Body'])
		return output_data