from five import grok

from z3c.form import group, field
from zope import schema
from zope.interface import invariant, Invalid
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from plone.dexterity.content import Container

from plone.directives import dexterity, form
from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.namedfile.interfaces import IImageScaleTraversable
from plone.dexterity.browser.view import DefaultView
from zope.interface import implementer

from collective.abovecontentportlets import MessageFactory as _
from datetime import date

from zope.component import queryMultiAdapter
from plone.app.layout.viewlets.common import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getMultiAdapter

class AboveContentPortletsViewlet(ViewletBase):
    index = ViewPageTemplateFile('abovecontentportlets_templates/portlet.pt')

    def update(self):
        super(AboveContentPortletsViewlet, self).update()
        self.year = date.today().year

    def render_abovecontent_portlets(self):
        portlet_manager = getMultiAdapter(
            (self.context, self.request, self.__parent__),
            name='collective.abovecontentportlets'
        )
        portlet_manager.update()
        return portlet_manager.render()