from flask import Flask, request
import requests
from markupsafe import escape

app = Flask(__name__)
