import discord

async def pingCommand(interaction: discord.Interaction):
    await interaction.response.send_message(f"🏓 Pong - 🕐 Latency {interaction.client.latency * 1000} ms")

