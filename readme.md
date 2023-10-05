# Twitter Auto-Liker with Tweepy

Automatically like tweets with a specific hashtag using Tweepy.

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Overview

This Python script allows you to automatically like tweets containing a specific hashtag on Twitter. It uses the Tweepy library to interact with Twitter's API.

## Getting Started

### Prerequisites

Before you begin, make sure you have the following:

- Python 3.x installed
- Twitter API credentials (consumer key, consumer secret, access token, access token secret)

### Installation

1. Clone the repository:

git clone https://github.com/yourusername/twitter-auto-liker.git


2. Install the required packages:

pip install tweepy


3. Replace the placeholder API keys in the `main.py` file with your actual Twitter API credentials.

## Usage

To use the script, run `main.py` in your preferred Python environment.


The script will automatically like tweets with the specified hashtag.

## Configuration

You can customize the behavior of the script by modifying the following parameters in `main.py`:

- `consumer_key`: Your Twitter API consumer key.
- `consumer_secret`: Your Twitter API consumer secret.
- `access_token`: Your Twitter API access token.
- `access_token_secret`: Your Twitter API access token secret.
- `hashtag`: The hashtag you want to target (e.g., `#PythonRocks`).
- `language`: The language of tweets to target (default is English).

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with a descriptive message.
4. Push your changes to your fork.
5. Open a pull request to the `main` branch of this repository.

## License

This project is licensed under the [MIT License](LICENSE).
