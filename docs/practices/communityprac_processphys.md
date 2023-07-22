[Community Practices for Working with Physiological Data](#bestpractice)
================================================

Ideally you have recorded physiological data throughout the entire scan session, and have trigger data to identify when scanning occurred. Phys2bids can be used to organize the various physiological data traces that you have collected. With this program, your data will have the appropriate BIDS labels to describe physiological information. As a sanity check, you should quickly plot each trace to ensure that it matches the type of information you think you collected.

After this restructuring of the data, there are numerous tools available to process each type of physiological trace, identifying end-tidal values for O2 and CO2, and phases of the cardiac and respiratory cycles. These data are then further processed via smoothing or convolution to create physiological regressors. 

Cardiac Pulsation
-------------------------------

Cardiac contractions can influence fMRI signals due to the pulsatility generating small movements in brain tissue as well as inflow effects in and near the vessels. These cardiac pulsation phenomena localize in tissue regions close to large arteries and draining veins, such as the sagittal sinus or the circle of Willis, as well as the edges of the brain and sulci (Bhattacharyya and Lowe, 2004, Dagli et al., 1999, Glover et al., 2000).

**Data-driven techniques**

1.	Principal Component Analysis (PCA)

	<u>About:</u> Defining multiple spatially uncorrelated nuisance regressors based on the principal component analysis (PCA) decomposition of voxels where no BOLD fMRI signals of neuronal origin are expected to originate (e.g., WM and CSF). The widely-used CompCor approach (Behzadi et al., 2007; Muschelli et al., 2014) defines multiple nuisance regressors from the principal components (PCs) of voxels within WM and CSF in the ventricles.

	<u>Cons:</u> An important question for debate is how many principal components (PCs) must be considered in the model. 

2.	Independent Component Analysis (ICA)

	<u>About:</u> Once the ICA is computed, the basis of these denoising approaches is to first distinguish between independent components (IC) arising from neuronal-related BOLD signal and ICs related to noise sources, and then remove the latter before reconstructing the dataset (Beckmann, 2012, McKeown et al., 2003).

	<u>Cons:</u> Manual classification of ICs is very time consuming, difficult to reproduce and requires expertise (Kelly Jr. et al., 2010). Automatic classification does help, however, it could mis-classify components and again, it is difficult to discern the number of components you need.

3.	Global Signal Regression (GSR)

	<u>About:</u> Removes the average fMRI signal across all the voxels in the brain under the assumption that the global signal mainly represents all the processes that confound the BOLD fMRI signals, including all instrumental, motion-related and physiological fluctuations.

	<u>Cons:</u> Use of GSR has always been debated since the global signal also includes neuronal-related BOLD fluctuations.

**Model-based techniques**

1. RETROICOR and phase-based models

	<u>Pros:</u> More specific denoising approach than others. 
	<u>Pros:</u> Slice-wise regressors are more complicated to deal with and sometimes have a more negligible effect than other correction techniques.

Other phase based algorithms have expanded from RETROICOR as described in Caballero-Gaudes and Reynolds 2017. One such extension is DRIFTER (Särkkä et al., 2012). 

Respiration
---------------------------------------------

There are three primary ways by which breathing can influence the fMRI signals. Firstly, breathing often leads to bulk motion of the body and head, leading to undesired artifacts in the images. To mitigate these effects, volume registration and motion correction algorithms are typically employed during data preprocessing (Brosch et al. 2002). 

Secondly, breathing changes the chest position which can influence the success of the shim, continuously changing B0 homogeneity throughout the scan and in turn affecting signal amplitude (Brosch et al. 2002, Raj et al. 2001). These effects are also modeled using techniques like RETROICOR.

Thirdly, changes in breathing rate and depth can affect the levels of blood gasses, such as oxygen and carbon dioxide, which can in turn drive vasodilation or vasoconstriction. These vascular changes have a substantial impact on the amplitude of the fMRI signal (Chang and Glover 2009). Respiratory volume per time (RVT) correction (Birn et al. 2008) estimates the change in breathing rate/depth to model these effects.

**Data-driven techniques**

1.	Principal Component Analysis (PCA)

	<u>About:</u> Defining multiple spatially uncorrelated nuisance regressors based on the principal component analysis (PCA) decomposition of voxels where no BOLD fMRI signals of neuronal origin are expected to originate (e.g., WM and CSF). The widely-used CompCor approach (Behzadi et al., 2007; Muschelli et al., 2014) defines multiple nuisance regressors from the principal components (PCs) of voxels within WM and CSF in the ventricles.

	<u>Cons:</u> An important question for debate is how many principal components (PCs) must be considered in the model. 

2.	Independent Component Analysis (ICA)

	<u>About:</u> Once the ICA is computed, the basis of these denoising approaches is to first distinguish between independent components (IC) arising from neuronal-related BOLD signal and ICs related to noise sources, and then remove the latter before reconstructing the dataset (Beckmann, 2012, McKeown et al., 2003).

	<u>Cons:</u> Manual classification of ICs is very time consuming, difficult to reproduce and requires expertise (Kelly Jr. et al., 2010). Automatic classification does help, however, it could mis-classify components and again, it is difficult to discern the number of components you need.

3.	Global Signal Regression (GSR)

	<u>About:</u> Removes the average fMRI signal across all the voxels in the brain under the assumption that the global signal mainly represents all the processes that confound the BOLD fMRI signals, including all instrumental, motion-related and physiological fluctuations.

	<u>Cons:</u> Use of GSR has always been debated since the global signal also includes neuronal-related BOLD fluctuations.

**Model-based techniques**

1. 	RETROICOR (Retrospective Image Correction) and phase-based models

	RETROICOR offers a more specific denoising approach compared to other methods and is complementary to measures such as CO2 (carbon dioxide), RV (respiration volume), and RVT (respiration volume per time) estimations. As this method treats each pixel separately, it has the advantage of preventing the artificial coupling of noise corrections across signal regions. However, one drawback of RETROICOR is that slice-wise regressors can be more complicated to handle, and their effects may sometimes be negligible.

2. 	Respiratory volume per time (RVT) and peak-based models

	RVT and peak-based models utilize peak detection on the respiratory trace to estimate the rate and depth of breaths, which enables an indirect estimation of gas volume exchange (Birn et al., 2006). These models rely on a respiratory response function (RRF) derived from empirical observations, considering inter-individual differences (Birn et al., 2008). They are advantageous in capturing time-delayed effects interacting with CO2 levels. However, peak detection in these models may require manual effort, and efforts should be made to automate this process.

3. 	Respiration variation (RV) and other models (standard deviation/signal property based)

	RV (standard deviation of the respiratory trace over a window) (Chang and Glover, 2009) and other signal property-based models such as ENV (envelope of the respiratory trace over a window) (Power et al., 2018) provide an alternative to RVT-based approaches. These models do not rely on peak detection, reducing the need for manual intervention. However, they are more susceptible to biases introduced by noise, which can affect the accuracy of the analysis.

In summary, several models and methods exist for analysing the effects of respiration on fMRI signal changes. Each approach has its strengths and limitations, ranging from specific denoising capabilities to the complexity of calculations and the need for manual peak detection. Researchers should carefully select and validate the appropriate approach based on their specific research questions and the characteristics of their data.

Blood Gasses
-------------------------

Importantly, the respiratory signals sampled show the fluctuations in CO2 and O2 
occurring during each breathing cycle. In order to retrieve the corresponding 
end-tidal signals it is necessary to perform some processing. Most of the processing 
steps are performed using in-house algorithms, and are highly dependent on the goal 
of the experiment. Nevertheless, there are steps that are commonly performed in most 
experiments, such as extracting the end-tidal points from the respiratory trace 
collected. This can be performed by identifying the lowest point per breath from 
the oxygen trace and the highest point per breath of the CO2 trace. Afterwards it 
is necessary to adjust this trace for the sampling delay. Every gas analysis system 
will have its own sampling delay, mainly determined by the length of the sampling 
line used and the power of the pump pulling the gas into the analysis device. The 
simplest way of estimating this delay is to use a breath-hold task 
(e.g. \"breathe in\", \"breathe out\", \"breathe in and hold your breath\"), 
set a marker (before the “hold your breath” cue) and measure the corresponding 
respiratory order to identify the delay between the marker and the expected 
respiratory signal changes (increase due to the \"breathe in\" cue and decrease due 
to the \"hold your breath\" cue). In order for this trace to be used as a regressor, 
it is also necessary to interpolate the end-tidal points and downsample the time 
course to match the fMRI resolution. 

Using Physiological Data as Signals of Interest
-------------------------
Physiological regressors can be incorporated into a generalized linear model 
framework to explain portions of your fMRI signal attributed to physiological 
effects.

1. 	Common cardiac pulsation regressors include heart rate (HR) and heart rate variability (HRV).
2.	Respiratory
3.	Blood Gasses
4.	Lymphatics

More coming... work in progress

References
----------

Bhattacharyya, P. K., & Lowe, M. J. (2004). Cardiac-induced physiologic noise in tissue is a direct observation of cardiac-induced fluctuations. Magnetic resonance imaging, 22(1), 9-13.

Dagli, M. S., Ingeholm, J. E., & Haxby, J. V. (1999). Localization of
cardiac-induced signal change in fMRI. NeuroImage, 9(4), 407--415.
<https://doi.org/10.1006/nimg.1998.0424>

Glover, G. H., Li, T., & Ress, D. (2000). Image‐based method for
retrospective correction of physiological motion effects in fMRI:
RETROICOR. Magnetic Resonance in Medicine, 44(1), 162--167.
<https://doi.org/10.1002/1522-2594(200007)44:1>\<162::AID-MRM23\>3.0.CO;2-E

Behzadi, Y., Restom, K., Liau, J., & Liu, T. T. (2007). A component based noise correction method (CompCor) for BOLD and perfusion based fMRI. Neuroimage, 37(1), 90-101.

Muschelli, J., Nebel, M. B., Caffo, B. S., Barber, A. D., Pekar, J. J., & Mostofsky, S. H. (2014). Reduction of motion-related artifacts in resting state fMRI using aCompCor. Neuroimage, 96, 22-35.

Beckmann, C. F. (2012). Modelling with independent components. Neuroimage, 62(2), 891-901.

McKeown, M. J., Hansen, L. K., & Sejnowsk, T. J. (2003). Independent component analysis of functional MRI: what is signal and what is noise?. Current opinion in neurobiology, 13(5), 620-629.

Kelly Jr, R. E., Alexopoulos, G. S., Wang, Z., Gunning, F. M., Murphy, C. F., Morimoto, S. S., ... & Hoptman, M. J. (2010). Visual inspection of independent components: defining a procedure for artifact removal from fMRI data. Journal of neuroscience methods, 189(2), 233-245.

Caballero-Gaudes, C., & Reynolds, R. C. (2017). Methods for cleaning the
BOLD fMRI signal. NeuroImage, 154(December 2016), 128--149.
<https://doi.org/10.1016/j.neuroimage.2016.12.018>

Särkkä, S., Solin, A., Nummenmaa, A., Vehtari, A., Auranen, T., Vanni, S., & Lin, F. H. (2012). Dynamic retrospective filtering of physiological noise in BOLD fMRI: DRIFTER. NeuroImage, 60(2), 1517-1527.

Brosch, J. R., Talavage, T. M., Ulmer, J. L., & Nyenhuis, J. A. (2002).
Simulation of human respiration in fMRI with a mechanical model. IEEE
Transactions on Biomedical Engineering, 49(7), 700--707.
<https://doi.org/10.1109/TBME.2002.1010854>

Raj, D., Anderson, A. W., & Gore, J. C. (2001). Respiratory effects in
human functional magnetic resonance imaging due to bulk susceptibility
changes. Phys. Med. Biol, 46, 3340.

Chang, C., & Glover, G. H. (2009). Relationship between respiration,
end-tidal CO2, and BOLD signals in resting-state fMRI. NeuroImage,
47(4), 1381--1393. <https://doi.org/10.1016/j.neuroimage.2009.04.048>

Birn, R. M., Smith, M. A., Jones, T. B., & Bandettini, P. A. (2008). The
respiration response function: The temporal dynamics of fMRI signal
fluctuations related to changes in respiration. NeuroImage, 40(2),
644--654. <https://doi.org/10.1016/j.neuroimage.2007.11.059>

Birn, R. M., Diamond, J. B., Smith, M. A., & Bandettini, P. A. (2006).
Separating respiratory-variation-related fluctuations from
neuronal-activity-related fluctuations in fMRI. NeuroImage, 31(4),
1536--1548. <https://doi.org/10.1016/j.neuroimage.2006.02.048>

Power, J. D., Plitt, M., Gotts, S. J., Kundu, P., Voon, V., Bandettini, P. A., & Martin, A. (2018). Ridding fMRI data of motion-related influences: Removal of signals with distinct spatial and physical bases in multiecho data. Proceedings of the National Academy of Sciences, 115(9), E2105-E2114.
