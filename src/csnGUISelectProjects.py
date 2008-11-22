#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
# generated by wxGlade 0.6.3 on Wed Oct 15 18:55:59 2008

import wx
import csnBuild

# begin wxGlade: extracode
# end wxGlade



class Dialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Dialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.checkbox_1 = wx.CheckBox(self, -1, "checkbox_1")
        self.btnClose = wx.Button(self, -1, "Close")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.OnClose, self.btnClose)
        # end wxGlade
        
        self.Bind(wx.EVT_CLOSE, self.OnClose, self)
        
    def __set_properties(self):
        # begin wxGlade: Dialog.__set_properties
        self.SetTitle("Select project types to be included")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Dialog.__do_layout
        sizerItems = wx.BoxSizer(wx.VERTICAL)
        sizerItems.Add(self.checkbox_1, 0, 0, 0)
        sizerItems.Add(self.btnClose, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(sizerItems)
        sizerItems.Fit(self)
        self.Layout()
        # end wxGlade
        self.sizerItems = sizerItems
        
    def ShowItems(self, categories, filter):
        """ 
        Shows all items in categories in a vertical layout as checkboxes.
        Categories that are in filter are unchecked.
        """
        self.sizerItems.Clear()
        self.checkbox_1.Hide()
        self.checkBoxes = dict()
        self.filter = filter
        for category in sorted(categories):
            self.checkBoxes[category] = wx.CheckBox(self, -1, category)
            self.checkBoxes[category].SetValue( not category in filter )
            self.sizerItems.Add(self.checkBoxes[category], 0, 0, 0)

        for super in csnBuild.globalSettings.subCategoriesOf.keys():
            value = True
            for sub in csnBuild.globalSettings.subCategoriesOf[super]:
                    value = value and (not sub in filter)
                    
            self.checkBoxes[super] = wx.CheckBox(self, -1, super)
            self.checkBoxes[super].SetValue( value )
            self.sizerItems.Insert(0, self.checkBoxes[super], 0, 0, 0)
            self.Bind(wx.EVT_CHECKBOX, self.OnSuperCategoryCheckBoxChanged, self.checkBoxes[super])
            
        self.sizerItems.Add(self.btnClose, 1, wx.ALL|wx.EXPAND, 5)
        self.sizerItems.Fit(self)
        self.Layout()
        return self.ShowModal()
        
    def OnSuperCategoryCheckBoxChanged(self, event): # wxGlade: CSnakeOptionsFrame.<event_handler>
        """ 
        Respond to checking a supercategory (such as Tests or Demos). Results in (un)checking all subcategories in that
        supercategory.
        """
        for super in csnBuild.globalSettings.subCategoriesOf.keys():
            value = self.checkBoxes[super].GetValue()
                    
            for cbName in self.checkBoxes.keys():
                if cbName in csnBuild.globalSettings.subCategoriesOf[super]:
                    self.checkBoxes[cbName].SetValue(value)
        
    def OnClose(self, event): # wxGlade: Dialog.<event_handler>
        """ 
        Updates the category filter, based on the current status of the checkbox for each category.
        """
        for category in self.checkBoxes.keys():
            if category in self.filter:
                self.filter.remove(category)
            if not self.checkBoxes[category].GetValue():
                self.filter.append(category)
        self.MakeModal(0)
        self.Destroy()

# end of class Dialog


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    dialog = Dialog(None, -1, "")
    app.SetTopWindow(dialog)
    dialog.Show()
    app.MainLoop()