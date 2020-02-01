import boto
import boto3
from boto3 import session
import io
import logging
from botocore.exceptions import ClientError
from config import awskey
from config import secret
from config import bucketname

FileHospitalGeneralData="MedicareDataAnalysis/HospitalData/Hospital General Information.csv"

class DataLoader():
	def LoadFile(file):
		s3 = boto3.client('s3',aws_access_key_id=awskey,aws_secret_access_key=secret)
		# Call S3 to list current buckets
		response = s3.list_buckets()
		Object_Read=s3.get_object(Bucket=bucketname,Key=file)
		output_data= pd.read_csv(Object_Read['Body'])
		return output_data

class DataLoader1():
	def LoadFile(file):
		s3 = boto3.client('s3',aws_access_key_id=awskey,aws_secret_access_key=secret)
		# Call S3 to list current buckets
		response = s3.list_buckets()
		#print (response)
		Object_Read=s3.get_object(Bucket=bucketname,Key=file)
		output_data= pd.read_csv(Object_Read['Body'])
		#return output_data
		print (output_data.head())