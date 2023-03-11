# import os
from zipfile import ZipFile
import pickle
import streamlit as st

with ZipFile('model.zip', 'r') as zip:
    model_pkl = zip.read('model.pkl')

model = pickle.loads(model_pkl)
# model_decomp = gzip.decompress(model_zip)

# pickle.dump(model, bz2.BZ2File("compressed_model.pkl",'wb'))

# pickle.dump(model,c_model)

# c_model.close()

# print(os.path.getsize("compressed_model.pkl"))

# model = get_local_pkl_file()

st.title('Sports Prediction')

col_names =  ['movement_reactions', 'mentality_composure', 'passing', 
    'potential', 'dribbling', 'wage_eur', 'power_shot_power', 'value_eur', 'lcm', 'rcm', 'cm', 'release_clause_eur', 
    'mentality_vision', 'attacking_short_passing']

pred_cols = []
for col in col_names:
    pred_cols.append(st.number_input(col))

# prediction code
if st.button('Predict'):
    print(pred_cols)
    prediction = model.predict([pred_cols])

    st.success("the overall potential {}".format(prediction))

