# G-Calisher
## What?
This program will connect to Google's API using an access token and inject a calendar event into a target's calendar.
## Who?
Author: Antonio Piazza (@antman1p)
This is a python version of the powershell Mailsniper module Invoke-InjectGEventAPI
(https://github.com/dafthack/MailSniper/blob/master/MailSniper.ps1) written by BlackHills Security's 
Beau Bullock (@dafthack) & Michael Felch (@ustayready), with **added functionality**.
## Why?
Because I'm a MacOS hacker and not everything is effing windows!  Also, Google STILL, since October 2018 has NOT FIXED 
THEIR SH**!
## How?
Original instructions on how to get a Google Calendar API key from 
https://www.blackhillsinfosec.com/google-calendar-event-injection-mailsniper/  
Updated instructions to follow.  
  
```
usage: gcalisher.py [-h] -e <ATTACKER EMAIL> -x <TARGETS> [TARGETS, ...]   
	-a <ACCESS TOKEN> -s <START DATETIME> -f <FINISH DATETIME>  
	[-t <EVENT TITLE>] [-l <EVENT LOCATION>]   
	[-d <EVENT DESCRIPTION>] [-z <TIME ZONE> (default = America/Chicago)]   
	[-m <ALLOW MODIFY>] [-i <ALLOW INVITE OTHERS> [{true, false}] (default = true)]   
	[-o <SHOW INVITEES> [{true, false}] (default = false)]   
	[-r <RESPONSE STATUS>[{needsAction,declined,tentative,accepted}] (default = accepted)] 

help:

arguments:
	-e <ATTACKER EMAIL>, --attacker_email <ATTACKER EMAIL>
			Email address of the Google account you are doing the
			injection as. (Attacker email address)
	-x <TARGETS> [TARGETS,...], --targets <TARGETS> [TARGETS ...]
			Comma-seperated list of victim email addresses
	-a <ACCESS TOKEN>, --access_token <ACCESS TOKEN>
			Google API Access Token.
	-s <START DATETIME>, --start_DateTime <START DATETIME>
			Start date and time for the event in the format of
			YYYY-MM-DDTHH:MM:SSlike this: 2019-08-16T20:00:00 for
			August 16, 2019 at 8:00:00 PM
	-f <FINISH DATETIME>, --finish_DateTime <FINISH DATETIME>
			Finish date and time for the event in the format of
			YYYY-MM-DDTHH:MM:SSlike this: 2019-08-16T20:00:00 for
			August 16, 2019 at 8:00:00 PM

optional arguments:
	-t <EVENT TITLE>, --event_title <EVENT TITLE>
			Title of the Google calendar event
	-l <EVENT LOCATION>, --event_location <EVENT LOCATION>
			Location field for the event
	-d <EVENT DESCRIPTION>, --event_description <EVENT DESCRIPTION>
			Description field for the event
	-z [<TIME ZONE>], --time_zone [<TIME ZONE>]
			Time zone for the event in the IANA tz database format:
			"America/New_York" (default: America/Chicago)
	-m [{true, false}], --allow_modify [{true, false}]
			If set to true allows targets to modify the calendar
			entry (default: false)
	-i [{true, false}], --allow_invite_others [{true, false}]
			If set to true allows targets to invite others to the
			calendar entry (default: true)
	-o [{true, false}], --show_invitees [{true, fasle}]
			If set to true will show all guests added to the event
			(default: false)
	-r [{needsAction,declined,tentative,accepted}],
			--response_status [{needsAction,declined,tentative,accepted}]
			Can be "needsAction", "declined", "tentative", or
			"accepted" (default: accepted)

	-h, --help		show this help message and exit

```
