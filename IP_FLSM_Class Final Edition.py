from PyQt4 import QtGui
import ipaddress


class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.container = QtGui.QWidget()
        self.resize(1000,500)
        self.setWindowTitle("Subnetting Calculator")
        self.setWindowIcon(QtGui.QIcon("ip.png"))

        self.label1 = QtGui.QLabel(self)
        self.label1.setText("Enter network address")
        self.label1.move(20,100)
        self.label1.resize(150,30)
        self.label2 = QtGui.QLabel(self)
        self.label2.setText("Enter networks number")
        self.label2.resize(150,30)
        self.label2.move(20,150)
        self.input1 = QtGui.QLineEdit(self)
        self.input1.setPlaceholderText("Enter Network Address [NID/P]")
        self.input1.resize(200,30)
        self.input1.move(150,100)
        self.input2 = QtGui.QLineEdit(self)
        self.input2.setPlaceholderText("Enter Number of Networks")
        self.input2.resize(200,30)
        self.input2.move(150,150)
        self.netmasklabel = QtGui.QLabel(self)
        self.netmasklabel.resize(200,30)
        self.netmasklabel.move(150,173)

        close_button = QtGui.QPushButton("Close",self)
        close_button.resize(100,50)
        close_button.move(300,350)

        submit_button = QtGui.QPushButton("Submit",self)
        submit_button.resize(50,30)
        submit_button.move(150,200)

        self.result = QtGui.QListWidget(self)
        self.result.resize(200,450)
        self.result.move(500,25)

        self.summaryLabel = QtGui.QLabel(self)
        self.summaryLabel.resize(120,32)
        self.summaryLabel.move(150,300)
        self.summaryLabel.setText("Summary Route")

        summary_network = QtGui.QPushButton("Summary Network" ,self)
        summary_network.resize(100,30)
        summary_network.move(750,250)

        self.first_net = QtGui.QLineEdit(self)
        self.first_net.resize(100,30)
        self.first_net.move(750,150)
        self.first_net.setPlaceholderText("First Network [NID/P]")

        self.second_net = QtGui.QLineEdit(self)
        self.second_net.resize(100,30)
        self.second_net.move(750,200)
        self.second_net.setPlaceholderText("Last Network [NID/P]")

        self.summ_result = QtGui.QLineEdit(self)
        self.summ_result.resize(100,30)
        self.summ_result.move(750,300)
        self.summ_result.setPlaceholderText("Summary Network")

        summary_network.clicked.connect(self.summary)
        submit_button.clicked.connect(self.check)
        close_button.clicked.connect(self.close_app)

    def close_app(self):
            exit_confirm = QtGui.QMessageBox.question(self, "Exit", "Do you want to exit?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)

            if exit_confirm == QtGui.QMessageBox.Yes:
                sys.exit()

            else:
                self

    def flsm_c(self):

                if self.networks_number <= 4:
                    self.a = list( self.network_Address.subnets( 2 ) )
                elif 4 <= self.networks_number <= 8:
                    self.a = list( self.network_Address.subnets( 3 ) )
                elif 9 <= self.networks_number <= 16:
                    self.a = list( self.network_Address.subnets( 4 ) )
                elif 17 <= self.networks_number <= 32:
                    self.a = list( self.network_Address.subnets( 5 ) )
                elif 33 <= self.networks_number <= 64:
                    self.a = list( self.network_Address.subnets( 6 ) )
                elif 65 <= self.networks_number <= 128:
                    self.a = list( self.network_Address.subnets( 7 ) )
                else:
                    self.a = list( self.network_Address.subnets( 8 ) )
                self.display()
    def flsm_b(self):

                if self.networks_number <= 255:
                    self.flsm_c()
                elif 256 <= self.networks_number <= 512 :
                    self.a = list (self.network_Address.subnets(9))
                    self.display()
                elif 512 <= self.networks_number <= 1024 :
                    self.a = list (self.network_Address.subnets(10))
                    self.display()
                elif 1024 <= self.networks_number <= 2048 :
                    self.a = list (self.network_Address.subnets(11))
                    self.display()
                elif 2048 <= self.networks_number <= 4096 :
                    self.a = list (self.network_Address.subnets(12))
                    self.display()
                elif 4096 <= self.networks_number <= 8192 :
                    self.a = list (self.network_Address.subnets(13))
                    self.display()
                elif 8192 <= self.networks_number <= 16384 :
                    self.a = list (self.network_Address.subnets(14))
                    self.display()
                elif 16384 <= self.networks_number <= 32768 :
                    self.a = list (self.network_Address.subnets(15))
                    self.display()
                else:
                    self.a = list (self.network_Address.subnets(16))
                    self.display()
    def flsm_a(self):

                if self.networks_number <= 255:
                    self.flsm_c()
                elif self.networks_number <= 65536:
                    self.flsm_b()
                elif 65536 <= self.networks_number <= 131072:
                    self.a = list(self.network_Address.subnets(17))
                    self.display()
                elif 131072 <= self.networks_number <= 262144:
                    self.a = list(self.network_Address.subnets(18))
                    self.display()
                elif 262144 <= self.networks_number <= 524288:
                    self.a = list(self.network_Address.subnets(19))
                    self.display()
                elif 524288 <= self.networks_number <= 1048576:
                    self.a = list(self.network_Address.subnets(20))
                    self.display()
                elif 1048576 <= self.networks_number <= 2097152:
                    self.a = list(self.network_Address.subnets(21))
                    self.display()
                elif 2097152 <= self.networks_number <= 4194304:
                    self.a = list(self.network_Address.subnets(22))
                    self.display()
                elif 4194304 <= self.networks_number <= 8388608:
                    self.a = list(self.network_Address.subnets(23))
                    self.display()
                else:
                    self.a = list(self.network_Address.subnets(24))
                    self.display()

    def check(self):

        self.inputIP = self.input1.text()
        self.inputNET = self.input2.text()
        self.ip_class_slice = self.inputIP.split( "." )


        if self.input1.text( ) =="" or self.input2.text( )=="":
            self.warning = QtGui.QMessageBox.warning(self,"Error","Enter Values First!",QtGui.QMessageBox.Ok)


        elif (len(self.ip_class_slice) != 4 ):
            self.warning = QtGui.QMessageBox.warning(self,"Error","Check IP Address Length!",QtGui.QMessageBox.Ok)

        else:
            self.networks_number = int(self.inputNET)
            self.network_Address = str(self.inputIP)
            self.prefix = self.network_Address.split("/")
            self.prefix=int(self.prefix[1])
            self.first_octet = self.ip_class_slice[0]
            self.second_octet = self.ip_class_slice [1]
            self.first_octetint = int( self.first_octet )
            self.second_octetint = int(self.second_octet)
            self.last_octet = self.ip_class_slice[3].split("/")


            if self.first_octetint in range( 1, 126 ) and self.networks_number >= 16777216 :
                self.warning = QtGui.QMessageBox.warning(self,"Error","Less than 16777216",QtGui.QMessageBox.Ok)

            elif self.first_octetint in range( 1, 126 ) and (self.prefix < 8 or self.second_octetint != 0 or int(self.ip_class_slice[2]) != 0 or int(self.last_octet[0]) !=0):
                self.warning = QtGui.QMessageBox.warning(self,"Error","Error in Prefix Value or host bits set",QtGui.QMessageBox.Ok)

            elif self.first_octetint == 127:
                self.warning = QtGui.QMessageBox.warning(self,"Error","It's a loopback address",QtGui.QMessageBox.Ok)

            elif self.first_octetint == 0:
                self.warning = QtGui.QMessageBox.warning(self,"Error","It's the default Route address",QtGui.QMessageBox.Ok)

            elif self.first_octetint in range(128, 191) and self.networks_number >= 65536:
                self.warning = QtGui.QMessageBox.warning(self,"Error","Less than 65536",QtGui.QMessageBox.Ok)

            elif self.first_octetint in range( 128, 191 ) and (self.prefix < 16 or int(self.ip_class_slice[2] ) != 0) or (int(self.last_octet[0]) != 0):
                self.warning = QtGui.QMessageBox.warning(self,"Error","Error in Prefix Value or host bits set",QtGui.QMessageBox.Ok)

            elif self.first_octetint == 169 and self.second_octetint == 254:
                self.warning = QtGui.QMessageBox.warning(self,"Error","APIPA",QtGui.QMessageBox.Ok)

            elif self.first_octetint in range( 192, 223 ) and self.networks_number > 255:
                self.warning = QtGui.QMessageBox.warning(self,"Error","Less than 256",QtGui.QMessageBox.Ok)

            elif (self.first_octetint in range(192, 223)) and (self.prefix < 24 or int(self.last_octet[0]) !=0):
                self.warning = QtGui.QMessageBox.warning(self,"Error","Error in Prefix Value or host bits set",QtGui.QMessageBox.Ok)


            else:
                self.network_Address = ipaddress.ip_network(self.network_Address)
                self.submit()
                self.supernet()

    def submit(self):
        self.result.clear()

        if self.first_octetint in range( 1, 127 ) and self.networks_number < 16777216 :
            self.flsm_a()
        elif self.first_octetint in range(128, 191) and self.networks_number < 65536:
            self.flsm_b()
        else:
            self.flsm_c()

    def display(self):
            self.b = ipaddress.ip_network(self.a[0])
            self.new_subnet_mask = str(self.b.netmask)
            self.netmasklabel.setText(self.new_subnet_mask)

            for self.netAdd in range (0,self.networks_number):
                self.netaddstr = str(self.a[self.netAdd])
                self.result.addItem(self.netaddstr)

    def supernet(self):
        self.firstNetaddress = self.a[0]
        self.lastNetaddress = self.a[self.networks_number-1]
        self.prefixlen = self.firstNetaddress.prefixlen
        self.lastNetbroadcast = self.lastNetaddress.broadcast_address
        i = 0
        while i < self.prefixlen:
            self.supernetted = self.firstNetaddress.supernet(i)
            self.supernetBC = self.supernetted.broadcast_address

            if self.supernetBC >= self.lastNetbroadcast:
                self.summaryLabel.setText(str(self.supernetted))
                break
            i += 1

    def summary(self):
        if (self.first_net.text() == "" or self.second_net.text() == ""):
                self.warning = QtGui.QMessageBox.warning(self,"Error","Enter Values First!",QtGui.QMessageBox.Ok)

        else:
                self.first_network = self.first_net.text()
                self.last_network = self.second_net.text()
                self.firstNetaddress = ipaddress.ip_network(self.first_network)
                self.lastNetaddress = ipaddress.ip_network(self.last_network)
                self.prefixlen = self.firstNetaddress.prefixlen
                self.lastNetbroadcast = self.lastNetaddress.broadcast_address

                i = 0
                while i < self.prefixlen:
                    self.summ_net = self.firstNetaddress.supernet(i)
                    self.supernetBC = self.summ_net.broadcast_address

                    if self.supernetBC >= self.lastNetbroadcast:
                        self.summ_result.setText(str(self.summ_net))
                        break
                    i += 1

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())