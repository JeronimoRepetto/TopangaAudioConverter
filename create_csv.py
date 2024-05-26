import os
import csv

# Directory where the WAV files are located
audio_directory = os.path.join(os.getcwd(), 'audio')

# Name of the CSV file
csv_filename = 'audios.csv'

# Get the list of WAV files in the directory
audio_files = [f for f in os.listdir(audio_directory) if f.endswith('.wav')]

# Create and write the CSV file
with open(csv_filename, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    # Write the CSV header
    csv_writer.writerow(['wav_filename', 'wav_filesize', 'transcript'])

    # Write the rows to the CSV
    for audio_file in audio_files:
        filepath = os.path.join(audio_directory, audio_file)
        filesize = os.path.getsize(filepath)
        transcript = 'Okay Topanga'  # You can adjust this part if you have different transcripts
        csv_writer.writerow([filepath, filesize, transcript])

print(f'CSV file "{csv_filename}" created successfully.')
