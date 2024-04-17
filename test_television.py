import pytest
from television import *


def test_init():
    initTestTT = Television(True, True)
    assert str(initTestTT) == "Power = True, Channel = 0, Volume = 0"

    initTestTF = Television(True, False)
    assert str(initTestTF) == "Power = True, Channel = 0, Volume = 0"

    initTestFT = Television(False, True)
    assert str(initTestFT) == "Power = False, Channel = 0, Volume = 0"

    initTestFF = Television(False, False)
    assert str(initTestFF) == "Power = False, Channel = 0, Volume = 0"

def test_power():
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_mute():
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"
    tv.power()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_channel_up():
    tv = Television()
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"
    tv.channel_up()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_channel_down():
    tv = Television()
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"
    tv.channel_down()
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_volume_down():
    tv = Television()
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.volume_up()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

def test_volume_up():
    tv = Television()
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
    tv.volume_up()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"
