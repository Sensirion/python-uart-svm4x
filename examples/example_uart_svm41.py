#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# (c) Copyright 2022 Sensirion AG, Switzerland
#
#     THIS FILE IS AUTOMATICALLY GENERATED!
#
# Generator:    sensirion-driver-generator 0.13.1
# Product:      svm41
# Version:      1.0
#

import time
import argparse
from sensirion_shdlc_driver import ShdlcSerialPort
from sensirion_driver_adapters.shdlc_adapter.shdlc_channel import ShdlcChannel
from sensirion_shdlc_svm41.device import Svm41Device
parser = argparse.ArgumentParser()
parser.add_argument('--serial_port', '-p', default='COM1')
args = parser.parse_args()

with ShdlcSerialPort(port=args.serial_port, baudrate=115200) as port:
    channel = ShdlcChannel(port)
    sensor = Svm41Device(channel)
    sensor.device_reset()
    time.sleep(2.0)
    serial_number = sensor.get_serial_number()
    print(f"serial_number: {serial_number}; "
          )
    sensor.start_measurement()
    for i in range(50):
        try:
            time.sleep(1.0)
            (a_humidity, a_temperature, a_voc_index, a_nox_index
             ) = sensor.read_measured_values()
            print(f"a_humidity: {a_humidity}; "
                  f"a_temperature: {a_temperature}; "
                  f"a_voc_index: {a_voc_index}; "
                  f"a_nox_index: {a_nox_index}; "
                  )
        except BaseException:
            continue
    sensor.stop_measurement()