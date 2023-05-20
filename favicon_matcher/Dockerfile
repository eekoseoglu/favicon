FROM python:3
ADD requirements.txt /
WORKDIR /
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt
ADD favicons.xml /
ADD main.py /
ADD md5hash.py /
ADD xml_file_parser.py /
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]