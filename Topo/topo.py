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
        s9 = self.addSwitch('s9', protocols='OpenFlow13')
        s10 = self.addSwitch('s10', protocols='OpenFlow13')

        # Definicion de los terminales
        h1 = self.addHost('h1', mac="00:00:00:00:00:01", ip="192.168.1.1/24")
        h2 = self.addHost('h2', mac="00:00:00:00:00:02", ip="192.168.1.2/24")
        h3 = self.addHost('h3', mac="00:00:00:00:00:03", ip="192.168.1.3/24")
        h4 = self.addHost('h4', mac="00:00:00:00:00:04", ip="192.168.1.4/24")
        
        # Definicion las conexiones
        # Primera linea de conexiones
        self.addLink(s1,h1,1,1)
        self.addLink(s1,h2,2,1)
        self.addLink(s1,s2,3,1)  
        self.addLink(s1,s3,4,1)
        self.addLink(s1,s4,5,1)

        # Segunda linea de conexiones
        self.addLink(s2,s5,2,1)
        self.addLink(s3,s6,2,1)
        self.addLink(s4,s7,2,1)
        self.addLink(s5,s8,2,1)
        self.addLink(s7,s9,2,1)

        # Tercera linea de conexiones
        self.addLink(s8,s10,2,1)
        self.addLink(s9,s10,2,2)
        self.addLink(s6,s10,2,3)
        self.addLink(h3,s10,2,4)
        self.addLink(h4,s10,2,5)

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
