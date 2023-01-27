from datetime import datetime, timezone , timedelta
import pytz, os
import pandas as pd

def utc_to_local(utc_dt):
    local = pytz.timezone("Asia/Kolkata")
    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=local)
 

def build_data(csv_path):
    csv = pd.read_csv(csv_path)
    time_data = []
    for utc_time in csv['time_non_dst']:
        local_iso_time = utc_to_local(datetime.strptime(utc_time, "%H:%M:%S%z"))
        utc_p2_time = datetime.strptime(utc_time, "%H:%M:%S%z") + timedelta(hours=2)
        utc_n2_time = datetime.strptime(utc_time, "%H:%M:%S%z") + timedelta(hours=-2)
        local_time = local_iso_time.time() 
        utc_offset =  local_iso_time.utcoffset()
        time_dict =  {
            'time_non_dst' : utc_time,
            'IST_time' : f'{local_time}+{utc_offset}',
            'UTC+02:00_time' : f'{utc_p2_time.time()}+02:00',
            'UTC-02:00_time' : f'{utc_n2_time.time()}-02:00'
        }
        time_data.append(time_dict)
    return time_data

def build_csv_using_pandas(data):
    df=pd.DataFrame(data)
    df.to_csv(f'{os.getcwd()}/Date-time-Convertion/Time_convertion-output.csv', index=False) 

if __name__ == '__main__':
    csv_path = f'{os.getcwd()}/Date-time-Convertion/time_non_dst.csv'
    data = build_data(csv_path)
    build_csv_using_pandas(data)