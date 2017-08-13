# EventGhost-HTTPRequest

This program is not very useful on its own. It's a plugin for
[EventGhost](http://www.eventghost.net/).
EventGhost is an automation tool for MS Windows
which listens for events -- whether user-triggered (like the press of a hotkey)
or system events (such as the screensaver activating) -- and runs actions
you specify. (It's like [Tasker](http://tasker.dinglisch.net/) for Android, or
[Cuttlefish](https://launchpad.net/cuttlefish) for Ubuntu.)

## Description

HTTPRequest is an action plugin for EventGhost. It lets you add an action
to your macros for making an HTTP request to a website without having to
script it in Python. (You will still need to use Python if you want to do
anything with the result, but at least this plugin takes some of the grindwork
out of the way for you.)

You can specify the following parameters for your HTTP request:

* host (and optionally port, separated with a ':' (colon) character)
* uri (include any URL request parameters here)
* request method -- supports GET, POST, HEAD, PUT, and DELETE
* request body (only for PUT or POST)
* timeout
* whether to use SSL
* whether to verify the remote server's SSL certificate

When called, the plugin returns a dict with two entries: "response" containing
the whole [HTTPResponse](https://docs.python.org/2/library/httplib.html#httpresponse-objects)
object returned by `httplib`, and "data" containing the HTTP response body
(i.e., the web page returned by the URL you fetched).

## Downloads and Support

Official releases of this plugin are being made available at
[this thread on the EventGhost forums](http://TODO). You can also provide
feedback and request support there. This is my first EventGhost plugin
so I look forward to hearing what I should be doing better/differently.

I also accept issues and pull requests from the official GitHub repo for
this project,
[Boolean263/EventGhost-HTTPRequest](https://github.com/Boolean263/EventGhost-HTTPRequest).

## Author

Boolean263, aka David Perry

