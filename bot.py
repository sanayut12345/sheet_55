import gspread
import datetime

#timing
get_datetime = datetime.datetime.now()
date = get_datetime.date()
time = get_datetime.timetuple()
#google sheet
gc = gspread.service_account(filename='service.json')
sh = gc.open_by_key('1WKj5jeVEsa0TA-sv7j_sGlcbZRNUgJJfgpk92SRPpKA')
worksheet = sh.worksheet("Suser")
body = [5888,str(date),str(time)]
res = worksheet.get_all_records()
index = len(res)+2

worksheet.insert_row(body,index=index)