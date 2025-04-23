#API KEY AIzaSyBgxL4_sHM9p4Wl6WL21xB1I1LTNykrOF8
from googleapiclient.discovery import build

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

    return video_urls

# Example
results = search_youtube_videos("happy video")
for url in results:
    print(url)
