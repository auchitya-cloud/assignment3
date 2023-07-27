import os
from moviepy.video.io.VideoFileClip import VideoFileClip

def convert_video_to_audio(video_path):
    try:
        video_clip = VideoFileClip(video_path)
        audio_clip = video_clip.audio
        audio_filename = os.path.splitext(os.path.basename(video_path))[0] + ".mp3"
        audio_clip.write_audiofile(audio_filename)

        print(f"Audio extracted from '{video_path}' and saved as '{audio_filename}'")
        audio_clip.close()
        video_clip.close()
    except Exception as e:
        print(f"Error occurred while converting video to audio: {str(e)}")

if __name__ == "__main__":
    video_folder = "videos"
    
    # Get a list of all video files in the 'videos' folder
    video_files = [f for f in os.listdir(video_folder) if f.endswith(".mp4")]

    # Convert each video to audio
    for video_file in video_files:
        video_path = os.path.join(video_folder, video_file)
