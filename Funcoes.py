from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.card import MDCard

from firebase_admin import credentials
import firebase_admin
from firebase_admin import db
from firebase_admin import auth

cred = credentials.Certificate('./projetologin-6eb01-firebase-adminsdk-13kq0-ccd1a2df0b.json')
firebase_admin.initialize_app(cred, {'databaseURL': 'https://projetologin-6eb01-default-rtdb.firebaseio.com/'})

