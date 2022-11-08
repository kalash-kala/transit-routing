"""
Enter the solution for Q3 here.
Note: You may use may define any additional class, functions if necessary.
However, DO NOT CHANGE THE TEMPLATE CHANGE THE TEMPLATE OF THE FUNCTIONS PROVIDED.
"""

import pandas as pd

stops = pd.read_csv("/Users/kalashkala/Desktop/GitFolder/transit-routing/python_exam/anaheim_gtfs/stops.txt")
trips = pd.read_csv("/Users/kalashkala/Desktop/GitFolder/transit-routing/python_exam/anaheim_gtfs/trips.txt")
routes = pd.read_csv('/Users/kalashkala/Desktop/GitFolder/transit-routing/python_exam/anaheim_gtfs/routes.txt')
stop_time = pd.read_csv("/Users/kalashkala/Desktop/GitFolder/transit-routing/python_exam/anaheim_gtfs/stop_times.txt")


trip_stop_time_df = {}
for idx, df in stop_time.groupby('trip_id'):
    trip_stop_time_df[idx] = df['stop_id'].to_list()


route = {}
for idx, df in trips.groupby(by='route_id'):
    route[idx] = set()
    for trip_id in df['trip_id']:
        for val in trip_stop_time_df[trip_id]:
            route[idx].add(val)



def number_of_routes(source_stopid: str, destination_stopid: str) -> int:
    """
    Find the number of routes going from source stop id to destination stop id.

    Args:
        source_stopid (str): Source Stop Id
        destination_stopid (str): Destination Stop Id

    Returns:
        final_count (int): Number of routes going from source to destination.
    """
    final_count = -1
    
    try:
        stops = pd.read_csv("/Users/kalashkala/Desktop/GitFolder/transit-routing/python_exam/anaheim_gtfs/stops.txt")
        trips = pd.read_csv("/Users/kalashkala/Desktop/GitFolder/transit-routing/python_exam/anaheim_gtfs/trips.txt")
        routes = pd.read_csv('/Users/kalashkala/Desktop/GitFolder/transit-routing/python_exam/anaheim_gtfs/routes.txt')
        stop_time = pd.read_csv("/Users/kalashkala/Desktop/GitFolder/transit-routing/python_exam/anaheim_gtfs/stop_times.txt")


        trip_stop_time_df = {}
        for idx, df in stop_time.groupby('trip_id'):
            trip_stop_time_df[idx] = df['stop_id'].to_list()


        route = {}
        for idx, df in trips.groupby(by='route_id'):
            route[idx] = set()
            for trip_id in df['trip_id']:
                for val in trip_stop_time_df[trip_id]:
                    route[idx].add(val)
        
        answer = 0
        for r in routes['route_id']:
            if((source_stopid in route[r]) and (destination_stopid in route[r])):
                answer+=1
        
        final_count = answer
        
        return final_count
    except:
        return final_count
