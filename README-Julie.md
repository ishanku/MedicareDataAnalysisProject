# GroupProject-1
First Group project for Data Bootcamp, Gatech - by Roopa, Siva, Khusboo, Victor and Julie

The R-Pythons

# Project Title - Data analysis of Trends in Medicare system
# Team Members
  Julie John, Khushboo Shah, Roopa Reddy, Siva Thangaraj, Victor Ime
# Project Description

  The scope of our project is to analyze and find if there is any correlation between quality of healthcare (using MIPS and Hospital Rating by Medicare as basis of comparison) and various parameters.
# Research Questions to Answer
    o	Is there any Correlation between Hospital Ratings and the kind of ownership?
    o	Is there any trend in quality of Healthcare provided and its location(State)?
    o	Does age,experience,gender,medical school attended impact the quality of Healthcare?
    
# Datasets to be Used
     Multiple datasets from data.medicare.gov
# Rough Breakdown of the tasks
  1. Define the Goal and questions for the Project
  2. Collect the data – Pull the Json files, online datasets
  3. Clean and extract the necessary data based on requiremets
  4. Link,Merge and group the data from multiple datasets
  5. Use Python and its various modules to Analyze data
  6. Data visualization and graphs
  7. Interpret Results and Make observations
  8. Limitations of the Analysis and How it can be improved.
  9. Bonus!

# 1. Analysis on Physician MIPS Score parameters
## Retrieving the datasets from the source data.medicare.com

1.	Downloaded the following datasets -  
•	Physician_Compare_2017_Individual_EC_Public_Reporting_Overall_MIPS_Performance.csv
•	Physician Compare National Downloadable File.csv

2.	Uploaded the dataset on to the S3 bucket in the folder (/gt-data-analytics-2020/MedicareDataAnalysis/PhysicianData)

3.	On main.py, Import the required modules for establishing connection with AWS S3 bucket along with config file containing awskey and secret key. Created a class DataLoader and method LoadFile() that can download a file from S3 bucket and create a file handle object.

4.	Using the DataLoader.LoadFile() method imported(inherited) from main.py, created an object

                physiciangeneraldata=DataLoader.LoadFile(FilePhysicianNationalData)
                physicianMISPdata=DataLoader.LoadFile(FilePhysicianIndivialMIPSData)

## Cleaning of the dataset
1.	Considering the parameters used to measure the Physician’s general data , extracted the following columns into another dataset (clean_physiciangeneraldata) and columns renamed

        NPI
        Individual Pac ID
        Last Name
        First Name
        Gender
        Medical School
        Graduation Yr
        Primary Speciality
        Organization Name
        Organization Pac ID
        No. Org Memebers
        Address ln 1
        Address ln 2
        City
        State
        Zip
        Phone No


2.	Physician_Compare_2017_Individual_EC_Public_Reporting_Overall_MIPS_Performance.csv data was merged into the clean_physiciangeneraldata
        merge_physiciandata_MIPS = pd.merge(clean_physiciangeneraldata,physicianMISPdata, on="NPI", how ="inner")

3.	Redundant columns were dropped, and the final columns were renamed to match the data. 

4.	Dropped the rows with MIPS score of 0.

5.	Final clean dataset was saved as csv file (final_physician_data.csv) and uploaded to S3 for analysis

## Physician MIPS Score dataset

1.	Created another dataframe to get the dataset with unique NPIs

2.	Grouped the dataset by gender and calculated the average MIPS score for each gender.

        grouped_gender=unique_pnpi.groupby(['Gender'])
        avg_gendermips=grouped_gender["Final MIPS Score"].mean()

3.	Grouped the dataset by state and calculated the average MIPS score for each state, displaying the list from largest to smallest by average MIPS score.

        grouped_state=unique_pnpi.groupby(['State'])
        avg_statemips=grouped_state["Final MIPS Score"].mean()
        avg_statemips.nlargest(50)

## Plotting the summarized data

1.	Pie Plots displaying the distribution by gender
        [Pie Chart Gender Distribution](https://github.com/ishanku/MedicareDataAnalysisProject/blob/master/output/gender_dist_MIPS.png) 

2.	Stacked bar plots displaying the states by average MIPS score of Physicians.
        [MIPS Score State Compare](https://github.com/ishanku/MedicareDataAnalysisProject/blob/master/output/State_AvgMIPS.png)

3.	Bar plot displaying MIPS score by gender.
        [MIPS Score by gender](https://github.com/ishanku/MedicareDataAnalysisProject/blob/master/output/gender_AvgMIPS.png)
