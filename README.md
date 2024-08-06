# Voxel

Voxel is a general microscope control repository designed to simplify the 
process of configuring and controling different microscopy systems. Microscopes
can be defined as a collection of any set of devices through a configuraiton
YAML file. Currently supported device types and models are listed below.

```yaml
Cameras
    eGrabber GenICam cameras
        Vieworks VP-151MX tested
        Vieworks VNP-604MX tested
    Hamamatsu cameras
        ORCA-Flash4.0 V3 tested
        ORCA-Fusion BT tested
    PCO cameras (untested)
    Simulated camera
Stages
    ASI
    Simulated stage
Lasers
    Coherent OBIS
    Coherent Genesis
    Vortran Stradus
    Oxxius LBX and LCX
    Cobolt
    Simulated laser
AOTF
    AAOpto
    Simulated AOTF
Filterwheel
    ASI FW-1000
    Simulated filter wheel
Flip mount
    Thorlabs MFF101
    Simulated flip mount
Power meter
    Thorlabs PM100D
    Simulated power meter
Rotation mount  
    Thorlabs K10CR1
    Simulated rotation mount
Tunable lens
    ASI TGTLC
    Optotune ELE41
    Optotune ICC4C
    Simulated tunable lens
DAQ
    National Instruments
        PCIe-6738 tested
    Simulated DAQ
```

### Documentation
coming soon

### Prerequisites
- **Python==3.11** (tested) 
(Recommended to install via 
[Anaconda](https://www.anaconda.com/products/individual) or 
[Miniconda](https://docs.conda.io/en/latest/miniconda.html))
- **eGrabber** (Windows and Linux)
To control the Vieworks VP-151MX camera you will need 
[eGrabber for CoaxLink and GigELink](https://www.euresys.com/en/Support/Download-area?Series=105d06c5-6ad9-42ff-b7ce-622585ce607f) installed for your particular 
system. Note that, to download the eGrabber SDK, you will first need to make 
an account. After downloading and installing eGrabber, you will need to install 
the eGrabber python package (stored as a wheel file). For more info installing 
the Python wheel file, see the [notes from Euresys](https://documentation.euresys.com/Products/COAXLINK/COAXLINK/en-us/Content/04_eGrabber/programmers-guide/Python.htm).

Generally, the process should be as simple as finding the wheel package in the 
eGrabber subfolder and invoking:
````
pip install egrabber-xx.xx.x.xx-py2.py3-none-any.whl
````
- **DCAM** (Windows only)
To control Hamamatsu cameras you will need 
[DCAM API](https://dcam-api.com/) installed for your particular system.
- **Coherent HOPS** (Windows only)
To control Coherent Genesis series lasers, you will need to install 
Coherent HOPS (instructions coming soon).

### Installation
1. Create a virtual environment and activate it:
- On Windows:
```bash
conda create -n voxel
conda activate voxel
```

2. Clone the repository:
```bash
git clone https://github.com/AllenNeuralDynamics/voxel.git
```

4. To use the software, in the root directory, run
```bash
pip install -e .
```

5. To develop the code, run
```bash
pip install -e .[dev]
```

### Usage
1. Instantiating a single device
Individual device can be instantiated by importing the appropriate driver
class with the expected arguments. For example a camera object for a Vieworks
VP-151MX can be invoked as:
```python
from voxel.devices.camera.vieworks_egrabber import VieworksCamera

camera = VieworksCamera(id='123456')
```
Camera properties can then be queried and set by accessing attributes of the
camera object:
```python
camera.exposure_time ms = 10.0
camera.pixel_type = 'mono16'
camera.bit_packing_mode = 'lsb'
camera.binning = 1
camera.width_px = 14192
camera.height_px = 10640
camera.trigger = {'mode': 'on', 'source': 'line0', 'polarity': 'risingedge'}
```
The camera can then be operated with:
```python
camera.prepare() # this function arms and creates the camera buffer
camera.start()
image = camera.grab_frame()
camera.stop()
camera.close()
```
2. Voxel facilitates defining entire instruments through a YAML file
```yaml
instrument:
  devices:
    vp-151mx camera:
      type: camera
      driver: voxel.devices.camera.simulated
      module: SimulatedCamera
      init:
        id: sim000
      settings:
        exposure_time_ms: 20.0
        pixel_type: mono16
        height_offest_px: 4744
        height_px: 1152
        width_offset_px: 6528
        width_px: 1152
        trigger:
          mode: 'off'
          polarity: rising
          source: external
    488 nm laser:
      type: laser
      driver: voxel.devices.lasers.simulated
      module: SimulatedLaser
      color: blue
      init:
        port: COM3
    x axis stage:
      type: scanning_stage
      driver: voxel.devices.stage.simulated
      module: Stage
      init:
        hardware_axis: x
        instrument_axis: z
      settings:
        speed_mm_s: 1.0
```
An instrument can be invoked by loading the YAML file with and the loaded devices
can be accessed with. The above example uses all simulated device classes.
```python
from voxel.instruments.instrument import Instrument

instrument = Instrument(config_path='example.yaml')
instrument.cameras['vp-151mx camera]
instrument.lasers['488 nm laser']
instrument.scanning_stages['x axis stage']
```
Experimental workflows may then be scripted by using the full instrument object
and the contained device objects as needed.

### Support and Contribution
If you encounter any problems or would like to contribute to the project, 
please submit an [Issue](https://github.com/AllenNeuralDynamics/voxel/issues) 
on GitHub.

### License
Voxel is licensed under the MIT License. For more details, see 
the [LICENSE](LICENSE) file.
