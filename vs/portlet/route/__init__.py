from zope.i18nmessageid import MessageFactory
RoutePortletMessageFactory = MessageFactory('vs.portlet.route')


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
