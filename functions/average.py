import numpy as np

def averageSpending(df):
    avg = np.round(np.mean(df[df['Order Status']!="Cancelled"]['Total Owed']),2)
    return avg

def monthly_spend(df):
    months=df.iloc[:,2].dt.month_name(locale="English")
    monthly_spending=df[df['Order Status']!="Cancelled"].groupby(months)['Total Owed'].mean()
    return monthly_spending
