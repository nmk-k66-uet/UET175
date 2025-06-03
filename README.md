# UET175: EEG database of motor imagery tasks in Vietnamese stroke patients

This is the UET175 dataset, which features a comprehensive collection of 
electroencephalogram (EEG) signals collected from 30 post-stroke patients at Hospital 175
in Ho Chi Minh City, Vietnam, during the time-frame from October 2024 to January 2025. 
Our research team's primary goal is to develop a standardized protocol for EEG data acquisition 
that guarantees both consistency and reliability in various research applications.

In this repository, we present download links for all dataset files in its compressed form.
For the decompression password, please contact our correspondence through these emails: **chaumt@vnu.edu.vn**, or **kienprb@gmail.com**   

![959ef362-eb7d-4d6f-b3ae-607b1ca92344](https://github.com/user-attachments/assets/ab1a2513-d7f0-4568-b3d8-ee5b7dc119b9)
## Recording device
EEG data was collected using the saline version of the Emotiv EPOC Flex device with 128Hz sampling rate. 22 out of the 32 supported channels are used, as illustrated in **Figure A**. 
Lab Streaming Layer settings were: Data stream - EEG, Sampling frequency - 128Hz, Data format - Double, Transmit type - Sample

## Recording scenario
**Figure B** illustrates the scenario used for data acquisition. 
In step 1, at the start of an action, the recording app plays a notification sound, prompting the patient to relax and loosen their body for 2 seconds. 
In step 2, the system displays a prompt image along with a notification sound corresponding to one of four MI tasks: lifting the right arm, lifting the left arm, lifting the right leg, or lifting the left leg, which lasts for 2 seconds. 
In step 3, the patient imagines the corresponding movement suggested by the prompt for 4 seconds. 
This process repeats 12 times (3 times for each task mentioned in step 2) in each run, followed by a 20-second resting period between runs.

## Data Directory Structure
The structure of the database is illustrate in **Figure C**. The main directory, "**Data**", contains 30 subdirectories, one for each patient.
Within each of these directories, there is a .json file containing information on the corresponding patient (year of birth, gender, medical conditions, professional diagnoses, medical assessments and number of EEG recording sessions) and one or more subdirectories for each session named based on the session's ID and date of recording.
Each session will contain multiple runs, the data relating to each consists of a Raw Signal (.csv) file, a Session setup (.json), an Action label (.txt), and an Event timestamp (.txt). The detailed content of these files are described in our paper.

If you make use of this dataset, please consider citing the following papers:

## Original UET175 paper:
```
Ma Thi C,Nguyen The H-A, Nguyen Minh K, 
Vu Thanh L, Nguyen Dinh H, Huynh Thi N-Y, 
Ha Thi T-H, Hoang Tien T-N, Au Dao D-T,
Nguyen Hoang K-L, Huynh Kha V and Le Hoang T-L (2025) UET175: EEG dataset of
motor imagery tasks in Vietnamese stroke
patients. Front.Neurosci. 19:1580931.
doi: 10.3389/fnis.2025.1580931
```

## Copyright:
© 2025 Ma Thi, Nguyen The, Nguyen Minh, 
Vu Thanh, Nguyen Dinh, Huynh Thi, Ha Thi,
Hoang Tien, Au Dao, Nguyen Hoang, Huynh
Kha and Le Hoang.This is an open-access
article distributed under the terms of the
Creative Commons Attribution License (CC
BY).The use, distribution or reproduction in
other forums is permitted, provided the
original author(s) and the copyright owner(s)
are credited and that the original publication
in this journal is cited, in accordance with
accepted academic practice. No use,
distribution or reproduction is permitted 
which does not comply with these terms.
