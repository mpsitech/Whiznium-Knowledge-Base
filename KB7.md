Efinix Titanium variant (KB7)
=============================

*Published: April 14, 2026*

*Highlights the platform-specifics and build instructions for Efinix\'s Ti180 dev kit.*

*Categories: Whiznium CV demonstrator, FPGA vendors*

<b><u>Overview</u></b>

The Efinix Titanium Ti180 is a fabric-only device which, by using the Sapphire SoC IP, can be configured to include up to four 32-bit RISC-V soft cores capable of running Linux. Its development kit [1] complements the SoC chip with DDR memory, JTAG and a microSD card slot. Additionally, the device's hardened MIPI interfaces as well as Ethernet are made available through Efinix-provided adapter boards.

<img src="KB7/setup_low.jpg" alt="setup_low.jpg" height="600">

*Figure 1: CV demonstrator based on Efinix Ti180 dev kit in action*

Parts specific to this variant ans provided with the delivery, include:

- Syzcam2 adapter PCB for 4+1 MIPI lanes routed as differential pairs, level shifters for I2C

- Syzpmod2 adapter PCB for 2x8 GPIO's ... connecting to skpph2 with power supply to the stepper motor only, the ZUBoard is powered via USB-C


<b><u>Quick Start</u></b>

The hardware setup needs to be established as depicted above. The first-stage boot loaded and FPGA configuration need to be flashed into a dedicated ... . A ready-to-use 16 GB microSD card image can be obtained and flashed using the commands

```
wget https://content.mpsitech.cloud/artefacts/titdvk_wzsk_v1.2.16_wskd_v1.2.15_SD_16GB.img.gz
sudo gunzip -c titdvk_wzsk_v1.2.16_wskd_v1.2.15_SD_16GB.img.gz | sudo dd of=/dev/sda bs=64K
```

<a href="https://content.mpsitech.cloud/artefacts/titdvk_wzsk_v1.2.16_wskd_v1.2.15_ti180-tsemac-linux.hex" target="_blank">titdvk_wzsk_v1.2.16_wskd_v1.2.15_ti180-tsemac-linux.hex</a>,
<a href="https://content.mpsitech.cloud/artefacts/titdvk_wzsk_v1.2.16_wskd_v1.2.15_jtag_spi_flash_loader_dual.bit" target="_blank">titdvk_wzsk_v1.2.16_wskd_v1.2.15_jtag_spi_flash_loader_dual.bit</a>

<b><u>VSP Core Efinity Workflow</u></b>

<a href="https://content.mpsitech.cloud/projects/titdvk_vsp_core_v1.2.15.tgz" target="_blank">titdvk_vsp_core_v1.2.15.tgz</a>

<b><u>Top-level Efinity Workflow</u></b>

<a href="https://content.mpsitech.cloud/projects/titdvk_ti180-tsemac-linux_v1.2.15.tgz" target="_blank">titdvk_ti180-tsemac-linux_v1.2.15.tgz</a>

<b><u>Buildroot Workflow</u></b>

<a href="https://content.mpsitech.cloud/projects/titdvk_wzsk_v1.2.16_br2-efinix-ext-ethernet.tgz" target="_blank">titdvk_wzsk_v1.2.16_br2-efinix-ext-ethernet.tgz</a>


