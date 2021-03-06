# MedicareDataAnalysisProject
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

# 1. Analysis on Hospital ranking parameters

 ## Retrieving the dataset from the source data.medicare.com
    
   i. Downloaded the latest(2019) Hospital General Information.csv from data.medicare.gov
   
   ii. Uploaded the dataset on to the S3 bucket in the folder (/gt-data-analytics-2020/MedicareDataAnalysis/HospitalData)
   
   iii. On main.py, Import the required modules for establishing connection with AWS S3 bucket along with config file containing awskey and secret key. Created a class DataLoader and method LoadFile() that can download a file from S3 bucket and create a file handle object.
   
   iv. Using the DataLoader.LoadFile() method imported(inherited) from main.py, created an object
   
           hospitalgeneraldata=DataLoader.LoadFile(FileHospitalGeneralData)
           
   v. Considering the parameters used to measure the Hospital overall rating, extracted the following columns into another dataset
           
           1. Effectiveness of care national compare
           2. Timeliness of care national compare
           3. Efficient use of medical imaging national compare
           4. Patient experience national compare
           5. Readmission national compare
    
   ## Cleaning of the dataset:
   1. The columns in the consolidated dataset had "Not Available" values and the rows containing these values were deleted.
   2. Column names were shortened to exclude the string "national compare" which is redundant among all columns
       
   ## Hospital Overall Ratings dataset:
   1. Created another dataframe extracting the column "Hospital Overall Rating" from the file object. 
   2. Cleaned the dataset to exclude "Not available" values
   3. Extracted the count of number of hospitals under each Rank category using seriesRatings.str.count()
   4. Created a Ranking_df with the counts of each rank.
    
   - Extracted the count of number of hospitals scored for each of the five measure parameter under the below categories:
           
           1. Above the national average
           2. Below the national average
           3. Same as the national average
   
   - Create a 5x3 dataframe (Count_summary_df) with the count values under each category for all five parameters.
   
   ## Plotting the summarized data
   - Pie Plots displaying the summarized information on hospital rating parameters
   
        [Pie Chart Rating Measures](https://github.com/ishanku/MedicareDataAnalysisProject/blob/master/output/Pie-Charts-Percentage.png) 
  
   - Stacked bar plots displaying the number of hospitals categorized as above, below and same as national average.
           
       [Stacked bar plot of Hospital Ratings in 2019](https://github.com/ishanku/MedicareDataAnalysisProject/blob/master/output/Measures-National-Compare.png)  
          
   - Bar plot displaying under the number of hospitals ranked overall.
   
       [Hospital Overall Ratings in 2019](https://github.com/ishanku/MedicareDataAnalysisProject/blob/master/output/Hospital-Overall-Ranking.png)
             
       
# 2. Analysis on Hospital rating from 2016 to 2019

 ## Retrieving the dataset from the source data.medicare.com
    
   i. Downloaded the Hospital General Information.csv from data.medicare.gov archives of 2016, 2017, 2018 and 2019
   
   ii. Uploaded the datasets on to the S3 bucket in the folder (/gt-data-analytics-2020/MedicareDataAnalysis/HospitalData)
   
   iii. On main.py, Import the required modules for establishing connection with AWS S3 bucket along with config file containing awskey and secret key. Created a class DataLoader and method LoadFile() that can download a file from S3 bucket and create a file handle object.
   
   iv. Using the DataLoader.LoadFile() method imported(inherited) from main.py, created an object
   
           hg2019_df=DataLoader.LoadFile(FileHospitalGeneralData)
           hg2018_df=DataLoader.LoadFile(FileHG_2018)
           hg2017_df=DataLoader.LoadFile(FileHG_2017)
           hg2016_df=DataLoader.LoadFile(FileHG_2016)
           
   v. Considering the parameters used to measure the Hospital overall rating, extracted the following columns into another dataset
           
           1. Effectiveness of care national compare
           2. Timeliness of care national compare
           3. Efficient use of medical imaging national compare
           4. Patient experience national compare
           5. Readmission national compare
    
   ## Cleaning of the datasets:
   1. The columns in the consolidated dataset had "Not Available" values and the rows containing these values were deleted.
   2. Column names were shortened to exclude the string "national compare" which is redundant among all columns
       
   ## Hospital Overall Ratings datasets:
   1. Created dataframes extracting the column "Hospital Overall Rating" from each file object. 
   2. Cleaned the dataset to exclude "Not available" values
   3. Extracted the count of number of hospitals under each Rank category using seriesRatings.str.count()
   4. Created a Ranking_df with the counts of each rank for each year.
    
   - Extracted the count of number of hospitals scored for each of the five measure parameter under the below categories:
           
           1. Above the national average
           2. Below the national average
           3. Same as the national average
      
   ## Plotting the summarized data
   - Line graph displaying the trend in number of hospitals in each rank from 2016 to 2019
   
        [2016-2019 Hospitals Rating trends](https://github.com/ishanku/MedicareDataAnalysisProject/blob/master/output/2016-2019hospitalRatings.png) 
  
   - Stacked bar plots displaying the number of hospitals rated for their Effectiveness of care, Timeliness of care, Efficient use of medical imaging, Patient Experience and Readmission
           
       [Effectiveness of care](https://github.com/ishanku/MedicareDataAnalysisProject/blob/master/output/Effectiveness-of-care.png)
       
       [Timeliness of care](https://github.com/ishanku/MedicareDataAnalysisProject/blob/master/output/Timeliness-of-care.png)
       
       [Efficient use of Medical imaging](https://github.com/ishanku/MedicareDataAnalysisProject/blob/master/output/Efficient-use-of-medical-imaging.png)
       
       [Patient Experience](https://github.com/ishanku/MedicareDataAnalysisProject/blob/master/output/Patient-experience.png)
   
        [Readmission](https://github.com/ishanku/MedicareDataAnalysisProject/blob/master/output/Readmission.png)
        
# 3. Analysis on Physician MIPS Score parameters
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

# Analysis of physician data

 1.Downloaded the following dataset -
  • final_physician_data.csv
  
2. Read the final_pyhisician file that was already cleaned up
   finalphysician_file = "Output/final_physician_data.csv"
   final_physician = pd.read_csv(finalphysician_file)
   final_physician.head()
   
3. The columns on the file where identified writing a single line of code
   final_physician.columns
   
4. The physician's genders were grouped then put on a data frame to identify the total number of the Female Physician and
  the Male Physician
  physician_gender = final_physician.groupby(["Final MIPS Score","Gender"])
  physician_gender then called the number of the sex using the function. size() physician_gender_df =
  pd.DataFrame(physician_gender.size())
  
5. I used the function .count to get a clearer number of the gender
   physician_gender = pd.DataFrame(physician_gender_df.groupby(["Gender"]).count())
   
6. create and format to determine the percentage of female vs male
   physician_gender["Percentage of Sex"] = (100*(physician_gender["Final MIPS Score"]/physician_gender["Final MIPS
    Score"].sum()))
    
7. Then format the "Percentage of Sex" in the column using the line of code
   physician_gender["Percentage of Sex"] = physician_gender["Percentage of Sex"]
   
8. created a dataframe of the Gender and the percentage of each gender
   physician_gender
   
9. Draw a pie chart to  to illustrate numerical proportion of our Gender Analyse.
  colors = ['orange', 'blue']
  explode = (0.1, 0)
  plot = physician_gender.plot.pie(y='Final MIPS Score',figsize=(5,5),
                                 colors = colors, startangle=140, explode = explode,
                                 
# Physician Analysis based on Gender, Years of Experience and Primary Specialty

##  1.Access Dataset
       a.	Imported necessary modules to conduct the analysis
       b.	On main.py, Import the required modules for establishing connection with AWS S3 bucket along with config file containing awskey and secret key. Created a class DataLoader and method LoadFile() that can download a file from S3 bucket and create a file handle object.
       c.	Imported files pertaining to current Physician Medicare Data.
       
##  2.	Clean the Dataset
        Edit the Dataset based on required parameters to conduct the analysis.
        a.	Dropped columns not needed for analysis
        b.	Drop rows with NaN values.
        c.	Calculate data based on Unique physicians NPI’s.
        d.	Calculate Years of Experience based on Graduation Year (Assumption – Physicians started working immediately post graduation  and were employed throughout the period)
        
##  3.	Physician Analysis – Based on Years of Experience
        a.	Conducted an MIPs Score Analysis based on Years of Experience to figure out if there was any correlation between both the variables
        b.	Used Boxplot as Data Visualization tool to help the the relation.
        c.	Results:
        i.	As seen from the Boxplot the average MIPS score tends to be on the rise in the beginning years and is quite high from around 4th year onwards and stays that way for a significant amount of time.
       ii.	The mean MIPS score starts lowering a little with high years of experience maybe due to factors such as age.
The analysis is insufficient to draw any kind of significant conclusion regarding the relation between these two variables. More data such as age, other factors affecting the MIPS score.

## 4.	Physician Analysis – Based on Gender
      a.	Conducted an MIPs Score Analysis based on Gender to figure out if there was any correlation between both the variables
      b.	Used Boxplot as Data Visualization tool to help see the relation.
      c.	Conducted Independent Samples T-test to compare the means of both the Groups.
      i.	Null Hypothesis – There is no correlation between Gender and MIPS score
Alternate Hypothesis – There is significant relationship between Gender and MIPS score
With the T-test results -  statistic=22.41969156703278, pvalue=3.526868410040483e-111) it can be said that there is a correlation between Gender and MIPS score which can be explored further.

## 5.	Physician Analysis – Based on Speciality
      a.	Conducted an MIPs Score Analysis based on Speciality to figure out if there was any correlation between both the variables
      b.	Zeroed in on the three specialties which occurred the most.
      c.	Used Boxplot as Data Visualization tool to help see the relation.
      d.	Conducted Anova Test to compare the means of both the Groups.
      i.	Null Hypothesis – There is no correlation between Speciality and MIPS score
Alternate Hypothesis – There is significant relationship between Speciality and MIPS score
Based on the results we conducted further T-tests between the groups which further indicated a high correlation between the kind of speciality and the MIPS score. We thus reject the Null Hypothesis.
