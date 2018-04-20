from pymel.core import *
import math

# How to use:
# Import unreal 4 actor and align it with the target mesh
# Selection order: Select source mesh first then the target mesh
# Activate the script

# give the script some time, it need to go through all the verts...

def __main__():
    r_mesh_vtx = dict()
    s_mesh_vtx = dict()

    # Get Reference mesh actor(s) as a list (Source)
    reference_mesh_root = ls(sl = True)[0]
    reference_meshes = GetChildMeshes(reference_mesh_root)

    # Get mesh(es) to project vertex color on as a list. (Target)
    target_mesh_root = ls(sl = True)[1]
    target_meshes = GetChildMeshes(target_mesh_root)

    # align the reference mesh with the source mesh
    AlignSourceMesh(reference_meshes, target_meshes)
    
    # Clean up the meshes to be projected on.
    CleanupTargetMeshes(target_meshes)
        
    #TODO refactor this to a function    
    for r_mesh in target_meshes:
        for vtx in r_mesh.vtx:         
            r_mesh_vtx[str(vtx.getPosition(space = 'world'))] = vtx

    for s_mesh in reference_meshes:
        for vtx in s_mesh.vtx:
            s_mesh_vtx[str(vtx.getPosition(space = 'world'))] = vtx
                      
    # compare point from the reference mesh against the source            
    for r_key, r_value in r_mesh_vtx.iteritems():

        for s_key, s_value in s_mesh_vtx.iteritems():
            if isNearlyEqual(s_key,r_key):
                r_value.setColor(s_value.getColor())
                del s_mesh_vtx[s_key]
                break              
                
    print 'Transfer done'
            
    return

def GetChildMeshes(root_input):

    child_object_list = root_input.getChildren()

    child_shape_list = []

    for child in child_object_list:
                
        if objectType(child) == 'mesh':
            child_shape_list.append(child)
        elif objectType(child) != 'locator':
            child_shape_list.append(child.getShape())

    return child_shape_list


def CleanupTargetMeshes(inMesh):   
    for i in inMesh:
        i_colorSets = polyColorSet(i, q = True, allColorSets = True)
        if i_colorSets != None:
            for set in i_colorSets:
                if set != 'colorSet':
                    polyColorSet(i, colorSet = set, d =True)
        if polyColorSet(i, q = True, allColorSets = True) == None:
            polyColorSet(i, create = True, colorSet = 'colorSet', clamped = True, rpt = 'RGBA')


def AlignSourceMesh(meshToMove,targetToMoveToo):
    pass


def throw_error(error):
    print error
    pass


def isNearlyEqual(a,b):
    threashold = 0.001

    point_a = str(a)[:-1]
    point_a = point_a[1:]
    
    point_b = str(b)[:-1]
    point_b = point_b[1:]
    
    sameInX = abs( float(point_a.split(', ')[0]) - float(point_b.split(', ')[0])) < threashold
    sameInY = abs( float(point_a.split(', ')[1]) - float(point_b.split(', ')[1])) < threashold
    sameInZ = abs( float(point_a.split(', ')[2]) - float(point_b.split(', ')[2])) < threashold

    return (sameInX and sameInY and sameInZ)
    
    
def construct_tool_window():
    pass


#cProfile.run('__main__()')

__main__()


