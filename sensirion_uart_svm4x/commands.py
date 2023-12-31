#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# (c) Copyright 2023 Sensirion AG, Switzerland
#
#     THIS FILE IS AUTOMATICALLY GENERATED!
#
# Generator:     sensirion-driver-generator 0.33.0
# Product:       svm4x
# Model-Version: 2.0.3
#
"""
The transfer classes specify the data that is transferred between host and sensor. The generated transfer classes
are used by the driver class and not intended for direct use.
"""

from sensirion_driver_adapters.transfer import Transfer
from sensirion_driver_adapters.rx_tx_data import TxData, RxData


class GetProductType(Transfer):
    """Gets the product type from the device."""

    CMD_ID = 0xd0

    def pack(self):
        return self.tx_data.pack([0x0])

    tx = TxData(CMD_ID, '>BB', device_busy_delay=0.05, slave_address=None, ignore_ack=False)
    rx = RxData('>32s')


class GetProductName(Transfer):
    """Gets the product name from the device."""

    CMD_ID = 0xd0

    def pack(self):
        return self.tx_data.pack([0x1])

    tx = TxData(CMD_ID, '>BB', device_busy_delay=0.05, slave_address=None, ignore_ack=False)
    rx = RxData('>8s')


class GetSerialNumber(Transfer):
    """Gets the serial number from the device."""

    CMD_ID = 0xd0

    def pack(self):
        return self.tx_data.pack([0x3])

    tx = TxData(CMD_ID, '>BB', device_busy_delay=0.05, slave_address=None, ignore_ack=False)
    rx = RxData('>32s')


class GetVersion(Transfer):
    """Gets the version information for the hardware, firmware and SHDLC protocol."""

    CMD_ID = 0xd1

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>B', device_busy_delay=0.05, slave_address=None, ignore_ack=False)
    rx = RxData('>BB?BBBB')


class DeviceReset(Transfer):
    """Executs a reset on the device."""

    CMD_ID = 0xd3

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>B', device_busy_delay=0.05, slave_address=None, ignore_ack=False)
    post_processing_time = 0.1


class GetSystemUpTime(Transfer):
    """Get the system up time of the device."""

    CMD_ID = 0x93

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>B', device_busy_delay=0.05, slave_address=None, ignore_ack=False)
    rx = RxData('>I')


class StartMeasurement(Transfer):
    """Starts measurement in polling mode."""

    CMD_ID = 0x0

    def pack(self):
        return self.tx_data.pack([0x0])

    tx = TxData(CMD_ID, '>BB', device_busy_delay=0.05, slave_address=None, ignore_ack=False)


class StopMeasurement(Transfer):
    """Leaves the measurement mode and returns to the idle mode."""

    CMD_ID = 0x1

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>B', device_busy_delay=0.05, slave_address=None, ignore_ack=False)


class ReadMeasuredValuesAsIntegers(Transfer):
    """
    Read measurement data as integers.
    This command is named get_signals in the datasheet.
    """

    CMD_ID = 0x3

    def pack(self):
        return self.tx_data.pack([0x10])

    tx = TxData(CMD_ID, '>BB', device_busy_delay=0.05, slave_address=None, ignore_ack=False)
    rx = RxData('>hhhh')


class ReadMeasuredRawValues(Transfer):
    """
    Read measuremed raw values.
    This command is named get_signals_raw in the datasheet.
    """

    CMD_ID = 0x3

    def pack(self):
        return self.tx_data.pack([0xd])

    tx = TxData(CMD_ID, '>BB', device_busy_delay=0.05, slave_address=None, ignore_ack=False)
    rx = RxData('>hhHH')


class GetTemperatureOffsetForRhtMeasurements(Transfer):
    """
    Gets the T-Offset for the temperature compensation of the RHT algorithm.
    This command is named get_temperature_offset in the datasheet.
    """

    CMD_ID = 0x60

    def pack(self):
        return self.tx_data.pack([0x1])

    tx = TxData(CMD_ID, '>BB', device_busy_delay=0.05, slave_address=None, ignore_ack=False)
    rx = RxData('>h')


class GetVocTuningParameters(Transfer):
    """
    Gets the currently set parameters for customizing the VOC algorithm.
    This command is named get_voc_parameters in the datasheet.
    """

    CMD_ID = 0x60

    def pack(self):
        return self.tx_data.pack([0xd])

    tx = TxData(CMD_ID, '>BB', device_busy_delay=0.05, slave_address=None, ignore_ack=False)
    rx = RxData('>hhhhhh')


