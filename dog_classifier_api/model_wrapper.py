from fastai.vision.core import *
from fastai import *
from fastai.learner import load_learner

from django.conf import settings

def classify_dog(img_bytes):
    '''
    NOTE: It would be better to have a cron type thing for this, so we don't have to load_leaner every time
    '''

    dog_model = load_learner(settings.DOG_CLASSIFIER_API_MODEL_PATH)

    pred, pred_idx, probs = dog_model.predict(img_bytes)
        

    return pred, float(probs[pred_idx])
    