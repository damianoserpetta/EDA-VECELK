# EDA-VECELK

Application and API Service for **semantic search** through _Haystack_ and vector database _Elasticsearch_

## Pre-requisite

### Hardware

The application follows hardware requirements of Haystack and Elasticsearch, which because of indexing, documents processing, filtering and searching with **NLP** (Natural Language Processing) **Models**, it needs at least **8-16GB** RAM and a powerful CPU like the one described below in Configuration chapter.

### Software

#### Haystack

library for semantic search on top.....

#### Python

Python 3 and pip (_package manager_) needs to be installed on target machine.

##### Dependecies

Haystack framework needs to be installed on target machine via pip.

```
pip install farm-haystack
```

> **Note:** For Windows you need to install _PyTorch_
>
> ```
> pip install farm-haystack -f https://download.pytorch.org/whl/torch_stable.html
> ```

chrome-driver (scraping), fastapi ..

#### Docker

Docker Engine & Docker Compose needs to be installed on target machine.

Docker Engine can be installed by follow instruction on Docker Website:
https://docs.docker.com/engine/install/

Docker Compose can be installed by follow instruction on Docker Website:
https://docs.docker.com/compose/install/

## Configuration

Development and Testing of the project are made on an Azure Virtual Machine.

|             | Used Configuration              |
| ----------- | ------------------------------- |
| **MACHINE** | Azure Standard D4s v3           |
| **CPU**     | Intel Xeon E5-2673 v4 (4 vCPUs) |
| **RAM**     | 16GB                            |
| **GPU**     | No                              |
| **STORAGE** | 256GB                           |

### Docker

### Elastic-Search (and Kibana)

screenshot di elastic search e kibana partiti...

### Application

## Usage

una volta configurato tutto, far partire elastic search con kibana...
far partire l'applicazione... (screenshots)
visualizzazione di elasticsearch via kibana...
visualizzazione api... (screenshots)
http requests...
http responses...

scrape requests...
query requests...
responses interpretations...
livello di affidabilità delle risposte...
parte del documento della risposta...

risposta più affidabile se ci sono più documenti...
fine tuning...
system working... (screenshots)

## Implementation

scelta di implementare invece che usare la demo...

### Haystack

how it works...
how implemented...
nodes...

### NLP Models

models used in...
models availables...
tuning models...
annotation tool...
answer feedbacks...
tuning using base model and pre-trained model...

### Search Engine

extractive qa pipeline...
caricamento all'inizio della pipeline...
configurazione pipeline...

#### Retriever

#### Reader

### Document Store

communication...
pre processing...
indexing...

### Scraper

configuration...
folder to download on...

### API

API Service is developed by using **FASTApi** framework for Python, which works as controller for the application.

API Service starts at port 5000 in localhost (_configurable_)

json...
authentication implementable...
swagger ui...
tests with postman...
elasticsearch api...
response models...

## Results

## Future Improvements
