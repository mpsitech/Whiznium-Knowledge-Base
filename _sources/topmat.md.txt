Topic matrix
============

wznm: WhizniumSBE (multi-threaded Linux daemons)<br>
wdbe: WhizniumDBE (FPGA subsystems talking to Linux hosts)<br>
wcvd: Whiznium Computer Vision Demonstrator (tabletop 3D laser scanner)<br>
vnd: FPGA vendor abstraction<br>
sys: system integration across the Embedded Full Stack<br>

|wznm|wdbe|wcvd|vnd|sys|identifier|release date|spotlight on ...|
|---|---|---|---|---|---|---|---|
|||x|||KB0 Whiznium CV Demonstrator|TBD|demontstrator hardware and paths of exploration|
||x|x|||KB1 Stepper Motor Control|2026-02-24|basic use of FPGA design sub-modules as virtual controllers|
||x|x|||<div style="color:lightgray">KB2 Pipelined Corner Detection Algorithm</div>|TBD|pipelined and parallel execition, a key FPGA strength|
||x|x|||KB3 HDR Image Generation DMA|2026-02-24|handling of large chunks of data shared between PS and PL|
|x||x|x||<div style="color:lightgray">KB4 Vendor-Agnostic Design Probing</div>|TBD|use of templates for signal-level debug outside of vendor IDE's|
|x||x|||<div style="color:lightgray">KB5 Daemon Command Line Debug</div>|TBD|built-in daemon features to debug job-job interaction and multi-threading|
|||x|x||KB6 AMD MPSoC Variant|2026-02-24|platform-specifics and build instructions for Avnet's ZUBoard|
|||x|x||KB7 Efinix Titanium Variant|2026-02-24|platform-specifics and build instructions for Efinix's Ti180 dev kit|
|||x|x||KB8 Microchip PolarFire SoC Variant|release pipeline #1|platform-specifics and build instructions for Microchip's MPFS Disco kit|
|x|x||||<div style="color:lightgray">KB9 Whiznium Initialization</div>|release pipeline #2|baseline combined with custom / project-specific tool initialization|
|x||||x|<div style="color:lightgray">KB10 Web UI Customization</div>|TBD|integration of non-standard UI features into auto-generated context|
|x|||||<div style="color:lightgray">KB11 Complex Database Structures</div>|TBD|modeling of relational SQL databases and auto-generated artefacts|
|x||||x|<div style="color:lightgray">KB12 C++ and Java Accessor Apps</div>|TBD|auto-generated API libraries used to automate remote / UI interactions|
|x||||x|<div style="color:lightgray">KB13 OPC UA and DDS Integration</div>|TBD|enabling M2M communication with industry-standard protocols|
|||x|x||<div style="color:lightgray">KB14 Altera Agilex 5 Variant</div>|TBD|platform-specifics and build instructions for Altera's Agilex 3 C-Series dev kit|
|||x|x||<div style="color:lightgray">KB15 Lattice Avant-E Variant</div>|TBD|platform-specifics and build instructions for Lattice's Avant-E FPGA eval board|
|x|||||<div style="color:lightgray">KB16 Import Export Complexes</div>|TBD|readers and writers for text-/XML-based data of relational SQL database|
||x||||<div style="color:lightgray">KB17 Parametrized Median Filter Module Template</div>|TBD|WhizniumDBE customization with modeling and vendor-specific code generation|
|x|||||<div style="color:lightgray">KB18 Managed File Archive Capability</div>|TBD|WhizniumSBE customization comprising modeling and code generation|
|||x|x||<div style="color:lightgray">KB19 AMD Artix 7 Variant</div>|TBD|platform-specifics and build instructions for Digilent's Nexys Video board|
|x||x|||<div style="color:lightgray">20 Mastering the Job Tree</div>|release pipeline #3|key concepts of the run-time job hierarchy including calls and dispatches|
|x||x|||<div style="color:lightgray">21 Modern Web UI's using Vue.js</div>|TBD|alternative Vue.js UI from generated code to transpilation and deployment|
