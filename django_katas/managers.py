from django.db import models
from django.db.models import F, Q, Count, Avg


class ArtistManager(models.Manager):
    def with_tracks_about_love(self):
        '''Returns Artists who have Albums which have tracks whose title
        contains the word "Love".

        Docs:
          topics/db/queries/#lookups-that-span-relationships
        '''
        pass


class AlbumManager(models.Manager):
    def earliest_released(self):
        '''Returns Album with earliest release_date.
        
        Docs:
          ref/models/querysets/#order-by
        '''
        pass


    def with_tracks_about_love(self):
        '''Returns Albums which have tracks whose title contains the word
        "Love".

        Docs:
          topics/db/queries/#lookups-that-span-relationships
        '''
        pass
    

    def released_in_month(self, month):
        '''Returns Albums whose release_date matches the given month.

        Docs:
          ref/models/querysets/#month
        '''
        pass


    def purchased_on_day_of_release(self):
        '''Returns Albums whose purchase_date is equal to the release_date.

        Docs:
          topics/db/queries/#filters-can-reference-fields-on-the-model
          ref/models/expressions/#f-expressions
        '''
        pass


    def purchased_after_day_of_release(self):
        '''Returns Albums whose purchase_date is after the release_date.

        Docs:
          ref/models/expressions/#f-expressions
        '''
        pass


    def with_more_than_one_artist(self):
        '''Returns Albums with more than one Artist.

        Docs:
          topics/db/aggregation/#generating-aggregates-for-each-item-in-a-queryset
        '''
        pass


    def with_highest_rating(self):
        '''Returns Album with highest rating.

        Docs:
          ref/models/querysets/#order-by
        '''
        pass


    def with_highest_average_track_rating(self):
        '''Returns Album with highest average track rating.

        Docs:
          topics/db/aggregation/#generating-aggregates-for-each-item-in-a-queryset
        '''
        pass


class TrackManager(models.Manager):
    def with_five_stars(self):
        '''Returns Tracks with rating of 5

        Docs:
          topics/db/queries/#retrieving-specific-objects-with-filters
        '''
        pass


    def with_more_than_twenty_listens(self):
        '''Returns Tracks with more than 20 listens.

        Docs:
          topics/db/queries/#field-lookups
        '''
        pass


    def n_most_listened_to(self, n):
        '''Returns n Tracks with most listens.

        Docs:
          topics/db/queries/#limiting-querysets
        '''
        pass


    def about_love(self):
        '''Returns Tracks whose title contains the word "Love".

        Docs:
          topics/db/queries/#field-lookups
        '''
        pass


    def not_about_love(self):
        '''Returns Tracks whose title does not contain the word "Love".

        Docs:
          topics/db/queries/#retrieving-specific-objects-with-filters
        '''
        pass


    def with_one_star_or_zero_listens(self):
        '''Returns Tracks which have either 0 listens or a rating of 1 (or
        both).

        Docs:
          topics/db/queries/#complex-lookups-with-q-objects
        '''
        pass
