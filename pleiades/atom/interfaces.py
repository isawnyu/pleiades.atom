from zope.interface import Attribute
from zope.interface import Interface


class IAtomMetadata(Interface):
    """See http://tools.ietf.org/html/rfc4287, section 4.2.6.
    """

    id = Attribute("""atom:id""")
    categories = Attribute("""List of categories""")


class IWritableAtomMetadata(Interface):

    def setId():
        """Set and return a urn:uuid id."""


class IWriteAtomMetadata(IAtomMetadata, IWritableAtomMetadata):
    """Write atomid as well as read."""


class ILink(Interface):
    """See http://tools.ietf.org/html/rfc4287.
    """

    href = Attribute("""A URI""")
    type = Attribute("""Content type of the linked resource""")
    rel = Attribute("""Link relationship: 'alternate', 'self', etc.""")


class IAtomBase(Interface):
    """See http://tools.ietf.org/html/rfc4287.
    """

    author = Attribute("""A mapping with name, URI, and email keys""")
    id = Attribute("""A universally unique identifier""")
    title = Attribute("""A human readable text""")
    updated = Attribute("""A RFC 3339 date/time string""")
    links = Attribute("""A dict of links""")


class IEntry(IAtomBase):
    """See http://tools.ietf.org/html/rfc4287.
    """

    summary = Attribute("""A human readable text summary""")
    updated = Attribute("""A RFC 3339 date/time string""")

    # geographic elements
    coords_georss = Attribute("""GML coordinate encoding of the location""")
    hasLineString = Attribute("""Boolean, True if has a line location""")
    hasPoint = Attribute("""Boolean, True if has a point location""")
    hasPolygon = Attribute("""Boolean, True if has a polygon location""")


class IFeed(IAtomBase):
    """See http://tools.ietf.org/html/rfc4287.
    """

    entries = Attribute("""An iterator over feed entries""")


class ISubscriptionFeed(IFeed):
    """See http://tools.ietf.org/html/rfc5005.

    Must contain a 'previous-archive' link.
    """


class IPagingFeed(IFeed):
    """See http://tools.ietf.org/html/rfc5005.

    Must contain 'first', 'last', 'previous', and 'next' links.
    """


class ISearchFeed(IPagingFeed):

    bounds = Attribute("""A (minx, miny, maxx, maxy) tuple""")
    page = Attribute("""Integer page number""")


class IAtomPubPOSTable(Interface):
    """Marker for collections."""


class IAtomPubPUTable(Interface):
    """Marker for editable members."""


class IAtomPubDELETEable(Interface):
    """Marker for deleteable members."""


class IAtomPublishable(IAtomPubPUTable, IAtomPubDELETEable):
    """Marker."""
