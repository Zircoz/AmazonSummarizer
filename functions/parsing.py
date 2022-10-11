import pandas as pd

def parseRetailOrderHistDtypes(df):
    
    #If not float, split by comma and convert to float
    df["Unit Price"] = df["Unit Price"].map(lambda x: float("".join(x.split(",")) if type(x)!=float else x ))
    df["Unit Price Tax"] = df["Unit Price Tax"].map(lambda x: float("".join(x.split(",")) if type(x)!=float else x ))
    df["Shipping Charge"] = df["Shipping Charge"].map(lambda x: float("".join(x.split(",")) if type(x)!=float else x ))
    df["Total Owed"] = df["Total Owed"].map(lambda x: float("".join(x.split(","))) if type(x)!=float else float(x))
    
    #strip '' from discounts then conversion as above
    df["Total Discounts"] = df["Total Discounts"].map(lambda x: float("".join(x.strip("'").split(","))) if "-" in x else float(x))
    
    #fill numpy's na with "0" then conversion as above
    df["Shipment Item Subtotal"] = df["Shipment Item Subtotal"].fillna("0").map(lambda x: float("".join(x.split(","))) if type(x)!=float else float(x))
    df["Shipment Item Subtotal Tax"] = df["Shipment Item Subtotal Tax"].fillna("0").map(lambda x: float("".join(x.split(","))) if type(x)!=float else float(x))
    
    #fill na with epoch and convert to datetime dtype
    df["Ship Date"] = pd.to_datetime(df["Ship Date"].fillna("01/01/1970 00:00:00 UTC"))
    df["Order Date"] = pd.to_datetime(df["Order Date"].fillna("01/01/1970 00:00:00 UTC"))
    
    return df