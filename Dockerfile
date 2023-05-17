FROM python:3
ADD requirements.txt /
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
ADD favicons.xml /
ADD main.py /
ADD md5hash.py /
ADD run_sys.sh /
ADD xml_file_parser.py /
CMD [ "./run_sys.sh" ]