# Roll Right
Roll Right is an innovative machine learning application designed to enhance accessibility in our everyday environment. Its primary function is to detect and interpret sign language, specifically tailored towards actions such as opening a door. By harnessing the power of machine learning algorithms, Roll Right aims to bridge the communication gap and provide a seamless interaction experience for individuals who use sign language. With Roll Right, command a door to open without physical touch, but through the universal language of signs.

---
## Hardware
The following components are required for this project:
1. [Coral Dev Board Mini](https://coral.ai/docs/dev-board-micro/get-started/)
2. USB 2.0 to TTL Module Serial Converter Adapter
3. USB-C Power Supply (5V 2A)
4. [Coral Camera Module](https://coral.ai/docs/camera/datasheet) or webcam feed
---

## Setup Coral Dev Board Micro
1. Follow the [Getting Started Guide](https://coral.ai/docs/dev-board-micro/get-started/) to setup the Coral Dev Board Micro for the platform you are using.
2. Connect the Coral Camera Module to the Coral Dev Board Micro
3. Connect the USB 2.0 to TTL Module Serial Converter Adapter to the Coral Dev Board Micro
4. Connect the USB-C Power Supply to the Coral Dev Board Micro

## Connect to the Coral Dev Board Micro
![image](https://github.com/builtwithai/rollright/assets/10250297/271d2038-2202-4b00-a4cc-a560bd3cb9d6)

```bash
screen /dev/cu.usbserial-0001 115200
```

## Flash Coral Dev Board before running the project

Install MDT & follow steps to flash the Coral Dev Board before using the project
```bash
python3 -m pip install --user mendel-development-tool

```
![image](https://github.com/builtwithai/rollright/assets/10250297/0dfb338b-49ff-4cee-9850-a44721beb3e4)

```bash
bash -x ./flash.sh
...
...
...
Writing 'rootfs'                                   OKAY [196.265s]
Finished. Total time: 477.691s
+216:try /Users/megamanics/bin/fastboot reboot
+28:/Users/megamanics/bin/fastboot reboot
Rebooting                                          OKAY [  0.000s]
Finished. Total time: 0.000s
+218:echo 'Flash completed.'
Flash completed.
+1:rm -rf /var/folders/0m/ksxyqjln0pxc21n2x7r02fbm0000gn/T/tmp.GKm1wYVo
```

## Power the Coral Dev Board Micro after flashing should see the following output
```bash
U-Boot 2019.10 (Dec 09 2020 - 23:51:30 +0000), Build: jenkins-excelsior.excelsior-bootloader-2

CPU:   MediaTek MT8516
DRAM:  512 MiB
WDT:   Started with servicing (60s timeout)
MMC:   mmc@11120000: 0
Loading Environment from MMC... OK
In:    serial@11005000
Out:   serial@11005000
Err:   serial@11005000
8GB mmc detected
Hit any key to stop autoboot:  0
gpio: pin 42 (gpio 42) value is 1
switch to partitions #0, OK
mmc0(part 0) is current device
1420 bytes read in 1 ms (1.4 MiB/s)
## Executing script at 4c000000
Loading image...
6747990 bytes read in 86 ms (74.8 MiB/s)
Loading device tree...
42834 bytes read in 2 ms (20.4 MiB/s)
104 bytes read in 1 ms (101.6 KiB/s)
## Loading kernel from FIT Image at 4a000000 .
.....
.....
.....
.....
.....
Starting kernel ...

[    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd041]
[    0.000000] Linux version 4.19.125-mtk (pbuilder@linux-mtk-44a92093-5a4b-410b-8ad5-805072874b42-7qs4k-8xlpx) (gcc version 8.3.0 (Debian 8.3.0-2)) #1 SMP PREEMPT Thu Dec 10 02:36:13 UTC 2020
[    0.000000] Machine model: Google Coral MT8167
[    0.000000] efi: Getting EFI parameters from FDT:
[    0.000000] efi: UEFI not found.
[    0.000000] cma: Reserved 64 MiB at 0x00000000bc000000
[    0.000000] psci: probing for conduit method from DT.
.....
.....
.....
.....
[  153.443830] IPv6: ADDRCONF(NETDEV_CHANGE): usb0: link becomes ready

Mendel GNU/Linux (eagle) elusive-eft ttyS0

elusive-eft login: mendel
Password:
Last login: Thu Dec 10 23:37:18 UTC 2020 from 192.168.100.72 on pts/0
Linux elusive-eft 4.19.125-mtk #1 SMP PREEMPT Thu Dec 10 02:36:13 UTC 2020 aarch64

The programs included with the Mendel GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Mendel GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
mendel@elusive-eft:~$
```

## Software
The following software is required for this project:

## Prerequisites
* Python 3.7 or higher
* The following Python packages:
  * numpy
  * tensorflow
  * pillow
  * opencv-python




To install the packages, run the following command in the terminal:

```
gh repo clone builtwithai/rollright
cd rollright
pip install -r requirements.txt
```


## Testing
To test the prediction functions, you can use the `unittest` module and the `test_main.py` file. The file contains three test cases, one for each function: `predict_label`, `predict_label_from_video`, and `preprocess`. The file uses some test images and a video from the `tests` directory.

To run the tests, use the following command:

```
python -m unittest tests/test_main.py
```

The expected output is:

```
image_path: tests/testdoor.jpeg
Predicted label for tests/testdoor.jpeg: Open Door
image_path: tests/testnotdoor.jpeg
Predicted label for tests/testnotdoor.jpeg: Other Sign
Predicted label for tests/test.mp4: Open Door
...
----------------------------------------------------------------------
Ran 3 tests in 3.456s

OK
```

## Model
The TensorFlow Lite model used for the project is `models/model_unquant.tflite`. The model was trained using https://teachablemachine.withgoogle.com/


## License
The project and the model are licensed under the MIT License. See the `LICENSE` file for more details.

## Credits
The project and the model were created by the following authors and contributors:

