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

from mods import install_v2,lod_del,syss,tool,update

ssl._create_default_https_context = ssl._create_unverified_context

def strat():
	sys1 = syss.test_sys()
	tool.tool_strat(sys1)

strat()