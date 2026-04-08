IP cores for vendor-agnostic design probing (KB4)
=================================================

*Published: official date pending*

*Highlights the use of templates for signal-level debug outside of vendor IDE's.*

*Categories: WhizniumSBE, Whiznium CV Demonstrator, FPGA Vendors*

Model and source code file pointers: in \[1\] \_mdl/IexWdbeMdl_wskd.xlsx, fpgawskd/zuvsp/Memtrack.vhd; in \[2\] wzskcmbd/gbl/JobWzskAcqMemtrack.{h/cpp}, wzskcmbd/CrdWzskHwc/PnlWzskHwcDebug.{h/cpp}

This deep-dive covers the use of Whiznium for a topic that oftentimes implies unnecessary vendor lock-in: live probing of an FPGA design. The module templates *gptrack_Easy_v1_0* (general purpose signals) and *fsmtrack_Easy_v1_0* (FSM states) serve this purpose.

<b><u>General-purpose signal tracking</u></b>


<img src="KB4/image1.png" alt="image1.png" height="501">

*Figure 1: Web UI for general-purpose signal track acquisition*



<img src="KB4/image2.png" alt="image2.png" height="281">

*Figure 2: GTKWave displaying AXI4 full handshake signals for DDR memory write-then-read for the HDR functionality at each end-of-line*


To track the relevant AXI4 full signals during DDR memory operations, *gptrack_Easy_v1_0* is instantiated as *memtrack*. In the module parameter section of the *IexWdbeMdl* model file entry, the capture signal clock, capture / trigger signal identifiers and the sequence buffer size are specified. Based on the vendor- and CPU-host-interface-agnostic IP core, then a customized version is generated which is accessible through commands and buffer transfers from the CPU side. A single instance captures up to 15-bit wide data with registered inputs, and it also features compressed storage for periods during which none of the signals change.

In the

<b><u>FSM state tracking</u></b>


<img src="KB4/image3.png" alt="image3.png" height="586">

*Figure 3: Web UI for FSM state track acquisition*



<img src="KB4/image4.png" alt="image4.png" height="237">

*Figure 4a: GTKWave displaying the RGB egress FSM states of the videoin module during 1+ lines*



<img src="KB4/image5.png" alt="image5.png" height="237">

*Figure 4b: GTKWave detail of the above towards close to end-of-line*


<b><u>CPU-side elements</u></b>

As in previous examples, a pre-defined WhizniumSBE *capability* is used for buffer read-out, .vcd file generation and storage. The corresponding control panel *PnlWzskHwcDebug* is shown at the bottom right of Figure 10. It instantiates *JobWzskAcqMemtrack* as sub-job which in turn interacts with the FPGA subsystem via *JobWzskSrc\*vsp* using a trigger / poll loop. Finally, Figure 11 displays a waveform captured on an AMD MPSoC system in an industry-standard tool.

The capability, currently limited to acquiring the track of a single module at a time, results in an interactive
