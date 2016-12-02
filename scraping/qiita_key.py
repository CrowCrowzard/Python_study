#!/usr/bin/env python3
# coding: UTF-8

import os
import os.path
import dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
dotenv.load_dotenv(dotenv_path)

ID = os.environ.get("QIITA_IDENTITY")
PW = os.environ.get("QIITA_PASSWORD")

