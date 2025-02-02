from spotdl.types import Artist

import pytest


def test_artist_init():
    """
    Test if Artist class initializes correctly.
    """

    artist = Artist(
        name="test",
        songs=[],
        urls=[],
        albums=[],
        genres=[],
        url="test",
    )

    assert artist.name == "test"
    assert artist.url == "test"
    assert artist.songs == []
    assert artist.albums == []
    assert artist.genres == []


def test_artist_wrong_init():
    """
    Test if Artist class raises exception when initialized with wrong parameters.
    """

    with pytest.raises(TypeError):
        Artist(
            name="test",
            songs=[],
            albums=[],
            genres=[],
            url="test",
            wrong_key="test",  # type: ignore
        )


@pytest.mark.vcr()
def test_artist_from_url():
    """
    Test if Artist class can be initialized from url.
    """

    artist = Artist.from_url("https://open.spotify.com/artist/1FPC2zwfMHhrP3frOfaai6")

    assert artist.name == "Kontinuum"
    assert artist.url == "https://open.spotify.com/artist/1FPC2zwfMHhrP3frOfaai6"
    assert len(artist.songs) > 1
    assert len(artist.albums) > 2
    assert len(artist.genres) >= 1
