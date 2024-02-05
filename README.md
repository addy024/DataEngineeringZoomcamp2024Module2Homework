# DataEngineeringZoomcamp2024Module2Homework

Now, let's build the container

```bash
docker compose build
```

Finally, start the Docker container:

```bash
docker compose up
```

Now, navigate to http://localhost:6789 in your browser! Voila! You're ready to get started with the course. 

### What just happened?

We just initialized a new mage repository. It will be present in your project under the name `magic-zoomcamp`. If you changed the varable `PROJECT_NAME` in the `.env` file, it will be named whatever you set it to.

This repository should have the following structure:

```
.
├── mage_data
│   └── magic-zoomcamp
├── magic-zoomcamp
│   ├── __pycache__
│   ├── charts
│   ├── custom
│   ├── data_exporters
│   ├── data_loaders
│   ├── dbt
│   ├── extensions
│   ├── interactions
│   ├── pipelines
│   ├── scratchpads
│   ├── transformers
│   ├── utils
│   ├── __init__.py
│   ├── io_config.yaml
│   ├── metadata.yaml
│   └── requirements.txt
├── Dockerfile
├── README.md
├── dev.env
├── docker-compose.yml
└── requirements.txt
```

