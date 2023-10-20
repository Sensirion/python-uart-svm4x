Execute measurements
====================

The following steps shows how to use this driver to execute a simple measurement on a Windows system.

1. Install the SVM4X sensor driver and all required packages as described in :ref:`Installation`.
2. Connect the SVM4X sensor to your system with the serial USB cable.
3. Run the example script from the root of the repository.

   By default the script assumes the sensor is connected to COM1 serial port. If this is different on your system,
   pass the port in use with the :code:`--serial-port` parameter as outlined below.

   .. sourcecode:: bash

    python examples/example_usage_uart_svm4x.py --serial-port <your COM port>

Example script
--------------

.. literalinclude:: ../examples/example_usage_uart_svm4x.py
    :language: python