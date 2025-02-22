#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from dotenv import load_dotenv

load_dotenv()

MY_SECRET = os.environ.get( "MY_SECRET" )
