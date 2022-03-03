# EDA-VECELK Project

Application and API Service for _semantic search_ over large document collections through **Haystack** and vector database **Elasticsearch**.

## Pre-requisite

### Hardware

The application follows hardware requirements of Haystack and Elasticsearch, because due to indexing, documents processing, filtering and searching with **NLP** (Natural Language Processing) **Models**, it needs at least **8-16GB** RAM and a powerful CPU like the one described below in Configuration chapter.

### Software

The application is compatible with Linux, Windows and MacOS. Hovewer, each OS requires his own measures to make the system work properly.

Python is the main core of the application.

### Haystack

Haystack is an open-source framework for building **search systems** that work through words and sentences' semantic similarities over large document collections.
Haystack functionalities are built using _Natural Language Processing_ Models, capable of understanding **natural human language** and perform searches by **semantic similarities**.

Recent advances in NLP have enabled the application of question answering, retrieval and summarization to real world settings and Haystack is designed to **be the bridge** between research and industry.

Haystack's core are made of **nodes**, to process informations, data, queries, answers, and **pipelines**, to envelop nodes in defined processes to obtain an result.

### Elastic Search

Elasticsearch is a **distributed engine** for all types of data, including textual, numerical, geospatial, structured, and unstructured.

Elasticsearch store data in **documents**, who are results of raw data processing from a variety of sources, including logs, system metrics, and web applications. After data processing, **data ingestion** is the process by which this raw data is parsed, normalized, and enriched before it is indexed in Elasticsearch.

Once indexed in Elasticsearch, users can run **complex queries** against their data and use aggregations to retrieve complex summaries of their data.

The combination of Elastic Search, Haystack and NLP Models results in a **complex** and **powerful** **search engine system** over unstructured data crawled from external sources.

Visualization of data over Elastic Search is provided by Kibana, tool who allows users to create powerful visualizations of their data, share dashboards, and manage the Elastic Stack.

TODO scrivere di più
TODO screenshots

TODO screenshots

#### Docker

Docker Engine is an open source **containerization** technology for building and containerizing applications.
In this application context, docker is used to create, start and manage the Elastic Stack instance, composed by Elastic Search, Kibana and the Docker Network who envelop them.

Docker Compose permits to manage several containers docker. In Docker Compose is defined, by the _docker-compose.yml_ file, the services that make up and run the application in an isolated and controlled environment.

TODO screenshots..

## Configuration

Development and Testing of the project are made on an Azure Virtual Machine.

|             | Used Configuration              |
| ----------- | ------------------------------- |
| **MACHINE** | Azure Standard D4s v3           |
| **CPU**     | Intel Xeon E5-2673 v4 (4 vCPUs) |
| **RAM**     | 16GB                            |
| **GPU**     | No                              |
| **STORAGE** | 128GB                           |

### Software Dependencies

Google Chrome needs to be installed on target machine. The _chrome-driver_ contained in is used by **Selenium Library** in Python for the purpose of crawl data from websites.

### Python

Python and pip (_package manager_) needs to be installed on target machine for the execution of the project.

#### Dependecies

Project's dependencies are resolved by pip using the _requirements.txt_ file present in the root path of the project.

|              | Description                                  |
| ------------ | -------------------------------------------- |
| **Uvicorn**  | ASGI Web Server for Python.                  |
| **FastAPI**  | Web Framework for building API in Python.    |
| **Selenium** | Tool for controlling web browsing in Python. |

To install dependencies:

> pip install -r requirements.txt

### Docker

Docker Engine & Docker Compose needs to be installed on target machine.

Docker Compose runs and manage Elastic Search and Kibana Stack

#### Installation

Docker Engine can be installed by follow instruction on Docker Website:
https://docs.docker.com/engine/install/

Docker Compose can be installed by follow instruction on Docker Website:
https://docs.docker.com/compose/install/

### Elastic Search (and Kibana)

Elastic Search and Kibana images are provided by docker repositories and installation doesn't needs any action from user because the services are defined by _docker-compose.yml_ file.

#### Installation

TODO Installazione

screenshot di elastic search e kibana partiti...

### Haystack

#### Installation

Haystack framework, within his crawler component, needs to be installed on target machine via pip.

```
pip install farm-haystack[crawler]
```

**Note:** For Windows you need to install _PyTorch_:

```
pip install farm-haystack[crawler] -f https://download.pytorch.org/whl/torch_stable.html
```

### Application

### Start services

una volta configurato tutto, far partire elastic search con kibana...
far partire l'applicazione... (screenshots)

## Usage

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
