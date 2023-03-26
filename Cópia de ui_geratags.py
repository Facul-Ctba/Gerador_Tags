# -*- coding: utf-8 -*-

###############################################################################
# Form generated from reading UI file 'geratags.ui'
#
# Created by: Qt User Interface Compiler version 6.4.2
#
# WARNING! All changes made in this file will be lost when recompiling UI file!
###############################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QFrame,
                               QHBoxLayout, QLabel, QLineEdit, QListWidget,
                               QMenu, QMenuBar, QStatusBar, QTableWidget,
                               QTableWidgetItem, QVBoxLayout, QWidget)
import rc_logo


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(994, 653)
        MainWindow.setStyleSheet(u"font: 12pt \"Arial\";\n"
                                 "QLineEdit:{\n"
                                 "	color: rgb(255, 255, 0);\n"
                                 "}")
        self.Save = QAction(MainWindow)
        self.Save.setObjectName(u"Save")
        icon = QIcon()
        iconThemeName = u"document-save"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.Save.setIcon(icon)
        self.Exit = QAction(MainWindow)
        self.Exit.setObjectName(u"Exit")
        icon1 = QIcon()
        iconThemeName = u"application-exit"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.Exit.setIcon(icon1)
        self.Limpar = QAction(MainWindow)
        self.Limpar.setObjectName(u"Limpar")
        icon2 = QIcon()
        iconThemeName = u"edit-clear"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.Limpar.setIcon(icon2)
        self.Excluir = QAction(MainWindow)
        self.Excluir.setObjectName(u"Excluir")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.fr_esquerda = QFrame(self.centralwidget)
        self.fr_esquerda.setObjectName(u"fr_esquerda")
        self.fr_esquerda.setStyleSheet(u"QLineEdit:{\n"
                                       "	color: rgb(255, 255, 0);\n"
                                       "}")
        self.fr_esquerda.setFrameShape(QFrame.StyledPanel)
        self.fr_esquerda.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.fr_esquerda)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.fr_esquerda)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 5))

        self.verticalLayout.addWidget(self.label)

        self.fr_cabecalho = QFrame(self.fr_esquerda)
        self.fr_cabecalho.setObjectName(u"fr_cabecalho")
        self.fr_cabecalho.setMinimumSize(QSize(0, 131))
        self.fr_cabecalho.setMaximumSize(QSize(16777215, 131))
        self.fr_cabecalho.setFrameShape(QFrame.StyledPanel)
        self.fr_cabecalho.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.fr_cabecalho)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lb_logo = QLabel(self.fr_cabecalho)
        self.lb_logo.setObjectName(u"lb_logo")
        self.lb_logo.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_3.addWidget(self.lb_logo)

        self.lb_titulo = QLabel(self.fr_cabecalho)
        self.lb_titulo.setObjectName(u"lb_titulo")

        self.horizontalLayout_3.addWidget(self.lb_titulo)

        self.verticalLayout.addWidget(self.fr_cabecalho)

        self.lb_nomarq = QLabel(self.fr_esquerda)
        self.lb_nomarq.setObjectName(u"lb_nomarq")
        self.lb_nomarq.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.lb_nomarq)

        self.le_arquivo = QLineEdit(self.fr_esquerda)
        self.le_arquivo.setObjectName(u"le_arquivo")
        self.le_arquivo.setMinimumSize(QSize(0, 30))
        self.le_arquivo.setStyleSheet(u"color: rgb(255, 255, 0);")

        self.verticalLayout.addWidget(self.le_arquivo)

        self.lb_tag = QLabel(self.fr_esquerda)
        self.lb_tag.setObjectName(u"lb_tag")
        self.lb_tag.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.lb_tag)

        self.le_tag = QLineEdit(self.fr_esquerda)
        self.le_tag.setObjectName(u"le_tag")
        self.le_tag.setMinimumSize(QSize(0, 30))
        self.le_tag.setStyleSheet(u"color: rgb(255, 255, 0);")
        self.le_tag.setInputMethodHints(Qt.ImhPreferUppercase)
        self.le_tag.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.le_tag)

        self.lb_quant = QLabel(self.fr_esquerda)
        self.lb_quant.setObjectName(u"lb_quant")
        self.lb_quant.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.lb_quant)

        self.le_quant = QLineEdit(self.fr_esquerda)
        self.le_quant.setObjectName(u"le_quant")
        self.le_quant.setMinimumSize(QSize(0, 30))
        self.le_quant.setStyleSheet(u"color: rgb(255, 255, 0);")
        self.le_quant.setInputMethodHints(Qt.ImhDigitsOnly)
        self.le_quant.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.le_quant)

        self.lb_recentes = QLabel(self.fr_esquerda)
        self.lb_recentes.setObjectName(u"lb_recentes")
        self.lb_recentes.setMinimumSize(QSize(0, 30))
        self.lb_recentes.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout.addWidget(self.lb_recentes)

        self.lw_arquivos = QListWidget(self.fr_esquerda)
        self.lw_arquivos.setObjectName(u"lw_arquivos")

        self.verticalLayout.addWidget(self.lw_arquivos)

        self.horizontalLayout_2.addWidget(self.fr_esquerda)

        self.fr_direita = QFrame(self.centralwidget)
        self.fr_direita.setObjectName(u"fr_direita")
        self.fr_direita.setFrameShape(QFrame.StyledPanel)
        self.fr_direita.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.fr_direita)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.tw_tabela = QTableWidget(self.fr_direita)
        if (self.tw_tabela.columnCount() < 1):
            self.tw_tabela.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tw_tabela.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.tw_tabela.setObjectName(u"tw_tabela")
        self.tw_tabela.setFrameShape(QFrame.WinPanel)
        self.tw_tabela.setSizeAdjustPolicy(
            QAbstractScrollArea.AdjustToContents)
        self.tw_tabela.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tw_tabela.verticalHeader().setVisible(False)

        self.horizontalLayout.addWidget(self.tw_tabela)

        self.horizontalLayout_2.addWidget(self.fr_direita)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 994, 24))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)
