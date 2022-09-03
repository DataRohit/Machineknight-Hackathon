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

    # temp_dict = {}
    # for key, val in zip(tmp_df.columns, tmp_df.values[0]):
    #     temp_dict[key] = val

    temp = np.array([list(tmp_df.values[0])])
    pred = float(round(list(loaded_model.predict(np.array(temp)))[0], 4))

    return pred

    # return float(pred[0])
