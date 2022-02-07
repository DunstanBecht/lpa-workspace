#!/usr/bin/env python
# coding: utf-8

from lpa.xrd import code, run

code.clone()

run.make()

run.distribution('input_data', impfmt='txt', expstm='output_data')
