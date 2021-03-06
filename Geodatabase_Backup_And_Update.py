# ---------------------------------------------------------------------------
# GeodatabaseDataBackupAndUpdate.py
# Created on: 2012-10-22 11:34:11.00000
#   (generated by ArcGIS/ModelBuilder)
#   (modified significantly by DAT)
# Description:
# This script creates a backup for the current geodatabases on the S & Z drives.
# It also updates the active databases on the O, S, & Z drives.
# The backups and updates are based on the geodatabases in use on the C drive
# of the machine which runs the update.
# Note that the operation will fail if the C drive has a setup different from
# this machine with regards to geodatabase location. This can be resolved by
# editing the C_Main path in this script, or by relocating the geodatabases
# to that location on the running machine's C drive.
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy
import datetime
import os
import shutil


def main():

  try:
    # Geodatabase path variables:
    App = "Appraiser.gdb"
    GIS = "GIS.gdb"
    Clerk = "Clerk.gdb"

    C_Main = "C:\\GISdata\\Maintenance\\"
    O_Active = "O:\\Geodatabases\\"
    S_Active = "S:\\Appr\\WorkingFiles\\"
    Z_Active = "Z:\\GISdata\\Working\\Appr\\WorkingFiles\\"
    
    S_Backup = "S:\\Appr\\Archive\\Backup\\"
    Z_Backup = "Z:\\GISdata\\Archive\\Backup\\"
    
    # Set the todaysDate variable to today's date.
    todaysDate = datetime.date.today()
    
    # Convert todaysDate to string type. -- Works fine now, but has the potential for errors.
    todaysDate = str(todaysDate)
    
    # Concat todaysDate onto the appropriate backup folder locations
    # and add a backslash to the end.
    Z_Backup = Z_Backup + todaysDate + "\\"
    S_Backup = S_Backup + todaysDate + "\\"
    
    ################# New path trial ####################
    S_Active_2 = "S:\\Public\\Geodatabases\\"
    S_Backup_2 = "S:\\Backup\\Geodatabases\\"
    S_Backup_2 = S_Backup_2 + todaysDate + "\\"
    ################# New path trial ####################

    print "..."

    #--------------------------O: Drive Section----------------------------#
    
    # Delete prior active GDBs
    if (os.path.isdir(O_Active + App) == bool("true")):
      # Is there a way to see if the database is locked before deleting?
      arcpy.Delete_management(O_Active + App, "Workspace")
    if (os.path.isdir(O_Active + GIS) == bool("true")):
      arcpy.Delete_management(O_Active + GIS, "Workspace")
      
    # Replace with new active GDBs from my machine via Copy
    arcpy.Copy_management(C_Main + App, O_Active + App, "Workspace")
    arcpy.Copy_management(C_Main + GIS, O_Active + GIS, "Workspace")
    
    print "..."
    
    #--------------------------S: Drive Section----------------------------#
    
    # Check to see if a backup directory with the current date already exists.
    # If so, remove that directories.
    if (os.path.isdir(S_Backup) == bool("true")):
      shutil.rmtree(S_Backup)
    
    # Create the backup directory using the mkdir command.
    os.mkdir(S_Backup)
    
    # Add backups to the newly created backup folders for today's date
    arcpy.Copy_management(C_Main + App, S_Backup + App, "Workspace")
    arcpy.Copy_management(C_Main + GIS, S_Backup + GIS, "Workspace")
    
    # Delete prior active GDBs
    if (os.path.isdir(S_Active + App) == bool("true")):
      arcpy.Delete_management(S_Active + App, "Workspace")
    if (os.path.isdir(S_Active + GIS) == bool("true")):
      arcpy.Delete_management(S_Active + GIS, "Workspace")
    
    # Replace with new active GDBs from my machine via Copy
    arcpy.Copy_management(C_Main + App, S_Active + App, "Workspace")
    arcpy.Copy_management(C_Main + GIS, S_Active + GIS, "Workspace")
    
    # The Clerk.gdb part is different in that it copies from O: to S:.
    # The C: drive is not involved.
    # Also, this is just for backup purposes, there is no Clerk.gdb
    # in the active geodatabases folder on S:.
    arcpy.Copy_management(O_Active + Clerk, S_Backup + Clerk, "Workspace")
    
    ######################################################################
    #################### New path trial start. ###########################
    ######################################################################
    
    if (os.path.isdir(S_Backup_2) == bool("true")):
      shutil.rmtree(S_Backup_2)
    
    # Create the backup directory using the mkdir command.
    os.mkdir(S_Backup_2)
    
    # Add backups to the newly created backup folders for today's date
    arcpy.Copy_management(C_Main + App, S_Backup_2 + App, "Workspace")
    arcpy.Copy_management(C_Main + GIS, S_Backup_2 + GIS, "Workspace")
    
    # Delete prior active GDBs
    if (os.path.isdir(S_Active_2 + App) == bool("true")):
      arcpy.Delete_management(S_Active_2 + App, "Workspace")
    if (os.path.isdir(S_Active_2 + GIS) == bool("true")):
      arcpy.Delete_management(S_Active_2 + GIS, "Workspace")
    
    # Replace with new active GDBs from my machine via Copy
    arcpy.Copy_management(C_Main + App, S_Active_2 + App, "Workspace")
    arcpy.Copy_management(C_Main + GIS, S_Active_2 + GIS, "Workspace")
    
    # The Clerk.gdb part is different in that it copies from O: to S:.
    # The C: drive is not involved.
    # Also, this is just for backup purposes, there is no Clerk.gdb
    # in the active geodatabases folder on S:.
    arcpy.Copy_management(O_Active + Clerk, S_Backup_2 + Clerk, "Workspace")
    
    ########################################################################
    ##################### New path trial end. ##############################
    ########################################################################
    
    print "..."
    
    #--------------------------Z: Drive Section----------------------------#

    # Check to see if a backup directory with the current date already exists.
    # If so, remove that directories.
    if (os.path.isdir(Z_Backup) == bool("true")):
      shutil.rmtree(Z_Backup)
    
    # Create the backup directory using the mkdir command.
    os.mkdir(Z_Backup)
    
    # Add backups to the newly created backup folders for today's date
    arcpy.Copy_management(C_Main + App, Z_Backup + App, "Workspace")
    arcpy.Copy_management(C_Main + GIS, Z_Backup + GIS, "Workspace")

    # Delete prior active GDBs
    if (os.path.isdir(Z_Active + App) == bool("true")):
      arcpy.Delete_management(Z_Active + App, "Workspace")
    if (os.path.isdir(Z_Active + GIS) == bool("true")):
      arcpy.Delete_management(Z_Active + GIS, "Workspace")
    
    # Replace with new active GDBs from my machine via Copy
    arcpy.Copy_management(C_Main + App, Z_Active + App, "Workspace")
    arcpy.Copy_management(C_Main + GIS, Z_Active + GIS, "Workspace")

  except Exception as e:
    # If an error occurred, print line number and error message
    import traceback, sys
    tb = sys.exc_info()[2]
    print "Line %i" % tb.tb_lineno
    print e.message

if __name__ == "__main__":
  print "Are you sure that you would like to update at this time?"
  print "Press ENTER to continue or close the script to quit."
  inputTest = raw_input("> ")

  print "The backup and update process has started."
  main()
  print "The update and backup process has completed."
  print "Press ENTER or close the script to quit."
  inputTest = raw_input("> ")
  inputTest = inputTest + "a"
  exit()
    
# The backups and updates are complete!
# /endscript