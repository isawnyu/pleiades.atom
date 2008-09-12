from zgeo.atom.browser import SubscriptionFeed, LinkEntry, rfc3339


class PleiadesEntry(LinkEntry):

    @property
    def id(self):
        return 'urn:uuid:%s' % self.context.UID()
    
class PlaceFeed(SubscriptionFeed):

    @property
    def updated(self):
        return rfc3339(self.context.ModificationDate())

    @property
    def entries(self):
        for item in self.context.getRefs('hasFeature'):
            yield PleiadesEntry(item, self.request)
