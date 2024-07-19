import pytube


class DownloadResult:
    def __init__(self, file_path, title):
        self.file_path = file_path
        self.title = title


def download_video(url, output_path="./download"):
    try:
        yt = pytube.YouTube(url)
        video = yt.streams.filter(progressive=True, file_extension="mp4").order_by('resolution').desc().first()
        filename = f"{yt.title}.mp4"
        video_path = video.download(output_path=output_path, filename=filename)

        print(f"Video downloaded successfully: {video_path}")

        return DownloadResult(video_path, video.title)
    except Exception as e:
        print(f"An error occurred while downloading the video: {e}")
