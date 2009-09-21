import os

from Acquisition import aq_inner
from pleiades.capgrids import Grid
from plone.app.content.batching import Batch
from Products.CMFCore.utils import getToolByName
from zgeo.atom.browser import FeedBase, SubscriptionFeed, LinkEntry, rfc3339
from zgeo.atom.browser import ViewPageTemplateFile
from zgeo.atom.link import Link
from zgeo.plone.atom.browser import BrainLinkEntry, TopicSubscriptionFeed
from zgeo.geographer.interfaces import IGeoreferenced
from zope.formlib.namedtemplate import NamedTemplate
from zope.formlib.namedtemplate import NamedTemplateImplementation


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


class PlaceArchiveFeed(Tagged, FeedBase):
    # Get data from catalog, paginated.
    __name__ = 'atom-archive-feed'
    template = NamedTemplate('archive-feed-template')
    pagesize = 2000
    
    def __call__(self):
        self.pagenum = int(self.request.get('page', '1'))
        self.pagecount = (len(self.context))/self.pagesize + 1
        if self.pagenum > self.pagecount:
           self.request.response.setStatus(404)
           return "No such page"
        return self.template().encode('utf-8')

    @property
    def links(self):
        url = self.request.getURL()
        links = {
            'alternate': Link(
                            self.context.absolute_url(),
                            rel='alternate',
                            type='text/html'
                            ),
            'self': Link(
                url,
                rel='self',
                type='application/atom+xml'
                )
            }
        if self.pagenum > 1:
            links['previous-archive'] = Link(
                '%s?start=%d' % (url, self.pagenum - 1),
                rel='previous-archive',
                type='application/atom+xml'
                )
        if self.pagenum < self.pagecount:
            links['next-archive'] = Link(
                '%s?start=%d' % (url, self.pagenum + 1),
                rel='next-archive',
                type='application/atom+xml'
                )
        return links

    @property
    def entries(self):
        for item in self.batch:
            yield TopicEntry(item, self.request)
        
    @property
    def batch(self):
        """Batch of Products (brains)."""
        context = aq_inner(self.context)
        search_filter = dict(
            path='/'.join(context.getPhysicalPath()),
            review_state='published',
            portal_type='Place'
            )
        catalog = getToolByName(context, 'portal_catalog')
        brains = catalog.searchResults(search_filter)
        batch = Batch(items=brains, pagesize=2000,
                  pagenumber=self.pagenum, navlistsize=5)
        return batch
            
            
archive_feed_template = NamedTemplateImplementation(
    ViewPageTemplateFile('archive_feed.pt')
    )