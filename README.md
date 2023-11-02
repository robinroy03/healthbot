# HealthBot: Health Management System for VITC Health Centre

HealthBot is an application made to streamline the campus health centre operations and improve the quality of life of students. 

__Index__
- [TODO](https://github.com/robinroy03/healthbot#todo)
- [How to run](https://github.com/robinroy03/healthbot#how-to-run)

The students interact with the application through the telegram interface, and the doctor can see it on a live dashboard given to them.
There are options for scheduling appointments with doctors & counsellors, viewing prescriptions and such on the student side.
In the health centre dashboard, there are features such as digitalized patient logs, and real-time monitoring of current symptoms/diseases around the campus to predict outbreaks.

Our live symptom-tracking feature provides a visual graph of the increasing frequency of cases day by day

HealthBot Queue Dashboard
<img src="https://github.com/robinroy03/healthbot/assets/115863770/6cf0dc57-bd0b-4ab8-afdc-b400e2865e29" height="400">

Real-Time Statistics
<img src="https://github.com/robinroy03/healthbot/assets/115863770/5159ac1b-2617-4754-a1cd-341b534e53b7" height="400">

Patient Logs Search
<img src="https://github.com/robinroy03/healthbot/assets/115863770/0ebd74e6-9b68-49c3-b8e8-2325addd3120" height="400">

Telegram Student Interface
<img src="https://github.com/robinroy03/healthbot/assets/115863770/d7467443-8fad-454b-a70e-8257eae98c8f" height="400">

Telegram notifications with prescriptions
<img src="https://github.com/robinroy03/healthbot/assets/115863770/d18cda64-f7ca-4a6f-894e-8a41177b8aca" height="400">

## TODO:

- [ ] Clean the rough edges. Since it was a quick hack, we didn't bother about a lot of edge cases. For example, the counsellor appointment could be spammed multiple times (but the doctor appointment couldn't be)
- [ ] Clean this readme.
- [ ] Reorganize this TODO list
- [ ] Use an actual ML model to predict outbreaks using data from the health centre.
- [ ] When everything else in this TODO list is done, do something about the UI. I'll say give the ML model the most priority.

## How to run

__.env file__
```
ATLAS_URI = 
DB_NAME = 
BOT_TOKEN =
NOTIF_BOT_TOKEN = 
```

__To start bot__
```
streamlit run dashboard.py
python3 bot.py
```

Was a fun cook with [Harizz](https://github.com/HarishChandran3304) for VITC Solve-A-Thon Hackathon. We came 4th and were awarded with a cash prize :) 
