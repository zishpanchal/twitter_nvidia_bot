# Twitter NVIDIA Price Bot

This project is a Twitter bot that tweets the current price of NVIDIA stock every day. It utilizes the Twitter API to post updates and a financial API to fetch the stock price.

## Project Structure

```
twitter_nvidia_bot
├── src
│   ├── main.py        # Entry point of the application
│   ├── api.py         # Functions for interacting with the Twitter API
│   └── utils.py       # Utility functions for fetching NVIDIA prices
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/twitter_nvidia_bot.git
   cd twitter_nvidia_bot
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your Twitter API credentials:
   - Create a Twitter Developer account and create an app to get your API keys.
   - Store your credentials in a `.env` file or directly in the code (not recommended for production).

## Usage

1. Run the bot:
   ```
   python src/main.py
   ```

2. The bot will fetch the current NVIDIA stock price and tweet it daily.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.