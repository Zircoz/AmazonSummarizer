import datetime as dt
import calendar as cl

def addYearMonthHour(df, sourceColName):
    """
    addOrderYearMonthHour
        Add 3 new columns to df from source column name
        returns a dataframe
        sourceColName needs to be of date time type
    """
    
    df["Order Month"] = df[sourceColName].dt.month
    df["Order Hour"] = df[sourceColName].dt.hour
    df["Order Year"] = df[sourceColName].dt.year
    return df

def hourly_spend(df):
    '''
    shows at average spending during each hour of day
    '''
    
    hourly_spending=df[df['Order Status']!="Cancelled"].groupby(df['Order Hour'])['Total Owed'].mean().round(2)
    return hourly_spending

def monthly_spend(df):
    '''
    shows at average spending during each month of year
    '''
    
    monthly_spending=df[df['Order Status']!="Cancelled"].groupby(df['Order Month'])['Total Owed'].mean().round(2)
    return monthly_spending

def yearly_spend(df):
    '''
    shows at average spending during each year of usage
    '''
    
    yearly_spending=df[df['Order Status']!="Cancelled"].groupby(df['Order Year'])['Total Owed'].mean().round(2)
    return yearly_spending

