# -*- coding: utf-8 -*-

import eg

eg.RegisterPlugin(
    name = "HTTPRequest",
    author = "David Perry <d.perry@utoronto.ca>",
    version = "0.0.1",
    kind = "other",
    description = "Send HTTP requests.",
    url = "https://github.com/Boolean263/TBD",
    guid = "{dea987ff-3281-4da2-b0e9-c396b4260c37}",
)

import wx
import httplib
from numbers import Number

class HTTPRequest(eg.PluginBase):

    def __init__(self):
        self.AddAction(sendRequest)

    def __start__(self):
        print "HTTPRequest Plugin started"

    #def Configure(self):
    #    panel = eg.ConfigPanel(self)
    #    while panel.Affirmed():
    #        panel.SetResult()

class sendRequest(eg.ActionBase):
    name = "Send HTTP request"
    description = "Sends an HTTP request."

    methods = ("GET", "POST", "HEAD", "PUT", "DELETE")
    body_methods = ("POST", "PUT")

    def __call__(self, host, uri="/", method="GET", body=None, timeout=0, ssl=False, sslVerify=True):
        if uri == "":
            uri = "/"

        if isinstance(method, Number):
            method = self.methods[method]
        elif method not in self.methods:
            raise ValueError("Invalid request method")

        ret_val = dict()
        if ssl:
            conn = httplib.HTTPSConnection(host, timeout=(timeout if timeout > 0 else None), context=(ssl._create_unverified_context() if not sslVerify else None))
        else:
            conn = httplib.HTTPSConnection(host, timeout=(timeout if timeout > 0 else None))
        conn.request(method, uri, body if method in self.body_methods else None)
        ret_val["response"] = conn.getresponse()
        ret_val["data"] = ret_val["response"].read()
        conn.close()
        return ret_val

    def GetLabel(self, host, uri="/", method="GET", body=None, timeout=0, ssl=False, sslVerify=True):
        method = self.methods[method] if isinstance(method, Number) else method
        return "{} {}://{}{}".format(method, "https" if ssl else "http", host, uri)

    def Configure(self, host="192.168.0.1", uri="/", method="GET", body="", timeout=0, ssl=False, sslVerify=True):
        panel = eg.ConfigPanel(self)
        methodCtrl = panel.Choice(method if isinstance(method, Number) else self.methods.index(method), choices=self.methods)
        hostCtrl = panel.TextCtrl(host)
        sslCtrl = panel.CheckBox(ssl, "Use HTTPS")
        sslVerifyCtrl = panel.CheckBox(sslVerify, "Verify certificate")
        timeoutCtrl = panel.SpinIntCtrl(timeout, min=0, max=600)
        uriCtrl = panel.TextCtrl(uri)
        bodyCtrl = panel.TextCtrl("\n\n", style=wx.TE_MULTILINE)
        bodyCtrlHeight = bodyCtrl.GetBestSize()[1]
        bodyCtrl.ChangeValue(body)
        bodyCtrl.SetMinSize((-1, bodyCtrlHeight))

        sizer = wx.GridBagSizer(5, 5)
        expand = wx.EXPAND
        align = wx.ALIGN_CENTER_VERTICAL
        sizer.AddMany([
            (panel.StaticText("Method"), (0, 0), (1, 1), align),
            (methodCtrl, (0, 1), (1, 1), expand),
            (panel.StaticText("Host:Port"), (1, 0), (1, 1), align),
            (hostCtrl, (1, 1), (1, 1), expand),
            (panel.StaticText("URI"), (2, 0), (1, 1), align),
            (uriCtrl, (2, 1), (1, 1), expand),
            (sslCtrl, (3, 1), (1, 1), align),
            (sslVerifyCtrl, (4, 1), (1, 1), align),
            (panel.StaticText("Timeout (seconds)"), (5, 0), (1, 1), align),
            (timeoutCtrl, (5, 1), (1, 1), align),
            (panel.StaticText("POST/PUT Body"), (6, 0), (1, 1), align),
            (bodyCtrl, (6, 1), (1, 1), expand),
        ])
        sizer.AddGrowableCol(1)
        panel.sizer.Add(sizer, 1, expand)

        while panel.Affirmed():
            panel.SetResult(
                hostCtrl.GetValue(),
                uriCtrl.GetValue(),
                methodCtrl.GetValue(),
                bodyCtrl.GetValue(),
                timeoutCtrl.GetValue(),
                sslCtrl.GetValue(),
                sslVerifyCtrl.GetValue()
            )



#
# Editor modelines  -  https://www.wireshark.org/tools/modelines.html
#
# Local variables:
# c-basic-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# coding: utf-8
# End:
#
# vi: set shiftwidth=4 tabstop=4 expandtab fileencoding=utf-8:
# :indentSize=4:tabSize=4:noTabs=true:coding=utf-8:
#
