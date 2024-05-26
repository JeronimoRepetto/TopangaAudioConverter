# TopangaAudioConverter

## Description

This project is designed to convert audio files from .ogg to .wav format, assign them a specific filename pattern, and delete the original .ogg files. The converted files are named in the format `okey_topanga_NUMERO.wav`. Additionally, the project includes a script to create a CSV file, which can be used to train DeepSpeech.

## Features

- Converts .ogg audio files to .wav format.
- Assigns filenames in the format `okey_topanga_N.wav`.
- Deletes the original .ogg files after conversion.
- Generates a CSV file with details about the .wav files for use in training DeepSpeech.

## Usage

### Convert .ogg to .wav

1. Place your .ogg files in the `audio` folder.
2. Run the conversion script:

    ```bash
    python create_audio_ogg_wav.py
    ```

### Create CSV

After converting the .ogg files to .wav, create the CSV file:

1. Run the CSV creation script:

    ```bash
    python create_csv.py
    ```

### Example Output

The `create_audio_ogg_wav.py` script will convert your .ogg files and produce .wav files named as follows:

```
audio/
    okey_topanga_1.wav
    okey_topanga_2.wav
    ...
```

The `create_csv.py` script will generate a CSV file named `audios.csv` with the following format:

```csv
wav_filename,wav_filesize,transcript
/path/to/audio/okey_topanga_1.wav,123456,Okay Topanga
/path/to/audio/okey_topanga_2.wav,123456,Okay Topanga
...
```

## Requirements

- Python 3.x
- [pydub](https://github.com/jiaaro/pydub)
- ffmpeg (Ensure ffmpeg is installed and added to your system PATH)

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/JeronimoRepetto/TopangaAudioConverter
    ```

2. Install the required Python packages:

    ```bash
    pip install pydub
    ```

3. Ensure `ffmpeg` is installed and added to your system PATH.

## License

This project is licensed under the MIT License.

## Acknowledgments

This project is a part of the TopangAIAssistant initiative. Special thanks to all contributors.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## Contact

For any inquiries, please contact jeronimorepetto@gmail.com.

---

### Project Structure

```
TopangaAudioConverter/
│
├── audio/
│   └── (Place your .ogg files here)
│
├── create_audio_ogg_wav.py
├── create_csv.py
├── README.md
```

---

### Related Project

This project is used for the TopangAIAssistant project. For more information, visit the [TopangAIAssistant repository](https://github.com/JeronimoRepetto/TopangAIAssistant).
