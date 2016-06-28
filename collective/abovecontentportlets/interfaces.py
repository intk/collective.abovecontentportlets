from plone.portlets.interfaces import IPortletAssignmentMapping
from plone.portlets.interfaces import IPortletManager
from plone.portlets.interfaces import IPlacelessPortletManager
from plone.portlets.interfaces import IPortletRenderer
from plone.app.portlets.interfaces import IColumn

class IAboveContentPortlets(IColumn):
    """
    Portlet manager 
    Viewlet that adds this portlet manager above the content
    """

