def save_mfcc(dataset_path, num_mfcc=13, n_fft=2048, hop_length=512, num_segments=10):
    import os
    import json
    import librosa
    import math
    SAMPLE_RATE = 22050
    TRACK_DURATION = 30 # measured in seconds
    SAMPLES_PER_TRACK = SAMPLE_RATE * TRACK_DURATION
    data = {
        "mfcc": []
    }
    DATASET_PATH = dataset_path

    samples_per_segment = int(SAMPLES_PER_TRACK / num_segments)
    num_mfcc_vectors_per_segment = math.ceil(samples_per_segment / hop_length)

    signal, sample_rate = librosa.load(dataset_path, sr=SAMPLE_RATE)

    for d in range(num_segments):
      start = samples_per_segment * d
      finish = start + samples_per_segment

      mfcc = librosa.feature.mfcc(signal[start:finish], sample_rate, n_mfcc=num_mfcc, n_fft=n_fft, hop_length=hop_length)
      mfcc = mfcc.T

      if len(mfcc) == num_mfcc_vectors_per_segment:
        data["mfcc"].append(mfcc.tolist())

    return(data) 