# Election_Data_Project

This Python script analyzes election data to explore the relationship between the elector ratio (the ratio of registered electors to the total population) and voter turnout. It performs data cleaning, analysis, visualization, and saving result. The script is designed to identify regions with a high elector ratio and low voter turnout, which could indicate potential anomalies or areas of interest for further investigation.

# Key Functionalities:

Data Loading and Cleaning:
	The load_and_clean_data function reads data from a CSV file, and creates a new column called Elector Ratio (calculated as Electors / Population). It filters out invalid or missing data and creates a file called cleaned_data that only contains the data we are looking for.
 
Data Analysis:
	The analyze_high_ratio_low_turnout function identifies regions where the elector ratio exceeds a specified threshold (0.75) and voter turnout falls below a threshold (55%). This step filters out regions of interest for further exploration.
 
Data Visualization:
	The visualize_data function creates a scatter plot showing the relationship between elector ratio (x-axis) and voter turnout (y-axis). Regions meeting the high ratio and low turnout criteria are highlighted in red.
 
Save the Result to a new file:
	The save_results function saves the filtered data to a CSV file named high_ratio_low_turnout.csv.
