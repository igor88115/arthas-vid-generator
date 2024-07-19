from moviepy.editor import VideoFileClip, clips_array, ColorClip, CompositeVideoClip
import os


def split_screen(primary_vid_path, secondary_vid_path, output_folder="./clips"):
    primary_vid = VideoFileClip(primary_vid_path)
    secondary_vid = VideoFileClip(secondary_vid_path).without_audio()

    duration = min(primary_vid.duration, secondary_vid.duration)
    clip1 = primary_vid.subclip(0, duration)
    clip2 = secondary_vid.subclip(0, duration)

    final_clip = clips_array([[clip1],
                              [clip2]])

    new_clip_path = os.path.join(output_folder, os.path.basename(primary_vid_path))
    final_clip.write_videofile(new_clip_path)
    clip1.close()
    clip2.close()
    final_clip.close()
    return primary_vid_path
