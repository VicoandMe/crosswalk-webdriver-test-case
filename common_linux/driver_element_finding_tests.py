# Licensed to the Software Freedom Conservancy (SFC) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The SFC licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import unittest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import InvalidSelectorException
from selenium.webdriver.remote.webdriver import WebDriver

class DriverElementFindingTests(unittest.TestCase):
    capabilities = {'loggingPrefs': {},'xwalkOptions': {'binary': '/usr/bin/xwalk','debugPort': '12450'}}
    driver = WebDriver('http://127.0.0.1:9515',desired_capabilities = capabilities,keep_alive=True)

    def testShouldFindElementById(self):
        self._loadSimplePage()
        e = self.driver.find_element_by_id("oneline")
        self.assertEqual("A single line of text", e.text)


    def testShouldFindElementByLinkText(self):
        self._loadSimplePage()
        e = self.driver.find_element_by_link_text("link with leading space")
        self.assertEqual("link with leading space", e.text)


    def testShouldFindElementByName(self):
        self._loadPage("nestedElements")
        e = self.driver.find_element_by_name("div1")
        self.assertEqual("hello world hello world", e.text)

    def testShouldFindElementByXPath(self):
        self._loadSimplePage()
        e = self.driver.find_element_by_xpath("/html/body/p[1]")
        self.assertEqual("A single line of text", e.text)

    def testShouldFindElementByClassName(self):
        self._loadPage("nestedElements")
        e = self.driver.find_element_by_class_name("one")
        self.assertEqual("Span with class of one", e.text)

    def testShouldFindElementByPartialLinkText(self):
        self._loadSimplePage()
        e = self.driver.find_element_by_partial_link_text("leading space")
        self.assertEqual("link with leading space", e.text)

    def testShouldFindElementByTagName(self):
        self._loadSimplePage()
        e = self.driver.find_element_by_tag_name("H1")
        self.assertEqual("Heading", e.text)

    def testShouldFindElementsById(self):
        self._loadPage("nestedElements")
        elements = self.driver.find_elements_by_id("test_id")
        self.assertEqual(2, len(elements))

    def testShouldFindElementsByLinkText(self):
        self._loadPage("nestedElements")
        elements = self.driver.find_elements_by_link_text("hello world")
        self.assertEqual(12, len(elements))

    def testShouldFindElementsByName(self):
        self._loadPage("nestedElements")
        elements = self.driver.find_elements_by_name("form1")
        self.assertEqual(4, len(elements))

    def testShouldFindElementsByXPath(self):
        self._loadPage("nestedElements")
        elements = self.driver.find_elements_by_xpath("//a")
        self.assertEqual(12, len(elements))

    def testShouldFindElementsByClassName(self):
        self._loadPage("nestedElements")
        elements = self.driver.find_elements_by_class_name("one")
        self.assertEqual(3, len(elements))

    def testShouldFindElementsByPartialLinkText(self):
        self._loadPage("nestedElements")
        elements = self.driver.find_elements_by_partial_link_text("world")
        self.assertEqual(12, len(elements))

    def testShouldFindElementsByTagName(self):
        self._loadPage("nestedElements")
        elements = self.driver.find_elements_by_tag_name("a")
        self.assertEqual(12, len(elements))

    def testShouldBeAbleToFindAnElementByCssSelector(self):
        self._loadPage("xhtmlTest")
        element = self.driver.find_element_by_css_selector("div.content")
        self.assertEqual("div", element.tag_name.lower())
        self.assertEqual("content", element.get_attribute("class"))

    def testShouldBeAbleToFindMultipleElementsByCssSelector(self):
        self._loadPage("frameset")
        elements = self.driver.find_elements_by_css_selector("frame")
        self.assertEqual(7, len(elements))

        elements = self.driver.find_elements_by_css_selector("frame#sixth")
        self.assertEqual(1, len(elements))
        self.assertEqual("frame", elements[0].tag_name.lower())
        self.assertEqual("sixth", elements[0].get_attribute("id"))

    def testShouldThrowAnErrorIfUserPassesInInteger(self):
        self._loadSimplePage()
        try:
           self.driver.find_element(By.ID, 333333)
           self.fail("Should have thrown WebDriver Exception")
        except InvalidSelectorException:
            pass #This is expected

    def testShouldThrowAnErrorIfUserPassesInTuple(self):
        self._loadSimplePage()
        try:
           self.driver.find_element((By.ID, 333333))
           self.fail("Should have thrown WebDriver Exception")
        except InvalidSelectorException:
            pass #This is expected

    def testShouldThrowAnErrorIfUserPassesInNone(self):
        self._loadSimplePage()
        try:
           self.driver.find_element(By.ID, None)
           self.fail("Should have thrown WebDriver Exception")
        except InvalidSelectorException:
            pass #This is expected

    def testShouldThrowAnErrorIfUserPassesInInvalidBy(self):
        self._loadSimplePage()
        try:
           self.driver.find_element("css", "body")
           self.fail("Should have thrown WebDriver Exception")
        except InvalidSelectorException:
            pass #This is expected

    def testShouldThrowAnErrorIfUserPassesInIntegerWhenFindElements(self):
        self._loadSimplePage()
        try:
           self.driver.find_elements(By.ID, 333333)
           self.fail("Should have thrown WebDriver Exception")
        except InvalidSelectorException:
            pass #This is expected

    def testShouldThrowAnErrorIfUserPassesInTupleWhenFindElements(self):
        self._loadSimplePage()
        try:
           self.driver.find_elements((By.ID, 333333))
           self.fail("Should have thrown WebDriver Exception")
        except InvalidSelectorException:
            pass #This is expected

    def testShouldThrowAnErrorIfUserPassesInNoneWhenFindElements(self):
        self._loadSimplePage()
        try:
           self.driver.find_elements(By.ID, None)
           self.fail("Should have thrown WebDriver Exception")
        except InvalidSelectorException:
            pass #This is expected

    def testShouldThrowAnErrorIfUserPassesInInvalidByWhenFindElements(self):
        self._loadSimplePage()
        try:
           self.driver.find_elements("css", "body")
           self.fail("Should have thrown WebDriver Exception")
        except InvalidSelectorException:
            pass #This is expected

    def _pageURL(self, name):
        return 'http://127.0.0.1/' + name + '.html'

    def _loadSimplePage(self):
        self._loadPage("simpleTest")

    def _loadPage(self, name):
        self.driver.get(self._pageURL(name))

if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(DriverElementFindingTests)
  unittest.TextTestRunner(verbosity=2).run(suite)
