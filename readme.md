# **The American Ultimate Disc League**
The American Ultimate Disc League (AUDL) was created in 2013 to bring the sport of ultimate (created in XXXX) to the professional stage. The league originally started with X teams and has now grown to Y. Since the inaugural year, the league has collected data during their games on many key player and team attributes. This is a deep dive into the stats provided by the AUDL on their [website](https://theaudl.com/league/stats). The site provides All-time Player Stats, Single-season Team Stats, and Single-season Player Stats.

## ❔ Problem Statement
This analysis does not seek to solve one problem, but rather explore the data available to learn and answer questions about **players** such as:
- Do players naturally divide into groups such as *Goal Scorers* and *Assist Throwers*, or are players who score goals more just as likely or more likely to throw more assists as well?
- What is the relationship between games played, points played, and goals scored? Are these all linearly correlated?
- Do players with more blocks (likely defensive players) play more points?

... and questions about **teams** such as:
- What short-term improvements lead to the biggest improvements in wins?

## 🔢 Data

All-Time Player Stats helps look at the league in its entirety. Since its inaugural year, there have been over 2000 players that have played in the league. This data set can be used to establish baseline information on how your average player performs, how players break down in terms of stats, and if players can be grouped into sub-categories.

Single-Season Team Stats provides yearly data on performance. Information on wins, losses, points scored, and offensive and defensive efficiency, as well as other stats, are tracked by team. This data set can show what factors are most important to winning. This can help point to what players can do to be most effective on a team.

Single-season Player Stats provide slices in time for each player. With this data set, the progress of a player can be tracked and, when combined with other data sets, can be linked with the impact on team performance.

**Definitions** 
- **+ / - or 'plus/minus'** is calculated by ASSISTS + BLOCKS + GOALS - TURNOVERS = +/-

## 🔁 Process
Data Scraping > Data Cleansing > Exploratory Data Analysis (EDA) > Model Building > Model Production

## 📊 Results
