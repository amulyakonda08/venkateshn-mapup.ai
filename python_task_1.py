Question 1: Car Matrix Generation
import pandas as pd
def generate_car_matrix():
    df = pd.read_csv('dataset-1.csv')
    pivot_df = df.pivot(index='id_1', columns='id_2', values='car').fillna(0)
    for i in range(min(pivot_df.shape)):
        pivot_df.iloc[i, i] = 0
    return pivot_df

Question 2: Car Type Count Calculation
  
import pandas as pd
def get_type_count(dataframe):
    dataframe['car_type'] = pd.cut(dataframe['car'], bins=[float('-inf'), 15, 25, float('inf')],
                                   labels=['low', 'medium', 'high'], right=False)
    type_counts = dataframe['car_type'].value_counts().to_dict()
    sorted_type_counts = {key: type_counts[key] for key in sorted(type_counts)}
    return sorted_type_counts

Question 3: Bus Count Index Retrieval

import pandas as pd
def get_bus_indexes(dataframe):
    mean_bus = dataframe['bus'].mean()
    bus_indexes = dataframe[dataframe['bus'] > 2 * mean_bus].index.tolist()
    bus_indexes.sort()
    return bus_indexes

Question 4:  Route Filtering

import pandas as pd
def filter_routes(data):
    if not isinstance(data, pd.DataFrame):
        data = pd.read_csv(data)
    data['truck'] = pd.to_numeric(data['truck'], errors='coerce')
    filtered_routes = data.groupby('route')['truck'].mean().loc[lambda x: x > 7].index.tolist()

Question 5: Matrix Value Modification

def multiply_matrix(dataframe):
    modified_df = dataframe.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25)
    modified_df = modified_df.round(1)
    return modified_df

Question 6: Time Check

import pandas as pd
def verify_timestamps(data):
    if not isinstance(data, pd.DataFrame):
        data = pd.read_csv(data)
    data['start_time'] = pd.to_datetime(data['startDay'] + ' ' + data['startTime'])
    data['end_time'] = pd.to_datetime(data['endDay'] + ' ' + data['endTime'])
    data['duration'] = data['end_time'] - data['start_time']
    full_day_duration = pd.to_timedelta('1 day')
    full_week_duration = pd.to_timedelta('7 days')
    grouped = data.groupby(['id', 'id_2']).agg(
        has_incorrect_timestamps=pd.NamedAgg(
            column='duration',
            aggfunc=lambda x: not (
                x.min() <= full_day_duration and x.max() >= full_day_duration and
                x.nunique() >= 7 and x.max() - x.min() >= full_week_duration
            )
        )
    )
    
    return grouped['has_incorrect_timestamps']