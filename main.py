# 1. Import necessary modules
import json
import os
# import re
from typing import List

import aiohttp
import discord
from discord import app_commands
# from discord.ui import Select, View, Button
from dotenv import load_dotenv

# 2. Define constants
load_dotenv()
MY_GUILD = discord.Object(id=os.environ["guild_id"])
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
report_channels = {}

# Create a PartialEmoji object for the custom emoji
custom_tank = discord.PartialEmoji(name="tank", id=637799796891058218)
custom_healer = discord.PartialEmoji(name="healer", id=637799810287534111)
custom_dps = discord.PartialEmoji(name="dps", id=671563456742162462)
custom_craft = discord.PartialEmoji(name="crafter", id=637799971441344534)
custom_gatherer = discord.PartialEmoji(name="gatherer", id=637799947286216714)
custom_ocean_fishing = discord.PartialEmoji(name="Fisher",
                                            id=554478937028427796)
custom_treasuremap = discord.PartialEmoji(name="treasuremap",
                                          id=679192676486086658)
custom_blue_mage = discord.PartialEmoji(name="BlueMage", id=554479007287214090)
custom_savage_raiding = discord.PartialEmoji(name="savage",
                                             id=638832705106346036)
custom_extreme_trials_raiding = discord.PartialEmoji(name="extreme",
                                                     id=638832720201515049)
custom_ultimate_raiding = discord.PartialEmoji(name="ultimate",
                                               id=638832734231592965)
custom_unreal_raiding = discord.PartialEmoji(name="unreal",
                                             id=638832750559756329)
custom_pvp = discord.PartialEmoji(name="pvp", id=638832685346979871)
custom_unsynced_content = discord.PartialEmoji(name="unsync",
                                               id=979082924022431784)
custom_he = discord.PartialEmoji(name="he", id=637813481826942987)
custom_she = discord.PartialEmoji(name="she", id=637813570779873291)
custom_they = discord.PartialEmoji(name="they", id=637813586550456320)
custom_tools = discord.PartialEmoji(name="toolsdiscussion",
                                    id=1013634974404051044)
custom_currentevents = discord.PartialEmoji(name="currentevents",
                                            id=719347909048402010)

custom_orange_star = discord.PartialEmoji(name="orange_star",
                                          id=874102281002430545)
custom_pink_star = discord.PartialEmoji(name="pink_star",
                                        id=874102281069555752)
custom_purple_star = discord.PartialEmoji(name="purple_star",
                                          id=874102281094717460)
custom_teal_star = discord.PartialEmoji(name="teal_star",
                                        id=874102281002426428)
custom_green_star = discord.PartialEmoji(name="green_star",
                                         id=983910897712001094)
custom_yellow_star = discord.PartialEmoji(name="yellow_star",
                                          id=983911288151347202)
custom_black_star = discord.PartialEmoji(name="black_star",
                                         id=983911288310730762)
custom_white_star = discord.PartialEmoji(name="white_star",
                                         id=983911288176517141)


# 3. Create classes
class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
        self.message_id_store = self.load_message_ids()

    def load_message_ids(self):
        data_file = os.path.expanduser("./data.json")
        if os.path.exists(data_file):
            with open(data_file, "r") as f:
                message_id_store = json.load(f)
                print(
                    f"Loaded message_id_store: {message_id_store}")  # Add this line
                return message_id_store
        return {}

    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)

    async def on_message_edit(self, before: discord.Message,
                              after: discord.Message):
        if after.interaction and after.interaction.user != self.user:
            await self._run_event("on_interaction", after.interaction)


def save_message_ids(client):
    data_file = os.path.expanduser("./data.json")
    with open(data_file, "w") as f:
        json.dump(client.message_id_store, f)
        print(
            f"Saved message_id_store: {client.message_id_store}")  # Add this line


role_categories = {
    "XIV Roles": ["Tank", "Healer", "DPS", "Crafter", "Gatherer",
                  "Ocean Fishing", "Maps", "Blue Mage",
                  "Savage Raiding", "Extreme Trials Raiding",
                  "Ultimate Raiding", "Unreal Raiding"],
    "Pronouns": ["He/him", "She/her", "They/them"],
    "Channel Access Roles": ["Tools Discussion", "Current Events"],
    # "Custom Color": ["Orange Star", "Pink Star", "Purple Star", "Teal Star",
    # "Green Star", "Yellow Star",
    # "Black Star",
    #                  "White Star"]
}


