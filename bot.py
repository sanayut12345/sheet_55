import gspread

gc = gspread.service_account(filename='service.json')
sh = gc.open_by_key('1WKj5jeVEsa0TA-sv7j_sGlcbZRNUgJJfgpk92SRPpKA')
worksheet = sh.worksheet("student")

res = worksheet.get_all_records()

print(res)