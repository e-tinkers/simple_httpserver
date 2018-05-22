# Control Raspberry Pi GPIO via http web server

This repository contains python code for demostrating on how to control Raspberry Pi GPIO via a simple http server implemented using python standard library http.server. The http.server library allows user to create its own http request handler class to handle the GET and POST requests.

In the `simple_webserver.py` example provided. the `do_GET()`` method creates an html template which read some data from the Raspberry Pi and provide an html interface for user to interact with the server. The `do_POST()`` method parse the post request sent by the browser and use its value to control the Raspberry Pi GPIO.

In the `simple_webserver2.py` example, it deomonstrates how to handle multiple GET requests based on various URL endpoints.

For more details about the codes, refer to my blog post [How to control Raspberry Pi via http web server](https://www.e-tinkers.com/2018/04/how-to-control-raspberry-pi-gpio-via-http-web-server/).

[YouTube demostration](https://youtu.be/SRf6HW_b3EE)
