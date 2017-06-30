# -*- coding: utf-8 -*- 
import os
import wx
from Ex02_browseFileDlg import browseFile

class browse(browseFile):
    
    deafultPATH = ''
        
    def loadDefaultDIR(self):
        stringPATH = os.path.dirname(os.path.abspath(__file__))
        self.deafultPATH = stringPATH + '\\testFolder'
        print(self.deafultPATH)
        
        
    def onFileChange( self, event ):
        print('User NEW Path')
        
    
    def onCANCEL_Click( self, event ):
        print('User Press CANCEL')
        self.EndModal(wx.ID_CANCEL)
    
    def onOK_Click( self, event ):
        print('User Press OK')
        self.EndModal(wx.ID_OK)

   
app  =  wx.App() 
c    = browse(None)
c.filePicker.SetPath('D:\\')
c.loadDefaultDIR()
c.ShowModal()
app.MainLoop()