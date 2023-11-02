<br/>
<p align="center">
  <h3 align="center">HealthBot 🏥</h3>

  <p align="center">
    Health Management System for the VITC Health Centre
    <br/>
    Automated Queue | Digitalized Prescriptions | Real-time Statistics
    <br/>
    <br/>
  </p>
</p>

![Contributors](https://img.shields.io/github/contributors/robinroy03/HealthBot?color=dark-green) ![Forks](https://img.shields.io/github/forks/robinroy03/HealthBot?style=social) ![Stargazers](https://img.shields.io/github/stars/robinroy03/HealthBot?style=social) ![Issues](https://img.shields.io/github/issues/robinroy03/HealthBot) 

## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Showcase](#showcase)
* [Roadmap](#roadmap)
* [Authors](#authors)

## About The Project

HealthBot is an application made to streamline the campus health centre operations and improve the quality of life of students. This was our Submission for the Summer Solve-A-Thon Hackathon conducted at VITC.

Features:
- Automated queue for appointments to reduce crowding and save time
- Digitalized prescriptions to reduce paper wastage and make it easier to search for past prescriptions
- Real-time statistics of current cases in campus and visual graph of the increasing frequency of cases day by day to predict and prevent outbreaks


There are 2 UIs to this application. One for the students and one for the health centre.
The students interact with a Telegram bot, whereas the health centre officials interact with a web dashboard.

Students' UI:
- Schedule doctor's appointment
- Call ambulance
- Schedule counsellor's appointment
- Get food delivered to room
- Notifications for appointments and prescriptions

Health Centre Dashboard:
- Manage appointments queue
- Enter prescriptions for patients
- Search patient logs for consultation history
- Monitor real-time statistics of current cases in campus and get a visual graph of the increasing frequency of cases day by day
- Appropriate notifications to authorities

## Built With

- [Python](https://www.python.org/)
- [MongoDB](https://www.mongodb.com/atlas/database)
- [PyMongo](https://pymongo.readthedocs.io/en/stable/)
- [pyTelegramBotAPI](https://pytba.readthedocs.io/en/latest/index.html)
- [Streamlit](https://streamlit.io/)

## Getting Started

To get the project up and running locally on your machine, follow these simple steps:

### Prerequisites

1) Create a database on [MongoDB](https://www.mongodb.com/atlas/database) and obtain the connection URI.
2) Create 2 telegram bots (One for student UI and one for notifications) using [BotFather](https://telegram.me/BotFather) and obtain their API tokens.

### Installation

3) Clone the repo
```bash
git clone https://github.com/robinroy03/healthbot.git
cd healthbot
```

4) Create a virtual environment and install dependencies
```bash
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

5) Create a .env file in the root directory with the following variables
```
ATLAS_URI = <your-MongoDB-connection-URI>
DB_NAME = <your-database-name>
BOT_TOKEN = <api-token-for-your-student-ui-bot>
NOTIF_BOT_TOKEN = <your-api-token-for-your-notifications-bot>
```

6) Start the bot
```bash
python3 bot.py
```

7) Launch the dashboard
```bash
streamlit run dashboard.py
```

8) You are all set! You can now begin messaging the bot on telegram.

## Showcase

![Image](https://media.discordapp.net/attachments/885781619519127573/1169723636446396426/image.png?ex=65567107&is=6543fc07&hm=615baf1e29fcc31e55f12b1651622a832f3b250536f7cc35d9dc0a075ce172f3&=&width=1200&height=557)
<sub>Health Centre Queue</sub>

![Image](https://cdn.discordapp.com/attachments/885781619519127573/1169724136726216827/image.png?ex=6556717e&is=6543fc7e&hm=c8abd4543fdf3516c01b74de92fd10ae85b90265bd5504e015e6701c4aa61864&)
<sub>Patient's Medical History Search</sub>

![Image](https://cdn.discordapp.com/attachments/885781619519127573/1169724276727885994/image.png?ex=6556719f&is=6543fc9f&hm=9f9b2cb06376a7cca590a61df2b1c1ed337cce63b4faa9b152accb8f596eeec6&)
<sub>Real-time Statistics</sub>

## Roadmap

- [ ] Get a logo
- [ ] Add contributing instructions, CONTRIBUTING.md and CODE_OF_CONDUCT.md
- [ ] Clean the code. It was a quick hack, so the code is a bit messy. A lot of edge cases are not yet handled.
- [ ] Combine the two telegram bots into one. Having a separate bot for notifications is not necessary.
- [ ] Make REST API endpoints for the dashboard to interact with instead of calling functions from db.py directly.
- [ ] Set up unit tests.
- [ ] Use an actual ML model to predict outbreaks using data from the health centre.
- [ ] Move to a better frontend framework (possibly [Reflex](https://reflex.dev)?)
- [ ] Deploy the app.

## Authors

- [Harish Chandran](https://github.com/HarishChandran3304)
- [Robin Roy](https://github.com/robinroy03)  
  
Was an overall fun cook and the vibes were immaculate! Finished as 3rd runners up and were awarded a cash prize :)