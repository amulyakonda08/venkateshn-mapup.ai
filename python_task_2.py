Question 1: Distance Matrix Calculation

import pandas as pd
def calculate_distance_matrix(file_path):
    dataset = pd.read_csv(file_path)
    unique_ids = dataset['ID'].unique()
    distance_matrix = pd.DataFrame(0, index=unique_ids, columns=unique_ids)
    for index, row in dataset.iterrows():
        from_id = row['From_ID']
        to_id = row['To_ID']
        distance = row['Distance']
        distance_matrix.at[from_id, to_id] += distance
        distance_matrix.at[to_id, from_id] += distance  # Accounting for bidirectional distances
    for id in unique_ids:
        distance_matrix.at[id, id] = 0
    return distance_matrix

Question 2: Unroll Distance Matrix

import itertools
import pandas as pd
def unroll_distance_matrix(distance_matrix):
    unrolled_distances = pd.DataFrame(columns=['id_start', 'id_end', 'distance'])
    for id_start, id_end in itertools.permutations(distance_matrix.index, 2):
        distance = distance_matrix.at[id_start, id_end]
        unrolled_distances = unrolled_distances.append({'id_start': id_start, 'id_end': id_end, 'distance': distance},
                                                       ignore_index=True)  
    return unrolled_distances

Question 3: Finding IDs within Percentage Threshold

import pandas as pd
def find_ids_within_ten_percentage_threshold(dataframe, reference_value):
    reference_data = dataframe[dataframe['id_start'] == reference_value]
    average_distance = reference_data['distance'].mean()
    lower_threshold = average_distance * 0.9
    upper_threshold = average_distance * 1.1
    filtered_ids = dataframe[(dataframe['distance'] >= lower_threshold) &
                             (dataframe['distance'] <= upper_threshold)]
    sorted_ids_within_threshold = sorted(filtered_ids['id_start'].unique())
    return sorted_ids_within_threshold

Question 4: Calculate Toll Rate

import pandas as pd
def calculate_toll_rate(data):
    data['moto'] = data['distance'] * 0.8
    data['car'] = data['distance'] * 1.2
    data['rv'] = data['distance'] * 1.5
    data['bus'] = data['distance'] * 2.2
    data['truck'] = data['distance'] * 3.6
    return data

Question 5: Calculate Time-Based Toll Rates

import pandas as pd
def calculate_time_based_toll_rates(data):
    data['entry_time'] = pd.to_datetime(data['entry_time'])
    data['exit_time'] = pd.to_datetime(data['exit_time'])
    data['start_day'] = data['entry_time'].dt.day_name()
    data['end_day'] = data['exit_time'].dt.day_name()
    data['start_time'] = data['entry_time'].dt.time
    data['end_time'] = data['exit_time'].dt.time
    def calculate_rate(row):
        if row['start_day'] in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
            if row['start_time'] <= pd.Timestamp('10:00:00').time():
                return 0.8 * row['distance']
            elif row['start_time'] <= pd.Timestamp('18:00:00').time():
                return 1.2 * row['distance']
            else:
                return 0.8 * row['distance']
        else:
            return 0.7 * row['distance']
    data['moto'] = data.apply(calculate_rate, axis=1)
    data['car'] = data.apply(calculate_rate, axis=1)
    data['rv'] = data.apply(calculate_rate, axis=1)
    data['bus'] = data.apply(calculate_rate, axis=1)
    data['truck'] = data.apply(calculate_rate, axis=1)
    return data