# VMAPView

Fork of [hdfview](https://github.com/marts/hdf5view) with support for showing VMAP geometries as pointclouds or meshes. 


## 1. Installing

#### Qt API Bindings

One of [pyqt5](https://www.riverbankcomputing.com/software/pyqt/), [pyside2](https://pyside.org), [pyqt6](https://www.riverbankcomputing.com/software/pyqt/) or [pyside6](https://pyside.org) is required in order to be able to run VMAPView. Please install one of these e.g. with pip:

```
pip install pyqt5
```

or on linux (Ubuntu/Debian), you can install a system package:

```
sudo apt install python3-pyqt5
```

[qtpy](https://github.com/spyder-ide/qtpy) is used as an abstraction layer for pyqt5/pyside2/pyqt6/pyside6. If you have any of these Qt API bindings installed, qtpy will take the first available one in the order shown in the previous sentence. VMAPView works with all of the bindings. If you have more than one of the bindings installed and want to specify which one should be used for VMAPView, you can do this by setting the `QT_API` environment variable before running VMAPView.

For example: if you have pyqt5 and pyside2 installed and you want VMAPView to use PySide2, on Windows PowerShell:

```
$env:QT_API = 'pyside2'
```

or on linux (Ubuntu/Debian)

```
export QT_API=pyside2
```

before running VMAPView


#### Other Dependencies

The other dependencies are [qtpy](https://github.com/spyder-ide/qtpy), [h5py](https://www.h5py.org/) and [pyqtgraph](https://www.pyqtgraph.org/). Currently installed versions of these dependencies will not be overwritten by installing VMAPView. If these are not already present on your system, they will be installed during the installation of VMAPView. 

If you prefer to install them in advance, you can use pip:

```
pip install h5py, qtpy, pyqtgraph
```

or on linux to install system packages:

```
sudo apt install python3-h5py python3-pyqtgraph python3-qtpy
```

Note: [pyqtgraph](https://www.pyqtgraph.org/) 0.12 supports all of pyqt5, pyside2, pyqt6 or pyside6. Older versions of pyqtgraph may not support all of them.


#### VMAPView

To install the current development version, download or clone the repo and install either system-wide on Windows:

```
cd vmapview
pip install .
```

or on linux:

```
cd vmapview
sudo pip3 install .
```

You could also use the flag -e with the pip command to install in editable mode, then you can pull changes from the repo and they are automatically available on your system.

To setup an isolated development environment using virtualenv:

```
python3 -m virtualenv -p python3 .
source bin/activate
pip install -e .
```

To uninstall vmapview:

```
pip uninstall vmapview
```

or:

```
sudo pip3 uninstall vmapview
```

## 2. Running

From the terminal:

```
vmapview
```

or

```
vmapview -f <vmapfile>
```

It is also possible to run the program without installing by executing the following command from insie the "src" directory:
```
python -m vmapview
```

VMAP files can also be dropped onto the application window once opened.

You can also create a desktop link to start the program for convenience. A Windows icon file hdf5view.ico is provided in the folder vmapview/resources/images.

## 3. Usage

The structure of the HDF5 file can be navigated using the tree view on the left hand side. The central panel displays a table of the data at the node selected. If the node has more than two dimensions, a 2D slice of the data is displayed in the table. On the right hand side you can see and modify the slice shown; and see details of the node and any associated attributes.

To display an image of a particular node, click the image icon on the toolbar at the top of the window. This will open an Image tab at the current node. You can have several image tabs open at once. Image tabs remember the node and slice if you switch to a different tab and back. Switching to a different node results in the default rendering behaviour for the image. The defaut image rendering is as follows: 

* Greyscale: if the node has two or more dimensions and the shape of the last dimension is greater than 4. The image is initially taken from the last two dimensions of the node. A scrollbar is provided, which currently can be used to scroll through the first dimension of the node. This is useful for viewing a stack of greyscale images. You can alternatively change the slice manually and the scrollbar will move accordingly.

* rgb or rgba: if the node has three or more dimensions and the shape of the last dimension is three or four. If the node has more than three dimensions, a scrollbar is provided, which can be used to scroll through the first dimension. This is useful for a stack of rgb or rgba images, for example.

To show the embeded geometries of the file as a point cloud or mesh, click on the respective icon in the top toolbar. This option is only available ater selecting a geometry group in the */VMAP/GEOMETRY/<id>* path where *id* stands for the id (usually a number) of the geometry to visualize.

## 4. Testing

Currently there are no unit tests for this package. The gui has been tested with qtpy=2.2.0, pyqtgraph=0.12.4 and h5py=3.7.0 in combination with pyqt5=5.15.7, pyside2=5.15.2.1, pyqt6=6.3.1 and pyside6=6.3.2, and it works with all of the Qt API bindings.

## 5. Issues

If there are any issues, please feel free to use the [issues mechanism on github](https://github.com/IFTE-EDA/VMAPview/issues) to get in touch.