# Replace the RoleAdditionSelect and RoleRemovalSelect classes with RoleButton
class RoleButton(discord.ui.Button):
    def __init__(self, *, role, label=None, style=None, emoji=None,
                 custom_id=None):
        self.role = role

        role_labels = {
            "Tank": custom_tank,
            "Healer": custom_healer,
            "DPS": custom_dps,
            "Crafter": custom_craft,
            "Gatherer": custom_gatherer,
            "Ocean Fishing": custom_ocean_fishing,
            "Maps": custom_treasuremap,
            "Blue Mage": custom_blue_mage,
            "Savage Raiding": custom_savage_raiding,
            "Extreme Trials Raiding": custom_extreme_trials_raiding,
            "Ultimate Raiding": custom_ultimate_raiding,
            "Unreal Raiding": custom_unreal_raiding,
            "PVP": custom_pvp,
            "He/him": custom_he,
            "She/her": custom_she,
            "They/them": custom_they,
            "Tools Discussion": custom_tools,
            "Current Events": custom_currentevents,
            # "Orange Star": custom_orange_star,
            # "Pink Star": custom_pink_star,
            # "Purple Star": custom_purple_star,
            # "Teal Star": custom_teal_star,
            # "Green Star": custom_green_star,
            # "Yellow Star": custom_yellow_star,
            # "Black Star": custom_black_star,
            # "White Star": custom_white_star
            # Add more roles and labels if needed
        }

        if role.name in role_labels:
            label = role.name
            emoji = role_labels[role.name]
            custom_id = role.name.lower().replace(" ", "_")
        else:
            label = role.name

        super().__init__(label=label, style=discord.ButtonStyle.secondary,
                         emoji=emoji, custom_id=custom_id)

    async def callback(self, interaction: discord.Interaction):
        try:
            if interaction.response.is_done():
                return

            # Fetch the updated member object for the user who clicked the button
            updated_member = await interaction.guild.fetch_member(
                interaction.user.id)

            if self.role in updated_member.roles:
                try:
                    await updated_member.remove_roles(self.role)
                    await interaction.response.send_message(
                        f"Successfully removed the {self.role.name} role from "
                        f"{updated_member.mention}.",
                        ephemeral=True, delete_after=30)
                except Exception as e:
                    await send_error_message(interaction, e)
            else:
                try:
                    await updated_member.add_roles(self.role)
                    await interaction.response.send_message(
                        f"Successfully added the {self.role.name} role to "
                        f"{updated_member.mention}.",
                        ephemeral=True,
                        delete_after=30)
                except Exception as e:
                    await send_error_message(interaction, e)
        except Exception as e:
            await send_error_message(interaction, e)


class ChannelSelectionView(discord.ui.View):
    def __init__(self, interaction: discord.Interaction):
        super().__init__(timeout=300)
        self.interaction = interaction
        self.selected_channel = None

    async def interaction_check(self,
                                interaction: discord.Interaction) -> bool:
        return self.interaction.user.id == interaction.user.id

    @discord.ui.select(
        placeholder="Choose a channel",
        min_values=1,
        max_values=1,
        options=[]
    )
    async def channel_select(self, select: discord.ui.Select,
                             interaction: discord.Interaction):
        self.selected_channel = int(select.values[0])
        await interaction.response.send_message(
            "Channel selected successfully!", ephemeral=True, delete_after=30)
        self.stop()


# Create views for each group
class XIVRolesView(discord.ui.View):
    def __init__(self, roles):
        super().__init__(timeout=100)  # Add timeout=300
        # self.timeout = None  # Remove this line
        for role in roles:
            self.add_item(RoleButton(role=role))


class PronounsView(discord.ui.View):
    def __init__(self, roles):
        super().__init__(timeout=100)  # Add timeout=300
        # self.timeout = None  # Remove this line
        for role in roles:
            self.add_item(RoleButton(role=role))


