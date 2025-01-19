import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


### Read in data

noteevents_path = "../data/raw/NOTEEVENTS.csv.gz"
diagnoses_path = "../data/raw/DIAGNOSES_ICD.csv.gz"

noteevents_df = pd.read_csv(noteevents_path, compression="gzip", low_memory=False)
diagnoses_df = pd.read_csv(diagnoses_path, compression="gzip", low_memory=False)


### Extract discharge summaries

discharge_summaries = noteevents_df[noteevents_df.CATEGORY == "Discharge summary"]

### Assigning ICD-9 Codes

grouped_icd = diagnoses_df.groupby("HADM_ID")["ICD9_CODE"].apply(list).reset_index()
labled_data = discharge_summaries.merge(grouped_icd, on="HADM_ID", how="inner")
