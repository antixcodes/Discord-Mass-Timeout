# Discord-Mass-Timeout
A Python script that efficiently applies timeouts to all members.

Features
- Scrape Members: Collects all member IDs from the server and stores them in a file named members.txt
- Timeout Members: Applies a timeout to members listed in members.txt for a fixed duration (28 days).

Requirements

- Python 3.8+
- discord.py (for Discord bot interactions)

Installation

1. Clone the Repository

   git clone https://github.com/yourusername/discord-bot-timeout-tool.git
   cd discord-bot-timeout-tool

2. Install Dependencies

   Ensure you have pip installed, then run:

   pip install -r requirements.txt

3. Setup Environment Variables

   Create a .env file in the project directory and add your Discord bot token:

   token=YOUR_DISCORD_BOT_TOKEN

4. Run the Bot

   Execute the bot script:
   python main.py

Commands

- $scrape: Scrapes all members IDs except bots from the server and writes their IDs to members.txt.
- $timeout: Applies a 28-day timeout to members listed in members.txt.

Notes

- Do not attempt to optimize the code: The current implementation is configured to run at its best.
- Ensure the bot has the necessary permissions: The bot needs appropriate permissions to manage members and apply timeouts.

Developer Information

- Author: Antix
- Discord Username: antixdev

Disclaimer: Use this bot responsibly and ensure compliance with Discord's Terms of Service and Community Guidelines.