class ChannelsView(discord.ui.View):
    def __init__(self, roles):
        super().__init__(timeout=100)  # Add timeout=300
        # self.timeout = None  # Remove this line
        for role in roles:
            self.add_item(RoleButton(role=role))


# class ColorView(discord.ui.View):
#     def __init__(self, roles):
#         super().__init__(timeout=100)
#         self.previous_role = None
#         for role in roles:
#             self.add_item(RoleButton(role=role))
#
#     async def interaction_check(self, interaction: discord.Interaction) ->
#     bool:
#         booster_role = discord.utils.get(interaction.guild.roles,
#         name="Nitro Booster")
#         if booster_role is None:
#             return False  # Don't show the view if the Nitro Booster role
#             doesn't exist
#         else:
#             if booster_role in interaction.user.roles:
#                 return True
#             else:
#                 await interaction.response.send_message(content="You must be
#                 a Nitro Booster to get one of these
#                 roles",
#                                                         ephemeral=True,
#                                                         delete_after=30)
#
#                 return False
#
#     async def callback(self, interaction: discord.Interaction):
#         if interaction.response.is_done():
#             return
#         # Fetch the updated member object for the user who clicked the button
#         updated_member = await
#         interaction.guild.fetch_member(interaction.user.id)
#
#         # Check if the user has the Nitro Booster role
#         nitro_booster_role = discord.utils.get(interaction.guild.roles,
#         name="Nitro Booster")
#         if nitro_booster_role not in updated_member.roles:
#             # Send an ephemeral message informing the user that they need
#             to have the Nitro Booster role to get a
#             custom color role
#
#             await interaction.response.send_message("You must be a Nitro
#             Booster to get one of these roles.",
#                                                     ephemeral=True,
#                                                     delete_after=30)
#             return
#
#         # Find the role associated with the button
#         role_name = interaction.data["custom_id"].replace("_", " ")
#         role = find_role(interaction.guild, role_name)
#
#         if role is not None:
#             if role in updated_member.roles:
#                 try:
#                     await updated_member.remove_roles(role)
#                     await interaction.response.send_message(
#                         f"Successfully removed the {role.name} role from
#                         {updated_member.mention}.", ephemeral=True,
#                         delete_after=30)
#                 except Exception as e:
#                     await send_error_message(interaction, e)
#             else:
#                 try:
#                     await updated_member.add_roles(role)
#                     await interaction.response.send_message(
#                         f"Successfully added the {role.name} role to
#                         {updated_member.mention}.", ephemeral=True,
#                         delete_after=30)
#                 except Exception as e:
#                     await send_error_message(interaction, e)
#         else:
#             await interaction.response.send_message(f"Role '{role_name}'
#             not found on the server.", ephemeral=True,
#                                                     delete_after=30)


# 4. Define functions

def is_hex(value: str) -> bool:
    try:
        int(value, 16)
        return True
    except ValueError:
        return False


def is_valid_image_url(url: str) -> bool:
    allowed_extensions = ('.jpg', '.jpeg', '.png', '.gif')
    return url.lower().endswith(allowed_extensions)


async def get_text_channels(guild: discord.Guild) -> List[discord.TextChannel]:
    return [channel for channel in guild.channels if
            isinstance(channel, discord.TextChannel)]


async def send_error_message(interaction: discord.Interaction, error):
    error_channel_id = os.environ["error_channel_id"]
    error_channel = client.get_channel(error_channel_id)

    print(error)

    if interaction.command is not None:
        command_name = interaction.command.name
        print(command_name)
    else:
        print(
            f"An error occurred in command execution by"
            f" {interaction.user.mention} in {interaction.command}.")


async def search_character(first_name: str, last_name: str, server: str):
    async with aiohttp.ClientSession() as session:
        base_url = "https://xivapi.com/character"
        search_url = f"{base_url}/search"

        completed_url = f"{search_url}?name={first_name} {last_name}&" \
                        f"server={server}"
        async with session.get(completed_url) as response:
            if response.status == 200:
                return await response.json()
            else:
                return None


async def get_character_details(character_id: int):
    async with aiohttp.ClientSession() as session:
        character_url = f"https://xivapi.com/character/{character_id}"
        async with session.get(character_url) as response:
            if response.status == 200:
                return await response.json()
            else:
                return None


