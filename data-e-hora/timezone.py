from datetime import datetime, timezone, timedelta

data_oslo = datetime.now(timezone(timedelta(hours=2), 'OSL'))
data_sp = datetime.now(timezone(timedelta(hours=-3), 'SP'))

print(data_oslo)
print(data_sp)