# Control Raspberry Pi GPIO using Node-RED

Here are two node-RED flows for controling GPIO and provide the same functionalities as the http server implementation using socket io.

### Control GPIO via node-RED Editor

The `simple-GPIO-flow.json` allows user to read the Raspberry Pi GPU temperature and control the LED that is cnnected to GPIO18 via node-RED Editor.

[![](https://github.com/e-tinkers/simple_httpserver/examples-using-node-red/images/simple_gpio_flow.png)](https://github.com/e-tinkers/simple_httpserver/examples-using-node-red/images/simple_gpio_flow.png)

### Control GPIO via node-RED dashboard

[![](https://github.com/e-tinkers/simple_httpserver/examples-using-node-red/images/simple_gpio_dashboard.png)](https://github.com/e-tinkers/simple_httpserver/examples-using-node-red/images/simple_gpio_dashboard.png)

The `simple-GPIO-dashboard.json` allows user to control via node-RED dashboard. Node-RED dashboad by default is not instaled on Raspberry Pi, to install it.

    cd ~/.node-red
    npm install

The dashboard can be accessed via http://your-rpi-ip:1880/ui, the ui path be default is disabled, edit settings.js to enable it.

    cd ~/.node-red
    nano settings.js

Scroll down to find the line `//ui: { path: "ui" }` and uncomment out the line by deleting the // in front of the line. Pressed ctrl-x to save the file.

For more details about the codes, refer to my blog post [Control Raspberry Pi using Node-RED](https://www.e-tinkers.com/2019/02/control-raspberry-pi-gpio-using-node-red/).
