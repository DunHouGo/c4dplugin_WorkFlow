"""
Author: 王敦厚Go (DunHou)
Written for Maxon Cinema 4D R2023.1.0
Python version 3.9.1
"""
###  ==========  UPDATE LIST  ==========  ###
# todo 
#--------------------------------------------------------------------
# Import Libraries
#--------------------------------------------------------------------
###  ==========  Import Libs  ==========  ###
import typing
from typing import Optional
import os
import c4d
#--------------------------------------------------------------------
# PLUGIN INFO

# Author : 王敦厚Go

#--------------------------------------------------------------------
###  ==========  Global Settings  ==========  ###

doc = c4d.documents.GetActiveDocument()
op: Optional[c4d.BaseObject]  # The active object, None if unselected
#--------------------------------------------------------------------
# Settings.
#--------------------------------------------------------------------

###  ==========  Plugin Settings  ==========  ###
#--------------------------------------------------------------------
# v1

#--------------------------------------------------------------------
# PLUGIN ID
PLUNIGID = 1259994  # Temp ID
PLUNGINNAME = "RenderFlow"
VERSION = "0.1"
TITLE = f"{PLUNGINNAME} v{VERSION}"
INFO = "wip"
PLUHINPATH = os.path.dirname(__file__)
ICONPATH = os.path.join(PLUHINPATH, 'res', 'bmp', 'RenderFlow.png')

###  ==========  Functions Definition  ==========  ###
class WorkFlow(c4d.plugins.CommandData):
    """Command Data class instance."""
    dialog = None
    def __init__(self) -> None:
        self.doc = c4d.documents.GetActiveDocument()
    #! 遍历场景
    def iterate(self,node: c4d.BaseObject) -> c4d.BaseObject:
        """
        Yields all lights that contained in TRACKED_TYPES.
        """
        while isinstance(node, c4d.BaseObject):
            
            #for listType in TRACKED_TYPES:
            if node.GetType() in TRACKED_TYPES:
                yield node

            for child in self.iterate(node.GetDown()):
                yield child

            node = node.GetNext()

    # Override - Called when the plugin is selected by the user.
    def Execute(self, doc = c4d.documents.BaseDocument):
        return True
#--------------------------------------------------------------------
# Plugin Class
#--------------------------------------------------------------------
###  ==========  Execute  ==========  ###
 
class Excute(WorkFlow):
    def __init__(self) -> None:
        pass
    # Override - Called when the plugin is selected by the user.
    def Execute(self, doc=c4d.documents.BaseDocument):
        print("RenderFlow")
        return True
#--------------------------------------------------------------------
# Shortcut.
#--------------------------------------------------------------------  


###  ==========  Register Plugin  ==========  ###
if __name__ == "__main__":
    # Plugins Register
    iconfile = c4d.bitmaps.BaseBitmap()
    iconfile.InitWith(ICONPATH)

    c4d.plugins.RegisterCommandPlugin(
        id = PLUNIGID,
        str = PLUNGINNAME,
        info = 0, # 
        help = "RenderFlow",
        dat = Excute(),
        icon = iconfile
)   
