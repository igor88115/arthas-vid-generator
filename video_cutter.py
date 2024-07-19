import os

from moviepy.editor import VideoFileClip, concatenate_videoclips


def cut_video_start_end(video, cut_from_start=0, cut_from_end=0):
    return video.subclip(cut_from_start, video.duration - cut_from_end) \
        if cut_from_start != 0 and cut_from_end != 0 \
        else video


def cut_video(video_path, subclip_duration_sec=59, overlap=1, cut_from_start=0, cut_from_end=0, output_folder="./temp"):
    video_file_clip = VideoFileClip(video_path)
    video = cut_video_start_end(video_file_clip, cut_from_start, cut_from_end)
    name, ext = os.path.splitext(video_path)
    clips = []
    has_more = True
    i = 0
    while has_more:
        start_time = i * subclip_duration_sec - overlap if i != 0 else i * subclip_duration_sec
        if start_time + 10 > video.duration:
            has_more = False
            clip.close
        else:
            start_time = i * subclip_duration_sec - overlap if i != 0 else i * subclip_duration_sec
            end_time = min((i + 1) * subclip_duration_sec, video.duration)
            clip = video.subclip(start_time, end_time)
            clip.set_fps(video.fps)

            filename = f"{name}_{i + 1}{ext}"
            clip_path = os.path.join(output_folder, os.path.basename(filename))
            clip.write_videofile(clip_path)
            clips.append(clip_path)
            i += 1

    video.close()
    return clips
