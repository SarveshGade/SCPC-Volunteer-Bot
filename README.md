# SCPC-Volunteer-Bot
Slackbot to parse volunteer sheets and send reminders to members about upcoming shifts!

## How does it work?
The user sends a slash command through slack (/remind, etc) and attaches the .csv file of the volunteer sheet. The bot will take that file, parse through the file, and collect the names of all volunteers. The bot will then send a DM to the volunteers, letting them know that their shift is soon.

## How do we handle requests?
Most probably AWS Lambda, a serverless solution.
