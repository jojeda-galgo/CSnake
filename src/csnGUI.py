#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
# generated by wxGlade 0.5 on Sat Sep 15 14:23:13 2007 from D:\Users\Maarten\Projects\Gimias\Prog\GIMIAS.cmake\GBuild\csnGUI.wxg

import csnGenerator
import wx
import csnGUIOptions
import csnGUISelectProjects
import csnGUIHandler
import csnBuild
import csnUtility
import os.path
import sys
import subprocess
from optparse import OptionParser

class RedirectText:
    """
    Used to redirect messages to stdout to the text control in CSnakeGUIFrame.
    """
    def __init__(self,aWxTextCtrl):
		self.out=aWxTextCtrl

    def write(self,string):
		self.out.WriteText(string)

class CSnakeGUIFrame(wx.Frame):
    """
    The main application frame.
    """
    def __init__(self, *args, **kwds):
        # begin wxGlade: CSnakeGUIFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.panelProjectAndInstance = wx.Panel(self, -1)
        self.panelThirdParty = wx.Panel(self, -1)
        self.panelKDevelop = wx.Panel(self.panelThirdParty, -1)
        self.panelSource = wx.Panel(self, -1)
        
        # Menu Bar
        self.frmCSnakeGUI_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        self.mnuLoadSettings = wx.MenuItem(wxglade_tmp_menu, wx.NewId(), "Load Settings", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.mnuLoadSettings)
        self.mnuSaveSettingsAs = wx.MenuItem(wxglade_tmp_menu, wx.NewId(), "Save Settings As...", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.mnuSaveSettingsAs)
        self.mnuExit = wx.MenuItem(wxglade_tmp_menu, wx.NewId(), "Exit", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.mnuExit)
        self.frmCSnakeGUI_menubar.Append(wxglade_tmp_menu, "File")
        wxglade_tmp_menu = wx.Menu()
        self.mnuEditOptions = wx.MenuItem(wxglade_tmp_menu, wx.NewId(), "Edit Options", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.mnuEditOptions)
        self.frmCSnakeGUI_menubar.Append(wxglade_tmp_menu, "Options")
        self.SetMenuBar(self.frmCSnakeGUI_menubar)
        # Menu Bar end
        self.label_1 = wx.StaticText(self, -1, "Root Folders ")
        self.lbRootFolders = wx.ListBox(self, -1, choices=[], style=wx.LB_SINGLE)
        self.btnAddRootFolder = wx.Button(self, -1, "Add")
        self.btnRemoveRootFolder = wx.Button(self, -1, "Remove")
        self.label_1_copy = wx.StaticText(self.panelSource, -1, "Bin Folder\n")
        self.txtBinFolder = wx.TextCtrl(self.panelSource, -1, "")
        self.btnSelectBinFolder = wx.Button(self.panelSource, -1, "...")
        self.label_2 = wx.StaticText(self.panelSource, -1, "Install Folder\n")
        self.txtInstallFolder = wx.TextCtrl(self.panelSource, -1, "")
        self.btnSelectInstallFolder = wx.Button(self.panelSource, -1, "...")
        self.label_1_copy_1 = wx.StaticText(self.panelThirdParty, -1, "ThirdParty Root Folder")
        self.txtThirdPartyRootFolder = wx.TextCtrl(self.panelThirdParty, -1, "")
        self.btnSelectThirdPartyRootFolder = wx.Button(self.panelThirdParty, -1, "...")
        self.label_1_copy_copy = wx.StaticText(self.panelThirdParty, -1, "ThirdParty Bin Folder\n")
        self.txtThirdPartyBinFolder = wx.TextCtrl(self.panelThirdParty, -1, "")
        self.btnSelectThirdPartyBinFolder = wx.Button(self.panelThirdParty, -1, "...")
        self.label_2_copy = wx.StaticText(self.panelKDevelop, -1, "KDevelop Project Folder\n\n")
        self.txtKDevelopProjectFolder = wx.TextCtrl(self.panelKDevelop, -1, "")
        self.btnSelectKDevelopProjectFolder = wx.Button(self.panelKDevelop, -1, "...")
        self.lbCSnakeFile = wx.StaticText(self.panelProjectAndInstance, -1, "CSnake File\n")
        self.cmbCSnakeFile = wx.ComboBox(self.panelProjectAndInstance, -1, choices=[], style=wx.CB_DROPDOWN)
        self.btnSelectCSnakeFile = wx.Button(self.panelProjectAndInstance, -1, "...")
        self.labelInstance = wx.StaticText(self.panelProjectAndInstance, -1, "Instance")
        self.cmbInstance = wx.ComboBox(self.panelProjectAndInstance, -1, choices=[], style=wx.CB_DROPDOWN)
        self.btnUpdateListOfTargets = wx.Button(self.panelProjectAndInstance, -1, "Update")
        self.textLog = wx.TextCtrl(self, -1, "", style=wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_WORDWRAP)
        self.btnDoAction = wx.Button(self, -1, "Do -->")
        self.cmbAction = wx.ComboBox(self, -1, choices=["Create CMake files and run CMake", "Only create CMake files", "Install files to Bin Folder", "Configure ThirdParty Folder"], style=wx.CB_DROPDOWN)
        self.btnSelectProjects = wx.Button(self, -1, "Select projects")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_MENU, self.OnLoadSettings, self.mnuLoadSettings)
        self.Bind(wx.EVT_MENU, self.OnSaveSettingsAs, self.mnuSaveSettingsAs)
        self.Bind(wx.EVT_MENU, self.OnExit, self.mnuExit)
        self.Bind(wx.EVT_MENU, self.OnEditOptions, self.mnuEditOptions)
        self.Bind(wx.EVT_BUTTON, self.OnAddRootFolder, self.btnAddRootFolder)
        self.Bind(wx.EVT_BUTTON, self.OnRemoveRootFolder, self.btnRemoveRootFolder)
        self.Bind(wx.EVT_BUTTON, self.OnSelectBinFolder, self.btnSelectBinFolder)
        self.Bind(wx.EVT_BUTTON, self.OnSelectInstallFolder, self.btnSelectInstallFolder)
        self.Bind(wx.EVT_BUTTON, self.OnSelectThirdPartyRootFolder, self.btnSelectThirdPartyRootFolder)
        self.Bind(wx.EVT_BUTTON, self.OnSelectThirdPartyBinFolder, self.btnSelectThirdPartyBinFolder)
        self.Bind(wx.EVT_BUTTON, self.OnSelectKDevelopProjectFolder, self.btnSelectKDevelopProjectFolder)
        self.Bind(wx.EVT_COMBOBOX, self.OnSelectRecentlyUsed, self.cmbCSnakeFile)
        self.Bind(wx.EVT_BUTTON, self.OnSelectCSnakeFile, self.btnSelectCSnakeFile)
        self.Bind(wx.EVT_BUTTON, self.OnUpdateListOfTargets, self.btnUpdateListOfTargets)
        self.Bind(wx.EVT_BUTTON, self.OnButtonDo, self.btnDoAction)
        self.Bind(wx.EVT_BUTTON, self.OnButtonSelectProjects, self.btnSelectProjects)
        # end wxGlade
        
        self.Bind(wx.EVT_CLOSE, self.OnExit, self)
        
        self.txtBinFolder.Bind(wx.EVT_KILL_FOCUS, self.OnKillFocus, self.txtBinFolder)        
        self.txtInstallFolder.Bind(wx.EVT_KILL_FOCUS, self.OnKillFocus, self.txtInstallFolder)        
        self.txtThirdPartyRootFolder.Bind(wx.EVT_KILL_FOCUS, self.OnKillFocus, self.txtThirdPartyRootFolder)        
        self.txtThirdPartyBinFolder.Bind(wx.EVT_KILL_FOCUS, self.OnKillFocus, self.txtThirdPartyBinFolder)        
        self.txtKDevelopProjectFolder.Bind(wx.EVT_KILL_FOCUS, self.OnKillFocus, self.txtKDevelopProjectFolder)        
        
    def __set_properties(self):
        # begin wxGlade: CSnakeGUIFrame.__set_properties
        self.SetTitle("CSnake GUI")
        self.SetSize((750, 567))
        self.label_1.SetBackgroundColour(wx.Colour(236, 233, 216))
        self.label_1_copy.SetMinSize((100, 15))
        self.txtBinFolder.SetMinSize((-1, -1))
        self.txtBinFolder.SetToolTipString("This is the location where CSnake will generate the \"make files\".")
        self.btnSelectBinFolder.SetMinSize((30, -1))
        self.label_2.SetMinSize((100, 15))
        self.txtInstallFolder.SetMinSize((-1, -1))
        self.txtInstallFolder.SetToolTipString("This is the location where CSnake will generate the \"make files\".")
        self.btnSelectInstallFolder.SetMinSize((30, -1))
        self.label_1_copy_1.SetMinSize((120, 15))
        self.txtThirdPartyRootFolder.SetMinSize((-1, -1))
        self.txtThirdPartyRootFolder.SetToolTipString("Optional field for the root of the source tree that contains the Project Folder. CSnake will search this source tree for other projects.")
        self.btnSelectThirdPartyRootFolder.SetMinSize((30, -1))
        self.label_1_copy_copy.SetMinSize((120, 15))
        self.txtThirdPartyBinFolder.SetMinSize((-1, -1))
        self.txtThirdPartyBinFolder.SetToolTipString("This is the location where CSnake will generate the \"make files\".")
        self.btnSelectThirdPartyBinFolder.SetMinSize((30, -1))
        self.label_2_copy.SetMinSize((120, 15))
        self.label_2_copy.SetBackgroundColour(wx.Colour(236, 233, 216))
        self.txtKDevelopProjectFolder.SetMinSize((-1, -1))
        self.txtKDevelopProjectFolder.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.txtKDevelopProjectFolder.SetToolTipString("This is the location where CSnake will generate the \"make files\".")
        self.btnSelectKDevelopProjectFolder.SetMinSize((30, -1))
        self.panelThirdParty.SetBackgroundColour(wx.Colour(236, 233, 216))
        self.lbCSnakeFile.SetMinSize((100, 15))
        self.btnSelectCSnakeFile.SetMinSize((30, -1))
        self.labelInstance.SetMinSize((100, 15))
        self.panelProjectAndInstance.SetBackgroundColour(wx.Colour(192, 191, 255))
        self.textLog.SetMinSize((100, 50))
        self.btnDoAction.SetMinSize((100, -1))
        self.cmbAction.SetSelection(0)
        # end wxGlade
        
        self.Initialize()
        
    def RedirectStdOut(self):
        # redirect std out
        redir=RedirectText(self.textLog)
        sys.stdout=redir
        sys.stderr=redir

    def PrintWelcomeMessages(self):
        print "CSnakeGUI loaded.\n"
        print "CSnake version = %s\n" % csnBuild.version

    def CreateMemberVariables(self):
        self.settings = csnGenerator.Settings()
        self.handler = csnGUIHandler.Handler(self.settings)
        
    def CreateOptionsFilenameAndOptionsMemberVariable(self):
        # find out location of application options file
        thisFolder = "%s" % (os.path.dirname(sys.argv[0]))
        thisFolder = thisFolder.replace("\\", "/")
        if thisFolder == "":
            thisFolder = "."
        self.optionsFilename = "%s/options" % thisFolder
        
        # create options
        self.options = csnGUIOptions.Options()
        self.options.currentGUISettingsFilename = "%s/settings" % thisFolder

    def InitializeOptions(self):
        # load options from options file
        self.LoadOptions()
        
        # Write the default options to the options file, and pass them to the handler
        self.WriteOptions()
        self.PassOptionsToHandler()

        iconFile = csnUtility.GetRootOfCSnake() + "/resources/Laticauda_colubrina.ico"
        icon1 = wx.Icon(iconFile, wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon1)
        
    def InitializeSettings(self):        
        # load previously saved settings
        if len(self.commandLineArgs) >= 1:
            self.LoadSettings(self.commandLineArgs[0])
        else:
            self.LoadSettings()
        self.lbRootFolders.SetSelection(self.lbRootFolders.GetCount()-1)

    def ParseCommandLine(self):
        parser = OptionParser()
        parser.add_option("-c", "--console", dest="console", default=False,
                          help="print all messages to the console window")
        (self.commandLineOptions, self.commandLineArgs) = parser.parse_args()
    
    def Initialize(self):
        """
        Initializes the application.
        """
        self.ParseCommandLine()
        if not self.commandLineOptions.console:
            self.RedirectStdOut()
        self.PrintWelcomeMessages()
        self.CreateMemberVariables()  
        self.CreateOptionsFilenameAndOptionsMemberVariable()
        self.InitializeOptions()    
        self.InitializeSettings()            

    def StoreSettingsFilename(self, lastUsedSettingsFile):
        """
        Write location of last used config settings to the application options file. 
        """
        self.options.currentGUISettingsFilename = lastUsedSettingsFile
        self.WriteOptions()
        
    def WriteOptions(self):
        """
        Write options to the application options file, and passes them to the handler. 
        """
        self.options.Save(self.optionsFilename)

    def PassOptionsToHandler(self):
        return self.handler.SetOptions(self.options)
        
    def LoadOptions(self):
        """
        Load options from the application options file. 
        """
        return self.options.Load(self.optionsFilename)
        
    def __do_layout(self):
        # begin wxGlade: CSnakeGUIFrame.__do_layout
        boxSettings = wx.BoxSizer(wx.VERTICAL)
        boxBuildProject = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        boxRootFolder_copy = wx.BoxSizer(wx.HORIZONTAL)
        boxProjectPath = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        boxKDevelopProjectFolder = wx.BoxSizer(wx.HORIZONTAL)
        boxThirdPartyBinFolder = wx.BoxSizer(wx.HORIZONTAL)
        boxThirdPartyRoot = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        boxInstallFolder = wx.BoxSizer(wx.HORIZONTAL)
        boxBinFolder = wx.BoxSizer(wx.HORIZONTAL)
        boxRootFolder = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        boxRootFolder.Add(self.label_1, 0, wx.RIGHT|wx.EXPAND, 0)
        boxRootFolder.Add(self.lbRootFolders, 4, wx.EXPAND|wx.FIXED_MINSIZE, 0)
        boxRootFolder.Add(sizer_4, 0, wx.EXPAND, 0)
        sizer_5.Add(self.btnAddRootFolder, 3, wx.EXPAND, 0)
        sizer_5.Add(self.btnRemoveRootFolder, 3, wx.EXPAND, 0)
        boxRootFolder.Add(sizer_5, 1, wx.EXPAND|wx.ALIGN_RIGHT, 0)
        boxSettings.Add(boxRootFolder, 0, wx.EXPAND, 0)
        boxBinFolder.Add(self.label_1_copy, 0, wx.RIGHT|wx.EXPAND, 5)
        boxBinFolder.Add(self.txtBinFolder, 2, wx.FIXED_MINSIZE, 0)
        boxBinFolder.Add(self.btnSelectBinFolder, 0, 0, 0)
        sizer_1.Add(boxBinFolder, 0, wx.EXPAND, 0)
        boxInstallFolder.Add(self.label_2, 0, wx.RIGHT|wx.EXPAND, 5)
        boxInstallFolder.Add(self.txtInstallFolder, 2, wx.FIXED_MINSIZE, 0)
        boxInstallFolder.Add(self.btnSelectInstallFolder, 0, 0, 0)
        sizer_1.Add(boxInstallFolder, 1, wx.EXPAND, 0)
        self.panelSource.SetSizer(sizer_1)
        boxSettings.Add(self.panelSource, 0, wx.EXPAND, 0)
        boxThirdPartyRoot.Add(self.label_1_copy_1, 0, wx.RIGHT|wx.EXPAND, 5)
        boxThirdPartyRoot.Add(self.txtThirdPartyRootFolder, 2, wx.FIXED_MINSIZE, 0)
        boxThirdPartyRoot.Add(self.btnSelectThirdPartyRootFolder, 0, 0, 0)
        sizer_2.Add(boxThirdPartyRoot, 1, wx.EXPAND, 0)
        boxThirdPartyBinFolder.Add(self.label_1_copy_copy, 0, wx.RIGHT|wx.EXPAND, 5)
        boxThirdPartyBinFolder.Add(self.txtThirdPartyBinFolder, 2, wx.FIXED_MINSIZE, 0)
        boxThirdPartyBinFolder.Add(self.btnSelectThirdPartyBinFolder, 0, 0, 0)
        sizer_2.Add(boxThirdPartyBinFolder, 1, wx.EXPAND, 0)
        boxKDevelopProjectFolder.Add(self.label_2_copy, 0, wx.RIGHT|wx.EXPAND, 5)
        boxKDevelopProjectFolder.Add(self.txtKDevelopProjectFolder, 2, wx.FIXED_MINSIZE, 0)
        boxKDevelopProjectFolder.Add(self.btnSelectKDevelopProjectFolder, 0, 0, 0)
        self.panelKDevelop.SetSizer(boxKDevelopProjectFolder)
        sizer_2.Add(self.panelKDevelop, 1, wx.EXPAND, 0)
        self.panelThirdParty.SetSizer(sizer_2)
        boxSettings.Add(self.panelThirdParty, 0, wx.EXPAND, 0)
        boxProjectPath.Add(self.lbCSnakeFile, 0, wx.RIGHT|wx.EXPAND, 5)
        boxProjectPath.Add(self.cmbCSnakeFile, 1, 0, 0)
        boxProjectPath.Add(self.btnSelectCSnakeFile, 0, 0, 0)
        sizer_3.Add(boxProjectPath, 0, wx.EXPAND, 0)
        boxRootFolder_copy.Add(self.labelInstance, 0, wx.RIGHT|wx.EXPAND, 5)
        boxRootFolder_copy.Add(self.cmbInstance, 1, wx.EXPAND, 0)
        boxRootFolder_copy.Add(self.btnUpdateListOfTargets, 0, 0, 0)
        sizer_3.Add(boxRootFolder_copy, 1, wx.EXPAND, 0)
        self.panelProjectAndInstance.SetSizer(sizer_3)
        boxSettings.Add(self.panelProjectAndInstance, 0, wx.EXPAND, 0)
        boxSettings.Add(self.textLog, 1, wx.TOP|wx.BOTTOM|wx.EXPAND, 5)
        boxBuildProject.Add(self.btnDoAction, 0, 0, 0)
        boxBuildProject.Add(self.cmbAction, 2, 0, 0)
        boxBuildProject.Add(self.btnSelectProjects, 0, 0, 0)
        boxSettings.Add(boxBuildProject, 0, wx.EXPAND, 0)
        self.SetSizer(boxSettings)
        self.Layout()
        # end wxGlade

        sizer_1.Remove(boxInstallFolder)
        
    def CopyGUIToSettings(self):
        self.settings.buildFolder = self.txtBinFolder.GetValue().replace("\\", "/")
        self.settings.installFolder = self.txtInstallFolder.GetValue().replace("\\", "/")
        self.settings.thirdPartyBinFolder = self.txtThirdPartyBinFolder.GetValue().replace("\\", "/")
        self.settings.kdevelopProjectFolder = self.txtKDevelopProjectFolder.GetValue().replace("\\", "/")
        self.settings.prebuiltBinariesFolder = ""
        self.settings.csnakeFile = self.cmbCSnakeFile.GetValue().replace("\\", "/")
        self.settings.rootFolders = []
        for i in range( self.lbRootFolders.GetCount() ):
            self.settings.rootFolders.append( self.lbRootFolders.GetString(i).replace("\\", "/") )
        self.settings.thirdPartyRootFolder = self.txtThirdPartyRootFolder.GetValue().replace("\\", "/")
        self.settings.instance = self.cmbInstance.GetValue()
    
    def SaveSettings(self, filename = ""):
        """
        Copy settings from the widget controls to self.settings.
        If filename is not "", save current configuration settings (source folder/bin folder/etc) 
        to filename.
        """
        self.CopyGUIToSettings()
        if not filename == "":
            self.settings.Save(filename)
            # record the settings filename in self.optionsFilename
            self.StoreSettingsFilename(filename)
    
    def OnButtonDo(self, event): # wxGlade: CSnakeGUIFrame.<event_handler>
        """
        Perform action specified in cmbAction.
        """
        
        self.textLog.Clear()
        self.textLog.Update()
        print "\n--- Working, patience please... ---"
        self.CopyGUIToSettings()
        configureProject = self.cmbAction.GetValue() in ("Only create CMake files", "Create CMake files and run CMake")
        alsoRunCMake = self.cmbAction.GetValue() in ("Create CMake files and run CMake")
        configureThirdPartyFolder = self.cmbAction.GetValue() in ("Configure ThirdParty Folder")

        # write application options, and pass them to the handler
        self.WriteOptions()
        if self.PassOptionsToHandler():
        
            try:
                # if configuring the target project...            
                if configureProject:
                    if self.handler.ConfigureProjectToBinFolder(alsoRunCMake):
                        if self.settings.instance.lower() == "gimias":
                            self.ProposeToDeletePluginDlls()
                        if self.options.askToLaunchVisualStudio:
                            self.AskToLaunchVisualStudio( self.handler.GetTargetSolutionPath() )
        
                # if installing dlls to the bin folder            
                copyDlls = self.cmbAction.GetValue() in ("Install files to Bin Folder")
                if copyDlls:
                    if not self.handler.InstallBinariesToBinFolder():
                        print "Error while installing files.\n"
                        
                # if configuring the third party folder            
                if( configureThirdPartyFolder ):
                    self.handler.ConfigureThirdPartyFolder()
                    if self.options.askToLaunchVisualStudio:
                        self.AskToLaunchVisualStudio( self.handler.GetThirdPartySolutionPath() )

            except AssertionError, e:
                print str(e) + '\n'
                
        print "--- Done ---\n"
        self.RefreshGUI()
        #self.Restart()
        
    def Restart(self):
        arglist = []
        if( os.path.splitext(os.path.basename(sys.executable))[0].lower() == "python" ):
            arglist = [sys.executable]
            arglist.extend(sys.argv)
        os.execv(sys.executable, arglist)
                
    def OnKillFocus(self, event):
        self.settings.buildFolder = self.txtBinFolder.GetValue()
        self.settings.thirdPartyBinFolder = self.txtThirdPartyBinFolder.GetValue()
        self.settings.installFolder = self.txtInstallFolder.GetValue()
        self.settings.thirdPartyRootFolder = self.txtThirdPartyRootFolder.GetValue()
        self.settings.kdevelopProjectFolder = self.txtKDevelopProjectFolder.GetValue()
        if os.path.exists(self.options.currentGUISettingsFilename):
            self.SaveSettings(self.options.currentGUISettingsFilename)
    
    def OnSelectBinFolder(self, event): # wxGlade: CSnakeGUIFrame.<event_handler>
        """
        Select folder where project binaries must be placed.
        """
        dlg = wx.DirDialog(None, "Select Binary Folder")
        if dlg.ShowModal() == wx.ID_OK:
            self.settings.buildFolder = dlg.GetPath()
            self.RefreshGUI()

    def OnSelectThirdPartyBinFolder(self, event): # wxGlade: CSnakeGUIFrame.<event_handler>
        """
        Select folder where third party binaries must be placed.
        """
        dlg = wx.DirDialog(None, "Select Third Party Binary Folder")
        if dlg.ShowModal() == wx.ID_OK:
            self.settings.thirdPartyBinFolder = dlg.GetPath()
            self.RefreshGUI()
            
    def OnSelectInstallFolder(self, event): # wxGlade: CSnakeGUIFrame.<event_handler>
        """
        Select folder where application binaries are installed when building the INSTALL target.
        """
        dlg = wx.DirDialog(None, "Select Install Folder")
        if dlg.ShowModal() == wx.ID_OK:
            self.settings.installFolder = dlg.GetPath()
            self.RefreshGUI()

    def OnSelectThirdPartyRootFolder(self, event): # wxGlade: CSnakeGUIFrame.<event_handler>
        """
        Select folder where third party sources are found.
        """
        dlg = wx.DirDialog(None, "Select Third Party Root Folder")
        if dlg.ShowModal() == wx.ID_OK:
            self.settings.thirdPartyRootFolder = dlg.GetPath()
            self.RefreshGUI()

    def OnSelectCSnakeFile(self, event): # wxGlade: CSnakeGUIFrame.<event_handler>
        """
        Select file containing the project that should be configured.
        """
        dlg = wx.FileDialog(None, "Select CSnake file", wildcard = "*.py")
        if dlg.ShowModal() == wx.ID_OK:
            self.settings.csnakeFile = dlg.GetPath()
            self.RefreshGUI()

    def OnSelectKDevelopProjectFolder(self, event): # wxGlade: CSnakeGUIFrame.<event_handler>
        dlg = wx.DirDialog(None, "Select folder for saving the KDevelop project file")
        if dlg.ShowModal() == wx.ID_OK:
            self.settings.kdevelopProjectFolder = dlg.GetPath()
            self.RefreshGUI()

    def OnAddRootFolder(self, event): # wxGlade: CSnakeGUIFrame.<event_handler>
        """
        Add folder where CSnake files must be searched to lbRootFolders.
        """
        dlg = wx.DirDialog(None, "Add Root Folder")
        if dlg.ShowModal() == wx.ID_OK:
            self.settings.rootFolders.append(dlg.GetPath())
            self.RefreshGUI()

    def OnRemoveRootFolder(self, event): # wxGlade: CSnakeGUIFrame.<event_handler>
        """
        Remove folder where CSnake files must be searched from lbRootFolders.
        """
        self.settings.rootFolders.remove(self.lbRootFolders.GetStringSelection())
        self.RefreshGUI()

    def OnLoadSettings(self, event): # wxGlade: CSnakeGUIFrame.<event_handler>
        """
        Let the user load configuration settings.
        """
        dlg = wx.FileDialog(None, "Select CSnake file", wildcard = "*.CSnakeGUI")
        if dlg.ShowModal() == wx.ID_OK:
            self.LoadSettings(dlg.GetPath())

    def OnSaveSettingsAs(self, event): # wxGlade: CSnakeGUIFrame.<event_handler>
        """
        Let the user save configuration settings.
        """
        dlg = wx.FileDialog(None, "Select CSnake file", wildcard = "*.CSnakeGUI", style = wx.FD_SAVE)
        if dlg.ShowModal() == wx.ID_OK:
            (root, ext) = os.path.splitext(dlg.GetPath())
            if ext == ".CSnakeGUI":
                settingsFilename = dlg.GetPath()
            else:
                settingsFilename = "%s.CSnakeGUI" % root
            settingsFilename = dlg.GetPath()
            self.SaveSettings(settingsFilename)

    def RefreshGUI(self):
        """ Also saves the current settings to the currentGUISettingsFilename """
        self.cmbCSnakeFile.Clear()
        self.cmbCSnakeFile.Append(self.settings.csnakeFile)
        for x in self.settings.recentlyUsed:
            self.cmbCSnakeFile.Append("%s - In %s" % (x.instance, x.csnakeFile))
        self.cmbCSnakeFile.SetSelection(0)
        
        self.lbRootFolders.Clear()
        for rootFolder in self.settings.rootFolders:
            self.lbRootFolders.Append(rootFolder)
        self.txtThirdPartyRootFolder.SetValue(self.settings.thirdPartyRootFolder)
        self.txtBinFolder.SetValue( self.settings.buildFolder )
        self.txtInstallFolder.SetValue( self.settings.installFolder )
        self.txtThirdPartyBinFolder.SetValue( self.settings.thirdPartyBinFolder )
        self.txtKDevelopProjectFolder.SetValue( self.settings.kdevelopProjectFolder )
        self.cmbInstance.Clear()
        if self.settings.instance != "":
            self.cmbInstance.Append(self.settings.instance)
            self.cmbInstance.SetSelection(0)
            
        self.panelKDevelop.Show( self.settings.compiler in ("KDevelop3", "Unix Makefiles") )
        self.Layout()
        
        if os.path.exists(self.options.currentGUISettingsFilename):
            self.SaveSettings(self.options.currentGUISettingsFilename)
    
    def LoadSettings(self, filename = ""):
        """
        Load configuration settings from filename.
        """
        if filename == "":
            filename = self.options.currentGUISettingsFilename
                
        if os.path.exists( filename ):
            self.settings.Load(filename)
            self.RefreshGUI()
            
        self.StoreSettingsFilename(filename)
    
    def OnEditOptions(self, event): # wxGlade: CSnakeGUIFrame.<event_handler>
        """
        Let user edit the application options.
        """
        frmEditOptions = csnGUIOptions.CSnakeOptionsFrame(None, -1, "")
        frmEditOptions.ShowOptions(self.settings, self.options, self.optionsFilename)
        frmEditOptions.MakeModal()
        frmEditOptions.Show(True, self.RefreshGUI)
        
    def OnUpdateListOfTargets(self, event): # wxGlade: CSnakeGUIFrame.<event_handler>
        self.SaveSettings()
        targets = self.handler.GetListOfPossibleTargets()
        self.cmbInstance.SetItems(targets)
        if len(targets):
            self.cmbInstance.SetSelection(0)
            self.SaveSettings()

    def ProposeToDeletePluginDlls(self):
        spuriousDlls = self.handler.GetListOfSpuriousPluginDlls()
        if len(spuriousDlls) == 0:
            return
            
        dllMessage = ""
        for x in spuriousDlls:
            dllMessage += ("%s\n" % x)
            
        message = "In the Bin folder, CSnake found GIMIAS plugins that have not been configured.\nThe following plugin dlls may crash GIMIAS:\n\n%s\nDelete them?" % dllMessage
        dlg = wx.MessageDialog(self, message, style = wx.YES_NO)
        if dlg.ShowModal() != wx.ID_YES:
            return
            
        for dll in spuriousDlls:
            os.remove(dll)

    def AskToLaunchVisualStudio(self, pathToSolution):
        message = "Launch Visual Studio with solution %s?" % pathToSolution
        dlg = wx.MessageDialog(self, message, style = wx.YES_NO)
        if dlg.ShowModal() == wx.ID_YES:
            argList = [self.options.visualStudioPath, pathToSolution]
            retcode = subprocess.Popen(argList)
                
    def OnExit(self, event): # wxGlade: CSnakeGUIFrame.<event_handler>
        self.CopyGUIToSettings()
        if os.path.exists(self.options.currentGUISettingsFilename):
            self.SaveSettings(self.options.currentGUISettingsFilename)
        self.Destroy()

    def Validate(self, action):
        if self.cmbAction.GetValue() == "Only create CMake files":
            pass
        
    def OnSelectRecentlyUsed(self, event): # wxGlade: CSnakeGUIFrame.<event_handler>
        item = self.cmbCSnakeFile.GetSelection() - 1
        settings = self.settings.recentlyUsed[item]
        self.settings.csnakeFile = settings.csnakeFile
        self.settings.instance = settings.instance
        self.RefreshGUI()

    def OnButtonSelectProjects(self, event): # wxGlade: CSnakeGUIFrame.<event_handler>
        previousFilter = self.settings.filter 
        self.settings.filter = list()
        categories = self.handler.GetCategories()
        self.settings.filter = previousFilter
        dlg = csnGUISelectProjects.Dialog(None, -1, "")
        if dlg.ShowItems(categories, self.settings.filter) == wx.ID_OK:
            pass

# end of class CSnakeGUIFrame


class CSnakeGUIApp(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        frmCSnakeGUI = CSnakeGUIFrame(None, -1, "")
        self.SetTopWindow(frmCSnakeGUI)
        frmCSnakeGUI.Show()
        return 1

# end of class CSnakeGUIApp

if __name__ == "__main__":
    app = CSnakeGUIApp(0)
    app.MainLoop()
