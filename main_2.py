import boto
import boto3
from boto3 import session
import io
import logging
import pandas as pd
from botocore.exceptions import ClientError
from config import awskey
from config import secret
from config import bucketname

FileHospitalGeneralData="MedicareDataAnalysis/HospitalData/Hospital General Information.csv"
FilePhysicianGroupReportingMIPSPerformance="MedicareDataAnalysis/PhysicianData/Physician_Compare_2017_Group_Public_Reporting-Overall_MIPS_Performance.csv"
FilePhysicianIndivReportingMIPSPerformance="MedicareDataAnalysis/PhysicianData/Physician_Compare_2017_Individual_EC_Public_Reporting_-_Overall_MIPS_Performance.csv"
FilePhysicianCompare="MedicareDataAnalysis/PhysicianData/Physician_Compare_National_Downloadable_File.csv"


class DataLoader():
	def LoadFile(file):
		s3 = boto3.client('s3',aws_access_key_id=awskey,aws_secret_access_key=secret)
		# Call S3 to list current buckets
		response = s3.list_buckets()
		#print (response)
		Object_Read=s3.get_object(Bucket=bucketname,Key=file)
		output_data= pd.read_csv(Object_Read['Body'])
		#return output_data
		print (output_data.head())

#DataLoader.LoadFile(FileHospitalGeneralData)
#DataLoader.LoadFile(FilePhysicianGroupReportingMIPSPerformance)
#DataLoader.LoadFile(FilePhysicianIndivReportingMIPSPerformance)
#DataLoader.LoadFile(FilePhysicianCompare)

class SimpleAdd():
	def __init__(self,a,b):
		self.firstNumb = a
		self.secNumb = b
		self.sum = a + b
	def get_sum(self):
		return self.sum	

