from pymel.core import *
import maya.api.OpenMaya as om
import math as math

import cProfile

def __main__():
    r_mesh_vtx = ([])
    s_mesh_vtx = ([])


    # Get Reference mesh actor(s) as a list
    reference_mesh_root = ls(sl = True)[0]
    reference_meshes = GetChildMeshes(reference_mesh_root)

    # Get mesh(es) to project vertex color on as a list.
    target_mesh_root = ls(sl = True)[1]
    target_meshes = GetChildMeshes(target_mesh_root)

    # align the reference mesh with the source mesh
    AlignSourceMesh(reference_meshes, target_meshes)

    print reference_meshes
    print target_meshes

    # Get all vertex locations as a dict(locations , point object) from the reference mesh(es)

    # compare point from the reference mesh against the source
    for r_mesh in target_meshes:
        for vtx in r_mesh.vtx:
            r_mesh_vtx.append(vtx)

    for s_mesh in reference_meshes:
        for vtx in s_mesh:
            s_mesh_vtx.append(vtx)


    itr = 0

    for ref_vtx in r_mesh_vtx:
        for source_vtx in r_mesh_vtx:
            if ref_vtx.getPosition() == source_vtx.getPosition():
                print 'Match'
                itr = itr + 1

    print itr
    # Clean up the meshes to be projected on.
    CleanupTargetMeshes(target_meshes)

    # Remove colors sets and add a clean one with the proper name.

    # Loop through all locations from the meshes to project on and check if their locations are keys in the stored list.

        # if its a key in the list, get the vertex color and apply it.

        # Store the number of adjusted verts, if the edited verts nr != number of verts in the source meshes, call an error that there might be artifacts.

        # and recommend that they do it per object bases

    pass

def GetChildMeshes(root_input):

    child_object_list = root_input.getChildren()

    child_shape_list = []

    for child in child_object_list:
        if objectType(child) != 'mesh':
            child_shape_list.append(child.getShape())
        else:
            child_shape_list.append(child)

    return child_shape_list

def GetTargetMeshes():
  # get BBox center location of target to move too
  # Group mesh to move and move it to the BBox target location.
  # Un group the mesh

  # Compare Bbox locations, if they don't align, throw an error
  return 'prototype'

def CleanupTargetMeshes(inMesh):
    return 'prototype'


def CompareLocations():
    return True


def AlignSourceMesh(meshToMove,targetToMoveToo):
    pass


def IsNearlyEqual(max_Tolerance):
    return False


def throw_error(error):
    print error

    pass


def construct_tool_window():
    pass

cProfile.run(__main__())
#__main__()

