#!/usr/bin/env python

import sys
import json
import pandas as pd
import os

from src.etl import run_etl
from src.data_processing import process_data
from src.logistic_regression import get_pred_regions

if __name__ == "__main__":
    try:
        run_etl()
        process_data()
        get_pred_regions()
    except Exception as e:
        print(f"An error occurred during the process: {e}")