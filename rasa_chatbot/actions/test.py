import requests as req
import json
from datetime import datetime as dt

# modules for visualization and storing / modifying data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from rkiapi import RKI_API

ger = RKI_API.Endpoint_Germany()
df2, updated = ger.get_history("incidence")
result=df2['weekIncidence'][-1]
print(r"the incidence in germany is",result)