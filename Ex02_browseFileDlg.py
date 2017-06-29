# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class browseFile
###########################################################################

class browseFile ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Select a File", pos = wx.DefaultPosition, size = wx.Size( 549,102 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        Sizers = wx.BoxSizer( wx.VERTICAL )
        
        self.filePicker = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
        Sizers.Add( self.filePicker, 0, wx.ALL|wx.EXPAND, 5 )
        
        sdbSizer = wx.StdDialogButtonSizer()
        self.sdbSizerOK = wx.Button( self, wx.ID_OK )
        sdbSizer.AddButton( self.sdbSizerOK )
        self.sdbSizerCancel = wx.Button( self, wx.ID_CANCEL )
        sdbSizer.AddButton( self.sdbSizerCancel )
        sdbSizer.Realize();
        
        Sizers.Add( sdbSizer, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( Sizers )
        self.Layout()
        
        self.Centre( wx.BOTH )
    
    def __del__( self ):
        pass
    
    