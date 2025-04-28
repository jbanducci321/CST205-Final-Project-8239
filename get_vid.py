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

    video_urls = []
    for item in response["items"]:
        video_id = item["id"]["videoId"]
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        video_urls.append(video_url)
        video_urls.append(video_id)
    random_index = random.randint(0, len(video_urls) - 1)
    video_info = [video_urls[random_index], video_urls[random_index+1]]
    return video_info

# Example
results = search_youtube_videos("happy video")
print(results[0])
print(results[1])