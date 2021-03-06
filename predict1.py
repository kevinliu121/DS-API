import logging
import random
import praw
from fastapi import APIRouter
import pandas as pd
from pydantic import BaseModel, Field, validator

log = logging.getLogger(__name__)
router = APIRouter()


class Item(BaseModel):
    """Use this data model to parse the request body JSON."""
    title: str = Field(..., example= 'I like Dragon Ball Z'
    post: str = Field(..., example= 'dragons are cool')
    

    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""
        return pd.DataFrame([dict(self)])

    # @validator('x1')
    # def x1_must_be_positive(cls, value):
    #     """Validate that x1 is a positive number."""
    #     assert value > 0, f'x1 == {value}, must be > 0'
    #     return value

@router.post('/predict')
async def predict(item: Item):
    """Make random baseline predictions for classification problem."""
    # X_new = item.to_df()
    # log.info(X_new)
    # y_pred = random.choice([True, False])
    # y_pred_proba = random.random() / 2 + 0.5

    example = {'title': "Is Fusion nullified for the Extreme Z Awakening Event?",
        'post': "On JP I missed out on my chance to do SSJ3 Goku the first time so I'm doing it now. Been lucked out of rotations for most of these stages and I've noticed that for my Fusions team, LR Gogeta would NEVER fuse. I'm genuinely curious if the mechanic is nullified for the event or i'm just getting AWFUL RNG.",
        'prediction': ["DBZDokkanBattle", "Subreddit2", "Subreddit3", "Subreddit4", "Subreddit5", "Subreddit6", "Subreddit7", "Subreddit8", "Subreddit9", "Subreddit10"]}
    return example
