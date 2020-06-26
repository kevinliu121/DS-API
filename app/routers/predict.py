
import logging
import random
import pickle
import bz2
import _pickle as cPickle
import praw
import sklearn
from fastapi import APIRouter
import pandas as pd
from pydantic import BaseModel, Field, validator

log = logging.getLogger(__name__)
router = APIRouter()


class Item(BaseModel):
    """Use this data model to parse the request body JSON."""

    title: str = Field(..., example="Is Fusion nullified for the Extreme Z Awakening Event?")
    body: str = Field(..., example="On JP I missed out on my chance to do SSJ3 Goku the first time so I'm doing it now. Been lucked out of rotations for most of these stages and I've noticed that for my Fusions team, LR Gogeta would NEVER fuse. I'm genuinely curious if the mechanic is nullified for the event or i'm just getting AWFUL RNG.")

# Load your pickled model here:
def decompress_pickle(file):
 data = bz2.BZ2File(file, 'rb')
 data = cPickle.load(data)
 return data


model = decompress_pickle('Baseline_SGD_Model.pbz2')

with open("subreddit_list.pkl", 'rb') as file:
    subreddit_list = pickle.load(file)


@router.post('/predict')
async def predict(item: Item):
    """Make baseline predictions for classification problem."""

    # You can access the attributes like this:
    post = item.title + ' ' + item.body
    log.info(post)

    # Prediction function utilized to make 10 predictions
    # based off post request
    preds = pd.Series(model.decision_function([post])[0])
    preds.index = model.classes_
    preds = preds.sort_values(ascending=False)
    preds = sorted(dict(preds).items(), key=lambda x: x[1], reverse=True)
    preds = [subreddit_list[x] for x,_ in preds[:10]]

    return {
        'title': item.title,
        'body': item.body,
        'prediction': preds        
    }