def find_role(guild: discord.Guild, role_name: str):
    for role in guild.roles:
        if role.name.lower() == role_name.lower():
            return role
    return None


# 5. Event handlers and command functions
client = MyClient(intents=intents)


@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')


@client.event
async def on_interaction(interaction: discord.Interaction):
    if interaction.response.is_done():
        return

    if interaction.type == discord.InteractionType.component:
        # Fetch the updated member object for the user who clicked the button
        updated_member = await interaction.guild.fetch_member(
            interaction.user.id)

        # Find the role associated with the button
        role_name = interaction.data["custom_id"].replace("_", " ")
        role = find_role(interaction.guild, role_name)

        if role is not None:
            if role in updated_member.roles:
                try:
                    await updated_member.remove_roles(role)
                    await interaction.response.send_message(
                        f"Successfully removed the {role.name} role from "
                        f"{updated_member.mention}.",
                        ephemeral=True,
                        delete_after=30)
                except Exception as e:
                    await send_error_message(interaction, e)
            else:
                try:
                    await updated_member.add_roles(role)
                    await interaction.response.send_message(
                        f"Successfully added the {role.name} role to "
                        f"{updated_member.mention}.",
                        ephemeral=True,
                        delete_after=30)
                except Exception as e:
                    await send_error_message(interaction, e)
        else:
            await interaction.response.send_message(
                f"Role '{role_name}' not found on the server.", ephemeral=True,
                delete_after=30)
    elif interaction.type == discord.InteractionType.application_command:
        # If you have other types of interactions (e.g. slash commands),
        # handle them here
        pass


@client.tree.command()
@app_commands.describe(
    first_name="The first name of the character",
    last_name="The last name of the character",
    server="The server of the character"
)
async def lookup_character(interaction: discord.Interaction, first_name: str,
                           last_name: str, server: str):
    try:
        await interaction.response.defer()
        character_data = await search_character(first_name, last_name, server)
        if character_data:
            results = character_data["Results"]
            if results:
                character = results[0]
                character_id = character["ID"]
                character_details = await get_character_details(character_id)
                main_class = character_details["Character"]["ActiveClassJob"][
                    "Name"]
                main_class_level = \
                    character_details["Character"]["ActiveClassJob"]["Level"]

                embed = discord.Embed(title=character["Name"],
                                      description=f"Server:"
                                                  f" {character['Server']}\n"
                                                  f"Main Class: "
                                                  f"{main_class} "
                                                  f"(Level "
                                                  f"{main_class_level})")
                embed.set_thumbnail(url=character["Avatar"])
                await interaction.edit_original_response(embed=embed)
            else:
                await interaction.edit_original_response(
                    content="No character found.")
        else:
            await interaction.edit_original_response(
                content="An error occurred while looking up the character.")
    except Exception as e:
        await interaction.edit_original_response(
            content="An error occurred while looking up the character.")
        await send_error_message(interaction, e)


@client.tree.command(description="Post role buttons in the specified channel")
@app_commands.describe(
    channel="The target channel for posting role buttons"
)
async def post_role_buttons(interaction: discord.Interaction,
                            channel: discord.TextChannel):
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message(
            "You do not have the required permissions to use this command.",
            ephemeral=True, delete_after=30)
        return

    try:
        guild = interaction.guild
        target_channel = channel

        for category, role_names in role_categories.items():
            category_roles = [role for role in guild.roles if
                              role.name in role_names]

            if category == "XIV Roles":
                message = "Please react to this message according to any " \
                          "roles that you would identify as. Keep in " \
                          "mind we may ping these roles to fill in groups " \
                          "and organize running content together. If " \
                          "you do not want to be pinged, you can mute that " \
                          "in the server settings. "
                view = XIVRolesView(category_roles)
            elif category == "Pronouns":
                message = "Please react to this message according to the " \
                          "pronoun that you wish to be called by. You " \
                          "can repeat this process to remove the role again. "
                view = PronounsView(category_roles)
            elif category == "Channel Access Roles":
                message = "React to this role to gain access to a text " \
                          "channel for discussion of XIV tools (mods, " \
                          "plugins, ACT). \n\n The intent is this role " \
                          "reaction is to provide access to a channel " \
                          "called #current-events which is a space for " \
                          "people to discuss their feelings and thoughts " \
                          "about what’s going on outside Eorzea. There will " \
                          "be a zero tolerance policy for breaking " \
                          "any of the server's rules, and if you are seen " \
                          "glorifying or joking about violence or " \
                          "racism in any way, you may be immediately removed " \
                          "from the FC/Discord. "
                view = ChannelsView(category_roles)
            # elif category == "Custom Color":
            #     message = "NITRO BOOSTER PERK! If you boost our server,
            #     you can select a custom color for your name!"
            #     view = ColorView(category_roles)

            message_text = f"**{category}** \n\n {message}"
            sent_message = await target_channel.send(message_text, view=view)
            client.message_id_store[category] = sent_message.id

        # Save message IDs to data.json
        await interaction.response.send_message(
            "Role buttons posted in the target channel.", ephemeral=True,
            delete_after=30)
        save_message_ids(client)  # Save message IDs to data.json

    except Exception as e:
        await interaction.response.send_message(
            "An error occurred while looking up the character.")
        await send_error_message(interaction, e)


