import pandas as pd
import matplotlib.pyplot as plt


# Function: Load and clean data from the CSV file
def load_and_clean_data(file_path):
    """
    Load data and clean it:
    - Create a new column 'Elector Ratio' (Electors / Population).
    - Drop rows with missing or invalid 'Elector Ratio'.
    - Save a cleaned and simplified version of the data to 'cleaned_data.csv'.
    """
    data = pd.read_csv(file_path)
    # Data cleaning
    data = data[data['Population'] > 0] 
    data['Elector Ratio'] = data['Electors'] / data['Population'].replace(0, pd.NA)  
    data.dropna(subset=['Elector Ratio'])
    cleaned_data = data[['Province', 'Electoral District Name', 'Elector Ratio', 'Percentage of Voter Turnout']]
    cleaned_data.to_csv('cleaned_data.csv') 
    return cleaned_data


# Function: Analyze and filter data based
def analyze_high_ratio_low_turnout(data):
    """
    Identify regions where the Elector Ratio exceeds the specified threshold and Voter Turnout is below the specified threshold.
    Returns the filtered data and prints the summary.
    """
    # standard 
    elector_ratio_threshold=0.75
    voter_turnout_threshold=55
    filtered_data = data[
        (data['Elector Ratio'] > elector_ratio_threshold) & 
        (data['Percentage of Voter Turnout'] < voter_turnout_threshold)
    ]
    return filtered_data

# Function: Visualize data and highlight specific regions
def visualize_data(data, filtered_data):
    """
    Create a scatter plot to visualize the relationship between:
    - Elector Ratio (x-axis) and Voter Turnout (y-axis).
    Highlight the filtered regions in red.
    """

    # Plot all data points
    plt.scatter(data['Elector Ratio'], data['Percentage of Voter Turnout'], label=f'Total: {len(data)}')
    # Highlight filtered data points
    plt.scatter(filtered_data['Elector Ratio'], 
                filtered_data['Percentage of Voter Turnout'], 
                color='red', label='High Ratio & Low Turnout')


    # Add titles and labels
    plt.title('Relationship Between Elector Ratio and Voter Turnout', fontsize=16)
    plt.xlabel('Elector Ratio (Electors / Population)', fontsize=12)
    plt.ylabel('Voter Turnout (%)', fontsize=12)
    plt.grid()
    plt.show()

# Function: Save the filtered results to a CSV file
def save_results(filtered_data):
    output_path = f'high_ratio_low_turnout.csv'
    filtered_data.to_csv(output_path, index=False)
    print(f"Results saved to {output_path}")


# Main function: Orchestrates the steps of the analysis
def main():
    """
    Main entry point of the script:
    - Load and clean the data.
    - Analyze and filter the data for specific regions.
    - Visualize the relationship and highlight filtered regions.
    - Save the filtered data to a CSV file.
    """
    file_path = 'election_data.csv'
    data = load_and_clean_data(file_path)  
    filtered_data = analyze_high_ratio_low_turnout(data)  
    visualize_data(data, filtered_data)  
    save_results(filtered_data)   

# Script execution starts here
if __name__ == "__main__":
    main()
