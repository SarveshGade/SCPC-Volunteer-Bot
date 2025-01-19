# SCPC-Volunteer-Bot
Slackbot to parse volunteer sheets and send reminders to members about upcoming shifts!

## How does it work?
The user sends a slash command through slack (/remind, etc) and attaches the .csv file of the volunteer sheet. The bot will take that file, parse through the file, and collect the names of all volunteers. The bot will then send a DM to the volunteers, letting them know that their shift is soon.

## What API are we using?
Most probably Slack Bolt, but feel free to use any solution that works!

## What do we need to figure out?
We'll need to create a pipeline/sequence of events that allows for our entire request to go through. Uploading/reading files via slackbot seems to be a little more complicated than creating a normal chatbot, and there aren't too many YouTube tutorials that show how to implement this functionality, so we'll need to do some trial and error.

## How do we handle requests?
Most probably AWS Lambda, a serverless solution.
