import sys
from googleapiclient.discovery import build
from setup import api_key

def parse_quotes(string):
  return string.replace("\"", "")

youtube = build('youtube', 'v3', developerKey=api_key)

if len(sys.argv) >= 2:
  command = sys.argv[1]
  channel_name = parse_quotes(sys.argv[2])
  if command == 'getsubscribers':
    request = youtube.channels().list(
      part='statistics',
      forUsername=channel_name
    )
    response = request.execute()
    print(response)
    if "items" in response:
      subscribers_number = response["items"][0]["statistics"]["subscriberCount"]
      print(subscribers_number)
    else:
      print("ERROR: couldn't get data")
    quit()
  elif command == 'getchannelviews':
    request = youtube.channels().list(
      part='statistics',
      forUsername=channel_name
    )
    response = request.execute()
    views_number = response["items"][0]["statistics"]["viewCount"]
    print(views_number)
    quit()
  elif command == 'getchanneldescription':
    request = youtube.channels().list(
      part=["snippet", "contentDetails", "statistics"],
      forUsername=channel_name
    )
    response = request.execute()
    views_number = response["items"][0]["snippet"]["description"]
    print(views_number)
    quit()
else:
  print('ERROR: too many few arguments')