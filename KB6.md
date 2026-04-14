AMD MPSoC variant (KB6)
=======================

*Published: April 14, 2026*

*Highlights the platform-specifics and build instructions for Avnet\'s ZUBoard.*

*Categories: Whiznium CV demonstrator, FPGA vendors*

<b><u>Overview</u></b>

The ZUBoard, featuring the AMD's lowest density 1CG Zynq UltraScale+ MPSoC, is a popular choice for prototyping FPGA-SoC designs. At relatively low cost (\< USD 200), it provides high-speed access to custom peripherals via its SYZYGY connectors, as well as all standard Single-Board Computer (SBC) outlets, such as Ethernet and a microSD card slot.

<img src="KB6/setup_low.jpg" alt="setup_low.jpg" height="600">

*Figure 1: CV demonstrator based on ZUBoard in action*

Parts specifically for this variant and provided with the delivery, include:

- the Syzcam2 adapter PCB bringing the IMX335 camera module's 4+1 MIPI lanes routed as differential pairs, and its I2C, to a SYZYGY Transceiver connector

- the Syzpmod2 adapter PCB which translates 2x8 GPIO's from PMOD to SYZYGY Standard

- the Skpph2 PCB with populated PMOD connectors, which drives the CV demonstrator's stepper motor and line lasers from its own power supply

- a USB-C power supply for the ZUBoard

- a 12 V / 2 A power supply for Skpph2 with 5.5/2.5 mm barrel connector

- a micro USB cable to access the MPSoC's serial console


<b><u>Quick Start</u></b>

The hardware setup needs to be established as depicted above, with the boot mode switches set to 0101 and J1 in the depicted 1.2 V position. A ready-to-use 16 GB microSD card image can be obtained and flashed using the commands

```
wget https://content.mpsitech.cloud/artefacts/zudvk_wzsk_v1.2.16_wskd_v1.2.15_SD_16GB.img.gz
sudo gunzip -c zudvk_wzsk_v1.2.16_wskd_v1.2.15_SD_16GB.img.gz | dd of=/dev/sda bs=64K
```

With the microSD card inserted into ZUBoard slot, and all power supplies connected, SW7 initiates the system boot into Linux. This should be accompanied by the D4 RGB LED pulsating. The image is configured for DHCP such that SSH into the board is possible. To start the daemon, run

```
cd /home/root/whiznium/bin/wzskcmbd
./Wzskcmbd
```

after which the web UI can be reached at http://192.168.178.99:13100, where 192.168.178.99 is the assumed IP address attributed by DHCP.


<b><u>VSP Core Vivado Workflow</u></b>

<a href="https://content.mpsitech.cloud/projects/zudvk_vsp_core_v1.2.15.tgz" target="_blank">zudvk_vsp_core_v1.2.15.tgz</a>

<b><u>Top-level Vivado Workflow</u></b>

<img src="KB6/wskd.png" alt="wskd.png" height="600">

*Figure 2: Vivado block design*

<a href="https://content.mpsitech.cloud/projects/zudvk_wskd_v1.2.15.tgz" target="_blank">zudvk_wskd_v1.2.15.tgz</a>

<b><u>PetaLinux (Yocto) Workflow</u></b>

<a href="https://content.mpsitech.cloud/projects/zudvk_wzsk_v1.2.16_project_spec.tgz" target="_blank">zudvk_wzsk_v1.2.16_project_spec.tgz</a>

<b><u>Gateware and firmware specifics</u></b>



<b><u>OLD FROM HERE</u></b>




Quick start

The SD card .wic image is available at ...

It can be flashed to a microSD card using

umount /dev/sda\*

dd if=xxx.wic of=/dev/sda bs=4M

Where /dev/sda is to be replaced with the path to which the microSD card is mounted.

The full hardware assembly is depicted in Figure xx. A standard 12 V power supply with 5.5/2.5 mm barrel connector supplies skpph2 and a USB-C supply powers the ZUBoard. 

Upon pressing the button, the system will boot with output shown on the serial console (settings 115200N1), the default login is root/root. No DHCP is configured, an IP address can be set using

ifconfig eth0 192.168.1.99

From this point onwards, the system can be accessed via SSH.

The relevant executables are located in /home/root/whiznium/bin/wskdterm and /home/root/whiznium/bin/wzskcmbd, respectively.

For the former, typical output looks like this

Whereas for the latter, this command line shows

And in addition, an internal web server is started such that control over the device can be achieved interactively by browsing the address

<b><u>[http://192.168.1.99:13100</u></b>](http://192.168.1.99:13100/)

Gateware

The Vsp\_core's key features of

Camif: instantiates AMD MIPI CSI-2 Receiver Subsystem (cf. PG232) configured to 4+1 MIPI lanes with 1188 Mbps. This allows the IMX335 to deliver its native resolution of 2592 x 1944 pixels at 30 fps. Direct application of 200 MHz clock as restored pixel data clock with the IP core's AXI-4 Stream output filtered to only consider RAW12 data type. Data of two adjacent pixels (24-bit words) is delivered towards videoin on each clock cycle

Videoin: delivers one RGB/grayscale value every other clock cycle at 1296 x 972 resolution

Decim: features a 38 kB DPBRAM which results in edge sizes of xxx for grayscale and xxx for RGB.

Hdreng/Ddrif: using fMemclk = 250 MHz on the 128-bit AXI-4 interconnect allows for a theoretical bandwidth of 4 GB/s; load and store operation is handled via 128-bit:64-bit DPRAM's implementing serving as CDC interface as well

Hostif: the PS-PL AXI-4 Lite interconnect is 64 bits wide which is also the bus width for all connected buffers to be read from the host

A straightforward block design, shown in Figure XXX, has been put together in Vivado 2024.2. Visible are the discrete vsp\_core I/O's promoted to top level, the PS-PL connection HPM0 which uses AXI4-Lite for core control from the CPU (base address 0x20\_0000\_0000) and the PL-PS connection HPS0 which allows the core to access the 256 MB:128 MB:384 MB section of the ZUBoard's 1 GB DDR memory. No RTL sources are required for the top-level design in addition to the auto-maintained HDL wrapper provided by Vivado.

Resource utilization is shown in Figure XXX.

Memory map ... DDR memory only?

Bring-up from sources

Two separate Vivado 2024.2 projects are available online, one for the Vision Processor IP core vsp\_core and one for the top-level project embedding it wskd. Bitstream generation is straightforward.

... https://content.mpsitech.cloud/kb6/wskd_v1.0.3/wskd.tgz, vsp\_core.tgz

As for the PetaLinux 2024.2 project (PetaLinux being a wrapper for Yocto ... / Bitbake ... in this case), the relevant configuration can be found at

... https://content.mpsitech.cloud/kb6/wskd_v1.0.3/project-spec.tgz

It can be built and deployed in the standard way detailed in \[1\].
