import selenium
import pandas as pd

# stats site and number of pages to scrape
site = 'https://theaudl.com/stats/players-all-time?page='
num_pages = 77

# master dataframe
master = pd.DataFrame()

# iterate over pages
for i in range(num_pages):
    print(f"Appending Page #{i}")
    link = site + str(i)

    # get information from table and append to df
    df = pd.read_html(link)
    df = df[0]
    print(f"\tdf size: {df.size}")
    
    #append to master
    master = master.append(df)
    master.reset_index(drop=True)
    print(f"\tmaster size: {master.shape}")
    
master.to_csv('player_all_time.csv')