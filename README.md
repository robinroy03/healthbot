# HealthBot: Health Management System for VITC Health Centre

HealthBot is an application made to streamline the campus health centre operations and improve the quality of life of students.<br>
Our Submission for the Summer Solve-A-Thon Hackathon conducted at VITC.

## __Index__
- ### [Features](https://github.com/rorbinroy03/healthbot#features)
- ### [Screenshots](https://github.com/rorbinroy03/healthbot#screenshots)
- ### [TODO](https://github.com/robinroy03/healthbot#todo)
- ### [How To Run](https://github.com/robinroy03/healthbot#how-to-run)
- ### [Tech Stack](https://github.com/rorbinroy03/healthbot#tech-stack)
- ### [Team](https://github.com/rorbinroy03/healthbot#team)

## Features
There are 2 UIs for the application. One for the students and one for the health centre.
The students interact with a Telegram bot, whereas the health centre officials interact with a web dashboard.

Students' UI Features:
- Schedule doctor's appointment
- Call ambulance
- Schedule counsellor's appointment
- Get food delivered to room
- Notifications for appointments and prescriptions

Health Centre Dashboard Features:
- Manage appointments queue
- Enter prescriptions for patients
- Search patient logs for consultation history
- Monitor real-time statistics of current cases in campus and get a visual graph of the increasing frequency of cases day by day
- Appropriate notifications to authorities

## Screenshots
Appointments Queue
<img src="https://github.com/robinroy03/healthbot/assets/115863770/6cf0dc57-bd0b-4ab8-afdc-b400e2865e29" height="400">

Patient Logs Search
<img src="https://github.com/robinroy03/healthbot/assets/115863770/0ebd74e6-9b68-49c3-b8e8-2325addd3120" height="400">

Real-Time Statistics
<img src="https://github.com/robinroy03/healthbot/assets/115863770/5159ac1b-2617-4754-a1cd-341b534e53b7" height="400">

Telegram Student Interface
<img src="https://github.com/robinroy03/healthbot/assets/115863770/d7467443-8fad-454b-a70e-8257eae98c8f" height="400">

Telegram prescription notifications
<img src="https://github.com/robinroy03/healthbot/assets/115863770/d18cda64-f7ca-4a6f-894e-8a41177b8aca" height="400">

## TODO:
- [ ] Fix images on this README
- [ ] Clean the code. It was a quick hack, so the code is a bit messy. A lot of edge cases are not yet handled.
- [ ] Combine the two telegram bots into one. Having a separate bot for notifications is not necessary.
- [ ] Make a REST API for the dasboard to interact with instead of calling functions from the bot.py file directly.
- [ ] Set up unit tests.
- [ ] Use an actual ML model to predict outbreaks using data from the health centre.
- [ ] Deploy the app.

## How to run
__1) Create a mongoDB Atlas cluster, create a databse and get the connection URI__

__2) Create 2 telegram bots (One for patients UI and one for the notifications) and get the bot tokens__

__3) Clone the repo__
```bash
git clone https://github.com/robinroy03/healthbot.git
cd healthbot
```

__4) Create a virtual environment and install dependencies__
```bash
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

__5) Create a .env file in the root directory with the following variables__
```
ATLAS_URI = 
DB_NAME = 
BOT_TOKEN =
NOTIF_BOT_TOKEN = 
```

__6) Start the bot__
```bash
python3 bot.py
```

__7) Launch the dashboard__
```bash
streamlit run dashboard.py
```

__8) You are all set! You can now begin messaging the bot on telegram.__

## Tech Stack
- Frontend: Streamlit, Telegram API<br>
- Backend: MongoDB, Python<br>

## Team
- [Harish Chandran](https://github.com/HarishChandran3304)
- [Robin Roy](https://github.com/robinroy03)
    
Was an overall fun cook and the vibes were immaculate. Finished as 3rd runners up and were awarded a cash prize :)