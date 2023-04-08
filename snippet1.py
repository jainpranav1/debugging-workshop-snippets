import os
import librosa  # might not support py 3.11
import soundfile
from moviepy.editor import *


def editAudio():
    # increase pitch by increasing y values of raw data
    y, sr = librosa.load("audio1.wav")
    y_shifted = librosa.effects.pitch_shift(y, sr=sr, n_steps=12)
    soundfile.write("audio2.mp3", y_shifted, sr)


def main():
    # functionality: increases pitch of video

    # checking if file path exists
    fileCheck = os.path.isfile("input.mp4")
    if (not fileCheck):
        print("File not found")
        return 0

    # audio processing part
    vid = VideoFileClip("input.mp4").subclip(0, 7)
    vid.audio.write_audiofile("audio1.wav")  # split audio
    editAudio()

    # add audio back to video
    finalvid = vid.set_audio(AudioFileClip("audio2.mp3"))
    finalvid.write_videofile("finalvid.mp4")


if __name__ == "__main__":
    main()
