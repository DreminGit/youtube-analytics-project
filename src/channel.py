import json
import os

# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build

# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('YT_API_KEY')

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.service = self.get_service()
        self.channel_data = self.get_channel_data()
        self.title = self.channel_data['snippet']['title']
        self.kind = self.channel_data["kind"][-7:]
        self.description = self.channel_data['snippet']['description']
        #self.url = "https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A"
        self.url = f"https://www.youtube.com/{self.kind}/{self.channel_id}"
        self.subscriber_count = self.channel_data['statistics']['subscriberCount']
        self.video_count = self.channel_data['statistics']['videoCount']
        self.view_count = self.channel_data['statistics']['viewCount']


    @property
    def channel_id(self):
        return self.__channel_id


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = youtube.channels().list(id=self.channel_id, part='id,snippet,statistics').execute()
        return channel