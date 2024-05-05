import googleapiclient.discovery

api_service_name = "youtube"
api_version = "v3"
api_key="AIzaSyCxnouVXR32Um0JVbVYMANI1KoGN3igoPY"

youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=api_key)

def channel_data(c_id):
    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id=c_id
    )
    response = request.execute()
    data={"channel_name":response['items'][0]['snippet']['title'],
          "channel_des":response['items'][0]['snippet']['description'],
          "channel_pat":response['items'][0]['snippet']['publishedAt'],
          "channel_pid":response['items'][0]['contentDetails']['relatedPlaylists']['uploads'],
          "channel_sub":response['items'][0]['statistics']['subscriberCount'],
          "channel_vc":response['items'][0]['statistics']['viewCount'],
          "type":response['items'][0]['kind']
          }
    print("channel pid",data['channel_pid'])
    return data

def playlist_data(p_id):
    request = youtube.playlists().list(
        part="snippet,id,contentDetails",
        id=p_id
    )
    response = request.execute()
    data={"channel_id":response['items'][0]['snippet']['channelId'],
          "playlist_name":response['items'][0]['snippet']['title'],
          "playlist_id":p_id}
    return data




