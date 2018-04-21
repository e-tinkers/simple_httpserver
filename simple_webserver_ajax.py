import time
import RPi.GPIO as GPIO
from http.server import BaseHTTPRequestHandler, HTTPServer


host_name = '192.168.0.115'    # This should match your Raspberry Pi IP address
host_port = 8000


class MyHandler(BaseHTTPRequestHandler):
    """ A special implementation of BaseHTTPRequestHander for reading data from
        and control GPIO of a Raspberry Pi
    """

    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def _redirect(self, path):
        self.send_response(303)
        self.send_header('Content-type', 'text/html')
        self.send_header('Location', path)
        self.end_headers()

    def do_GET(self):
        html = '''
        <html>
        <body>
        <p>this webpage turn on and turn off LED</p>
        <script src="http://code.jquery.com/jquery-1.12.4.min.js"></script>
        <script>
          function setLED()
            {{
            $.ajax({
              type: "POST",
              url: "http://%s:%s",
              data :"on",
              success: function(response) {
                alert("LED triggered")
              }
            });
          }}
          setLED();
        </script>
        </body>
        </html>
        '''
        self.do_HEAD()
        html=html % (self.server.server_name, self.server.server_port)
        self.wfile.write(html.encode("utf-8"))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])    # Get the size of data
        post_data = self.rfile.read(content_length).decode("utf-8")   # Get the data
        if post_data == "on":
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(18, GPIO.OUT)
            GPIO.output(18, GPIO.HIGH)
            print("LED on")
            time.sleep(2)
            GPIO.output(18, GPIO.LOW)
            print("LED off")
        self._redirect('/')


if __name__ == '__main__':

    http_server = HTTPServer((host_name, host_port), MyHandler)
    print("serving %s:%s" % (host_name, host_port))
    http_server.serve_forever()