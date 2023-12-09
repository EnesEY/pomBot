class URLFactory:
    def create_message_url(channel_id: int) -> str:
        return f"https://discord.com/api/v9/channels/{channel_id}/messages"

    def create_react_with_emoji_url(
        channel_id: int, message_id, emoji_string: str
    ) -> str:
        return f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}/reactions/{emoji_string}/%40me?location=Message"

    def create_mark_own_message_unread_url(channel_id: int, message_id: int) -> str:
        return f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}/ack"

    def create_before_message_url(channel_id: int, message_id: int) -> str:
        return f"https://discord.com/api/v9/channels/{channel_id}/messages?before={message_id}"

    def create_recipients_url(channel_id: int):
        return f"https://discord.com/api/v9/channels/{channel_id}"
