#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import OVSSwitch, Controller, RemoteController
from time import sleep


class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."
    def build(self):
        # Definicion de los switches
        s1 = self.addSwitch('s1', protocols='OpenFlow13')
        s2 = self.addSwitch('s2', protocols='OpenFlow13')
        s3 = self.addSwitch('s3', protocols='OpenFlow13')
        s4 = self.addSwitch('s4', protocols='OpenFlow13')
        s5 = self.addSwitch('s5', protocols='OpenFlow13')
        s6 = self.addSwitch('s6', protocols='OpenFlow13')
        s7 = self.addSwitch('s7', protocols='OpenFlow13')
        s8 = self.addSwitch('s8', protocols='OpenFlow13')

        # Definicion de los terminales
        h1 = self.addHost('h1', mac="00:00:00:00:00:01", ip="192.168.1.1/24")
        h2 = self.addHost('h2', mac="00:00:00:00:00:02", ip="192.168.1.2/24")
        #h3 = self.addHost('h3', mac="00:00:00:00:00:03", ip="192.168.1.3/24")
        #h4 = self.addHost('h4', mac="00:00:00:00:00:04", ip="192.168.1.4/24")
        
        # Definicion las conexiones
        # Conexiones de S1
        self.addLink(s1,s2,3,1)  
        self.addLink(s1,s3,2,1)
        self.addLink(s1,h1,1,1)
            
        # Conexiones de S2
        # self.addLink(s1,s2,3,1)
        self.addLink(s2,s4,2,1)
        self.addLink(s2,s5,3,1)

        # Conexiones de S3
        # self.addLink(s1,s3,2,1)
        self.addLink(s3,s4,2,4)
        self.addLink(s3,s6,3,2)
        self.addLink(s3,s7,4,1)

        # Conexiones de S4
        # self.addLink(s2,s4,2,1)
        # self.addLink(s3,s4,2,4)
        self.addLink(s4,s5,2,2)
        self.addLink(s4,s6,3,1)
        self.addLink(s4,s8,5,4)

        # Conexiones de S5
        # self.addLink(s4,s5,2,2)
        # self.addLink(s4,s5,2,2)
        self.addLink(s5,s8,3,5)

        # Conexiones de S6
        # self.addLink(s4,s6,3,1)
        # self.addLink(s3,s6,3,2)
        self.addLink(s6,s8,4,3)
        self.addLink(s6,s7,3,2)

        # Conexiones de S7
        # self.addLink(s3,s7,4,1)
        # self.addLink(s6,s7,3,2)
        self.addLink(s7,s8,3,2)

        # Conexiones de S8
        # self.addLink(s5,s8,3,5)
        # self.addLink(s4,s8,5,4)
        # self.addLink(s6,s8,4,3)
        # self.addLink(s7,s8,3,2)
        self.addLink(s8,h2,1,1)

if __name__ == '__main__':
    setLogLevel('info')
    topo = SingleSwitchTopo()
    c1 = RemoteController('c1', ip='127.0.0.1')
    net = Mininet(topo=topo, controller=c1)
    net.start()
    #sleep(5)
    print("Topology is up, lets ping")
    #net.pingAll()
    CLI(net)
    net.stop()
