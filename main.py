import youtube_vid_downloader
import video_screen_splitter
import video_cutter
import excel_parser
import os
import random


def get_random_template_vid(folder_path):
    filenames = os.listdir(folder_path)
    random_filename = random.choice(filenames)
    return os.path.join(folder_path, random_filename)

def merge_as_split_screen(video_path):
    template_vid_path = get_random_template_vid("./template")
    return video_screen_splitter.split_screen(video_path, template_vid_path)

def get_input_from_excel(file_path):
    if os.path.exists(file_path):
        return excel_parser.get_input_from_excel(file_path)
    else:
        print(f"Input file doesn't exist: {file_path}")


def process_video(video_to_process):
    video = youtube_vid_downloader.download_video(video_to_process.video_link)
    clips_paths = video_cutter.cut_video(video.file_path, cut_from_start = 1, cut_from_end = 1)
    for clip_path in clips_paths:
        merge_as_split_screen(clip_path)


if __name__ == '__main__':
    videos_to_process = get_input_from_excel("./input/input.xlsx")
    for video_to_process in videos_to_process:
        process_video(video_to_process)




