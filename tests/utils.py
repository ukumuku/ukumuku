
def load_settings(fpath):
    import os, imp
    return imp.load_source('settings', os.path.join(os.path.dirname(__file__), fpath))
