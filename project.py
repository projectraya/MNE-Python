import mne
import matplotlib.pyplot as plt

sample_data_folder = mne.datasets.sample.data_path()
raw_path = sample_data_folder / 'MEG' / 'sample' / 'sample_audvis_raw.fif'

raw = mne.io.read_raw_fif(raw_path, preload=True)

raw.pick_types(meg=False, eeg=True, exclude='bads')

raw.notch_filter(freqs=50.0, fir_design='firwin')

raw.filter(l_freq=1.0, h_freq=40.0, fir_design='firwin')

raw.plot(duration=10.0, n_channels=15, scalings='auto', title='Изчистени EEG сигнали (MNE-Python)');

plt.show()
raw.plot(duration=10.0, n_channels=15, scalings='auto', title='Изчистени EEG сигнали (MNE-Python)', block=True);