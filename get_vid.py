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
        maxResults=10
    ).execute()

    # video_urls = []
    # for item in response["items"]:
    #     video_id = item["id"]["videoId"]
    #     video_url = f"https://www.youtube.com/watch?v={video_id}"
    #     video_urls.append(video_url)
    #     video_urls.append(video_id)
    
    video_info = []
    random_index = random.randint(0, len(response["items"]) - 1)
    video_id = response["items"][random_index]["id"]["videoId"]
    video_url = f"https://www.youtube.com/watch?v={video_id}"   
    video_info.append(video_id)
    video_info.append(video_url)
    return video_info

# Example
results = search_youtube_videos("happy video")
print(results[0]) # video_id
print(results[1]) # video_url
