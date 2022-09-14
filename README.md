# Tournament-Scheduler-Round-Robin
A round robin match scheduling application written in Python. After you specify team names, number of groups, venues, starting date, timeslots, and other parameters, the app will create a schedule of matches between teams in the same group and save it in excel files. Additionally it will also create an excel file exclusively for each team.

# Why use this?
- **Simple Interface**

If you want to create a schedule of matches for your tournament in round robin fashion (each team plays every other team once), this application will easily and efficiently do that for you by providing a simple GUI interface for setting up your tournament info.
- **Teams get break between matches**

An important feature of this scheduling software is you can specify the minimum break each team gets between consecutive matches. 

For example, if minimum break is 1 day, no team will play twice on the same day.

if minimum break is 2 days, no team will play twice in two days. 

- **Excel output**

After confirming your parameters, the schedule will be created and saved in excel files in just a few seconds.

---------------------
# Installation
- Clone/Download the repository.
- Make sure Python is installed. (Version 3.4 or above)
- Install openpyxl library for Python
```
pip install openpyxl
```
- Run the program "app.py" in Python
```
python app.py
```

---------------------
# How to use

![op1](https://user-images.githubusercontent.com/55421311/190156682-327c38e5-caf8-4c2a-bcc8-edb28ca348e5.png)

- **Enter teams**

Under the "Teams and Groups" tab, enter team names on separate lines. Specify the number of groups that the teams will be divided into. Make sure that the number of teams is divisble by the number of groups. For e.g. if you enter 20 team names and specify "number of groups" as 4, the 20 teams will be divided into 4 groups with 5 teams each. Within each group each team will play against every other team.

- **Add Venues** (Optional)

You can add venues under the "Venues" tab by clicking on "Add Venues". Add venue names in separate lines. By default the venues are not homegrounds. If you enable the "Venues are homegrounds" feature, the venue in the "Venues" tab will be the homeground of the corresponding team in "Teams and Groups" tab.

- **Add Dates** (Optional)

Enable dates by clicking on "Add Dates" under "Dates" tab. You can specify the date of the first match, number of matches on weekdays and number of matches on sundays.
If you have specified that there are more than one group in your set of teams then you will be prompted to choose between "Serial Group Matching" and "Parallel Group Matching". In the former each group plays on separate days, while in the latter each group plays on the same day everyday. 

Note:- If you select "Parallel Group Matching" and specify number of groups as 4 and number of matches per day as 2, then it will mean that 2 matches will be played within every single group, resulting in total 8 matches per day (since 4 groups x 2 matches = 8 matches per day)

- **Add Timeslots** (Optional, available only if Dates are enabled)

If "Dates" are enabled, you can add timeslots for weekdays and sundays under the "Timeslots" tab by clicking on "Add Timeslots".
Time format is [hh][mm][am/pm]. Set a time and add it using the "Add Timeslot" button. The required number of timeslots will be mentioned by the "Entries" value below the entry box.

- **Set the other parameters**

You can enable first match constraint i.e. specify two teams who play the first match.

You can specify number of rounds. The round robin scheduling will repeat for each round. For e.g. if "number of rounds" is 3, then each team will play 3 matches with every other team in the same group.

You can specify the minimum break. As explained in the "Why use this?" section above, this can be used to give break to every team between consecutive matches.
 
 ![op2](https://user-images.githubusercontent.com/55421311/190156733-fd329f84-1e0c-43be-9916-f5e5c62695c1.png)

- Once all parameters are set, click the "CREATE SCHEDULE" button. The schedule for all matches will be saved in an excel file "demo.xlsx" while matches for each group will be saved in separate sheets. 

![op3](https://user-images.githubusercontent.com/55421311/190158537-9c13d17b-e30f-4e63-9c2e-8e32402678a6.png)

- A separate excel file will be created for each team with their schedule

![op4](https://user-images.githubusercontent.com/55421311/190159460-a8922120-aba8-456b-a7ac-c5470d377e08.png)

 
