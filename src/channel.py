import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    YOUTUBE_API_NAME = 'youtube'

    YOUTUBE_API_VERSION = 'v3'

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""

        self.channel_id = channel_id

        api_key: str = os.getenv('YouTube-API')

        youtube = build('youtube', 'v3', developerKey=api_key)

        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""

        api_key: str = os.getenv('YouTube-API')

        youtube = build('youtube', 'v3', developerKey=api_key)

        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()

        print(channel)