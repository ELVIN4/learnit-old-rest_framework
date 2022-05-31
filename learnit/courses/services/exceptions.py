class PlaylistParseError(Exception):
    """Playlist parse error. """

class YoutubePlaylistParseError(PlaylistParseError):
    """Error to parse youtube playlist. """