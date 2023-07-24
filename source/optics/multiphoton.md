# Multiphoton microscope

```{note}
This page is still under active development
```

## 2P2

2P2 is a very flexible and custom-made system which has a Mai Tai
imaging laser between 690-1040 nm manipulated by a galvo-galvo scanner
OR a resonant-resonant scanner. Compared to InsightX3+ and DeepSee
laser on 2P3 or 2P4, laser power is relatively low, but it is great
enough to see GCaMP/GFP  and GECO/ tdTomato at the 0-500um deep
inside.
You can use up to three Hamamatsu GaAsP PMTs at the same time or two
GaAsP PMTs/stimulation lightpaths through objective for optogenetics.
I am typically using BFP/EGFP/tdTomato recording by 720/920 nm
wavelength or GCaMP6f + wide field optical stimulation with
yellow-orange Laser, and 700 nm excitation with BFP emission filter
for NADH recording. But you can change the filter combination as you
like.

One interesting feature of 2P2 is that you can swing the objective
between +-45 degree range (but I never used it). Also, I have set up
an environmental chamber to keep 37C and 5% CO2 inside for live cells
or brain slices.

Disadvantage of 2P2 compared to 2P3 or 2P4 is you need to operate with
Scanimage software, which is not user friendly like PrairieView. And
you cannot change some of the parameters through the software, etc,
PMT voltages and Pockel’s. Also there are no eye-piece, which is bad
when you find the focus, although it has a camera.

Lastly, I would recommend 2P3 or 2P4 as the primary choice to meet
most of the imaging needs from imaging quality's and UI's point of
view, but if you need extra setup, I am happy to show you and help
with the setup.

## 2P3

2P3 has an Insight X3+ imaging laser that not only performs well at traditional wavelengths used for GCaMP/GFP, but performs better at higher wavelengths (960-1300 nm) than the older Mai Tai models. In addition, 2P3 has a Mai Tai laser and both laser are aligned through the imaging path allowing dual wavelength imaging if desired. To achieve this, we sacrificed the capability to do 2P uncaging. Thanks to a recent upgrade, both lasers and their Pockel’s are controllable through the PrairieView software. Please check with me if you’d like to be trained on this feature. Additionally, the Insight X3+ has a fixed wavelength output that is not in use (Do not open this shutter!). The microscope has attachments for optogenetics with an opto laser and built in LEDs. Make sure that  your opto stimulation effectively triggers the PMT shutters before using to prevent damage to the PMTs. Both lasers have tunable dispersion compensation.

 

2P4 has a Mai Tai DeepSee for the imaging laser that was recently refurbished. It also has a traditional Mai Tai (the old 2P4 imaging laser) in the uncaging path (these two lasers currently use separate Mai Tai software labeled on the desktop). This means that 2P4 can be used for targeted 2P optogenetics and for uncaging. It technically has a module that allows it to switch between uncaging and dual wavelength imaging, but according to Grayson this does not work well. Thomas aligned the laser for uncaging, but no one has used it yet so it may require debugging/optimizing or at the very least some pilots before beginning. It also has an attachment option for opto lasers.

 

In conclusion, 2P3 is great for applications requiring higher wavelengths or multiple wavelengths for imaging. 2P4 is the only laser currently capable of targeted 2P opto or uncaging. For everything else, these two microscope are equivalently good and I would advise planning your experiments for whatever scope is being underutilized, or even making your rig/code easily transferrable between the two if you are just starting out (and join their respective Slack channels!).

 

For any questions, training, or before utilizing a feature you are unfamiliar with be sure to reach out to Jen (2P4) or me (2P3).  
## 3P1