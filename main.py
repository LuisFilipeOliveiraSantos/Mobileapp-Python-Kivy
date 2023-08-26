from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.card import MDCard
from kivy.uix.popup import Popup
from kivy.uix.image import Image

from firebase_admin import credentials
import firebase_admin
from firebase_admin import db
from firebase_admin import auth
import requests

cred = credentials.Certificate('./projetologin-6eb01-firebase-adminsdk-13kq0-ccd1a2df0b.json')
firebase_admin.initialize_app(cred, {'databaseURL': 'https://projetologin-6eb01-default-rtdb.firebaseio.com/'})

Window.size = (400, 650)


class TelaDeInicio(Screen):
    pass


class TelaDeRegistro(Screen):
    pass

    def on_pre_enter(self, *args):
        try:
            self.ids.register_email.text = ""
            self.ids.register_password.text = ""
        except:
            pass

    def create_user(self):
        email = self.ids.register_email.text
        password = self.ids.register_password.text

        if not password and not email:
            self.ids.label_error.text = "Email e Senha Invalidos"
            print("Email e senha Invalidos")
            return

        elif not email:
            self.ids.label_error.text = "Digite seu Email para Cadastrar"
            print("Digite seu Email para castrar")
            return

        elif not password:
            self.ids.label_error.text = "Digite sua Senha para Cadastrar"
            print("Digite sua senha para cadastrar")
            return

        else:

            try:
                user = auth.create_user(email=email, password=password)
                self.ids.label_error.text = "Conta criada com sucesso!"
                print("usuario criado com sucesso: {}".format(user.uid))
                self.manager.current = "Login"
            except Exception as e:
                self.ids.label_error.text = "Email já cadastrado"
                print("Email já existe!", e)

        nome = self.ids['register_user'].text
        email = self.ids['register_email'].text
        password = self.ids['register_password'].text

        if nome and email and password:
            ref_usuarios = db.reference('/Usuarios')
            usuarios_ref = ref_usuarios.child('Novo_usuario')

            usuarios_data = usuarios_ref.get()

            if usuarios_data is not None:
                email_existe = any(
                    usuarios['email'] == email for Novo_usuario_key, usuarios in usuarios_data.items())
            else:
                email_existe = False

            if not email_existe:
                novo_usuario = {

                    'nome': nome,
                    'email': email,
                    'password': password
                }

                usuarios_ref.push().set(novo_usuario)


class TelaDeLogin(Screen):
    pass

    def on_pre_enter(self, *args):
        try:
            self.ids.text_email.text = ""
            self.ids.text_password.text = ""
            self.ids.label_erro.text = ""
        except:
            pass

    def login(self):
        email = self.ids.text_email.text
        password = self.ids.text_password.text

        if not email and not password:
            self.ids.label_erro.text = "Insira o seu Email e Senha"
            return
        elif not password:
            self.ids.label_erro.text = "Insira sua Senha para Logar"
            return

        elif not email:
            self.ids.label_erro.text = "Insira seu Email para Logar"
            return

        else:
            try:
                response = requests.post(
                    "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyBSGtEmdeZrtb4dQsPcMi5UucFGUymY3Z4",
                    json={
                        "email": email,
                        "password": password,
                        "returnSecureToken": True
                    }
                )
                data = response.json()
                if "error" in data:
                    self.ids.label_erro.text = "Email ou Senha Inválidos"
                    print("Email ou Senha invalido:", data["error"]["message"])
                else:
                    self.ids.label_erro.text = "Login bem-sucedido"
                    print("Login bem-sucedido:", data)
                    self.manager.current = 'Home'
            except Exception as e:
                print("Error:", e)


class HomePage(Screen):
    pass


# PAGINAS DE CAMPEONATOS DE JIU

class PageJiu(Screen):
    pass


class Camp1Jiu(Screen):
    pass


class Camp2Jiu(Screen):
    pass


# PAGINAS DE CAMPEONATOS BOXING

class PageBoxing(Screen):
    pass


class Camp1Boxing(Screen):
    pass


# TELAS_DE_INSCRIÇÃO

