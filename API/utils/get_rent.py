import pandas as pd
import numpy as np


def get_rent(features, building_type_encoder, facing_encoder, furnishing_encoder, lease_type_encoder, parking_encoder, type_encoder, water_supply_encoder, loaded_model):
    tmp_df = pd.DataFrame([list(features.values())],
                          columns=list(features.keys()))

    tmp_df['building_type'] = building_type_encoder.transform(
        tmp_df['building_type'])
    tmp_df['facing'] = facing_encoder.transform(tmp_df['facing'])
    tmp_df['furnishing'] = furnishing_encoder.transform(tmp_df['furnishing'])
    tmp_df['lease_type'] = lease_type_encoder.transform(tmp_df['lease_type'])
    tmp_df['parking'] = parking_encoder.transform(tmp_df['parking'])
    tmp_df['type'] = type_encoder.transform(tmp_df['type'])
    tmp_df['water_supply'] = water_supply_encoder.transform(
        tmp_df['water_supply'])

    # return [list(tmp_df.values[0])]

    # temp_dict = {}
    # for col, val in zip(tmp_df.columns, tmp_df.values[0]):
    #     temp_dict[col] = val

    # return temp_dict

    temp = np.array([list(tmp_df.values[0])])
    pred = float(list(loaded_model.predict(np.array(temp)))[0])

    return pred
