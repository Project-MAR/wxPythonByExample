# -*- coding: utf-8 -*- 

import wx
from Ex02_browseFileDlg import browseFile
   
app  =  wx.App() 
c    = browseFile(None)
c.ShowModal()
app.MainLoop()