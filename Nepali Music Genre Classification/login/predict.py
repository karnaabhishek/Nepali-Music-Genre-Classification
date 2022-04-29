def predict_gen(X):
    import pickle
    import os
    import keras
    import tensorflow as tf
    from django.conf import settings
    print(os.listdir())
    
    data = tf.keras.models.load_model(r'C:\Users\akarn\Desktop\mysite\login\models\my_model.h5')
    print(data)
    y = data.predict(X)
    apple = []
    for i in range(10):
        apple.append(y[i].argmax())
    max = 0
    res = apple[0]
    for i in apple:
        freq = apple.count(i)
        if freq > max:
            max = freq
            res = i
    return res

