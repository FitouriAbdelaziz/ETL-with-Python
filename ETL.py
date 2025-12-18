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


