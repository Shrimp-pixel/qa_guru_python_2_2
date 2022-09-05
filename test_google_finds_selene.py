from selene.support.shared import browser
from selene import be, have
import pytest


@pytest.fixture(scope='session', autouse=True)
def open_browser():
    browser.config.window_height = 600
    browser.config.window_width = 200


def test_first():
    browser.open('https://google.com/ncr')
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_second():
    browser.open('https://google.com/ncr')
    browser.element('[name="q"]').should(be.blank).type('qwerty').press_enter()
    browser.element('[id="search"]').should_not(have.text('Selene - User-oriented Web UI browser tests in Python'))
