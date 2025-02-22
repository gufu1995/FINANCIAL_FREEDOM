#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import config.default as cfg


def main():
	"""
    This is the main entry point for the financial_freedom command.
    """
	my_secret = cfg.MY_SECRET
	print( "Hello from Financial Freedom!" )
	print( f"Here is my secret: {my_secret}" )


if __name__ == "__main__":
	main()
