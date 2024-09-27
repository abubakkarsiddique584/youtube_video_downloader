import yt_dlp

def download_video(video_url, download_path):
    try:
        ydl_opts = {
            'outtmpl': f'{download_path}/%(title)s.%(ext)s',  # Save to the download path
            'ffmpeg_location': r'C:\ffmpeg\bin\ffmpeg.exe',  # Provide full path to ffmpeg
            'format': 'bestvideo[height>=720]+bestaudio/best[height>=720]',  # Download HD (720p and above)
            'merge_output_format': 'mp4',  # Specify the format after merging
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print("Video downloaded successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
video_url = input("Enter the YouTube video link: ")
download_path = r"D:\video songs"  # Updated download path
download_video(video_url, download_path)
