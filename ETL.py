import glob
import pandas as pd
from datetime import datetime

def extract_from_csv(file_to_process):
    df = pd.read_csv(file_to_process)
    return df

def extract_from_json(file_to_process):
    df = pd.read_json(file_to_process, orient = 'split')
    return df

def extract_from_excel(file_to_process):
    df = pd.read_excel(file_to_process)
    return df


##Implementation of the transform function
def transform(data):
    # Standardizing column names to lowercase
    data.columns = [col.lower() for col in data.columns]
    
    # Handling missing values by filling with 'Unknown'
    data.fillna('Unknown', inplace=True)
    
    # Converting date columns to datetime format
    if 'date' in data.columns:
        data['date'] = pd.to_datetime(data['date'], errors='coerce')
    
    return data
def load(target_file, data_to_load):
    data_to_load.to_csv(target_file, index=False)
def etl_process():
    extracted_data = pd.DataFrame()
    
    # Extract phase
    for csvfile in glob.glob("data/*.csv"):
        extracted_data = pd.concat([extracted_data, extract_from_csv(csvfile)], ignore_index=True)
    
    for jsonfile in glob.glob("data/*.json"):
        extracted_data = pd.concat([extracted_data, extract_from_json(jsonfile)], ignore_index=True)
    
    for excelfile in glob.glob("data/*.xlsx"):
        extracted_data = pd.concat([extracted_data, extract_from_excel(excelfile)], ignore_index=True)
    
    # Transform phase
    transformed_data = transform(extracted_data)
    
    # Load phase
    load("output/processed_data.csv", transformed_data)

if __name__ == "__main__":
    etl_process()

# End of ETL.py