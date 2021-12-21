python3 -m venv .
source ./bin/activate

pip install prometheus_fastapi_instrumentator -i https://nexus3.onap.org/repository/PyPi/simple && pip freeze > requirements.txt

pip install -r requirements.txt -i https://nexus3.onap.org/repository/PyPi/simple 

uvicorn main:app --reload 

--port=5000


docker run -d --name gsheet-backend -p 80:80 gsheet-backend:dev


Promethus
 - https://github.com/kozhushman/prometheusrock
 - https://www.scalyr.com/blog/prometheus-tutorial-detailed-guide-to-getting-started/