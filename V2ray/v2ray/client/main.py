# -- coding:utf-8--
import multiprocessing
from urllib import request
import os
import shutil
import zipfile
import time
import datetime
import json
import sys
import socket
import uuid
import ssl 
from mod import *

ssl._create_default_https_context = ssl._create_unverified_context

def strat():
    syss = mod.sys.test_sys()
    mod.tool.tool_strat("windows")

strat()