# if QT_CONFIG(shortcut)
        self.lb_nomarq.setBuddy(self.le_arquivo)
        self.lb_tag.setBuddy(self.le_tag)
        self.lb_quant.setBuddy(self.le_quant)
# endif // QT_CONFIG(shortcut)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.Save)
        self.menuFile.addAction(self.Limpar)
        self.menuFile.addAction(self.Excluir)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.Exit)

        self.retranslateUi(MainWindow)
        self.le_arquivo.textChanged.connect(MainWindow.Open_File)
        self.le_quant.editingFinished.connect(MainWindow.Add_Item)
        self.lw_arquivos.itemClicked.connect(MainWindow.esc_arq)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.Save.setText(QCoreApplication.translate(
            "MainWindow", u"&Salvar", None))
# if QT_CONFIG(shortcut)
        self.Save.setShortcut(QCoreApplication.translate(
            "MainWindow", u"Ctrl+S", None))
# endif // QT_CONFIG(shortcut)
        self.Exit.setText(QCoreApplication.translate(
            "MainWindow", u"Sai&r", None))
# if QT_CONFIG(shortcut)
        self.Exit.setShortcut(QCoreApplication.translate(
            "MainWindow", u"Ctrl+X", None))
# endif // QT_CONFIG(shortcut)
        self.Limpar.setText(QCoreApplication.translate(
            "MainWindow", u"&Limpar Excel", None))
# if QT_CONFIG(shortcut)
        self.Limpar.setShortcut(QCoreApplication.translate(
            "MainWindow", u"Ctrl+L", None))
# endif // QT_CONFIG(shortcut)
        self.Excluir.setText(QCoreApplication.translate(
            "MainWindow", u"&Excluir Excel", None))
# if QT_CONFIG(shortcut)
        self.Excluir.setShortcut(
            QCoreApplication.translate("MainWindow", u"Ctrl+E", None))
# endif // QT_CONFIG(shortcut)
        self.label.setText("")
        self.lb_logo.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/Gerador_Tags/Avitech_m.jpg\"/></p></body></html>", None))
        self.lb_titulo.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:700; vertical-align:super;\">Programa Gerador de Tags</span></p></body></html>", None))
        self.lb_nomarq.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">&amp;Nome do Arquivo ( sem extens\u00e3o )</span></p></body></html>", None))
        self.le_arquivo.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Digite o nome do < Arquivo >", None))
        self.lb_tag.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">&amp;TAG</span></p></body></html>", None))
        self.le_tag.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Digite a Tag", None))
        self.lb_quant.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">&amp;Quantidade</span></p></body></html>", None))
        self.le_quant.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Digite a Quantidade", None))
        self.lb_recentes.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Arquivos Recentes</span></p></body></html>", None))
        ___qtablewidgetitem = self.tw_tabela.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("MainWindow", u"TAG", None))
        self.menuFile.setTitle(QCoreApplication.translate(
            "MainWindow", u"Arquivo", None))
    # retranslateUi
