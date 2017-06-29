# -*- coding: utf-8 -*- 

import wx
from Ex02_browseFileDlg import browseFile
   
app = wx.App(False)
frame = browseFile(None)
frame.Show(True)

app.MainLoop()