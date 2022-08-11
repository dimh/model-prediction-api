# model-prediction-api

## Build Image

```
    docker-compose build
```


## Run API

```
    docker-compose up
```

## Trying API

```
valid values:
    job_remote: [0, 1]
    experience_level: ["EN", "MI", "SE", "EX"]
    job_category: ["business", "engineering", "scientist" ]

    curl -X POST -H "Content-Type=application/json" -d '{"job_remote": 0, "experience_level": "EX", "job_category": "engineering"}' http://localhost:8000/predict
```