@client.tree.command(description="Send an announcement to a channel")
async def announcement(interaction: discord.IntegrationAccount):
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message(
            "You do not have the required permissions to use this command.",
            ephemeral=True, delete_after=30)
    return

    announcement_modal = SendAnnouncementMessage()
    await interaction.response.send_modal(announcement_modal)


class SendAnnouncementMessage(discord.ui.Modal,
                              title="Send an announcement to a channel"):
    announcement_title = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Title",
        required=True,
        placeholder="Enter Title"
    )

    announcement_message = discord.ui.TextInput(
        style=discord.TextStyle.long,
        label="Message",
        required=True,
        max_length=1024,
        placeholder="Enter your message"
    )

    announcement_url = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Image",
        required=False,
        max_length=100,
        placeholder="Insert a url with an image (should end with .jpg, .png, "
                    "etc"
    )

    announcement_channel_id = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Channel ID",
        required=True,
        placeholder="Insert a channel ID"
    )

    announcement_custom_color = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Custom Color",
        required=False,
        placeholder="Insert a hex color code (e.g. FF0000)",
        min_length=6,
        max_length=6
    )

    async def on_submit(self, interaction: discord.Interaction):
        title = self.announcement_title.value
        message = self.announcement_message.value
        url = self.announcement_url.value
        channel_id = int(self.announcement_channel_id.value)

        if self.announcement_custom_color.value:
            if is_hex(self.announcement_custom_color.value):
                color = discord.Color(
                    int(self.announcement_custom_color.value, 16))
            else:
                await interaction.response.send_message(
                    "Invalid hex color value provided. Please provide a valid"
                    " hex "
                    "color code (e.g. FF0000).",
                    ephemeral=True, delete_after=30)
                return
        else:
            color = discord.Color.green()

        try:
            target_channel = client.get_channel(channel_id)
            if target_channel is not None:
                if isinstance(target_channel, discord.TextChannel):
                    if target_channel.permissions_for(
                            interaction.guild.me).send_messages:
                        embed = discord.Embed(title=title, description=message,
                                              color=color)

                        if url and is_valid_image_url(url):
                            embed.set_image(url=url)

                        await target_channel.send(embed=embed)
                        await interaction.response.send_message(
                            "Announcement sent successfully!", ephemeral=True,
                            delete_after=30)
                    else:
                        await interaction.response.send_message(
                            "I do not have permission to send messages in "
                            "the specified channel.",
                            ephemeral=True,
                            delete_after=30)
                else:
                    await interaction.response.send_message(
                        "The provided ID is not a Text Channel.",
                        ephemeral=True,
                        delete_after=30)
            else:
                await interaction.response.send_message(
                    "Invalid channel ID provided.", ephemeral=True,
                    delete_after=30)
        except Exception as e:
            await interaction.response.send_message(
                "An error occurred while sending the announcement.",
                ephemeral=True,
                delete_after=30)
            await send_error_message(interaction, e)

    async def on_error(self, interaction: discord.Interaction, error):
        print(self, interaction, error)


client.run(os.environ["token"])
