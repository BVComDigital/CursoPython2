import os

# Consultar funcionalidades do módulo os

print(os.getcwd()) # pasta atual

print(os.listdir()) # lista arquivos e pastas

os.system('ver') # versão do SO

os.system('systeminfo') # configuração da máquina

os.system('cls') # limpa tela do terminal

os.system('shutdowm /s') # desliga o computador
os.system('shutdowm /a') # cancela desliga o computador


def turn_off_one_hour():
   os.system('shutdown /s /t 3600')

def turn_off_half_one_hour():
   os.system('shutdown /s /t 1800')

def cancel_shutdown():
   os.system('shutdown /a')
