# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from newsite.theme.testing import NEWSITE_THEME_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that newsite.theme is properly installed."""

    layer = NEWSITE_THEME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if newsite.theme is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'newsite.theme'))

    def test_browserlayer(self):
        """Test that INewsiteThemeLayer is registered."""
        from newsite.theme.interfaces import (
            INewsiteThemeLayer)
        from plone.browserlayer import utils
        self.assertIn(INewsiteThemeLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = NEWSITE_THEME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['newsite.theme'])

    def test_product_uninstalled(self):
        """Test if newsite.theme is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'newsite.theme'))

    def test_browserlayer_removed(self):
        """Test that INewsiteThemeLayer is removed."""
        from newsite.theme.interfaces import \
            INewsiteThemeLayer
        from plone.browserlayer import utils
        self.assertNotIn(INewsiteThemeLayer, utils.registered_layers())
