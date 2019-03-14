# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sample1.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import xlrd


count=0
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(923, 705)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(670, 20, 201, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(380, 20, 113, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(350, 20, 51, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(550, 20, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(490, 96, 139, 451))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_25 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_3.addWidget(self.label_25)
        self.label_24 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_3.addWidget(self.label_24)
        self.label_23 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_3.addWidget(self.label_23)
        self.label_22 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_3.addWidget(self.label_22)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.label_29 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_3.addWidget(self.label_29)
        self.label_30 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.verticalLayout_3.addWidget(self.label_30)
        self.label_28 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_3.addWidget(self.label_28)
        self.label_21 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_3.addWidget(self.label_21)
        self.label_27 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_3.addWidget(self.label_27)
        self.layoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(708, 90, 171, 481))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEdit_26 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.verticalLayout_4.addWidget(self.lineEdit_26)
        self.lineEdit_25 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.verticalLayout_4.addWidget(self.lineEdit_25)
        self.lineEdit_24 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.verticalLayout_4.addWidget(self.lineEdit_24)
        self.lineEdit_23 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.verticalLayout_4.addWidget(self.lineEdit_23)
        self.lineEdit_21 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.verticalLayout_4.addWidget(self.lineEdit_21)
        self.lineEdit_20 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.verticalLayout_4.addWidget(self.lineEdit_20)
        self.lineEdit_19 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.verticalLayout_4.addWidget(self.lineEdit_19)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.verticalLayout_4.addWidget(self.lineEdit_18)
        self.lineEdit_22 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.verticalLayout_4.addWidget(self.lineEdit_22)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 600, 251, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(160, 20, 113, 22))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 100, 111, 441))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.Mass = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Mass.setFont(font)
        self.Mass.setObjectName("Mass")
        self.verticalLayout_5.addWidget(self.Mass)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_5.addWidget(self.label_19)
        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_5.addWidget(self.label_18)
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_5.addWidget(self.label_17)
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_5.addWidget(self.label_16)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(190, 100, 160, 451))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_6.addWidget(self.lineEdit_5)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_6.addWidget(self.lineEdit_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_6.addWidget(self.lineEdit_2)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.verticalLayout_6.addWidget(self.lineEdit_15)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.verticalLayout_6.addWidget(self.lineEdit_16)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.verticalLayout_6.addWidget(self.lineEdit_14)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.verticalLayout_6.addWidget(self.lineEdit_17)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_6.addWidget(self.lineEdit_8)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_6.addWidget(self.lineEdit_3)
        self.lineEdit_6.raise_()
        self.lineEdit_7.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.layoutWidget_2.raise_()
        self.layoutWidget_3.raise_()
        self.pushButton.raise_()
        self.label_18.raise_()
        self.lineEdit_9.raise_()
        self.label.raise_()
        self.verticalLayoutWidget.raise_()
        self.verticalLayoutWidget_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 923, 26))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd_New_Steel = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionAdd_New_Steel.setFont(font)
        self.actionAdd_New_Steel.setObjectName("actionAdd_New_Steel")
        self.actionOpen_Steel = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionOpen_Steel.setFont(font)
        self.actionOpen_Steel.setObjectName("actionOpen_Steel")
        #self.actionUpdate_Steel = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        #self.actionUpdate_Steel.setFont(font)
        #self.actionUpdate_Steel.setObjectName("actionUpdate_Steel")
        self.actionSave_Steel = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        #self.actionSave_Steel.setFont(font)
        #self.actionSave_Steel.setObjectName("actionSave_Steel")
        self.menuOptions.addAction(self.actionAdd_New_Steel)
        self.menuOptions.addAction(self.actionOpen_Steel)
        #self.menuOptions.addAction(self.actionUpdate_Steel)
        #self.menuOptions.addAction(self.actionSave_Steel)
        self.menubar.addAction(self.menuOptions.menuAction())

        self.pushButton.clicked.connect(self.exit)

        
        self.menuOptions.triggered[QtWidgets.QAction].connect(self.menu)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_7.setText(_translate("MainWindow", "ID"))
        self.label_8.setText(_translate("MainWindow", "Chosen Option"))
        self.label_25.setText(_translate("MainWindow", "Zz"))
        self.label_24.setText(_translate("MainWindow", "Zy"))
        self.label_23.setText(_translate("MainWindow", "TW"))
        self.label_22.setText(_translate("MainWindow", "Iz"))
        self.label_9.setText(_translate("MainWindow", "Iy"))
        self.label_29.setText(_translate("MainWindow", "Zpy"))
        self.label_30.setText(_translate("MainWindow", "Zpz"))
        self.label_28.setText(_translate("MainWindow", "Ry"))
        self.label_21.setText(_translate("MainWindow", "Rz"))
        self.label_27.setText(_translate("MainWindow", "Source"))
        self.pushButton.setText(_translate("MainWindow", "Exit Application"))
        self.label.setText(_translate("MainWindow", "Steel Section"))
        self.label_2.setText(_translate("MainWindow", "Designation"))
        self.Mass.setText(_translate("MainWindow", "Mass"))
        self.label_6.setText(_translate("MainWindow", "Area"))
        self.label_3.setText(_translate("MainWindow", "B"))
        self.label_4.setText(_translate("MainWindow", "D"))
        self.label_19.setText(_translate("MainWindow", "R"))
        self.label_18.setText(_translate("MainWindow", "R2"))
        self.label_17.setText(_translate("MainWindow", "FlangeSlope"))
        self.label_16.setText(_translate("MainWindow", "T"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.actionAdd_New_Steel.setText(_translate("MainWindow", "Add New Steel"))
        self.actionOpen_Steel.setText(_translate("MainWindow", "Open Steel"))
        #self.actionUpdate_Steel.setText(_translate("MainWindow", "Update Steel"))
        #self.actionSave_Steel.setText(_translate("MainWindow", "Save Steel"))

    
    def menu(self,action):
        txt=(action.text())

        if txt=='Open Steel':
            self.opensteel()

        if txt=='Add New Steel':
            global count
            count=count+1
            self.addsteel()



    

    def addsteel(self):
        #print("wscw")
      
        book = xlrd.open_workbook('new_sections.xlsx')
        sheet=book.sheet_by_index(0)
        list=[]
        if count<10:
            #print(count)
            for i in range(sheet.ncols):
                list.append(sheet.cell_value(count,i))
        else:
            self.showdlg("No Data entries left to be appended !! ")
            return
        #print(list)
        
        sql="INSERT  INTO Beams (ID,Designation,Mass,Area,D,B,tw,T,FlangeSlope,R1,R2,Iz,Iy,rz,ry,Zz,Zy,Zpz,Zpy,Source) VALUES ('"+str(list[0])+"',\
             '"+str(list[1])+"', '"+str(list[2])+"', '"+str(list[3])+"', '"+str(list[4])+"', '"+str(list[5])+"',\
        '"+str(list[6])+"', '"+str(list[7])+"', '"+str(list[8])+"', '"+str(list[9])+"', '"+str(list[10])+"', '"+str(list[11])+"','"+str(list[12])+"','"+str(list[13])+"',\
          '"+str(list[14])+"','"+str(list[15])+"','"+str(list[16])+"','"+str(list[17])+"','"+str(list[18])+"','"+str(list[19])+"') ;"
        
        try:
            cur=conn.execute(sql)
            self.showdlg("New Data Entry added Succesfully into Steel sections !!")
            conn.commit()
        except:
            self.showdlg("Error in Operation")
            conn.rollback()


    def opensteel(self):
        steels=["Angles","Beams","Channels"]

        steel_chosen, ok=QtWidgets.QInputDialog.getItem(MainWindow,"Steel","Choose a Steel Section",steels,0,False)
        if ok and steel_chosen:
            self.lineEdit_9.setText(steel_chosen)

        if steel_chosen=='Angles':

            sql="select Designation from Angles"
            angles=[]
            cur=conn.execute(sql)
            for row in cur:
                angles.append(row[0])

            angle_option, ok=QtWidgets.QInputDialog.getItem(MainWindow,"Steel","Choose a Designation from Angles Section",angles,0,False)
            if ok and angle_option:
                self.lineEdit_6.setText(angle_option)

            sql="select * from Angles where Designation='"+angle_option+"';"
            cur=conn.execute(sql)
            for row in cur:
                #print((row))
                self.lineEdit_7.setText(str(row[0]))
                self.lineEdit_5.setText(str(row[1]))
                self.lineEdit_4.setText(str(row[2]))
                self.lineEdit_2.setText(str(row[3]))
                self.lineEdit_16.setText(str(row[4]))
                self.lineEdit_14.setText(str(row[5]))
                self.lineEdit_17.setText(str(row[6]))
                self.lineEdit_8.setText(str(row[7]))
                self.lineEdit_3.setText(str(row[8]))
                self.lineEdit_15.setText(str(row[17]))


                self.lineEdit_26.setText(str(row[9]))
                self.lineEdit_25.setText(str(row[16]))
                self.lineEdit_24.setText(str(row[11]))
                self.lineEdit_23.setText(str(row[12]))
                self.lineEdit_21.setText(str(row[13]))
                self.lineEdit_20.setText(str(row[14]))
                self.lineEdit_19.setText(str(row[15]))
                self.lineEdit_18.setText(str(row[11]))
                self.lineEdit_22.setText(str(row[23]))
                
                
    
        elif steel_chosen=='Beams':
            sql="select Designation from Beams"
            beams=[]
            cur=conn.execute(sql)
            for row in cur:
                beams.append(row[0])

            beam_option, ok=QtWidgets.QInputDialog.getItem(MainWindow,"Steel","Choose a Designation from Beams Section",beams,0,False)
            if ok and beam_option: 
                self.lineEdit_6.setText(beam_option)


            sql="select * from Beams where Designation='"+beam_option+"';"
            cur=conn.execute(sql)
            for row in cur:
                #print((row))
                self.lineEdit_7.setText(str(row[0]))
                self.lineEdit_5.setText(str(row[1]))
                self.lineEdit_4.setText(str(row[2]))
                self.lineEdit_2.setText(str(row[3]))
                self.lineEdit_16.setText(str(row[4]))
                self.lineEdit_14.setText(str(row[5]))
                self.lineEdit_17.setText(str(row[6]))
                self.lineEdit_8.setText(str(row[7]))
                self.lineEdit_3.setText(str(row[8]))
                self.lineEdit_15.setText(str(row[17]))


                self.lineEdit_26.setText(str(row[9]))
                self.lineEdit_25.setText(str(row[16]))
                self.lineEdit_24.setText(str(row[11]))
                self.lineEdit_23.setText(str(row[12]))
                self.lineEdit_21.setText(str(row[13]))
                self.lineEdit_20.setText(str(row[14]))
                self.lineEdit_19.setText(str(row[15]))
                self.lineEdit_18.setText(str(row[11]))
                self.lineEdit_22.setText(str(row[19]))




        else:
            sql="select Designation from Channels"
            channels=[]
            cur=conn.execute(sql)
            for row in cur:
                channels.append(row[0])

            channel_option, ok=QtWidgets.QInputDialog.getItem(MainWindow,"Steel","Choose a Designation from Channels Section",channels,0,False)
            if ok and channel_option:
                self.lineEdit_6.setText(channel_option)


            
            sql="select * from Channels where Designation='"+channel_option+"';"
            cur=conn.execute(sql)
            for row in cur:
                #print(len(row))
                self.lineEdit_7.setText(str(row[0]))
                self.lineEdit_5.setText(str(row[1]))
                self.lineEdit_4.setText(str(row[2]))
                self.lineEdit_2.setText(str(row[3]))
                self.lineEdit_16.setText(str(row[4]))
                self.lineEdit_14.setText(str(row[5]))
                self.lineEdit_17.setText(str(row[6]))
                self.lineEdit_8.setText(str(row[7]))
                self.lineEdit_3.setText(str(row[8]))
                self.lineEdit_15.setText(str(row[17]))


                self.lineEdit_26.setText(str(row[9]))
                self.lineEdit_25.setText(str(row[16]))
                self.lineEdit_24.setText(str(row[11]))
                self.lineEdit_23.setText(str(row[12]))
                self.lineEdit_21.setText(str(row[13]))
                self.lineEdit_20.setText(str(row[14]))
                self.lineEdit_19.setText(str(row[15]))
                self.lineEdit_18.setText(str(row[11]))
                self.lineEdit_22.setText(str(row[20]))


    def exit(self):
        import sys
        self.showdlg("Thank YOU for Visiting....Hope you enjoyed !!")
        sys.exit()

    
    def showdlg(self,msg):
        #print("ecb")
        Dialog=QtWidgets.QMessageBox()
        Dialog.setText(msg)
        Dialog.setWindowTitle("Dream Team selector")
        ret=Dialog.exec()



if __name__ == "__main__":

    import sqlite3
    conn = sqlite3.connect('steel_sections.sqlite')
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

