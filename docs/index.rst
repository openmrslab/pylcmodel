.. pylcmodel documentation master file, created by
   sphinx-quickstart on Thu Sep 29 15:00:03 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

PyLCModel |release|
===================

PyLCModel is a little utility to make it easier to run LCModel from remote
systems, in particular to make LCModel more accessible from inside the
OpenMRSLab Docker image. It provides a local version of the LCModel executable
which can be called with the same arguments as the real program, but then it
uses an SSH connection to the system where LCModel is actually installed to
copy the necessary files across, run the program there, and then copy all
resulting output files back to the local system.

PyLCModel can be installed with pip:

.. code-block:: bash

    pip install pylcmodel

Installing the program automatically adds a terminal command called lcmodel
which behaves in the same way as running LCModel itself.

PyLCModel requires a small amount of initial configuration to get working.
This is stored in a file called .pylcmodel which should be in your home folder.
The .pylcmodel file has a very simple format as you can see from the example
file below.

.. code-block::
   :caption: .pylcmodel

   hostname=lcmodel
   user=lcm_user

Required Parameters
-------------------
**hostname**: the hostname or IP address of the remote system where the actual
LCModel program is installed.

**user**: the user on the remote system who can run LCModel.

Optional Parameters
-------------------
**port** the port on the remote system where the SSH server is listening.
Defaults to 22 if not supplied.

**password** the preferred option for authenticating with the remote server is
by setting up a public/private key pair, however you can also provide the
password for the remote host user here. N.B. this means that your password is
stored in plain text in this file, only use this option if you are ok with
this. See here for more information about authentication options.

**key_filename** an optional private key file to be used for authentication.
See here for more information about authentication options.

**passphase** used to unlock encrypted private keys. See here for more
information about authentication options.

**lcmodel_path** the location of the lcmodel executable on the remote machine.
If this parameter is not provided, pylcmodel will first check to see if the
executable is available on the remote $PATH, and will then check the default
location for the executable in ~/.lcmodel/bin/lcmodel.

**remote_dir** necessary input files from the local machine will be copied to
the remote LCModel host and stored in this folder. Requested output files will
also be created here for transfer back to the local machine. If no path is
provided, by default a folder called `pylcmodel' will be created in the remote
user's home folder.

**keep_remote_files** by default, all files copied to or created on the LCModel
machine will be deleted once the output files have been copied back to the
local system. To leave these files available on the remote machine this
parameter can be set to True. N.B. this option is designed for debugging errors
with running LCModel, not for long term preservation of data on the remote
machine, as most files will be overwritten by the next run of pylcmodel. If you
require persistent storage of LCModel run results on the remote machine, please
raise an issue at http://github.com/openmrslab/pylcmodel.



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

