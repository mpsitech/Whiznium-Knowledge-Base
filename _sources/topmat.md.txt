Getting around
==============

The Whiznium Knowledge Base (which you are looking at) is a great way to explore various Whiznium-related topics in depth.

Its articles refer to the Whiznium tools, [WhizniumSBE](https://github.com/mpsitech/wznm-WhizniumSBE) (Service Builder's Edition, for Linux daemons) and [WhizniumDBE](https://github.com/mpsitech/wdbe-WhizniumDBE) (Device Builder's Edition, for RTL designs and their host-side access libraries), for which you can find step-by-step setup instructions in [The Whiznium Documentation](https://github.com/mpsitech/The-Whiznium-Documentation/blob/main/setup.md).

Many examples found here are based on the Whiznium Computer Vision Demonstrator which is tabletop 3D laser scanner hardware, powered by entry-level development kits of various FPGA(-SoC) vendors. [Contact MPSI](mailto:contact@mpsitechnologies.com) to obtain your unit with the hardware variant of your choice. Discounts are available for classroom quantities.

Finally, experienced Whiznium users will appreciate the [WhizniumSBE Reference](https://mpsitech.github.io/The-WhizniumSBE-Reference) and [WhizniumDBE Reference](https://mpsitech.github.io/The-WhizniumDBE-Reference) guides for quick lookup e.g. of model file structure.


Topic matrix
============

wznm: WhizniumSBE (multi-threaded Linux daemons)<br>
wdbe: WhizniumDBE (FPGA subsystems talking to Linux hosts)<br>
wcvd: Whiznium Computer Vision Demonstrator (tabletop 3D laser scanner)<br>
vnd: FPGA vendor abstraction<br>
sys: system integration across the Embedded Full Stack<br>

|wznm|wdbe|wcvd|vnd|sys|identifier|release date|spotlight on ...|
|:--:|:--:|:--:|:-:|:-:|---|---|---|
|    |    |x   |   |   |KB0 Whiznium CV Demonstrator|2026-04-06|demontstrator project and paths of exploration|
|    |x   |x   |   |   |KB1 Stepper Motor Control|2026-04-06|basic use of FPGA design sub-modules as virtual controllers|
|    |x   |x   |   |x  |KB2 Image Decimation for Preview|2026-04-06|vertical integration from RTL level across Linux to web UI|
|    |x   |x   |   |   |KB3 HDR Image Generation DMA|2026-04-06|inclusion of external memory and platform-specific implications|
|x   |    |x   |x  |   |KB4 Vendor-Agnostic Design Probing|2026-04-08|use of templates for signal-level debug outside of vendor IDE's|
|x   |    |x   |   |   |KB5 Mastering the Job Tree|2026-04-12|key concepts of the run-time job hierarchy including calls and dispatches|
|    |    |x   |x  |   |KB6 AMD MPSoC Variant|2026-04-13|platform-specifics and build instructions for Avnet's ZUBoard|
|    |    |x   |x  |   |KB7 Efinix Titanium Variant|2026-04-13|platform-specifics and build instructions for Efinix's Ti180 dev kit|
|    |    |x   |x  |   |<div style="color:lightgray">KB8 Microchip PolarFire SoC Variant</div>|release pipeline #2|platform-specifics and build instructions for Microchip's MPFS Disco kit|
|    |x   |x   |   |   |<div style="color:lightgray">KB9 Pipelined Corner Detection Algorithm</div>|release pipeline #1|pipelined and parallel execition, a key FPGA strength|
|x   |    |    |   |x  |<div style="color:lightgray">KB10 Web UI Customization</div>|TBD|integration of non-standard UI features into auto-generated context|
|x   |    |    |   |   |<div style="color:lightgray">KB11 Complex Database Structures</div>|TBD|modeling of relational SQL databases and auto-generated artefacts|
|x   |    |    |   |x  |<div style="color:lightgray">KB12 C++ and Java Accessor Apps</div>|TBD|auto-generated API libraries used to automate remote / UI interactions|
|x   |    |    |   |x  |<div style="color:lightgray">KB13 OPC UA and DDS Integration</div>|TBD|enabling M2M communication with industry-standard protocols|
|    |    |x   |x  |   |<div style="color:lightgray">KB14 Altera Agilex 3 Variant</div>|TBD|platform-specifics and build instructions for Altera's Agilex 3 C-Series dev kit|
|    |    |x   |x  |   |<div style="color:lightgray">KB15 Lattice Avant-E Variant</div>|TBD|platform-specifics and build instructions for Lattice's Avant-E FPGA eval board|
|x   |    |    |   |   |<div style="color:lightgray">KB16 Import Export Complexes</div>|TBD|readers and writers for text-/XML-based data of relational SQL database|
|    |x   |    |   |   |<div style="color:lightgray">KB17 Parametrized Median Filter Module Template</div>|TBD|WhizniumDBE customization with modeling and vendor-specific code generation|
|x   |    |    |   |   |<div style="color:lightgray">KB18 Managed File Archive Capability</div>|TBD|WhizniumSBE customization comprising modeling and code generation|
|    |    |x   |x  |   |<div style="color:lightgray">KB19 AMD Artix 7 Variant</div>|TBD|platform-specifics and build instructions for Digilent's Nexys Video board|
|x   |    |x   |   |   |KB20 Daemon Command Line Debug|2026-04-12|built-in daemon features to debug job-job interaction and multi-threading|
|x   |    |x   |   |   |<div style="color:lightgray">KB21 Modern Web UI's using Vue.js</div>|TBD|alternative Vue.js UI from generated code to transpilation and deployment|
|x   |x   |    |   |   |<div style="color:lightgray">KB22 Whiznium Initialization</div>|TBD|baseline combined with custom / project-specific tool initialization|
|x   |    |x   |   |   |<div style="color:lightgray">KB23 Anatomy of a WhizniumSBE Project</div>|TBD|source code tree organization and coding best practices|
