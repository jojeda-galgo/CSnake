## @package csnProjectPaths
# Definition of the Project path handling related class. 
import glob
import os
import csnUtility

class Manager:
    def __init__(self, _project, _sourceRootFolder):
        self.project = _project
        
        # check compiler
        if not self.project.context.GetCompiler():
            raise AssertionError("Missing compiler in project.")
        
        # get build sub folder
        if self.project.type == "dll":
            self.buildSubFolder = self.project.context.GetCompiler().GetBuildSubFolder("library", self.project.name)
        else:
            self.buildSubFolder = self.project.context.GetCompiler().GetBuildSubFolder(self.project.type, self.project.name)

        self.configFilePath = "%s/%sConfig.cmake" % (self.buildSubFolder, self.project.name)
        self.useFilePath = "%s/Use%s.cmake" % (self.buildSubFolder, self.project.name)
        self.cmakeListsSubpath = "%s/CMakeLists.txt" % (self.buildSubFolder)
        self.sourceRootFolder = _sourceRootFolder
        
    def PrependRootFolderToRelativePath(self, _path):
        """ 
        Returns _path prepended with self.sourceRootFolder, unless _path is already an absolute path (in that case, _path is returned).
        """
        path = csnUtility.NormalizePath(_path)
        if not os.path.isabs(path):
            path = os.path.abspath("%s/%s" % (self.sourceRootFolder, path))
        return csnUtility.NormalizePath(path)
    
    def Glob(self, _path):
        """ 
        Returns a list of files that match _path (which can be absolute, or relative to self.sourceRootFolder). 
        If _path is a list, then every element of _path will be Globbed.
        The return paths are absolute, containing only forward slashes.
        """
        if type(_path) == type(list()):
            result = []
            for x in _path:
                moreResults = self.Glob(x)
                result.extend(moreResults)
            return [csnUtility.NormalizePath(x) for x in result]
        else:
            return [csnUtility.NormalizePath(x) for x in glob.glob(self.PrependRootFolderToRelativePath(_path))]
        
    def GetPathToUseFile(self):
        """ 
        Returns self.project.useFilePath if it is absolute. Otherwise, returns self.project.GetBuildRootFolder() + self.project.useFilePath.
        """
        if os.path.isabs(self.useFilePath):
            result = self.useFilePath
        else:
            result = "%s/%s" % (self.project.context.GetBuildFolder(), self.useFilePath)
            
        return csnUtility.NormalizePath(result)

    def GetPathToConfigFile(self, _public):
        """ 
        Returns self.useFilePath if it is absolute. Otherwise, returns self.GetBuildRootFolder() + self.useFilePath.
        If _public is false, and the project is not of type 'third party', then the postfix ".private" 
        is added to the return value.
        """
        if os.path.isabs(self.configFilePath):
            result = self.configFilePath
        else:
            result = "%s/%s" % (self.project.context.GetBuildFolder(), self.configFilePath)

        postfix = ""
        if self.project.type in ("dll", "library", "executable") and (not _public):
            postfix = ".private"

        return csnUtility.NormalizePath(result + postfix)

    def GetBuildFolder(self):
        """
        Returns the folder for storing intermediate build files for this project.
        """
        return csnUtility.NormalizePath(self.project.context.GetBuildFolder() + "/" + self.buildSubFolder)
        
    def GetBuildResultsFolder(self, _configurationName = "${CMAKE_CFG_INTDIR}"):
        """ 
        Returns location in the binary folder where binaries for this project must be installed.
        This functions is used for being able to "install" all files in the build folder that are needed to run the application
        from the binary folder without having to install to the Install Folder.
        """
        result = self.project.context.GetOutputFolder(_configurationName)
        if self.project.installSubFolder != "":
            if _configurationName == "DebugAndRelease":
                result += "/${CMAKE_CFG_INTDIR}"
            result += "/%s" % self.project.installSubFolder
        return csnUtility.NormalizePath(result)

    def GetSourceRootFolder(self):
        return csnUtility.NormalizePath(self.sourceRootFolder)

    def Dump(self):
        return { \
            "buildSubFolder" : self.buildSubFolder, \
            "configFilePath" : self.configFilePath, \
            "useFilePath" : self.useFilePath, \
            "cmakeListsSubpath" : self.cmakeListsSubpath, \
            "sourceRootFolder" : self.sourceRootFolder \
        }
