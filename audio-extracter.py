import os
from moviepy.video.io.VideoFileClip import VideoFileClip

input_video = "video.mp4"
output_audio = "audio.mp3"

if not os.path.isfile(input_video):
    raise FileNotFoundError(f"Input video file not found: {input_video}")

cvt_video = VideoFileClip(input_video)

ext_audio = cvt_video.audio
ext_audio.write_audiofile(output_audio)
print(f"Audio extracted and saved to {output_audio}")