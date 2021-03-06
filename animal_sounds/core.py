# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/00_core.ipynb (unless otherwise specified).

__all__ = ['scale_minmax', 'save_encoder', 'load_encoder']

# Cell
from fastai2.vision.all import *

# Cell
def scale_minmax(X, min=0.0, max=1.0):
    X_std = (X - X.min()) / (X.max() - X.min())
    X_scaled = X_std * (max - min) + min
    return X_scaled

# Cell
@patch
@delegates(Learner.save)
def save_encoder(self:Learner, file, with_opt=False, **kwargs):
  model, self.model = self.model, self.model[0]
  self.save(file, with_opt=with_opt, **kwargs)
  self.model = model

# Cell
@patch
@delegates(Learner.load)
def load_encoder(self:Learner, file, **kwargs):
    model, self.model = self.model, self.model[0]
    self.load(file, **kwargs)
    self.model = model