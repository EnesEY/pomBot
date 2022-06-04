
def get_channel_string(channel_id: int):
    channel_string_start = "https://discord.com/api/v9/channels/"
    channel_string_end = "/messages"
    return (channel_string_start + str(channel_id) + channel_string_end)
