#!/usr/bin/env python

import csv_combiner
import pytest
import pandas as pd
import os

def test_two_small():
    csv_combiner.combine_csv(["accessories.csv", "clothing.csv"], ["email_hash", "category", "filename"], 10**5, "output.csv")
    assert os.path.getsize("output.csv") > 1000
    first_line = pd.read_csv("output.csv", nrows=1)
    assert list(first_line.columns) == ["email_hash", "category", "filename"]

def test_one_empty():
    if os.path.exists("output.csv"):
        os.remove("output.csv")
    csv_combiner.combine_csv(["accessories.csv", "empty_test.csv"], ["email_hash", "category", "filename"], 10**5, "output.csv")
    assert not os.path.exists("output.csv")

def test_both_empty():
    if os.path.exists("output.csv"):
        os.remove("output.csv")
    csv_combiner.combine_csv(["empty_test.csv", "empty_test.csv"], ["email_hash", "category", "filename"], 10**5, "output.csv")
    assert not os.path.exists("output.csv")

def test_one_non_csv():
    if os.path.exists("output.csv"):
        os.remove("output.csv")
    csv_combiner.combine_csv(["accessories.csv", "non_csv_test.csv"], ["email_hash", "category", "filename"], 10**5, "output.csv")
    assert not os.path.exists("output.csv")

def test_one_extra_col():
    if os.path.exists("output.csv"):
        os.remove("output.csv")
    csv_combiner.combine_csv(["accessories.csv", "household_cleaners_extra_col.csv"], ["email_hash", "category", "filename"], 10**5, "output.csv")
    assert not os.path.exists("output.csv")

def test_col_mismatch():
    if os.path.exists("output.csv"):
        os.remove("output.csv")
    csv_combiner.combine_csv(["accessories.csv", "train_timeseries.csv"], ["email_hash", "category", "filename"], 10**5, "output.csv")
    assert not os.path.exists("output.csv")

def test_two_large():
    csv_combiner.combine_csv(["train_timeseries.csv", "train_timeseries.csv"],
                             ["fips","date","PRECTOT","PS","QV2M","T2M","T2MDEW","T2MWET", \
                              "T2M_MAX","T2M_MIN","T2M_RANGE","TS","WS10M","WS10M_MAX","WS10M_MIN", \
                              "WS10M_RANGE","WS50M","WS50M_MAX","WS50M_MIN","WS50M_RANGE","score"], 10**5, "output.csv")
    assert os.path.getsize("output.csv") > 4000000000
    first_line = pd.read_csv("output.csv", nrows=1)
    return list(first_line.columns) == \
           ["fips","date","PRECTOT","PS","QV2M","T2M","T2MDEW","T2MWET","T2M_MAX","T2M_MIN","T2M_RANGE","TS","WS10M","WS10M_MAX","WS10M_MIN", \
            "WS10M_RANGE","WS50M","WS50M_MAX","WS50M_MIN","WS50M_RANGE","score"]
