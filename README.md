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
https://www.blackhillsinfosec.com/google-calendar-event-injection-mailsniper/  
Steps to get a Google API Access Token needed for connecting to the API
 - A. Login to Google
 - B. Go to https://console.developers.google.com/flows/enableapi?apiid=calendar&pli=1
 - C. Create/select a Project and agree to ToS and continue
 - D. Name your project and click "create"
 - E. Click "Go to Credentials"
 - F. On the "Add credentials to your project" page click cancel
 - G. At the top of the page, select the "OAuth consent screen" tab. Select an Email address, enter a Product name if not already set, and click the Save button.
 - H. Select the Credentials tab, click the Create credentials button and select OAuth client ID.
 - I. Select the application type Web application, under "Authorized redirect URIs" paste in the following address: https://developers.google.com/oauthplayground". Then, click the Create button.
 - J. Copy your "Client ID" and "Client Secret"
 - K. Navigate here: https://developers.google.com/oauthplayground/
 - L. Click the "gear icon" in the upper right corner and check the box to "Use your own OAuth credentials". Enter the OAuth2 client ID and OAuth2 client secret in the boxes.
 - M. Make sure that "OAuth flow" is set to Server-side, and "Access Type" is set to offline.
 - N. Select the "Calendar API v3" dropdown and click both URLs to add them to scope. Click Authorize APIs
 - O. Select the account you want to authorize, then click Allow. (If there is an error such as "Error: redirect_uri_mismatch" then it's possible the changes haven't propagated yet. Just wait a few minutes, hit the back button and try to authorize again.)
 - P. You should now be at "Step 2: Exchange authorization code for tokens." Click the "Exchange authorization code for tokens button". The "Access token" is item we need for accessing the API. Copy the value of the "Access token."

  
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
