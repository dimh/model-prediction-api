import pandas as pd
import pickle
from sanic import Sanic
from sanic.response import json as json_response


app = Sanic("ModelApiApp")
model = pickle.load(open('/opt/model_app/model.pkl', 'rb'))

async def get_df(data: dict):

    columns_new_df = [
        'job_remote',
        'experience_level_EN',
        'experience_level_EX',
        'experience_level_MI',
        'experience_level_SE',
        'job_category_business',
        'job_category_engineering',
        'job_category_scientist'
    ]
    job_remote = data['job_remote']
    experience_level_EN = 1 if data['experience_level'] == 'EN' else 0
    experience_level_EX = 1 if data['experience_level'] == 'EX' else 0
    experience_level_MI = 1 if data['experience_level'] == 'MI' else 0
    experience_level_SE = 1 if data['experience_level'] == 'SE' else 0

    job_category_business =  1 if data['job_category'] == 'business' else 0
    job_category_engineering =  1 if data['job_category'] == 'engineering' else 0
    job_category_scientist =  1 if data['job_category'] == 'scientist' else 0
    data_new_df = [[
        job_remote,
        experience_level_EN,
        experience_level_EX,
        experience_level_MI,
        experience_level_SE,
        job_category_business,
        job_category_engineering,
        job_category_scientist,
    ]]
    
    new_df = pd.DataFrame(data_new_df, columns=columns_new_df)
    return new_df


@app.post("/predict/")
async def predict(request):
    payload = request.json
    new_payload = await get_df(payload)
    response = model.predict(new_payload)
    response_encoded = {"prediction": response[0]}
    return json_response(response_encoded)


app.run(
    host="0.0.0.0",
    port=80,
    access_log=False,
    debug=True,
    workers=2,
)