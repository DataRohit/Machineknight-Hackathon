def get_obj_features(df):
    obj_cols = {
        "message": "Each feature has a list of unique values / categories",
    }

    features = {}
    for col in df.select_dtypes("object").columns:
        features[col] = df[col].unique().tolist()

    obj_cols["features"] = features

    return obj_cols

def get_num_features(df):
    num_cols = {"message": [
        "Each feature has a list of min and max values (range) of values on which model was trained",
        "In case of only two values (0 and 1), 0 means False and 1 means True"
        ]}
    
    features = {}
    for col in df.select_dtypes("number").columns:
        features[col] = [float(df[col].min()), float(df[col].max())]

    num_cols["features"] = features
    return num_cols