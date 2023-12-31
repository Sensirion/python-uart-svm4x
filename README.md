# Python UART Driver for Sensirion SVM4X

This repository contains the Python driver to communicate with a Sensirion SVM4X sensor over UART using the SHDLC protocol.

<img src="https://raw.githubusercontent.com/Sensirion/python-uart-svm4x/master/images/svm4x.png"
    width="300px" alt="SVM4X picture">

Click [here](https://www.sensirion.com/my-sgp-ek/) to learn more about the Sensirion SVM4X sensor.


The SVM4x evaluation kit covers evaluation of the SGP40 and SGP41 sensors.





## Connect the sensor

You can connect your sensor over the provided USB cable.  
For special setups check out the sensor pinout in the section below.

<details><summary>Sensor pinout</summary>
<p>
<img src="https://raw.githubusercontent.com/Sensirion/python-uart-svm4x/master/images/svm41-pinout-uart.png"
     width="300px" alt="sensor wiring picture">

| *Pin* | *Cable Color* | *Name* | *Description*  | *Comments* |
|-------|---------------|:------:|----------------|------------|
| 1 | red | VDD | Supply Voltage | 3.3 or 5V
| 2 | black | GND | Ground | 
| 3 | green | RX | UART: Transmission pin for communication | 
| 4 | yellow | TX | UART: Receiving pin for communication | 
| 5 | blue | SEL | Interface select | Leave floating or pull to VDD to select UART
| 6 | purple | NC | Do not connect | 


</p>
</details>

## Documentation & Quickstart

See the [documentation page](https://sensirion.github.io/python-uart-svm4x) for an API description and a 
[quickstart](https://sensirion.github.io/python-uart-svm4x/execute-measurements.html) example.


## Contributing

We develop and test this driver using our company internal tools (version
control, continuous integration, code review etc.) and automatically
synchronize the `master` branch with GitHub. But this doesn't mean that we
don't respond to issues or don't accept pull requests on GitHub. In fact,
you're very welcome to open issues or create pull requests :-)

### Check coding style

The coding style can be checked with [`flake8`](http://flake8.pycqa.org/):

```bash
pip install -e .[test]  # Install requirements
flake8                  # Run style check
```

In addition, we check the formatting of files with
[`editorconfig-checker`](https://editorconfig-checker.github.io/):

```bash
pip install editorconfig-checker==2.0.3   # Install requirements
editorconfig-checker                      # Run check
```

## License

See [LICENSE](LICENSE).
