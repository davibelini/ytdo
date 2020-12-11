import sys
from googleapiclient.discovery import build
from setup import api_key

def parse_quotes(string):
  return string.replace("\"", "")

if len(sys.argv) >= 2:
  command = sys.argv[1]
  channel_name = parse_quotes(sys.argv[2])
  if command == 'getsubscribers':
    youtube = build('youtube', 'v3', developerKey=api_key)
    request = youtube.channels().list(
      part='statistics',
      forUsername=channel_name
    )
    response = request.execute()
    subscribers_number = response["items"][0]["statistics"]["subscriberCount"]
    print(subscribers_number)
    quit()
else:
  print('ERROR: too many few arguments')