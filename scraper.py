import selenium
import pandas as pd

# stats site and number of pages to scrape
# site = 'https://theaudl.com/stats/players-all-time?page='
site = 'https://theaudl.com/stats/player-stats?page='
num_pages = 77

# master dataframe
master = pd.DataFrame()

# iterate over pages
for i in range(num_pages):
    print(f"Appending Page #{i}")
    link = site + str(i)
    print(f'***\n{link}\n***')

    # get information from table and append to df
    df = pd.read_html(link)
    df = df[0]
    # print(f"\tdf size: {df.size}")
    
    #append to master
    master = master.append(df)
    master.reset_index(drop=True)

 #save to csv
master.to_csv('.\\DATA\\20220225_player_all_time.csv')