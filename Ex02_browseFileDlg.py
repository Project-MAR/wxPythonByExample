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

class browseFile ( wx.Dialog ):
    
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 577,90 ), style = wx.DEFAULT_DIALOG_STYLE )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizers = wx.BoxSizer( wx.VERTICAL )
        
        self.filePicker = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
        bSizers.Add( self.filePicker, 1, wx.ALL|wx.EXPAND, 5 )
        
        m_OkCencel_sdbSizer = wx.StdDialogButtonSizer()
        self.m_OkCencel_sdbSizerOK = wx.Button( self, wx.ID_OK )
        m_OkCencel_sdbSizer.AddButton( self.m_OkCencel_sdbSizerOK )
        self.m_OkCencel_sdbSizerCancel = wx.Button( self, wx.ID_CANCEL )
        m_OkCencel_sdbSizer.AddButton( self.m_OkCencel_sdbSizerCancel )
        m_OkCencel_sdbSizer.Realize();
        
        bSizers.Add( m_OkCencel_sdbSizer, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizers )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.filePicker.Bind( wx.EVT_FILEPICKER_CHANGED, self.onFileChange )
        self.m_OkCencel_sdbSizerCancel.Bind( wx.EVT_BUTTON, self.onCANCEL_Click )
        self.m_OkCencel_sdbSizerOK.Bind( wx.EVT_BUTTON, self.onOK_Click )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def onFileChange( self, event ):
        event.Skip()
    
    def onCANCEL_Click( self, event ):
        event.Skip()
    
    def onOK_Click( self, event ):
        event.Skip()
    

