def fit_scaler(values):
    """Return (min, max) of the values -- the learned min-max scaler params."""
    pass

def scale(values, scaler):
    """Return [(v-min)/(max-min) rounded 2dp]; all 0.0 when max==min."""
    pass

def one_hot(value, vocab):
    """Return a one-hot vector for `value` over sorted(vocab); unknown -> all zeros."""
    pass

def build_features(readings, vocab):
    """Return feature rows [scaled_value, *one_hot(pollutant)], value min-max scaled
    with the scaler fitted on these readings."""
    pass
