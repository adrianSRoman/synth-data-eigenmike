# Room Impulse Reponse (RIR) - Verbose

## Data information (TAU SRIR dataset)

- Room indexes: a total of 10 rooms

```
room_idx = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
```

- Measurement information: 10 rooms 

```
room_name = 'bomb_shelter', 'gym', 'pb132', 'pc226', 'sa203', 'sc203', 'se203', 'tb103', 'tc352'
```

```
meas_info_dict:
{
    <room_name>: 
    {
        "trajectories": list,
        "trajectoryType": str,
        "distances": np.array,
        "heights": np.array,
        "micPosition": np.array
    }
}
```

Example:
```
measinfo = 
{
    'bomb_shelter': 
    {   
        'trajectories': ['close', 'far'], 
        'trajectoryType': 'circular', 
        'distances': array([[2.5, 5. ]]), 
        'heights': array([[0.4, 0.6, 0.8, 1. , 1.2, 1.4, 1.6, 1.8, 2. ]]), 
        'micPosition': array([[0. , 0. , 1.2]])},
    ...
    }
```

- Room impulse reponse data structure (`dict`):

```
rirdata_dict = {
    'doa_xyz':
    'dist':
}
```