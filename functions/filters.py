import datetime as dt
import calendar as cl
def addMonth(df):
    months=df.iloc[:,2].dt.month_name(locale="English")
    df['month']=months

def addTime(df):
    '''
    diveds the purchases by tme of day{morning,afternoon,evening,night}
    '''
    time=df.iloc[:,2].dt.hour
    times= {(4,5,6,7,8,9,10,11,12): 1, (13,14,15,16): 2, (17,18,19,20): 3, (21,22,23,24,1,2,3): 4}
    time_name={
        1:"morning",
        2:"afternoon",
        3:"evening",
        4:"night"
    }
    def tm(ser):
        for k in times.keys():
            if ser in k:
                return time_name[times[k]]
    df['time']=time.apply(tm)

def addSeason(df):
    '''
    diveds the purchases by season
    '''
    month_no=df.iloc[:,2].dt.month
    seasons = {(1, 12, 2): 1, (3, 4, 5): 2, (6, 7, 8): 3, (9, 10, 11): 4}
    season_name={
        1:"winter",
        2:"summer",
        3:"rainy",
        4:"autumn"
    }
    def season(ser):
        for k in seasons.keys():
            if ser in k:
                return season_name[seasons[k]]

    df['season'] = month_no.apply(season)


def timely_spend(df):
    '''
    shows at average spending during each time of day
    '''
    timely_spending=df[df['Order Status']!="Cancelled"].groupby(df['time'])['Total Owed'].mean()
    return timely_spending

def seasonly_spend(df):
    '''
    shows at average spending during each season of year
    '''
    seasonly_spending=df[df['Order Status']!="Cancelled"].groupby(df['season'])['Total Owed'].mean()
    return seasonly_spending

