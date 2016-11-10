# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import newsite.theme


class NewsiteThemeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=newsite.theme)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'newsite.theme:default')


NEWSITE_THEME_FIXTURE = NewsiteThemeLayer()


NEWSITE_THEME_INTEGRATION_TESTING = IntegrationTesting(
    bases=(NEWSITE_THEME_FIXTURE,),
    name='NewsiteThemeLayer:IntegrationTesting'
)


NEWSITE_THEME_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(NEWSITE_THEME_FIXTURE,),
    name='NewsiteThemeLayer:FunctionalTesting'
)


NEWSITE_THEME_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        NEWSITE_THEME_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='NewsiteThemeLayer:AcceptanceTesting'
)