class InscrevaJiu1(Screen):
    pass

    def on_pre_enter(self, *args):
        try:
            self.ids['nome1'].text = ""
            self.ids['cpf1'].text = ""
            self.ids['data1'].text = ""
        except:
            pass

    def campeonato_1(self):

        nome = self.ids['nome1'].text
        cpf = self.ids['cpf1'].text
        data_nascimento = self.ids['data1'].text

        if nome and cpf and data_nascimento:

            ref_campeonato1 = db.reference('/Campeonatos/Jiu-jitsu/Campeonato1')
            participantes_ref = ref_campeonato1.child('participantes')

            participantes_data = participantes_ref.get()

            if participantes_data is not None:
                cpf_existe = any(
                    participante['cpf'] == cpf for participante_key, participante in participantes_data.items())
            else:
                cpf_existe = False

            if not cpf_existe:
                dados_participantes = {
                    'nome': nome,
                    'cpf': cpf,
                    'data_nascimento': data_nascimento
                }

                nova_chave_participante = participantes_ref.push().key

                participantes_ref.child(nova_chave_participante).set(dados_participantes)

                self.ids.ins_error.text = "Inscrição realizada com sucesso!"

            else:
                self.ids.ins_error.text = "CPF já cadastrado"

        else:
            self.ids.ins_error.text = "Preencha todos os campos"


class InscrevaJiu2(Screen):

    def on_pre_enter(self, *args):
        try:
            self.ids['nome2'].text = ""
            self.ids['cpf2'].text = ""
            self.ids['data2'].text = ""
        except:
            pass

    def campeonato_2(self):

        nome = self.ids['nome2'].text
        cpf = self.ids['cpf2'].text
        data_nascimento = self.ids['data2'].text

        if nome and cpf and data_nascimento:

            ref_campeonato2 = db.reference('/Campeonatos/Jiu-jitsu/Campeonato2')
            participantes_ref = ref_campeonato2.child('participantes')

            participantes_data = participantes_ref.get()

            if participantes_data is not None:
                cpf_existe = any(
                    participante['cpf'] == cpf for participante_key, participante in participantes_data.items())
            else:
                cpf_existe = False

            if not cpf_existe:
                dados_participantes = {
                    'nome': nome,
                    'cpf': cpf,
                    'data_nascimento': data_nascimento
                }

                nova_chave_participante = participantes_ref.push().key

                participantes_ref.child(nova_chave_participante).set(dados_participantes)

                self.ids.ins_error.text = "Inscrição realizada com sucesso!"

            else:
                self.ids.ins_error.text = "CPF já cadastrado"

        else:
            self.ids.ins_error.text = "Preencha todos os campos"


class InscrevaBoxing1(Screen):
    pass

    def on_pre_enter(self, *args):
        try:
            self.ids['nome3'].text = ""
            self.ids['cpf3'].text = ""
            self.ids['data3'].text = ""
        except:
            pass

    def campeonato_boxing1(self):

        nome = self.ids['nome3'].text
        cpf = self.ids['cpf3'].text
        data_nascimento = self.ids['data3'].text

        if nome and cpf and data_nascimento:

            ref_campeonato1 = db.reference('/Campeonatos/Boxing/Campeonato1')
            participantes_ref = ref_campeonato1.child('participantes')

            participantes_data = participantes_ref.get()

            if participantes_data is not None:
                cpf_existe = any(
                    participante['cpf'] == cpf for participante_key, participante in participantes_data.items())
            else:
                cpf_existe = False

            if not cpf_existe:
                dados_participantes = {
                    'nome': nome,
                    'cpf': cpf,
                    'data_nascimento': data_nascimento
                }

                nova_chave_participante = participantes_ref.push().key

                participantes_ref.child(nova_chave_participante).set(dados_participantes)

                self.ids.ins_error.text = "Inscrição realizada com sucesso!"

            else:
                self.ids.ins_error.text = "CPF já cadastrado"

        else:
            self.ids.ins_error.text = "Preencha todos os campos"


class Aplicativo(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "DeepOrange"
        self.screen = ScreenManager()
        self.screen.add_widget(TelaDeInicio(name="Inicio"))
        self.screen.add_widget(TelaDeLogin(name="Login"))
        self.screen.add_widget(TelaDeRegistro(name="Registro"))
        self.screen.add_widget(HomePage(name="Home"))
        self.screen.add_widget(PageJiu(name='Jiu'))

        kv = Builder.load_file("Aplicativo.kv")
        return kv

    def go_back(self):
        self.root.current = self.root.previous()

    def volta_homepage(self):
        self.root.current = 'Home'

    def voltar_inicio(self):
        self.root.current = 'Inicio'

    def volta_pagejiu(self):
        self.root.current = 'Jiu'

    def volta_camp2(self):
        self.root.current = 'camp2'

    def volta_pagebox(self):
        self.root.current = 'Boxing'


if __name__ == "__main__":
    Aplicativo().run()
