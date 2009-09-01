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
        x = self.context.getLocations()
        if len(x) > 0:
            yield PleiadesEntry(self.context, self.request)
        for item in self.context.getFeatures():
            yield PleiadesEntry(item, self.request)
