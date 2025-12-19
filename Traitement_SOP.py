import pandas as pd

sop = pd.read_excel("SOP Prévisionnel - 2026.xlsx","Prev S&OP 2026")

sop = pd.melt(sop,id_vars = ["Marque","Modèle","Typologie"]).rename(columns={'variable' : 'Date' , 'value' : 'Quantité'})

# print(sop.head())

# sop["Date"] = sop["Date"].astype("date32[pyarrow]")
sop = sop.fillna(0)
# sop["Quantité"] = sop["Quantité"].replace("NaN",0)



sop["Quantité"] = sop["Quantité"].astype(int)

sop["Date"] = pd.to_datetime(sop["Date"])

# print(sop.head(50))

sop.to_excel("SOP Prévisionnel - 2026 - Unpivoted.xlsx")




# import sys

# print(sys.executable)
# print(sys.version)
# print(sys.path)

#I HAVEN'T BEEN ABLE TO INSTALL ANY PACKAGES FROM THE WORK COMPUTER
#I HAVE TO DO THIS FROM THE HOME COMPUTER

##UPDATE
##WAS ABLE TO ADD THE PACKAGES, IT WAS A PROBLEM RELATED WITH THE DAMN NETWORK SPEED, OR IN THIS CASE, LACK OF IT