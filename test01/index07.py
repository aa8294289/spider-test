import tushare as ts
import datetime
tr=ts.get_hist_data('688010')
print(tr)
dateToday=datetime.datetime.today().strftime('%Y%m%d')
file='/Users/wangjian/Desktop/python file/TicketList01_'+dateToday+'.csv'
tr.to_csv(file)
print('Tickets saved. ')