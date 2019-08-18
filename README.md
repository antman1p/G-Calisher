# G-Calisher
## What?
This program will connect to Google's API using an access token and inject a calendar event into a target's calendar.
## Who?
Author: Antonio Piazza (@antman1p)
This is a python version of the powershell Mailsniper module Invoke-InjectGEventAPI
(https://github.com/dafthack/MailSniper/blob/master/MailSniper.ps1) written by BlackHills Security's 
Beau Bullock (@dafthack) & Michael Felch (@ustayready)
## Why?
Becasue I'm a MacOS hacker and not everything is effing windows!  Also, Google STILL, since October 2018 has NOT FIXED 
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
```
