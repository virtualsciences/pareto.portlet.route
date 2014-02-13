from zope import schema
from zope.formlib import form
from zope.interface import implements


from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider

from vs.portlet.route import RoutePortletMessageFactory as _

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class IRoutePortlet(IPortletDataProvider):
    """ A portlet displaying a (live) route box
    """

    daddr = schema.TextLine(
            title = _(u"Destination address"),
            description = _(u""),
            required = True)


class Assignment(base.Assignment):
    implements(IRoutePortlet)

    daddr = u""

    def __init__(self, daddr=u""):
        self.daddr = daddr

    @property
    def title(self):
        return _(u"Route")


class Renderer(base.Renderer):
    render = ViewPageTemplateFile('route.pt')

    def __init__(self, context, request, view, manager, data):
        base.Renderer.__init__(self, context, request, view, manager, data)

    def route_url(self):
        return 'http://maps.google.com/maps?daddr=%s' % self.data.daddr


class AddForm(base.AddForm):
    form_fields = form.Fields(IRoutePortlet)
    label = _(u"Add Route Portlet")
    description = _(u"This portlet shows a generated route link to Google maps"
                    u" from any start point to the portlet end point.")

    def create(self, data):
        return Assignment(**data)


class EditForm(base.EditForm):
    form_fields = form.Fields(IRoutePortlet)
    label = _(u"Edit Route Portlet")
    description = _(u"This portlet shows a generated route link to Google maps"
                    u" from any start point to the portlet end point.")
