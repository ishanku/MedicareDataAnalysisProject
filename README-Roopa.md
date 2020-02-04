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
   - Pie Plots displaying the summarized information on hospital ranking parameters
   
           <Pie Plot image>
           
   - Stacked bar plots displaying the number of hospitals categorized as above, below and same as national average.
           
           <Stacked Bar plot>
          
   - Bar plot displaying under the number of hospitals ranked overall.
   
           <Ranking Bar plot>

