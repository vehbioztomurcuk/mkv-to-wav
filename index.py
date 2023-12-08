from pydub import AudioSegment
import os

def convert_to_wav(input_folder, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)

        # Check if it's a file and not a directory
        if os.path.isfile(input_path):
            # Load the audio file
            audio = AudioSegment.from_file(input_path)

            # Convert to WAV format
            wav_filename = os.path.splitext(filename)[0] + ".wav"
            output_path = os.path.join(output_folder, wav_filename)
            audio.export(output_path, format="wav")

            print(f"Converted {filename} to {wav_filename}")

# Specify the input and output folders
input_folder = "/home/user1/Videos/obs-videos"
output_folder = "/home/user1/Videos/obs-videos/wav"

# Call the function to perform the conversion
convert_to_wav(input_folder, output_folder)
