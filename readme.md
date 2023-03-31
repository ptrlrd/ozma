Discord Role Management and FFXIV Lookup Bot

This Discord bot provides various features such as role management, reporting messages, and looking up characters in the game Final Fantasy XIV. It is built using the discord.py library and asyncio for asynchronous operations.
Features

    Add and remove roles for users in the server.
    Report messages to a specified channel for moderation.
    Lookup characters in the game Final Fantasy XIV by their name and server.

Installation

    Clone the repository:

    bash

git clone https://github.com/yourusername/discord-role-management-and-ffxiv-lookup-bot.git
cd discord-role-management-and-ffxiv-lookup-bot

Create a virtual environment and activate it:

bash

python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate  # For Windows

Install the required dependencies:

pip install -r requirements.txt

Create a .env file in the project directory and add your Discord bot token:

makefile

    token=YOUR_BOT_TOKEN

Usage

    Run the bot:
    
    python bot.py
    
    Invite the bot to your Discord server and give it the necessary permissions.
    
    Use the available commands:
        hello: The bot will greet the user.
        set_report_channel [channel_name]: Set the channel where reported messages will be sent.
        report_message: Report a message to the specified report channel.
        add_role: Add a role to the user who invoked the command.
        remove_role: Remove a role from the user who invoked the command.
        lookup_character [first_name] [last_name] [server]: Lookup a character in Final Fantasy XIV by their name and server.

## Contributing

Fork the repository and create a new branch for your feature or bugfix.

Make your changes and commit them to your branch.

Create a pull request and describe the changes you made.

Wait for a maintainer to review and merge your changes.




License

This project is licensed under the MIT License. See the LICENSE file for more details.