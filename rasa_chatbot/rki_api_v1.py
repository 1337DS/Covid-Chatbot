# -*- coding: utf-8 -*-



# Testing the Robert Koch Institute COVID-19 API

#The documentation for the API can be found [here](https://api.corona-zahlen.org/docs/endpoints/germany.html#germany-2)
# load modules to send and receive HTTP messages
import requests as req
import json
from datetime import datetime as dt

# modules for visualization and storing / modifying data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# thread to run the file server to serve the plots as a URL
import asyncio
import picture_server as server

class Endpoint_Requester():
  def __init__(self, endpoint, file_server: bool):
    self.base_url = "https://api.corona-zahlen.org"
    self.endpoint = endpoint # this must be definied by when the class is instanciated
    self.plot_server = "http://localhost:4321"
    self.use_plot_server = file_server
    print("Remember to start the picture_server.py seperately")

    

  def get_json(self, url_param=None, payload=None):
    """
    Send a HTTP GET request to the API Endpoint that is provided 
    when an object is instanciated and processes the JSON response.
    If there is an error or the HTTP status code is not OK (200) 
    the return value is None.

    Parameters:
    ---
    :url_param (str): 
    is appended to the end of the URL. It can be used to specify 
    things like amount of days or pages. 
    E.g. "URL/germany/history/cases/:days" 

    :payload (dict):
    Dict that is treated as a URL encoded JSON string.
    E.g. {"key1": "val1", "key2": "val2"} 
    will be encoded as
    URL/?key1=val1&key2=val2
    """
    # use either an empty string or use a slash followed by the parameters
    param_str = "" if url_param is None else f"/{url_param}"
    
    # send the request and convert it to json
    res = req.get(
        f"{self.base_url}{self.endpoint}{param_str}",
        params=payload
        )
    
    status = res.status_code
    if status == 200: # if the request status code is successfull
      try:
        return res.json()
      except:
        print("Could not convert the request to JSON.")
        return None 
    else:
      print(f"The request wasn't successfull. The HTTP response status code was {status}")
      return None

  def to_df(self, data, time_att="date"):
    """
    Returns a pd.DataFrame based on the data input.

    Parameters:
    ---
    :data (list): 
    Is expected to be a list of dicts.
    
    :time_att (str | None): 
    Column name that is converted to datetime and 
    used as index of the dataframe.
    If it is None no index is set.
    
    returns:
    ---
    pd.DataFrame
    """
    df = pd.DataFrame(data)

    if time_att is not None:
      # this conversion could lead to an error if the request doesn't
      # have the literals ".000z" in the end
      df[time_att] = df[time_att].apply(lambda date: dt.strptime(date, "%Y-%m-%dT%H:%M:%S.000z"))
      df = df.set_index(time_att)

    return df

"""## 2. Germany Endpoint"""

