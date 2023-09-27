import ctypes
import os
import subprocess
import sys


def install_packages(load_libs=False):
    if not os.path.isfile("/content/env.tar.gz"):
        print("Downloading binaries...", end=" ")
        subprocess.run(['wget', '-O', '/content/env.tar.gz', 'https://www.dropbox.com/s/ron3hjegmwu7ram/environ.tar.gz'],
                       check=True, text=True)
        print("✔️")

        print("Extracting files...", end=" ")
        subprocess.run(['tar', '-xf' 'env.tar.gz', '-C', '/content'],
                       check=True, text=True)
        print("✔️")

        print("Installing dependencies....", end=" ")
        subprocess.run(['apt-get', 'install', 'libgsl-dev'],
                       check=True, text=True)
        subprocess.run(['pip3', 'install', '--upgrade', 'gmsh'],
                       check=True, text=True)
        print("✔️")

    print("Loading libs...", end=" ")
    # Set the environment variables.
    os.environ["GARFIELD_HOME"] = "/content/garfield/garfieldpp"
    os.environ["ROOTSYS"] = "/content/root/install"
    os.environ["PATH"] += ":/content/elmer/install/bin"

    # Load the ROOT and Garfield libraries.
    sys.path.append("/content/root/install/lib")

    ctypes.cdll.LoadLibrary('/content/root/install/lib/libCore.so')
    ctypes.cdll.LoadLibrary('/content/root/install/lib/libThread.so')
    ctypes.cdll.LoadLibrary('/content/root/install/lib/libImt.so')
    ctypes.cdll.LoadLibrary('/content/root/install/lib/libRIO.so')
    ctypes.cdll.LoadLibrary('/content/root/install/lib/libNet.so')
    ctypes.cdll.LoadLibrary('/content/root/install/lib/libTree.so')
    ctypes.cdll.LoadLibrary('/content/root/install/lib/libMathCore.so')
    ctypes.cdll.LoadLibrary('/content/root/install/lib/libMatrix.so')
    ctypes.cdll.LoadLibrary('/content/root/install/lib/libHist.so')
    ctypes.cdll.LoadLibrary('/content/root/install/lib/libGeom.so')
    ctypes.cdll.LoadLibrary('/content/root/install/lib/libXMLIO.so')
    ctypes.cdll.LoadLibrary('/content/root/install/lib/libGdml.so')
    ctypes.cdll.LoadLibrary('/content/root/install/lib/libGraf.so')
    ctypes.cdll.LoadLibrary('/content/root/install/lib/libGpad.so')
    ctypes.cdll.LoadLibrary('/content/root/install/lib/libGraf3d.so')
    ctypes.cdll.LoadLibrary('/content/root/install/lib/libcppyy_backend3_9.so')
    print("✔️")

    import ROOT
    ROOT.gSystem.Load("/content/garfield/install/lib/libmagboltz.so")
    ROOT.gSystem.Load("/content/garfield/install/lib/libGarfield.so")
    print("All done! 🚀")
