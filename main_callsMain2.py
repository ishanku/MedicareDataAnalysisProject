from main_2 import DataLoader
from main_2 import SimpleAdd


FileHospitalGeneralData="MedicareDataAnalysis/HospitalData/Hospital General Information.csv"
FilePhysicianGroupReportingMIPSPerformance="MedicareDataAnalysis/PhysicianData/Physician_Compare_2017_Group_Public_Reporting-Overall_MIPS_Performance.csv"
FilePhysicianIndivReportingMIPSPerformance="MedicareDataAnalysis/PhysicianData/Physician_Compare_2017_Individual_EC_Public_Reporting_-_Overall_MIPS_Performance.csv"
FilePhysicianCompare="MedicareDataAnalysis/PhysicianData/Physician_Compare_National_Downloadable_File.csv"

DataLoader.LoadFile(FileHospitalGeneralData)
DataLoader.LoadFile(FilePhysicianGroupReportingMIPSPerformance)
DataLoader.LoadFile(FilePhysicianIndivReportingMIPSPerformance)
#DataLoader.LoadFile(FilePhysicianCompare)


f = SimpleAdd(5,2)
print("Results of the numbers: ", f.firstNumb, f.secNumb,"is: ", f.sum)
# Using getattr method to return the attributes
print ("getattr of get_sum", getattr(f, "get_sum")())
print ("getattr of get_firstNumb and secNumb", getattr(f, "firstNumb"), getattr(f, "secNumb"))
