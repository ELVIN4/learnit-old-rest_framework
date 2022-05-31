from typing import NamedTuple, Protocol

from pytube import Playlist as Plist
from pytube.exceptions import PytubeError

from .exceptions import YoutubePlaylistParseError


class PlaylistInfo(NamedTuple):
    img_url: str
    title: str
    views: int
    playlist_id: str
    videos_count: int
    owner: str
    owner_url: str


class Playlist(Protocol):
    """Interface for any playlist service"""

    def info(self) -> PlaylistInfo:
        raise NotImplementedError


class YoutubePlaylist:
    """Youtube playlist parser"""

    def info(self, url: str) -> PlaylistInfo:
        try:
            playlist = Plist(url)
            playlist_img: str = playlist.videos[0].thumbnail_url
            playlist_videos_count = len(playlist)
        except (PytubeError, KeyError):
            raise YoutubePlaylistParseError

        return PlaylistInfo(
            img_url=playlist_img,
            title=playlist.title,
            views=playlist.views,
            playlist_id=playlist.playlist_id,
            videos_count=playlist_videos_count,
            owner=playlist.owner,
            owner_url=playlist.owner_url,
        )


def _playlist_info(url: str, playlist: Playlist) -> PlaylistInfo:
    return playlist.info(url)


def playlist_info(playlist_link: str) -> PlaylistInfo:
    return _playlist_info(playlist_link, YoutubePlaylist)
