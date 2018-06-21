#!/usr/bin/env python3
"""Simple server for send post requests to zoho cliq message api."""

import datetime
import logging
import requests
import json
import os
import time
from http.server import BaseHTTPRequestHandler, HTTPServer


def cliq_send_message(text, user_name):
    """Send message to cliq api."""
    r = requests.post(
        CLIQ_URL + 'message',
        json={
            "text": text,
            "bot": {
                "name": user_name,
                "image": AVATAR,
            },
        },
        headers={
            'Content-type': 'application/json',
            'Authorization': 'Zoho-authtoken ' + AUTH_TOKEN
        },
    )
    print(r.status_code, r.reason)


def cliq_send_file(file_name, file_path, text):
    """Send message to cliq api as form-data."""
    with open(file_path, 'rb') as f:
        r = requests.post(
            CLIQ_URL + 'files',
            headers={
                'Authorization': 'Zoho-authtoken ' + AUTH_TOKEN
            },
            files={
                'file': (file_name, f.read()),
                'comments': (None, json.dumps([text]))
            },
        )
        print(r.status_code, r.reason)


def prepare_file(text, user_name, user_id, channel_id, timestamp, file_ids):
    """Prepare files full path for sending."""
    print('Get files in request!!!')
    if text:
        cliq_send_message(text, user_name)
    files_list = file_ids.split(',')
    date = datetime.datetime.fromtimestamp(int(timestamp // 1000)).strftime(
        '%Y%m%d')
    msg = 'Uploaded by ' + user_name
    data_path = '/opt/mattermost/data/' + str(date) + '/teams/noteam/channels/'
    data_path += channel_id + '/users/' + user_id + '/'
    for file in files_list:
        file_path = data_path + file + '/'
        if not os.path.exists(file_path):
            msg = "Can't find this file: " + file
            print(msg)
            logging.info(msg)
        else:
            for r, d, f in os.walk(file_path):
                for file_ in f:
                    if ('_preview.' not in file_) and ('_thumb.' not in file_):
                        full_path = os.path.join(r, file_)
                        cliq_send_file(file_, full_path, msg)


def cliq_request_prepare(bbody):
    """Prepare request for sending to cliq api."""
    body = json.loads(str(bbody.decode("utf-8")))
    logging.info('Get JSON')
    token = body.get("token", '')
    # team_id = body.get("team_id", '')
    # team_domain = body.get("team_domain", '')
    channel_id = body.get("channel_id", '')
    # channel_name = body.get("channel_name", '')
    timestamp = body.get("timestamp", '')
    user_id = body.get("user_id", '')
    user_name = body.get("user_name", '')
    # post_id = body.get("post_id", '')
    text = body.get("text", '')
    # trigger_word = body.get("trigger_word", '')
    file_ids = body.get("file_ids", '')
    if token == MM_TOKEN:

        if file_ids:
            prepare_file(
                text,
                user_name,
                user_id,
                channel_id,
                timestamp,
                file_ids
            )
        else:
            cliq_send_message(text, user_name)

    else:
        msg = 'Error: Get incorrect token!'
        print(msg)
        logging.info(msg)


class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        headers = self.headers
        bbody = self.rfile.read(content_length)

        logging.info('Headers: ' + str(headers))
        logging.info('Body: ' + str(bbody.decode("utf-8")))
        logging.info('=======')
        if content_length:
            cliq_request_prepare(bbody)
        self.send_response(200)
        self.end_headers()


if __name__ == '__main__':
    HOST_NAME = 'localhost'
    PORT_NUMBER = 8088
    MM_TOKEN = '73qxuufmofnux81ww5yfe36w1h'
    AUTH_TOKEN = '9123a90b1ac2fa0c1d22ab91ae71a1e7'
    CLIQ_URL = 'https://cliq.zoho.eu/api/v2/channelsbyname/testingmm/'
    # https://cliq.zoho.com/api/v2/channelsbyname/{CHANNEL_UNIQUE_NAME}/files
    AVATAR = "https://www.zoho.com/cliq/help/restapi/images/bot-custom.png"

    logging.basicConfig(
        filename="dummy_server.log",
        filemode="w",
        level=logging.INFO)

    httpd = HTTPServer((HOST_NAME, PORT_NUMBER), MyHandler)
    print(time.asctime(), 'Server Starts - {}:{}'.format(HOST_NAME, PORT_NUMBER))
    logging.info(
        str(time.asctime()) +
        ' Server Starts - {}:{}'.format(HOST_NAME, PORT_NUMBER)
    )
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
    print(time.asctime(), 'Server Stops - {}:{}'.format(HOST_NAME, PORT_NUMBER))
    logging.info(
        str(time.asctime()) +
        ' Server Stops - {}:{}'.format(HOST_NAME, PORT_NUMBER)
    )
