from pytube import YouTube

def download_machine_learning_videos(search_query, num_videos):
    query = search_query + " tutorial"  # Adding "tutorial" to get more educational videos.
    videos = YouTube.search(query, limit=num_videos)

    for video in videos:
        try:
            stream = video.streams.filter(file_extension="mp4", progressive=True).first()
            if stream:
                video_title = video.title
                print(f"Downloading '{video_title}'...")
                stream.download(output_path="videos")
                print(f"Video '{video_title}' downloaded successfully!")
        except Exception as e:
            print(f"Error occurred while downloading video: {str(e)}")

if __name__ == "__main__":
    search_query = "Machine Learning"
    num_videos = 10

    download_machine_learning_videos(search_query, num_videos)
