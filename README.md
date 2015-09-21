# crosswalk-webdriver-test-case

We need some test case to test Webdriver. I have some suggestiones will help you to test Webdriver. 
I download some test cases from :https://github.com/SeleniumHQ/selenium/tree/master/py/test/selenium/webdriver/common

These test cases are used to test chromedriver and selenium. We can use them to test xwalkdriver, too. But we have to make some changes.

TEST CASE: 
e.g

import unittest
from selenium.webdriver.remote.webdriver import WebDriver

class NAMETest (unittest.TestCase):

  capabilities = {'loggingPrefs': {},'xwalkOptions': {'binary': '/usr/bin/xwalk','debugPort': '12450'}}
  
  driver = WebDriver('http://127.0.0.1:9515',desired_capabilities = capabilities,keep_alive=True)

  def test(self):
  /*Add your test code*/

if __name__ == '__main__':

  suite = unittest.TestLoader().loadTestsFromTestCase(ApiExampleTest)
  
  unittest.TextTestRunner(verbosity=2).run(suite)

Test cases List:

alerts_tests.py                         --Not do yet

api_example_tests.py                    --PASS

appcache_tests.py                       --Not do yet

children_finding_tests.py               --PASS (ignore "Expected NoSuchElementException")

clear_tests.py                          --Not do yet

click_scrolling_tests.py                --PASS  --Failed in Android(Due to click method not work well for
Android)

click_tests.py                          --FAILED

cookie_tests.py                         --Not do yet

correct_event_firing_tests.py           --Not do yet

driver_element_finding_tests.py         --PASS

element_attribute_tests.py              --PASS  --Failed in Android(Due to click method not work well for Android)

element_equality_tests.py               --PASS

executing_async_javascript_tests.py     --Not do yet

executing_javascript_tests.py           --Not do yet

form_handling_tests.py                  --FAILED (ignore Exception)

frame_switching_tests.py                --Not do yet

implicit_waits_tests.py                 --Not do yet

interactions_tests.py                   --Not do yet

opacity_tests.py                        --Not do yet

page_loading_tests.py                   --Not do yet

page_load_timeout_tests.py              --Not do yet

proxy_tests.py                          --Not do yet

rendered_webelement_tests.py            --Not do yet

repr_tests.py                           --Not do yet

select_class_tests.py                   --FAILED (Some unexpected spaces)

select_element_handling_tests.py        --PASS

stale_reference_tests.py                --Not do yet

takes_screenshots_tests.py              --Not do yet

text_handling_tests.py                  --Not do yet

typing_tests.py                         --Not do yet

visibility_tests.py                     --Not do yet

webdriverwait_tests.py                  --Not do yet

window_switching_tests.py               --Not do yet

window_tests.py                         --Not do yet
