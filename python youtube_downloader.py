{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPyLG5xKUOjDTOuIosH3qBK",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/joedone1/HiLab.internship/blob/master/python%20youtube_downloader.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "SmAa7jZadSqc"
      },
      "outputs": [],
      "source": [
        "import pytube\n",
        "import os\n",
        "\n",
        "def download_video(url):\n",
        "    # Create the output directory if it doesn't exist\n",
        "    if not os.path.exists('downloads'):\n",
        "        os.makedirs('downloads')\n",
        "\n",
        "    # Use the YouTube() class to get video details\n",
        "    yt = pytube.YouTube(url)\n",
        "\n",
        "    # Get the video stream with the highest resolution and bitrate\n",
        "    stream = yt.streams.get_highest_resolution()\n",
        "\n",
        "    # Download the video stream and save it to the output directory\n",
        "    stream.download('downloads')\n",
        "\n",
        "    print(f'Downloaded {yt.title} to the downloads directory.')\n",
        "\n",
        "if __name__ == '__main__':\n",
        "    # Ask the user to enter a YouTube video URL\n",
        "    url = input('Enter a YouTube video URL: ')\n",
        "\n",
        "    # Call the download_video() function with the entered URL\n",
        "    download_video(url)"
      ]
    }
  ]
}