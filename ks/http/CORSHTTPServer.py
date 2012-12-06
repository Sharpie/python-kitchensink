"""
    A quick extension to the SimpleHTTPServer that allows cross-origin resource
    sharing.

    Based on:

        https://gist.github.com/4063325
"""

import SimpleHTTPServer


class CORSHTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def end_headers(self):
        # The whole reason for this hack.
        self.send_header("Access-Control-Allow-Origin", "*")

        # Business as usual.
        SimpleHTTPServer.SimpleHTTPRequestHandler.end_headers(self)


if __name__ == '__main__':
    SimpleHTTPServer.test(HandlerClass=CORSHTTPRequestHandler)
