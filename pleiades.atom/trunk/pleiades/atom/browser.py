from pleiades.capgrids import Grid
from zgeo.atom.browser import SubscriptionFeed, LinkEntry, rfc3339
from zgeo.plone.atom.browser import BrainLinkEntry, TopicSubscriptionFeed
from zgeo.geographer.interfaces import IGeoreferenced


class Tagged(object):
    
    @property
    def id(self):
        year = self.context.CreationDate().split('-')[0]
        return 'tag:atlantides.org,%s:pleiades/%s' % (year, self.context.UID())


class TaggedBrain(object):
    
    @property
    def id(self):
        year = self.context.CreationDate.split('-')[0]
        return 'tag:atlantides.org,%s:pleiades/%s' % (year, self.context.UID)


class PleiadesEntry(Tagged, LinkEntry):
    pass


class PlaceFeed(Tagged, SubscriptionFeed):
    
    @property
    def updated(self):
        return rfc3339(self.context.ModificationDate())
    
    @property
    def entries(self):
        x = list(self.context.getLocations())
        if len(x) > 0: # and x[0].getGeometry():
            yield PleiadesEntry(self.context, self.request)
        # if len(x) == 0 or not x[0].getGeometry():
        #     if dc_coverage.startswith('http://atlantides.org/capgrids'):
        #         s = dc_coverage.rstrip('/')
        #         mapid, gridsquare = s.split('/')[-2:]
        #         grid = Grid(mapid, gridsquare)
        #         e = PleiadesEntry(self.context, self.request)
        #         e.geom = IGeoreferenced(grid)
        #         yield e
        for item in self.context.getFeatures():
            yield PleiadesEntry(item, self.request)


class TopicEntry(TaggedBrain, BrainLinkEntry):
    pass

class TopicFeed(Tagged, TopicSubscriptionFeed):
    
    @property
    def entries(self):
        for brain in self.context.queryCatalog():
            yield TopicEntry(brain, self.request)
    