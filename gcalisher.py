import requests
import argparse

parser = argparse.ArgumentParser(description='This module will connect to '
    + 'Google\'s API using an access token and inject a calendar event into a '
    + 'target\'s calendar.')
parser.add_argument('-e', '--attacker_email', required=True, type=str,
    help='Email address of the Google account you are doing the injection as.'
    + ' (Attacker email address)', nargs=1)
parser.add_argument('-x', '--targets', required=True, type=str,
    help='Comma-seperated list of victim email addresses', nargs='+')
parser.add_argument('-a', '--access_token', required=True, type=str,
    help='Google API Access Token.', nargs=1)
parser.add_argument('-s', '--start_DateTime', required=True, type=str,
    help='Start date and time for the event in the format of YYYY-MM-DDTHH:MM:SS'
    + 'like this: 2019-08-16T20:00:00 for August 16, 2019 at 8:00:00 PM',
    nargs=1)
parser.add_argument('-f', '--finish_DateTime', required=True, type=str,
    help='Finish date and time for the event in the format of YYYY-MM-DDTHH:MM:SS'
    + 'like this: 2019-08-16T20:00:00 for August 16, 2019 at 8:00:00 PM',
    nargs=1)
parser.add_argument('-t', '--event_title', required=False, type=str,
    help='Title of the Google calendar event')
parser.add_argument('-l', '--event_location', required=False, type=str,
    help='Location field for the event')
parser.add_argument('-d', '--event_description', required=False, type=str,
    help='Description field for the event')
parser.add_argument('-z', '--time_zone', required=False, type=str,
    default='America/New_York', help='Time zone for the event in the format '
    + '"America/New_York" (default: %(default)s)', nargs='?')
parser.add_argument('-m', '--allow_modify', required=False, type=str,
    default='false', help='If set to true allows targets to modify the calendar '
    + 'entry (default: %(default)s)', nargs='?')
parser.add_argument('-i', '--allow_invite_others', required=False, type=str,
    default='true', help='If set to true allows targets to invite others to the '
    + 'calendar entry (default: %(default)s)', nargs='?')
parser.add_argument('-o', '--show_invitees', required=False, type=str,
   default='false', help='If set to true will show all guests added to the '
   + 'event (default: %(default)s)', nargs='?')
parser.add_argument('-r', '--response_status', required=False, type=str,
    default='accepted', choices=['needsAction', 'declined', 'tentative',
    'accepted'], help='Can be "needsAction", "declined", "tentative", or '
    + '"accepted" (default: %(default)s)', nargs='?')


args = parser.parse_args('--attacker_email ATTACKER_EMAIL'.split())


# api endpoint
URL = "https://www.googleapis.com/calendars/" + ATTACKER_EMAIL + "/events"
