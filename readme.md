<p align="center" width="150" height="150"><img src="ozma.png" /></p>
<h1 align="center">Ozma</h1>
<h2 align="center">The Role Management and FFXIV Lookup Bot for Dawntreaders</h2>

<p align="center">
This Discord bot provides various features such as role management, sending announcements, and looking up characters in the game Final Fantasy XIV. It is built using the discord.py library and asyncio for asynchronous operations.

</p>

## Features

- Lookup characters in the game Final Fantasy XIV by their name and server.
- Send an announcement to a specified channel with the option to include an
  image and custom embed color.
- Post role buttons in a specified channel for users to easily add or remove
  roles related to FFXIV, pronouns, and channel access.

## Some Commands

- post_role_buttons [channel]: Post role buttons in the specified channel.
  Administrators can use this command to post a message with interactive
  buttons in the given text channel. Users can click these buttons to add or
  remove roles related to FFXIV, pronouns, and channel access. The bot will
  automatically update their roles based on their selections.
- lookup_character [first_name] [last_name] [server]: Lookup a character in
  Final Fantasy XIV by their name and server.
- announcement [channel_name]: Send an announcement to a specified channel with
  a user-defined title, message, optional image URL, and optional custom embed
  color.

## Discord Markdown

Discord supports the use of markdown, a lightweight markup language for
formatting text. You can use these formatting options when creating your
announcement messages to make them more visually appealing.

For codeblock replace `language` with the desired language for syntax
highlighting (e.g., `python`, `javascript`, `html`, etc.). If you don't need
syntax highlighting, you can leave it blank.

Here are some basic formatting options in Discord:

- Bold: `**text**`
- Italic: `*text*` or `_text_`
- Strikethrough: `~~text~~`
- Underline__: `__text__`
- Inline code: `` `text` ``
- Code block: ` ``` language Code block: ``` `
- Hyperlinking: `[Example](example.com)`

## Continuous Integration and Deployment with GitHub Actions

This project uses a GitHub Actions workflow to automatically lint, build, and
deploy the Ozma bot using Docker. The workflow is triggered on every push to
the main branch.

Here's a summary of the steps in the workflow:

1. Lint the code with Flake8.
2. Check out the code and set up Docker Buildx.
3. Log in to Docker Hub with provided credentials.
4. Build and push the Docker image to Docker Hub.
5. Deploy the bot using Docker Compose on a self-hosted runner.

The workflow file can be found in the repository
under `.github/workflows/deploy.yml`. Make sure to set up the required secrets
in your repository settings for the workflow to work correctly. These secrets
include:

- DOCKERHUB_USERNAME: A Docker Hub username.
- DOCKERHUB_TOKEN: A Docker Hub access token.
- DOCKER_IMAGE_NAME: The name of the Docker image.
- GH_USERNAME: A GitHub username.
- GH_ACCESS_TOKEN: A GitHub access token.
- GH_REPO: The GitHub repository name.
- TOKEN: The Discord bot token.
- ERROR_CHANNEL_ID: The Discord channel ID for sending error messages.
- GUILD_ID: The Discord server (guild) ID.

## Contributing

- Fork the repository and create a new branch for your feature or bugfix.
- Make your changes and commit them to your branch.
- Create a pull request and describe the changes you made.
- Wait for a maintainer to review and merge your changes.

## Support

If you encounter any issues or need help with Ozma, please feel free to reach
out to us by sending an email to [ozma@ptrlrd.com](mailto:ozma@ptrlrd.com) or join my [discord](https://discord.gg/aWdj37Edyq)

## License

This project is licensed under the MIT License. See the LICENSE file for more
details.
