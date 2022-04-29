def save_mfcc(dataset_path, num_mfcc=40, num_segments=20):
  import os
  import json
  import librosa
  import math
  import numpy as np

  data = {
      "mfcc": []
      }
  SAMPLE_RATE = 22050
  TRACK_DURATION = 30 # measured in seconds
  SAMPLES_PER_TRACK = SAMPLE_RATE * TRACK_DURATION

  samples_per_segment = int(SAMPLES_PER_TRACK / num_segments)

  signal, sample_rate = librosa.load(dataset_path, sr=SAMPLE_RATE)

  for d in range(num_segments):
    start = samples_per_segment * d
    finish = start + samples_per_segment

    mfcc = librosa.feature.mfcc(signal[start:finish], sample_rate, n_mfcc=num_mfcc)
    mfccs_scaled_features = np.mean(mfcc.T,axis=0)

    data["mfcc"].append(mfccs_scaled_features.tolist())
  return(data)
