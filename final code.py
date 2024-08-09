import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset from the specified path
file_path = r"D:\vidit\prodigy infotech internship\task 1\world_demographics.csv"
df = pd.read_csv(file_path)

# Handle missing data by dropping rows with any missing values in key columns
df.dropna(subset=['Country or Area', 'Year', 'Age', 'Value'], inplace=True)

# Convert 'Year' to integer if it's not already, to avoid any type issues
df['Year'] = df['Year'].astype(int)

# Check the unique values for 'Country or Area' and 'Year'
available_countries = df['Country or Area'].unique()
available_years = df['Year'].unique()

# Specify the country and year you want to analyze
country = 'India'  # Example country; modify as needed
year = 2011  # Example year; modify as needed

# Validate the inputs and select a valid country and year if the specified ones don't exist
if country not in available_countries or year not in available_years:
    print(f"Specified country '{country}' and/or year '{year}' not found in the dataset.")
    # Automatically select the first available country and year
    country = available_countries[0]
    year = available_years[0]
    print(f"Defaulting to the first available country '{country}' and year '{year}'.")

# Filter the dataset for the selected country and year
filtered_df = df[(df['Country or Area'] == country) & (df['Year'] == year)]

# Check if the filtered DataFrame is empty
if filtered_df.empty:
    print(f"No data found for {country} in {year}. Please check the inputs.")
else:
    # Create a unique color palette based on the number of unique ages
    unique_ages = filtered_df['Age'].nunique()
    palette = sns.color_palette("viridis", n_colors=unique_ages)

    # Plotting the age distribution as a bar chart
    plt.figure(figsize=(14, 8))
    sns.barplot(x='Age', y='Value', data=filtered_df, palette=palette)

    # Customize the plot
    plt.title(f'Population Distribution by Age in {country} ({year})', fontsize=20, weight='bold')
    plt.xlabel('Age', fontsize=14)
    plt.ylabel('Population', fontsize=14)
    
    # Set x-ticks to show every 5th age to reduce clutter
    plt.xticks(ticks=range(0, len(filtered_df['Age']), 5), rotation=45, fontsize=12)
    
    # Reduce grid line visibility
    plt.grid(True, linestyle='--', alpha=0.3)

    # Show the plot
    plt.tight_layout()
    plt.show()