class Endpoint_Germany(Endpoint_Requester):
  def __init__(self, file_server: bool):
    """
    Parameters:
    : file_server (bool) : If true the file server is started when an instance of this class is created.
    """
    super().__init__("/germany", file_server)
    self.valid_history_endpoints = [
      "incidence", 
      "deaths",
      "recovered",
      "frozen-incidence",
      "hospitalization"
    ]

    self.valid_hospitalization_endpoints = [
      "incidence7Days",
      "cases7Days"
    ]

    self.valid_demographic_endpoints = [
      "cases",
      "casesPer100k"
      "deaths",
      "deathsPer100k"
    ]

  def valid_list_items(self, l1, l2):
    """
    Checks if all items from l1 are also inside l2.
    """
    s1 = set(l1)
    s2 = set(l2)

    # check if the list items are unique
    if not (len(l1) == len(s1) and len(l2) == len(s2)):
      print(f"The items in either list is not unique l1 = {l1} l2 = {l2}")
      return False

    # check if the intersection between the lists is identical to the length of the whole list
    if len(l1.intersection(l2)) == len(l1):
      return True
    
    # if the check didn't give a result, then the items are not valid
    return False

  def get_history(self, metric, hospitalization=None, days=None, as_df=True):
    """
    Returns the historic data of a Covid-19 metric in germany.
    An example what metric means in this context can be found below.
    
    Parameters:
    ---
    :metric (str):
    The name of a /germany/history/<metric> endpoint.
    Possible metric values are listed in the variable
    self.valid_history_endpoints

    :hospitalization (str):
    This parameter is the name of the hospitalization sub-metric.
    Only use this if you use "hospitalization" for the 'metric' parameter.
    If you don't provide a value, while using metric='hospitalization' 
    you will get all sub-metrics.
    Possible values are listed in the variable
    self.valid_hospitalization_endpoints:
    - "incidence7Days",
    - "cases7Days"


    :days (int): 
    number of days that are requested from now into the past. 
    Without providing a value all dates are requested.
    
    :as_df (bool): 
    This function returns a pd.DataFrame if True. 
    Otherwise it returns a dict.

    Returns:
    ---
    (data, last_updated) or (None, None)
    
    :data (pd.DataFrame|dict): The received data value depends on parameter "as_df"
    :last_updated (datetime): Date of the last update of that data
    :None: in case of an error
    """
    # The returned json is structured like so:
    # data: [{"cases": (integer), "date": (datetime)}, ...],
    # meta: {"lastUpdate": (datetime)}
    if not metric in self.valid_history_endpoints:
      print(f"You must provide a valid endpoint. \
      Available endpoints are: {self.valid_history_endpoints}")
      return None, None

    if isinstance(days, int):
      days_param = f"/{days}"
    else:
      days_param = ""

    # send json to get covid cases and use days if it was an integer
    json = self.get_json(url_param=f"history/{metric}{days_param}")

    try:
      last_updated = json["meta"]["lastUpdate"]
    except:
      print("Corrupted JSON couldn't read last update date")
      return None, None

    # if no hospitalization sub-metric is needed, just use the json.data list
    if hospitalization is None:
      json_data = json["data"]
    # extract the correct sub-metric from "hospitalization" metric
    elif hospitalization in self.valid_hospitalization_endpoints:
      # only extract the value of 'hospitalization' and the date
      # the variable json is a list of dicts.
      # each dict hast a date and the sub-metrics listed in self.valid_hospitalization_endpoints
      json_data = [
        {"date": j["date"], hospitalization: j[hospitalization]} 
        for j in json["data"]
        ]
    else:
      print(f"You didn't specify a valid option for the parameter 'hospitalization'. \
      Valid options are: {self.valid_hospitalization_endpoints}")
      return None, None

    if as_df:
      return self.to_df(json_data), last_updated
    else:
      return json_data, last_updated
    
  def add_sex_to_metric(self, metric):
    """
    Returns the correct metric label for the get_demographic() method.
    """
    # add Female and Male to the metric names
    if  metric == "deathsPer100k":
      return ["deathsMalePer100k", "deathsFemalePer100k"]
    elif metric == "casesPer100k":
      return ["casesMalePer100k", "casesFemalePer100k"]
    else:
      return [metric + "Male", metric + "Female"]

  def save_plot(self, df, name):
    """
    Saves the plot of the dataframe as 'name' and returns a URL to access the plot.

    Params:
    ---
    : df (pd.DataFrame) : The dataframe that should be plotted.
    : name (str) : The name of the plot, when it is saved to a file.
    """
      out = f"{self.plot_server}/plot/{name}.png"
      ax = df.plot()
      fig = ax.get_figure()
      fig.savefig(name)
      # assuming that the picture_server.py is already running this URL will provide the plot that was just generated
      return out

  def get_demographic(self, metric, split_sex=True, as_df=True):
    """
    Returns the current data of one or multiple Covid-19 metrics 
    in germany grouped by age groups and gender.
    An example what metric means in this context can be found below.
    It uses the endpoint URL/germany/age-groups.
    
    Parameters:
    ---
    :metric (str | list):
    The name or list of names of the metrics.
    Possible metric values are listed in the variable
    self.valid_demographic_endpoints.
    
    :split_sex (bool):
    If True will group each metric in two different columns for male and female.
    If False male and female are combined into one value.

    :as_df (bool): 
    This function returns a pd.DataFrame if True. 
    Otherwise it returns a dict.

    Returns:
    ---
    (data, last_updated) or (None, None)
    
    :data (pd.DataFrame|dict): The received data value depends on parameter "as_df"
    :last_updated (datetime): Date of the last update of that data
    :None: in case of an error
    """
    # send json to get demographics data, no further URL parameters needed
    json = self.get_json(url_param="age-groups")
    df = self.to_df(json["data"], time_att=None)

    try:
      last_updated = json["meta"]["lastUpdate"]
    except:
      print("Corrupted JSON couldn't read last update date")
      return None, None
    
    if isinstance(metric, str) and metric in self.valid_demographic_endpoints:
      metrics = self.add_sex_to_metric(metric)
      df = df.loc[metrics]

    # check if all items from metric list are also in self.valid_demographic_endpoints
    elif isinstance(metric, list) and self.valid_list_items(metric, self.valid_demographic_endpoints):
      metrics = []
      for m in metric:
        # add the items from the metrics with sex to the total list of metrics
        metrics.extend(self.add_sex_to_metric(m))
      df = df.loc[metrics]

    # if metric is invalid 
    else:
      return None, None
    
    # if the plot server is running save the picture and serve it with that server
    if self.use_plot_server:
      # name of the plot will be the name of the metrics devided with a underscore
      name = f'{"_".join(metrics)}'
      # save to figure to ./plot and return the url to access the plot
      url = self.save_plot(df, name)
      return url

    return df, last_updated

# Examples to get cases and test the picture server
##### comment this out if you want to use it in production #####
ger = Endpoint_Germany(file_server=True)
print(ger.get_demographic("cases",split_sex=False))
#df, updated = ger.get_history("deaths", as_df=True)
# Examples to get yesterdays incidence
#df2, updated = ger.get_history("incidence")
#ger = Endpoint_Germany()