class GetNoxTuningParameters(Transfer):
    """
    Gets the currently set parameters for customizing the NOx algorithm.
    This command is named get_nox_parameters in the datasheet.
    """

    CMD_ID = 0x60

    def pack(self):
        return self.tx_data.pack([0xe])

    tx = TxData(CMD_ID, '>BB', device_busy_delay=0.05, slave_address=None, ignore_ack=False)
    rx = RxData('>hhhhhh')


class StoreNvData(Transfer):
    """
    This command stores all parameters previously set with the commands
    set_temperature_offset_for_rht_measurements, set_voc_tuning_parameters and
    set_nox_tuning_parameters to the non-volatile
    memory of SVM4x. These parameters will not be erased
    during reset and will be used by the corresponding algorithms
    after start-up. To reset the storage to factory settings the
    master has to set all parameters to the default values followed
    by a subsequent call of the store_nv_data command.
    This command is named store_input_parameters in the datasheet.
    """

    CMD_ID = 0x60

    def pack(self):
        return self.tx_data.pack([0x80])

    tx = TxData(CMD_ID, '>BB', device_busy_delay=0.05, slave_address=None, ignore_ack=False)


class SetTemperatureOffsetForRhtMeasurements(Transfer):
    """Sets the T-Offset for the temperature compensation of the RHT algorithm."""

    CMD_ID = 0x60

    def __init__(self, t_offset):
        self._t_offset = t_offset

    def pack(self):
        return self.tx_data.pack([0x81, self._t_offset])

    tx = TxData(CMD_ID, '>BBh', device_busy_delay=0.05, slave_address=None, ignore_ack=False)


class SetVocTuningParameters(Transfer):
    """
    Sets parameters to customize the VOC algorithm. This command is only available
    in idle mode.
    This command is named set_voc_parameters in the datasheet.
    """

    CMD_ID = 0x60

    def __init__(self, voc_index_offset, learning_time_offset_hours, learning_time_gain_hours,
                 gating_max_duration_minutes, std_initial, gain_factor):
        self._voc_index_offset = voc_index_offset
        self._learning_time_offset_hours = learning_time_offset_hours
        self._learning_time_gain_hours = learning_time_gain_hours
        self._gating_max_duration_minutes = gating_max_duration_minutes
        self._std_initial = std_initial
        self._gain_factor = gain_factor

    def pack(self):
        return self.tx_data.pack([0x8d, self._voc_index_offset, self._learning_time_offset_hours,
                                 self._learning_time_gain_hours, self._gating_max_duration_minutes, self._std_initial,
                                 self._gain_factor])

    tx = TxData(CMD_ID, '>BBhhhhhh', device_busy_delay=0.05, slave_address=None, ignore_ack=False)


class SetNoxTuningParameters(Transfer):
    """
    Sets parameters to customize the NOx algorithm. This command is only available
    in idle mode.
    This command is named set_nox_parameters in the datasheet.
    """

    CMD_ID = 0x60

    def __init__(self, nox_index_offset, learning_time_offset_hours, learning_time_gain_hours,
                 gating_max_duration_minutes, std_initial, gain_factor):
        self._nox_index_offset = nox_index_offset
        self._learning_time_offset_hours = learning_time_offset_hours
        self._learning_time_gain_hours = learning_time_gain_hours
        self._gating_max_duration_minutes = gating_max_duration_minutes
        self._std_initial = std_initial
        self._gain_factor = gain_factor

    def pack(self):
        return self.tx_data.pack([0x8e, self._nox_index_offset, self._learning_time_offset_hours,
                                 self._learning_time_gain_hours, self._gating_max_duration_minutes, self._std_initial,
                                 self._gain_factor])

    tx = TxData(CMD_ID, '>BBhhhhhh', device_busy_delay=0.05, slave_address=None, ignore_ack=False)


class GetVocState(Transfer):
    """
    Gets the current VOC algorithm state. Retrieved values can be used to set the
    VOC algorithm state to resume operation after a short interruption, skipping
    initial learning phase. This command is only available during measurement mode.
    """

    CMD_ID = 0x61

    def pack(self):
        return self.tx_data.pack([0x8])

    tx = TxData(CMD_ID, '>BB', device_busy_delay=0.05, slave_address=None, ignore_ack=False)
    rx = RxData('>8B')


class SetVocState(Transfer):
    """
    Set previously retrieved VOC algorithm state to resume operation after a short
    interruption, skipping initial learning phase. This command is only available in
    idle mode.
    """

    CMD_ID = 0x61

    def __init__(self, state):
        self._state = state

    def pack(self):
        return self.tx_data.pack([0x88, self._state])

    tx = TxData(CMD_ID, '>BB8B', device_busy_delay=0.05, slave_address=None, ignore_ack=False)
