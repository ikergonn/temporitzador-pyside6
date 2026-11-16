"""Conexiones de los botones de la ventana."""


def boton_1_pulsado():
    print("Boton 1 pulsado")


def boton_2_pulsado():
    print("Boton 2 pulsado")


def boton_3_pulsado():
    print("Boton 3 pulsado")


def connect_button_prints(ui):
    """Conecta cada boton con la funcion que se ejecuta al pulsarlo."""
    ui.pushButton.clicked.connect(boton_1_pulsado)
    ui.pushButton_2.clicked.connect(boton_2_pulsado)
    ui.pushButton_3.clicked.connect(boton_3_pulsado)
