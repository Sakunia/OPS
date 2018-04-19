
def __main__():
  # Get Reference mesh actor(s) as a list
  ReferenceMeshes = GetReferenceMeshes()
  
  # Get mesh(es) to project vertex color on as a list.
  TargetMeshes = GetTargetMeshes()
  
  # align the reference mesh with the source mesh
  AlignSourceMesh(ReferenceMeshes,TargetMeshes)
  
  # Get all vertex locations as a dict(locations , point object) from the reference mesh(es)
  
  
  # Clean up the meshes to be projected on.
  CleanupTargetMeshes(TargetMeshes)
    #Remove colors sets and add a clean one with the proper name.
      
  # Loop through all locations from the meshes to project on and check if their locations are keys in the stored list.
    # if its a key in the list, get the vertex color and apply it.
    
    # Store the number of adjusted verts, if the edited verts nr != number of verts in the source meshes, call an error that there might be artifacts.
    # and recommend that they do it per object bases
  
  pass

def GetReferenceMeshes():
  pass

def GetTargetMeshes(meshToMove,targetToMoveToo):
  # get BBox center location of target to move too
  # Group mesh to move and move it to thet BBox target location.
  # Ungroup the mesh
  
  #compare Bbox locations, if they dont align, throw an error
  pass

def CleanupTargetMeshes():
  pass

def CompareLocations():
  return True

def AlignSourceMesh():
  pass

def IsNearlyEqual(max_Tolerance):
  return False

def ThrowError(error):
  pass

def constructToolWindow():
  pass
