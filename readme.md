# **The American Ultimate Disc League**
The American Ultimate Disc League (AUDL) was created in 2012 to bring the sport of ultimate to the professional stage. The league originally started with 8 teams and has now grown to 25, spanning the US and Canada. Since the inaugural year, the league has collected data during their games on many key player and team attributes. This is a look into both player and team stats provided by the AUDL on their [website](https://theaudl.com/league/stats). The site provides All-time Player Stats, Single-season Team Stats, and Single-season Player Stats.

## ❔ Problem Statement
This analysis seeks to look at two separate problems:

1.  Does playing a game at home versus away give a team an advantage? If so, what kind of advantage and how much of an advantage?
- The "Home Court Advantage" is a well known phenomenon in team sports. When your friends and family are surrounding you, it can bolster teams to perform at a more peak level. In this project, I'll assess team performance in several categories, as well as player performance in several categories for a specific team (#CantStopWontStop) to see how playing at home versus away affects performance.

2. Can we effectively categorize players into sub-categories based on their player attributes?
- Within some player pages on the AUDL website, next to their team name players may have an on-field designation of 'Cutter', 'Handler', 'Defender', or 'Hybrid'. Of the ~2,700 players on the website, nearly 500 of these players have a designation. In this project, I'll test two separate classifiers (KNN and Decision Tree) in an attempt to determine if it's possible to properly classify players based on attributes such as goals, assists, points played, etc.

## 🔢 Data

Data was scraped from the AUDL website and saved to a series of CSV files. For Problem #1 (Home Field Advantage), I will use both team stats by season and player stats as a whole. For Problem #2 (Categorization), data was scraped from each player page. This data will be merged with each player's overall season stats for each season. One paired with these stats, the attributes will be normalized by points played to make sure players with the most playing time don't skew the data set.

For future work, it would be useful to identify players that have shifted roles across seasons. If a player changes from being primarily a Cutter in 2020, to primarily a Handler in 2021, they will likely be noted on the website as a Handler, but their 2020 stats may not reflect that.


## 📊 Results
