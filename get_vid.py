'''
Function to get video search results
CST-205
Uses the youtube google API to obtain a list of video urls from a search string.
5/13/25
Joshua Sumagang
'''
#API KEY AIzaSyBgxL4_sHM9p4Wl6WL21xB1I1LTNykrOF8
from googleapiclient.discovery import build
import random

def search_youtube_videos(query):
    api_key = "AIzaSyBgxL4_sHM9p4Wl6WL21xB1I1LTNykrOF8"
    youtube = build("youtube", "v3", developerKey=api_key)

    response = youtube.search().list(
        q=query,
        part="snippet",
        type="video",
        videoLicense='creativeCommon',
        maxResults=10
    ).execute()

    video_info = []
    random_index = random.randint(0, len(response["items"]) - 1)
    video_id = response["items"][random_index]["id"]["videoId"]
    video_url = f"https://www.youtube.com/watch?v={video_id}"   
    video_info.append(video_id)
    video_info.append(video_url)
    return video_info

