from pydub import AudioSegment
import os

AudioSegment.ffmpeg = "C:\\Users\\Ayan\\AppData\\Local\\ffmpegio\\ffmpeg-downloader\\ffmpeg\\bin"
def split_audio(input_file, output_folder, duration_ms):
    # Load the audio file
    audio = AudioSegment.from_mp3(input_file)

    # Calculate the number of samples based on duration
    num_samples = len(audio) // duration_ms

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Split audio and save samples
    for i in range(num_samples):
        start_time = i * duration_ms
        end_time = start_time + duration_ms
        sample = audio[start_time:end_time]

        # Save the sample as WAV file
        base_filename = os.path.splitext(os.path.basename(input_file))[0]
        output_filename = f"{base_filename}_{i}.wav"
        sample.export(os.path.join(
            output_folder, output_filename), format="wav")


if __name__ == "__main__":
    # Provide input folder containing MP3 files, output folder, and duration of each sample in milliseconds
    input_folder = "C:\\Users\\Ayan\\Desktop\\kobyz"
    output_folder = "C:\\Users\\Ayan\\Desktop\\kob"
    duration_ms = 3000

    # Iterate over all MP3 files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".mp3"):
            input_file = os.path.join(input_folder, filename)
            split_audio(input_file, output_folder, duration_ms)
