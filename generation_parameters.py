# Parameters used in the data generation process.


def get_params(argv='1'):
    print("SET: {}".format(argv))
    # ########### default parameters (NIGENS data) ##############
    params = dict(
        db_name = 'nigens',  # name of the audio dataset used for data generation
        rirpath = '/scratch/data/TAU-SRIR/TAU-SRIR_DB',   # path containing Room Impulse Responses (RIRs)
        mixturepath = '/scratch/data/TAU_Spatial_RIR_Database_2021/Dataset-NIGENS',  # output path for the generated dataset
        noisepath = '/scratch/data/TAU-SRIR/TAU-SNoise_DB',  # path containing background noise recordings
        nb_folds = 2,  # number of folds (default 2 - training and testing)
        rooms2fold = [[10, 6, 1, 4, 3, 8], # FOLD 1, rooms assigned to each fold (0's are ignored)
                      [9, 5, 2, 0, 0, 0]], # FOLD 2
        db_path = '/scratch/data/TAU_Spatial_RIR_Database_2021/Dataset-NIGENS/NIGENS',  # path containing audio events to be utilized during data generation
        max_polyphony = 3,  # maximum number of overlapping sound events
        active_classes = [0, 1, 2, 3, 5, 6, 8, 9, 10, 11, 12],  # list of sound classes to be used for data generation
        nb_mixtures_per_fold = [900, 300], # if scalar, same number of mixtures for each fold
        mixture_duration = 60., #in seconds
        event_time_per_layer = 40., #in seconds (should be less than mixture_duration)
        audio_format = 'both', # 'foa' (First Order Ambisonics) or 'mic' (four microphones) or 'both'
            )
        

    # ########### User defined parameters ##############
    if argv == '1':
        print("USING DEFAULT PARAMETERS FOR NIGENS DATA\n")

    elif argv == '2': ###### FSD50k DATA
        params['db_name'] = 'fsd50k'
        params['rirpath'] = '/scratch/data/TAU-SRIR/TAU-SRIR_DB'
        params['mixturepath'] = '/scratch/data/FSD50K-DCASE-SYNTH'
        params['noisepath'] = '/scratch/data/TAU-SRIR/TAU-SNoise_DB'
        params['db_path'] = '/scratch/data/FSD50K/FSD50K_DCASE'
        params['active_classes'] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        params['max_polyphony'] = 2
        params['obj_path'] = 'dcase22_updated_obj_dist.pkl'

    elif argv == '3': ###### NIGENS interference data
        params['active_classes'] = [4, 7, 14] 
        params['max_polyphony'] = 1
        
    else:
        print('ERROR: unknown argument {}'.format(argv))
        exit()

    for key, value in params.items():
        print("\t{}: {}".format(key, value))
    return params