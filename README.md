# Alzheimers_Data_Decoding
 
This dataset, cited as OpenNeuro Dataset ds004504, found on: https://openneuro.org/datasets/ds004504/versions/1.0.7 is being used to practice ML on Alzheimers patient data, and potentially identify or predict any patterns that might be happening. 

V.1.0.7 

Citation: 
Andreas Miltiadous and Katerina D. Tzimourta and Theodora Afrantou and Panagiotis Ioannidis and Nikolaos Grigoriadis and Dimitrios G. Tsalikakis and Pantelis Angelidis and Markos G. Tsipouras and Evripidis Glavas and Nikolaos Giannakeas and Alexandros T. Tzallas (2024). A dataset of EEG recordings from: Alzheimer's disease, Frontotemporal dementia and Healthy subjects. OpenNeuro. [Dataset] doi: doi:10.18112/openneuro.ds004504.v1.0.7

- "A": "Alzheimer Disease Group",
- "F": "Frontotemporal Dementia Group",
- "C": "Healthy Group"

Channels used and measured from EEG: 'Fp1', 'Fp2', 'F3', 'F4', 'C3', 'C4', 'P3', 'P4', 'O1', 'O2', 'F7', 'F8', 'T3', 'T4', 'T5', 'T6', 'Fz', 'Cz', 'Pz'. This is taken from standardized 10-20 testing, specifically of the cerebral cortex. (https://en.wikipedia.org/wiki/Cerebral_cortex)

Specifically, this reads from the Fp (Pre-frontal), F (Frontal), C (Central), P (Parietal), O (Occipital), T (Temporal) areas of the brain. A diagram of these channel locations can be found in figures, taken from a generated image from EEGLab. The rest of this code is done with reference to: https://www.mdpi.com/2306-5729/8/6/95, https://mne.tools/stable/auto_tutorials/machine-learning/, and of course, stack exchange. 
