from collections import Counter
from datetime import datetime

from django.test import TestCase

from .models import Artist, Album, Track


class TestManagers(TestCase):
    def setUp(self):
        self.track_ix = 0
        self.album_ix = 0
        self.artist_ix = 0


    def test_00_tracks_with_five_stars(self):
        track1 = self.create_track(rating=5)
        track2 = self.create_track(rating=4)
        track3 = self.create_track(rating=5)

        self.assertItemsEqual(
            [track1, track3],
            Track.objects.with_five_stars()
        )


    def test_01_tracks_with_more_than_twenty_listens(self):
        track1 = self.create_track(listens=19)
        track2 = self.create_track(listens=20)
        track3 = self.create_track(listens=21)

        self.assertItemsEqual(
            [track3],
            Track.objects.with_more_than_twenty_listens()
        )


    def test_02_albums_earliest_released(self):
        album1 = self.create_album(release_date=datetime(2013, 1, 1))
        album2 = self.create_album(release_date=datetime(2014, 1, 1))
        album3 = self.create_album(release_date=datetime(2012, 1, 1))

        self.assertEqual(album3, Album.objects.earliest_released())


    def test_03_tracks_n_most_listened_to(self):
        track1 = self.create_track(listens=19)
        track2 = self.create_track(listens=20)
        track3 = self.create_track(listens=21)

        self.assertItemsEqual(
            [track3],
            Track.objects.n_most_listened_to(1)
        )

        self.assertItemsEqual(
            [track3, track2],
            Track.objects.n_most_listened_to(2)
        )


    def test_04_tracks_about_love(self):
        track1 = self.create_track(title='All you need is love')
        track2 = self.create_track(title='Love me do')
        track3 = self.create_track(title='Yesterday')

        self.assertItemsEqual(
            [track1, track2],
            Track.objects.about_love()
        )


    def test_05_tracks_not_about_love(self):
        track1 = self.create_track(title='All you need is love')
        track2 = self.create_track(title='Love me do')
        track3 = self.create_track(title='Yesterday')

        self.assertItemsEqual(
            [track3],
            Track.objects.not_about_love()
        )


    def test_06_albums_with_tracks_about_love(self):
        album1 = self.create_album()
        album2 = self.create_album()
        self.create_track(title='All you need is love', album=album1)
        self.create_track(title='Yesterday', album=album2)

        self.assertItemsEqual(
            [album1],
            Album.objects.with_tracks_about_love()
        )


    def test_07_artists_with_tracks_about_love(self):
        artist1 = self.create_artist()
        artist2 = self.create_artist()
        album1 = self.create_album(artists=[artist1])
        album2 = self.create_album(artists=[artist2])
        self.create_track(title='All you need is love', album=album1)
        self.create_track(title='Yesterday', album=album2)

        self.assertItemsEqual(
            [artist1],
            Artist.objects.with_tracks_about_love()
        )


    def test_08_albums_released_in_month(self):
        album1 = self.create_album(release_date=datetime(2014, 1, 1))
        album2 = self.create_album(release_date=datetime(2014, 2, 1))
        album3 = self.create_album(release_date=datetime(2014, 3, 1))

        self.assertItemsEqual(
            [album2],
            Album.objects.released_in_month(2)
        )


    def test_09_tracks_with_one_star_or_zero_listens(self):
        track1 = self.create_track(listens=0, rating=3)
        track2 = self.create_track(listens=10, rating=3)
        track3 = self.create_track(listens=10, rating=1)

        self.assertItemsEqual(
            [track1, track3],
            Track.objects.with_one_star_or_zero_listens()
        )


    def test_10_albums_purchased_on_day_of_release(self):
        album1 = self.create_album(
            release_date=datetime(2014, 1, 1),
            purchase_date=datetime(2014, 2, 1)
        )
        album2 = self.create_album(
            release_date=datetime(2014, 2, 1),
            purchase_date=datetime(2014, 2, 1)
        )
        album3 = self.create_album(
            release_date=datetime(2014, 3, 1),
            purchase_date=datetime(2014, 3, 2)
        )

        self.assertItemsEqual(
            [album2],
            Album.objects.purchased_on_day_of_release()
        )


    def test_11_albums_purchased_after_day_of_release(self):
        album1 = self.create_album(
            release_date=datetime(2014, 1, 1),
            purchase_date=datetime(2014, 2, 1)
        )
        album2 = self.create_album(
            release_date=datetime(2014, 2, 1),
            purchase_date=datetime(2014, 2, 1)
        )
        album3 = self.create_album(
            release_date=datetime(2014, 3, 1),
            purchase_date=datetime(2014, 3, 2)
        )

        self.assertItemsEqual(
            [album1, album3],
            Album.objects.purchased_after_day_of_release()
        )


    def test_12_albums_with_more_than_one_artist(self):
        artist1 = self.create_artist()
        artist2 = self.create_artist()
        album1 = self.create_album(artists=[artist1])
        album2 = self.create_album(artists=[artist1, artist2])
        album3 = self.create_album(artists=[artist2])

        self.assertItemsEqual(
            [album2],
            Album.objects.with_more_than_one_artist()
        )


    def test_13_album_with_highest_rating(self):
        album1 = self.create_album(rating=3)
        album2 = self.create_album(rating=5)
        album3 = self.create_album(rating=4)

        self.assertEqual(
            album2,
            Album.objects.with_highest_rating()
        )


    def test_14_album_with_highest_average_track_rating(self):
        album1 = self.create_album()
        album2 = self.create_album()
        self.create_track(album=album1, rating=2)
        self.create_track(album=album1, rating=3)
        self.create_track(album=album2, rating=3)
        self.create_track(album=album2, rating=4)

        self.assertEqual(
            album2,
            Album.objects.with_highest_average_track_rating()
        )


    def create_track(self, **extra_params):
        params = {
            'title': self.get_next_track_title(),
            'rating': 3,
            'listens': 10,
        }

        params.update(extra_params)

        if 'album' not in params:
            params['album'] = self.create_album()

        track = Track(**params)
        track.save()
        return track


    def create_album(self, **extra_params):
        params = {
            'name': self.get_next_album_name(),
            'rating': 3,
            'release_date': datetime(2014, 6, 1),
            'purchase_date': datetime(2014, 6, 2),
        }

        params.update(extra_params)

        if 'artists' in params:
            artists = params.pop('artists')
        else:
            artists = None

        album = Album(**params)
        album.save()

        if artists is not None:
            album.artists = artists
            album.save()

        return album


    def create_artist(self, **extra_params):
        params = {
            'name': self.get_next_artist_name(),
        }

        params.update(extra_params)
        artist = Artist(**params)
        artist.save()
        return artist


    def get_next_track_title(self):
        self.track_ix += 1
        return 'Track {}'.format(self.track_ix)


    def get_next_album_name(self):
        self.album_ix += 1
        return 'Album {}'.format(self.album_ix)


    def get_next_artist_name(self):
        self.artist_ix += 1
        return 'Artist {}'.format(self.artist_ix)


    def assertItemsEqual(self, lhs, rhs):
        '''This method was removed from Python 3.'''
        if Counter(lhs) != Counter(rhs):
            raise AssertionError('Expected {} to equal {}'.format(lhs, rhs))

