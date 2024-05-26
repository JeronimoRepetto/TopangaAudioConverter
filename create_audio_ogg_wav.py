import os
from pydub import AudioSegment
import re

def get_next_wav_number(folder_path):
    max_number = 0
    pattern = re.compile(r"okey_topanga_(\d+).wav")
    
    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        match = pattern.match(filename)
        if match:
            number = int(match.group(1))
            if number > max_number:
                max_number = number
    
    return max_number + 1

def convert_ogg_to_wav(folder_path):
    next_number = get_next_wav_number(folder_path)
    
    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".ogg"):
            # Full path of the input and output files
            input_file_path = os.path.join(folder_path, filename)
            output_file_name = f"okey_topanga_{next_number}.wav"
            output_file_path = os.path.join(folder_path, output_file_name)
            
            # Load the audio file in .ogg format
            audio = AudioSegment.from_ogg(input_file_path)
            
            # Convert and save the file in .wav format
            audio.export(output_file_path, format="wav")
            
            # Delete the original .ogg file
            os.remove(input_file_path)
            
            print(f"Converted and saved: {output_file_name}, original file deleted: {filename}")
            
            # Increment the number for the next file
            next_number += 1

# Path to the folder containing the .ogg files
folder_path = os.path.join(os.getcwd(), 'audio')

# Call the function to convert the files
convert_ogg_to_wav(folder_path)
