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
script it in Python. (You may still need to use Python if you want to do
anything non-trivial with the result, but at least this plugin takes some
of the grindwork out of the way for you.)

You can specify the following parameters for your HTTP request:

* host (and optionally port, separated with a ':' (colon) character)
* uri (include any URL request parameters here)
* request method -- supports GET, POST, HEAD, PUT, DELETE, OPTIONS, and PATCH
* request body (only for PUT/POST/PATCH)
* timeout
* whether to use SSL
* whether to verify the remote server's SSL certificate

This plugin is really just a pretty wrapper around the wonderful
[requests](http://docs.python-requests.org/en/master/) library, which
is included as part of EventGhost.

## Usage

Adding a HTTPRequest action to your EventGhost macro is no different from
most other actions. The configuration dialog gives you access to every option.

EventGhost variables are automatically expanded in the "Host:Port" and "URI"
fields. You can optionally also have them expanded in the "Body" field by
checking the checkbox beneath it. Variable expansion works by enclosing the
variable name in {curly braces}. (If you need to use an actual curly brace
in any of these fields without it being parsed by EventGhost, double it up,
as in "{{".)

You can also call this plugin as a python function call, though honestly
you'd be better off using `requests.get()` or similar directly. Requests
does the real work.

This action performs the HTTP request, and fetches the whole body immediately
(that is, the parameter `stream=False` is passed to `requests.request()`, and
the connection is `close()`d immediately).
The return value of this action (which gets put into `eg.result` if you
use the GUI) is the
[requests.Response](http://docs.python-requests.org/en/master/api/#requests.Response)
object from the call. The most likely attribute you want from this object
is the text response, as in `eg.result.text`.

## Downloads and Support

Official releases of this plugin are being made available at
[this thread on the EventGhost forums](http://www.eventghost.net/forum/viewtopic.php?f=9&t=9780).
You can also provide
feedback and request support there. This is my first EventGhost plugin
so I look forward to hearing what I should be doing better/differently.

I also accept issues and pull requests from the official GitHub repo for
this project,
[Boolean263/EventGhost-HTTPRequest](https://github.com/Boolean263/EventGhost-HTTPRequest).

## Author

Boolean263, aka David Perry

## Changelog

### v0.1.0 - 2017-08-18

* Switch from httplib to requests (this changed the format of `eg.result`!)
* Allow parsing EventGhost variables in host, uri, and optionally body
* Add support for OPTIONS and PATCH request methods

### v0.0.1 - 2017-08-13

* Initial release
