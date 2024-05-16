from alpha_vantage.timeseries import TimeSeries
import os
import time

ts = TimeSeries(key='01UB5FQT0GLC0G3T', output_format='pandas')

save_dir = 'data'

while True:
    data, meta_data = ts.get_intraday(symbol='MSFT', interval='1min', outputsize='full')
    
    current_time = time.strftime("%Y-%m-%d_%H-%M-%S")
    
    filename = os.path.join(save_dir, f'data_{current_time}.csv')
    
    data.to_csv(filename, index=False)
    
    print(f"Data saved to {filename}")

    os.system('dvc add data/'+filename+'.csv')
    os.system('dvc push')
    
    print("Data pushed to DVC")

    os.system('git add .')
    os.system('git commit -m "Updated dataset"')
    os.system('git push origin main')
    os.system('git status')
    
    time.sleep(60)
