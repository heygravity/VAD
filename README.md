# Video Audio Downloader

📺🎵 A web application built with Flask that allows users to search for YouTube videos, download them, and extract audio in MP3 format.

## Features

- 📹 Search for YouTube videos using keywords.
- 📃 View search results in a card format with video title, channel name, and publication year.
- ⬇️ Download and extract audio from selected videos in MP3 format.
- 💻 Easy-to-use web interface.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher installed.
- Flask 2.0.1 or higher installed.
- 🌐 Your YouTube Data API Key.

## Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/heygravity/VAD.git
   ```

2. **Install the required Python packages:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set your YouTube Data API Key in `main.py`:**

   ```python
   YOUTUBE_API_KEY = 'YOUR_API_KEY_HERE'
   ```

4. **Run the Flask application:**

   ```bash
   python app.py
   ```

5. **Access the web application in your browser at** `http://localhost:5000`.

## Usage

1. Enter the name of the YouTube video you want to search for in the search bar and press Enter.
2. Browse the search results and click the "Download" button on the desired video.
3. An alert will appear, indicating that your download will start shortly. Click "OK."
4. The audio will be downloaded and saved to your local system in MP3 format.

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/)
- [pytube](https://pytube.io/en/latest/)
- [YouTube Data API](https://developers.google.com/youtube/registering_an_application)

---

Made with ❤️ by [Pritish Rajpurohit]([https://github.com/your-username](https://github.com/smashcoder))
