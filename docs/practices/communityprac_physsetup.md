[Physiological Data Setup](#setup)
========================

Where to start in setting up a physiological monitoring system?
-------------------------

#### Peripheral devices:

**Cardiac**  
 
-	finger photoplethysmograph (pulse-oximeter)
- 	ECG electrodes

**Respiratory**

-   respiratory belt
-   disposable nasal cannula

**Gasses**

-	nasal cannula
-   long sample line to connect from the scan room to the control room

Some peripheral devices can be passed through a waveguide in the penetration panel 
from the control room to the scan room (e.g., gas sampling line); others must be 
plugged into the penetration panel for noise filtering (e.g., some pulse sensors). 
Devices native to the MRI scanner may communicate wirelessly with the scanner. 
When adding non-native peripheral devices to the scanner environment, we recommend 
that you check that you are not bringing any outside noise into the scan room or 
bringing too much scanner noise into the physiological recordings. It may be 
necessary to develop additional devices or mechanisms to shield these connections.

#### Recording devices:

**Cardiac**

-	analog-to-digital (ADC) or other data acquisition (DAQ)
    device
-   associated signal recording/analysis software

**Respiratory**

-   analog-to-digital converter (ADC) or other data acquisition (DAQ)
    device
-   associated signal recording/analysis software

**Gasses**

-   CO2 and O2 analyzer
-   analog-to-digital converter (ADC) or other data acquisition (DAQ)
    device
-   associated signal recording/analysis software

There are several devices that can be used for physiological data acquisition, such 
as ADInstruments (https://www.adinstruments.com/) or Biopac (https://www.biopac.com/). 
ADInstruments developed Powerlab and this system uses the LabChart software; 
Biopac developed the MP160 system and uses the AcqKnowledge software. It is 
possible to combine ADInstruments stacks and Biopac sensors. Nevertheless, the 
community recommended practices stated here should be valid independently of the 
acquisition system used. [SETUP_170322]

Syncing physiological data with the neuroimaging acquistion
-------------------------
In most cases, it is important to sync the physiological recordings with the 
neuroimaging recordings. In the case of fMRI, scan triggers may be used for this 
purpose. To do this, it will be necessary to extract the trigger pulses from your 
MRI scanner, typically inputting these analog signals via BNC into the same ADC 
that is recording the physiological information. If this option cannot be used, 
another way of obtaining some information from the scanner is to send a volt pulse 
as a block for the whole duration of the scan. [SETUP_170322]. 

Depending on the physiological acquisition equipment, this process may be more or 
less challenging. Using ADI, the integration of volume triggers is straightforward, 
and for BIOPAC, we may use a USB sniffer to record changes in signal in the USB 
stream (https://www.bugblat.com/products/minisniff/index.html). [SETUP_170322]

Examples setups from our community members
-------------------------
Siemens MR Physiological recording
- 	coming soon...

3T Philips Intera Achieva with BIOPAC MP160
-	coming soon...
