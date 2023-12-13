from input import list_of_instructions
from delay import delay_max
from delay import all_delays
from delay import x as given_delays
import matplotlib.pyplot as plt

outfile = open('log_pva.txt' , 'w')
report_file = open('report_pva.txt','w')
outfile_pvs = open('log_pvs.txt' , 'w')
report_file_pvs = open('report_pvs.txt','w')
delay_now =0
pelinks=[0 for i in range(9)]
links=[0 for i in range(12)]
latency_1={}
latency_2={}
class Instruction:
    route = []
    head = False
    body = False
    tail = False
    index = 0
    clock_cycle = 0
    end_time = 0
    start_time = -1
    source = ""
    destination = ""
    name=""

    head1 = ""
    data1=""
    tail1 = ""
    body1 = ""
    pvs_pva=0
    tail_head_diff=0

    def __init__(self,x,routing,router_list,pvs_pva):
        self.clock_cycle = int(x[0])
        self.source = x[1]
        self.destination = x[2]
        self.pvs_pva=pvs_pva
        self.make_path(routing,router_list)
        # print(len(self.route))

        self.data1 = x[3]  #To find_instructions if given flit is head,tail or body
        if (self.data1[-2:] == "01"):
            self.body1 = self.data1
            self.body = True
            self.name=" Body "
        elif (self.data1[-2:] == "00"):
            self.head1 = self.data1
            self.head = True
            self.name=" Head "
        elif (self.data1[-2:] == "10"):
            self.tail1 = self.data1
            self.tail = True
            self.name=" Tail "
    
    def make_path(self,direction,router_list):
        if direction == 1:
            self.route = self.get_path_XY(router_list)
        elif direction == 2:
            self.route = self.get_path_YX(router_list)


    def get_path_XY(self,router_list):
        path=[]
        path.append(Router(router_list[int(self.source)-1],int(self.source)-1,self.pvs_pva))
        row1=["1","2","3"]
        row2=["4","5","6"]
        row3=["7","8","9"]
        col1=["1","6","7"]
        col2=["2","5","8"]
        col3=["3","4","9"]
        #Write code for XY routing
        #Separate codes for head, body and tail
        if self.source==self.destination:
            return
        if self.source=="1":
            if self.destination in col1:
                if (self.destination=="6"):
                    links[7]+=1
                    path.append(Router(router_list[5],5, self.pvs_pva))
                elif (self.destination=="7"):
                    links[7]+=1
                    links[6]+=1
                    path.append(Router(router_list[5],5, self.pvs_pva))
                    path.append(Router(router_list[6],6, self.pvs_pva))
            elif self.destination in col2:
                links[0]+=1
                path.append(Router(router_list[1],1, self.pvs_pva))
                if (self.destination=="5"):
                    links[8]+=1
                    path.append(Router(router_list[4],4, self.pvs_pva))
                elif (self.destination=="8"):
                    links[8]+=1
                    links[10]+=1
                    path.append(Router(router_list[4],4, self.pvs_pva))
                    path.append(Router(router_list[7],7, self.pvs_pva))
            elif self.destination in col3:
                links[0]+=1
                links[1]+=1
                path.append(Router(router_list[1],1, self.pvs_pva))
                path.append(Router(router_list[2],2, self.pvs_pva))
                if (self.destination=="4"):
                    links[2]+=1
                    path.append(Router(router_list[3],3, self.pvs_pva))
                elif (self.destination=="9"):
                    links[2]+=1
                    links[3]+=1
                    path.append(Router(router_list[3],3, self.pvs_pva))
                    path.append(Router(router_list[8],8, self.pvs_pva))

        elif self.source=="2":
            if self.destination in col1:
                links[0]+=1
                path.append(Router(router_list[0],0, self.pvs_pva))
                if (self.destination=="6"):
                    links[7]+=1
                    path.append(Router(router_list[5],5, self.pvs_pva))
                elif (self.destination=="7"):
                    links[7]+=1
                    links[6]+=1
                    path.append(Router(router_list[5],5, self.pvs_pva))
                    path.append(Router(router_list[6],6, self.pvs_pva))
            elif self.destination in col2:
                if (self.destination=="5"):
                    links[8]+=1
                    path.append(Router(router_list[4],4, self.pvs_pva))
                elif (self.destination=="8"):
                    links[8]+=1
                    links[10]+=1
                    path.append(Router(router_list[4],4, self.pvs_pva))
                    path.append(Router(router_list[7],7, self.pvs_pva))
            elif self.destination in col3:
                links[1]+=1
                path.append(Router(router_list[2],2, self.pvs_pva))
                if (self.destination=="4"):
                    links[2]+=1
                    path.append(Router(router_list[3],3, self.pvs_pva))
                elif (self.destination=="9"):
                    links[2]+=1
                    links[3]+=1
                    path.append(Router(router_list[3],3, self.pvs_pva))
                    path.append(Router(router_list[8],8, self.pvs_pva))

        elif self.source=="3":
            if self.destination in col1:
                links[0]+=1
                links[1]+=1
                path.append(Router(router_list[1],1, self.pvs_pva))
                path.append(Router(router_list[0],0, self.pvs_pva))
                if (self.destination=="6"):
                    links[7]+=1
                    path.append(Router(router_list[5],5, self.pvs_pva))
                elif (self.destination=="7"):
                    links[7]+=1
                    links[6]+=1
                    path.append(Router(router_list[5],5, self.pvs_pva))
                    path.append(Router(router_list[6],6, self.pvs_pva))
            elif self.destination in col2:
                links[1]+=1
                path.append(Router(router_list[1],1, self.pvs_pva))
                if (self.destination=="5"):
                    links[8]+=1
                    path.append(Router(router_list[4],4, self.pvs_pva))
                elif (self.destination=="8"):
                    links[8]+=1
                    links[10]+=1
                    path.append(Router(router_list[4],4, self.pvs_pva))
                    path.append(Router(router_list[7],7, self.pvs_pva))
            elif self.destination in col3:
                if (self.destination=="4"):
                    links[2]+=1
                    path.append(Router(router_list[3],3, self.pvs_pva))
                elif (self.destination=="9"):
                    links[2]+=1
                    links[3]+=1
                    path.append(Router(router_list[3],3, self.pvs_pva))
                    path.append(Router(router_list[8],8, self.pvs_pva))

        elif self.source=="4":
            if self.destination in col1:
                links[9]+=1
                links[11]+=1
                path.append(Router(router_list[4],4, self.pvs_pva))
                path.append(Router(router_list[5],5, self.pvs_pva))
                if (self.destination=="1"):
                    links[7]+=1
                    path.append(Router(router_list[0],0, self.pvs_pva))
                elif (self.destination=="7"):
                    links[6]+=1
                    path.append(Router(router_list[6],6, self.pvs_pva))
            elif self.destination in col2:
                links[9]+=1
                path.append(Router(router_list[4],4, self.pvs_pva))
                if (self.destination=="2"):
                    links[8]+=1
                    path.append(Router(router_list[1],1, self.pvs_pva))
                elif (self.destination=="8"):
                    links[10]+=1
                    path.append(Router(router_list[7],7, self.pvs_pva))
            elif self.destination in col3:
                if (self.destination=="3"):
                    links[2]+=1
                    path.append(Router(router_list[2],2, self.pvs_pva))
                elif (self.destination=="9"):
                    links[3]+=1
                    path.append(Router(router_list[8],8, self.pvs_pva))

        elif self.source=="5":
            if self.destination in col1:
                links[11]+=1
                path.append(Router(router_list[5],5, self.pvs_pva))
                if (self.destination=="1"):
                    links[7]+=1
                    path.append(Router(router_list[0],0, self.pvs_pva))
                elif (self.destination=="7"):
                    links[6]+=1
                    path.append(Router(router_list[6],6, self.pvs_pva))
            elif self.destination in col2:
                if (self.destination=="2"):
                    links[8]+=1
                    path.append(Router(router_list[1],1, self.pvs_pva))
                elif (self.destination=="8"):
                    links[10]+=1
                    path.append(Router(router_list[7],7, self.pvs_pva))
            elif self.destination in col3:
                links[9]+=1
                path.append(Router(router_list[3],3, self.pvs_pva))
                if (self.destination=="3"):
                    links[2]+=1
                    path.append(Router(router_list[2],2, self.pvs_pva))
                elif (self.destination=="9"):
                    links[3]+=1
                    path.append(Router(router_list[8],8, self.pvs_pva))

        elif self.source=="6":
            if self.destination in col1:
                if (self.destination=="1"):
                    links[7]+=1
                    path.append(Router(router_list[0],0, self.pvs_pva))
                elif (self.destination=="7"):
                    links[6]+=1
                    path.append(Router(router_list[6],6, self.pvs_pva))
            elif self.destination in col2:
                links[11]+=1
                path.append(Router(router_list[4],4, self.pvs_pva))
                if (self.destination=="2"):
                    links[8]+=1
                    path.append(Router(router_list[1],1, self.pvs_pva))
                elif (self.destination=="8"):
                    links[10]+=1
                    path.append(Router(router_list[7],7, self.pvs_pva))
            elif self.destination in col3:
                links[11]+=1
                links[9]+=1
                path.append(Router(router_list[4],4, self.pvs_pva))
                path.append(Router(router_list[3],3, self.pvs_pva))
                if (self.destination=="3"):
                    links[2]+=1
                    path.append(Router(router_list[2],2, self.pvs_pva))
                elif (self.destination=="9"):
                    links[3]+=1
                    path.append(Router(router_list[8],8, self.pvs_pva))

        elif self.source=="7":
            if self.destination in col1:
                if (self.destination=="1"):
                    links[7]+=1
                    links[6]+=1
                    path.append(Router(router_list[5],5, self.pvs_pva))
                    path.append(Router(router_list[0],0, self.pvs_pva))
                elif (self.destination=="6"):
                    links[6]+=1
                    path.append(Router(router_list[5],5, self.pvs_pva))
            elif self.destination in col2:
                links[5]+=1
                path.append(Router(router_list[7],7, self.pvs_pva))
                if (self.destination=="2"):
                    links[8]+=1
                    links[10]+=1
                    path.append(Router(router_list[4],4, self.pvs_pva))
                    path.append(Router(router_list[1],1, self.pvs_pva))
                elif (self.destination=="5"):
                    links[10]+=1
                    path.append(Router(router_list[4],4, self.pvs_pva))
            elif self.destination in col3:
                links[5]+=1
                links[4]+=1
                path.append(Router(router_list[7],7, self.pvs_pva))
                path.append(Router(router_list[8],8, self.pvs_pva))
                if (self.destination=="3"):
                    links[3]+=1
                    links[2]+=1
                    path.append(Router(router_list[3],3, self.pvs_pva))
                    path.append(Router(router_list[2],2, self.pvs_pva))
                elif (self.destination=="4"):
                    links[3]+=1
                    path.append(Router(router_list[3],3, self.pvs_pva))

        elif self.source=="8":
            if self.destination in col1:
                links[5]+=1
                path.append(Router(router_list[6],6, self.pvs_pva))
                if (self.destination=="1"):
                    links[7]+=1
                    links[6]+=1
                    path.append(Router(router_list[5],5, self.pvs_pva))
                    path.append(Router(router_list[0],0, self.pvs_pva))
                elif (self.destination=="6"):
                    links[6]+=1
                    path.append(Router(router_list[5],5, self.pvs_pva))
            elif self.destination in col2:
                if (self.destination=="2"):
                    links[8]+=1
                    links[10]+=1
                    path.append(Router(router_list[4],4, self.pvs_pva))
                    path.append(Router(router_list[1],1, self.pvs_pva))
                elif (self.destination=="5"):
                    links[10]+=1
                    path.append(Router(router_list[4],4, self.pvs_pva))
            elif self.destination in col3:
                links[4]+=1
                path.append(Router(router_list[8],8, self.pvs_pva))
                if (self.destination=="3"):
                    links[3]+=1
                    links[2]+=1
                    path.append(Router(router_list[3],3, self.pvs_pva))
                    path.append(Router(router_list[2],2, self.pvs_pva))
                elif (self.destination=="4"):
                    links[3]+=1
                    path.append(Router(router_list[3],3, self.pvs_pva))

           
        elif self.source=="9":
            if self.destination in col1:
                links[4]+=1
                links[5]+=1
                path.append(Router(router_list[7],7, self.pvs_pva))
                path.append(Router(router_list[6],6, self.pvs_pva))
                if (self.destination=="1"):
                    links[7]+=1
                    links[6]+=1
                    path.append(Router(router_list[5],5, self.pvs_pva))
                    path.append(Router(router_list[0],0, self.pvs_pva))
                elif (self.destination=="6"):
                    links[6]+=1
                    path.append(Router(router_list[5],5, self.pvs_pva))
            elif self.destination in col2:
                links[4]+=1
                path.append(Router(router_list[7],7, self.pvs_pva))
                if (self.destination=="2"):
                    links[8]+=1
                    links[10]+=1
                    path.append(Router(router_list[4],4, self.pvs_pva))
                    path.append(Router(router_list[1],1, self.pvs_pva))
                elif (self.destination=="5"):
                    links[10]+=1
                    path.append(Router(router_list[4],4, self.pvs_pva))
            elif self.destination in col3:
                if (self.destination=="3"):
                    links[2]+=1
                    links[3]+=1
                    path.append(Router(router_list[3],3, self.pvs_pva))
                    path.append(Router(router_list[2],2, self.pvs_pva))
                elif (self.destination=="4"):
                    links[3]+=1
                    path.append(Router(router_list[3],3, self.pvs_pva))

        return path

    def get_path_YX(self,router_list):
        path=[]
        path.append(Router(router_list[int(self.source)-1],int(self.source)-1,self.pvs_pva))
        row1=["1","2","3"]
        row2=["4","5","6"]
        row3=["7","8","9"]
        col1=["1","6","7"]
        col2=["2","5","8"]
        col3=["3","4","9"]
        #Write code for YX routing
        #Separate codes for head, body and tail
        if self.source==self.destination:
            return
        if self.source=="1":
            if self.destination in row1:
                if (self.destination=="2"):
                    links[0]+=1
                    path.append(Router(router_list[1],1, self.pvs_pva))
                elif (self.destination=="3"):
                    links[0]+=1
                    links[1]+=1
                    path.append(Router(router_list[1],1, self.pvs_pva))
                    path.append(Router(router_list[2],2, self.pvs_pva))
            elif self.destination in row2:
                links[7]+=1
                path.append(Router(router_list[5],5, self.pvs_pva))
                if (self.destination=="5"):
                    links[11]+=1
                    path.append(Router(router_list[4],4, self.pvs_pva))
                elif (self.destination=="4"):
                    links[11]+=1
                    links[9]+=1
                    path.append(Router(router_list[4],4, self.pvs_pva))
                    path.append(Router(router_list[3],3, self.pvs_pva))
            elif self.destination in row3:
                links[7]+=1
                links[6]+=1
                path.append(Router(router_list[5],5, self.pvs_pva))
                path.append(Router(router_list[6],6, self.pvs_pva))
                if (self.destination=="8"):
                    links[5]+=1
                    path.append(Router(router_list[7],7, self.pvs_pva))
                elif (self.destination=="9"):
                    links[5]+=1
                    links[4]+=1
                    path.append(Router(router_list[7],7, self.pvs_pva))
                    path.append(Router(router_list[8],8, self.pvs_pva))

        elif self.source=="2":
            if self.destination in row1:
                if (self.destination=="1"):
                    links[0]+=1
                    path.append(Router(router_list[0],0, self.pvs_pva))
                elif (self.destination=="3"):
                    links[1]+=1
                    path.append(Router(router_list[2],2, self.pvs_pva))
            elif self.destination in row2:
                links[8]+=1
                path.append(Router(router_list[4],4, self.pvs_pva))
                if (self.destination=="6"):
                    links[11]+=1
                    path.append(Router(router_list[5],5, self.pvs_pva))
                elif (self.destination=="4"):
                    links[9]+=1
                    path.append(Router(router_list[3],3, self.pvs_pva))
            elif self.destination in row3:
                links[8]+=1
                links[10]+=1
                path.append(Router(router_list[4],4, self.pvs_pva))
                path.append(Router(router_list[7],7, self.pvs_pva))
                if (self.destination=="7"):
                    links[5]+=1
                    path.append(Router(router_list[6],6, self.pvs_pva))
                elif (self.destination=="9"):
                    links[4]+=1
                    path.append(Router(router_list[8],8, self.pvs_pva))

        elif self.source=="3":
            if self.destination in row1:
                if (self.destination=="2"):
                    links[1]+=1
                    path.append(Router(router_list[1],1, self.pvs_pva))
                elif (self.destination=="1"):
                    links[1]+=1
                    links[0]+=1
                    path.append(Router(router_list[1],1, self.pvs_pva))
                    path.append(Router(router_list[0],0, self.pvs_pva))
            elif self.destination in row2:
                links[2]+=1
                path.append(Router(router_list[3],3, self.pvs_pva))
                if (self.destination=="5"):
                    links[9]+=1
                    path.append(Router(router_list[4],4, self.pvs_pva))
                elif (self.destination=="6"):
                    links[9]+=1
                    links[11]+=1
                    path.append(Router(router_list[4],4, self.pvs_pva))
                    path.append(Router(router_list[5],5, self.pvs_pva))
            elif self.destination in row3:
                links[2]+=1
                links[3]+=1
                path.append(Router(router_list[3],3, self.pvs_pva))
                path.append(Router(router_list[8],8, self.pvs_pva))
                if (self.destination=="8"):
                    links[4]+=1
                    path.append(Router(router_list[7],7, self.pvs_pva))
                elif (self.destination=="7"):
                    links[4]+=1
                    links[5]+=1
                    path.append(Router(router_list[7],7, self.pvs_pva))
                    path.append(Router(router_list[6],6, self.pvs_pva))

        elif self.source=="4":
            if self.destination in row1:
                links[2]+=1
                path.append(Router(router_list[2],2, self.pvs_pva))
                if (self.destination=="2"):
                    links[1]+=1
                    path.append(Router(router_list[1],1, self.pvs_pva))
                elif (self.destination=="1"):
                    links[1]+=1
                    links[0]+=1
                    path.append(Router(router_list[1],1, self.pvs_pva))
                    path.append(Router(router_list[0],0, self.pvs_pva))
            elif self.destination in row2:
                if (self.destination=="5"):
                    links[9]+=1
                    path.append(Router(router_list[4],4, self.pvs_pva))
                elif (self.destination=="6"):
                    links[9]+=1
                    links[11]+=1
                    path.append(Router(router_list[4],4, self.pvs_pva))
                    path.append(Router(router_list[5],5, self.pvs_pva))
            elif self.destination in row3:
                links[3]+=1
                path.append(Router(router_list[8],8, self.pvs_pva))
                if (self.destination=="8"):
                    links[4]+=1
                    path.append(Router(router_list[7],7, self.pvs_pva))
                elif (self.destination=="7"):
                    links[4]+=1
                    links[5]+=1
                    path.append(Router(router_list[7],7, self.pvs_pva))
                    path.append(Router(router_list[6],6, self.pvs_pva))

        elif self.source=="5":
            if self.destination in row1:
                links[8]+=1
                path.append(Router(router_list[1],1, self.pvs_pva))
                if (self.destination=="1"):
                    links[0]+=1
                    path.append(Router(router_list[0],0, self.pvs_pva))
                elif (self.destination=="3"):
                    links[1]+=1
                    path.append(Router(router_list[2],2, self.pvs_pva))
            elif self.destination in row2:
                if (self.destination=="6"):
                    links[11]+=1
                    path.append(Router(router_list[5],5, self.pvs_pva))
                elif (self.destination=="4"):
                    links[9]+=1
                    path.append(Router(router_list[3],3, self.pvs_pva))
            elif self.destination in row3:
                links[10]+=1
                path.append(Router(router_list[7],7, self.pvs_pva))
                if (self.destination=="7"):
                    links[5]+=1
                    path.append(Router(router_list[6],6, self.pvs_pva))
                elif (self.destination=="9"):
                    links[4]+=1
                    path.append(Router(router_list[8],8, self.pvs_pva))

        elif self.source=="6":
            if self.destination in row1:
                links[7]+=1
                path.append(Router(router_list[0],0, self.pvs_pva))
                if (self.destination=="2"):
                    links[0]+=1
                    path.append(Router(router_list[1],1, self.pvs_pva))
                elif (self.destination=="3"):
                    links[0]+=1
                    links[1]+=1
                    path.append(Router(router_list[1],1, self.pvs_pva))
                    path.append(Router(router_list[2],2, self.pvs_pva))
            elif self.destination in row2:
                if (self.destination=="5"):
                    links[11]+=1
                    path.append(Router(router_list[4],4, self.pvs_pva))
                elif (self.destination=="4"):
                    links[11]+=1
                    links[9]+=1
                    path.append(Router(router_list[5],5, self.pvs_pva))
                    path.append(Router(router_list[3],3, self.pvs_pva))
            elif self.destination in row3:
                links[6]+=1
                path.append(Router(router_list[6],6, self.pvs_pva))
                if (self.destination=="8"):
                    links[5]+=1
                    path.append(Router(router_list[7],7, self.pvs_pva))
                elif (self.destination=="9"):
                    links[5]+=1
                    links[4]+=1
                    path.append(Router(router_list[7],7, self.pvs_pva))
                    path.append(Router(router_list[8],8, self.pvs_pva))

        elif self.source=="7":
            if self.destination in row1:
                links[6]+=1
                links[7]+=1
                path.append(Router(router_list[5],5, self.pvs_pva))
                path.append(Router(router_list[0],0, self.pvs_pva))
                if (self.destination=="2"):
                    links[0]+=1
                    path.append(Router(router_list[1],1, self.pvs_pva))
                elif (self.destination=="3"):
                    links[0]+=1
                    links[1]+=1
                    path.append(Router(router_list[1],1, self.pvs_pva))
                    path.append(Router(router_list[2],2, self.pvs_pva))
            elif self.destination in row2:
                links[6]+=1
                path.append(Router(router_list[5],5, self.pvs_pva))
                if (self.destination=="4"):
                    links[11]+=1
                    links[9]+=1
                    path.append(Router(router_list[4],4, self.pvs_pva))
                    path.append(Router(router_list[3],3, self.pvs_pva))
                elif (self.destination=="5"):
                    links[11]+=1
                    path.append(Router(router_list[4],4, self.pvs_pva))
            elif self.destination in row3:
                if (self.destination=="8"):
                    links[5]+=1
                    path.append(Router(router_list[7],7, self.pvs_pva))
                elif (self.destination=="9"):
                    links[5]+=1
                    links[4]+=1
                    path.append(Router(router_list[7],7, self.pvs_pva))
                    path.append(Router(router_list[8],8, self.pvs_pva))

        elif self.source=="8":
            if self.destination in row1:
                links[10]+=1
                links[8]+=1
                path.append(Router(router_list[4],4, self.pvs_pva))
                path.append(Router(router_list[1],1, self.pvs_pva))
                if (self.destination=="1"):
                    links[0]+=1
                    path.append(Router(router_list[0],0, self.pvs_pva))
                elif (self.destination=="3"):
                    links[1]+=1
                    path.append(Router(router_list[2],2, self.pvs_pva))
            elif self.destination in row2:
                links[10]+=1
                path.append(Router(router_list[4],4, self.pvs_pva))
                if (self.destination=="6"):
                    links[11]+=1
                    path.append(Router(router_list[5],5, self.pvs_pva))
                elif (self.destination=="4"):
                    links[9]+=1
                    path.append(Router(router_list[3],3, self.pvs_pva))
            elif self.destination in row3:
                if (self.destination=="7"):
                    links[5]+=1
                    path.append(Router(router_list[6],6, self.pvs_pva))
                elif (self.destination=="9"):
                    links[4]+=1
                    path.append(Router(router_list[8],8, self.pvs_pva))

           
        elif self.source=="9":
            if self.destination in col1:
                links[3]+=1
                links[2]+=1
                path.append(Router(router_list[3],3, self.pvs_pva))
                path.append(Router(router_list[2],2, self.pvs_pva))
                if (self.destination=="1"):
                    links[0]+=1
                    links[1]+=1
                    path.append(Router(router_list[1],1, self.pvs_pva))
                    path.append(Router(router_list[0],0, self.pvs_pva))
                elif (self.destination=="2"):
                    links[1]+=1
                    path.append(Router(router_list[1],1, self.pvs_pva))
            elif self.destination in row2:
                links[3]+=1
                path.append(Router(router_list[3],3, self.pvs_pva))
                if (self.destination=="6"):
                    links[9]+=1
                    links[11]+=1
                    path.append(Router(router_list[4],4, self.pvs_pva))
                    path.append(Router(router_list[5],5, self.pvs_pva))
                elif (self.destination=="5"):
                    links[9]+=1
                    path.append(Router(router_list[4],4, self.pvs_pva))
            elif self.destination in row3:
                if (self.destination=="7"):
                    links[5]+=1
                    links[4]+=1
                    path.append(Router(router_list[7],7, self.pvs_pva))
                    path.append(Router(router_list[6],6, self.pvs_pva))
                elif (self.destination=="8"):
                    links[4]+=1
                    path.append(Router(router_list[7],7, self.pvs_pva))

        return path

    def print_route(self):
        for i in self.route:
            print(i, end=" ")
        print()



class Router:
    name = ""
    id=0
    counter = 0
    busy = False
    source = ""
    destination = ""
    crossbar = []
    sw_allocator = []
    ip_buffer = []
    current_element=-1  #0 for input_buffer, 1 for SW, 2 for crossbar
    ip_port = ["North", "South", "East", "West", "Local"]
    op_port = ["North", "South", "East", "West", "Local"]
    delayed= False
    spec_delay=0
    pvs=False
    pva=False
    def __init__(self, name,num,pvs_pva):
        self.name = name
        self.id=num
        if pvs_pva==0:
            self.pva=True
        elif pvs_pva==1:
            self.pvs=True
    def update(self,instruction, clock_cyle,partname, source, destination,delay_now):
        self.current_element+=1
        type_of_element=""
        if(self.current_element==0):
            type_of_element="Input buffer"
        elif(self.current_element==1):
            type_of_element="SA"
        elif(self.current_element==2):
            type_of_element="Crossbar"
        else:
            type_of_element=str(self.current_element)
        self.spec_delay=all_delays[self.id][self.current_element]
        if(self.pva):
            L = ["Clock cycle: ", str(clock_cyle) + " ||", " Flit: ",partname + " ||", " Source: ", instruction.source + " ||"," Destination: ",instruction.destination + " ||", " Present Router: ",self.name +" ||"," Next Router: ", destination.name+" ||"," Type: " +type_of_element," \n"]
            outfile.writelines(L)
            R = ["Clock cycle: ", str(clock_cyle) + " ||","curr_delay: "+str(given_delays[self.current_element]) + " ||", " Flit: ",partname +" ||"," Source: ", instruction.source + " ||"," Destination: ",instruction.destination + " ||"," Present router: ",self.name+" ||"," Type: "+type_of_element +" ||"," Delay: ",str(delay_now), "\n"]
            report_file.writelines(R)
        elif(self.pvs):
            if(self.spec_delay>delay_max and self.delayed==False):
                self.delayed=True
                self.current_element-=1
                return
            L1 = ["Clock cycle: ", str(clock_cyle) + " ||", " Flit: ",partname + " ||", " Source: ", instruction.source + " ||"," Destination: ",instruction.destination + " ||", " Present Router: ",self.name +" ||"," Next Router: ", destination.name+" ||"," Type: " +type_of_element," \n"]
            outfile_pvs.writelines(L1)
            if(self.delayed):
                delayy="Yes"
            else:
                delayy="No "
    
            R1 = ["delayed "+delayy + " ||","curr_delay: "+str(round(self.spec_delay,4)) + " ||"," Clock cycle: ", str(clock_cyle) + " ||", " Flit: ",partname +" ||"," Source: ", instruction.source + " ||"," Destination: ",instruction.destination + " ||"," Present router: ",self.name+" ||"," Type: "+type_of_element +" ||"," Delay: ",str(delay_now), "\n"]
            report_file_pvs.writelines(R1)
        return 



class NoC:
    traffic = [[] for i in range(9)]
    all_instructions=[]
    clk1 = 50 #iniitiating with 50 total cycles and increase if an instruction comes with clock cycle>50

    router_list = ["Router 1","Router 2","Router 3","Router 4","Router 5","Router 6","Router 7","Router 8","Router 9"]

    def add_instruction(self,instructions,routing,pvs_pva):
        index=1
        for x in instructions:
            x1 = x.split()
            x = list(map(str,x1))
            print(x)
            input = Instruction(x,routing,self.router_list,pvs_pva)
            if input.tail==True:
                input.tail_head_diff=input.clock_cycle-self.all_instructions[-2].clock_cycle
            # print(input.source)
            # print(input.clock_cycle)
            self.all_instructions.append(input)
            if (input.clock_cycle >= self.clk1):
                self.clk1 = input.clock_cycle+1
            pelinks[int(input.source)-1]+=1
            pelinks[int(input.destination)-1]+=1
            if(input.source=="1"):
                self.traffic[0].append(input)
                self.traffic[0].sort(key = lambda x:x.clock_cycle)
            if(input.source=="2"):
                self.traffic[1].append(input)
                self.traffic[1].sort(key = lambda x:x.clock_cycle)
            if(input.source=="3"):
                self.traffic[2].append(input)
                self.traffic[2].sort(key = lambda x:x.clock_cycle)
            if(input.source=="4"):
                self.traffic[3].append(input)
                self.traffic[3].sort(key = lambda x:x.clock_cycle)    
            if(input.source=="5"):
                self.traffic[4].append(input)
                self.traffic[4].sort(key = lambda x:x.clock_cycle)
            if(input.source=="6"):
                self.traffic[5].append(input)
                self.traffic[5].sort(key = lambda x:x.clock_cycle)
            if(input.source=="7"):
                self.traffic[6].append(input)
                self.traffic[6].sort(key = lambda x:x.clock_cycle)
            if(input.source=="8"):
                self.traffic[7].append(input)
                self.traffic[7].sort(key = lambda x:x.clock_cycle)
            if(input.source=="9"):
                self.traffic[8].append(input)
                self.traffic[8].sort(key = lambda x:x.clock_cycle)
            index+=1

    def find_instructions(self, clock_cycle):
        list = []
        if len(self.traffic[0])>0 and int(self.traffic[0][0].clock_cycle) == clock_cycle:
            list.append(self.traffic[0][0])
            self.traffic[0].pop(0)
        if len(self.traffic[1])>0 and int(self.traffic[1][0].clock_cycle)  == clock_cycle:
            list.append(self.traffic[1][0])
            self.traffic[1].pop(0)
        if len(self.traffic[2])>0 and int(self.traffic[2][0].clock_cycle)  == clock_cycle:
            list.append(self.traffic[2][0])
            self.traffic[2].pop(0)
        if len(self.traffic[3])>0 and int(self.traffic[3][0].clock_cycle)  == clock_cycle:
            list.append(self.traffic[3][0])
            self.traffic[3].pop(0)
        if len(self.traffic[4])>0 and int(self.traffic[4][0].clock_cycle) == clock_cycle:
            list.append(self.traffic[4][0])
            self.traffic[4].pop(0)
        if len(self.traffic[5])>0 and int(self.traffic[5][0].clock_cycle)  == clock_cycle:
            list.append(self.traffic[5][0])
            self.traffic[5].pop(0)
        if len(self.traffic[6])>0 and int(self.traffic[6][0].clock_cycle)  == clock_cycle:
            list.append(self.traffic[6][0])
            self.traffic[6].pop(0)
        if len(self.traffic[7])>0 and int(self.traffic[7][0].clock_cycle)  == clock_cycle:
            list.append(self.traffic[7][0])
            self.traffic[7].pop(0)
        if len(self.traffic[8])>0 and int(self.traffic[8][0].clock_cycle)  == clock_cycle:
            list.append(self.traffic[8][0])
            self.traffic[8].pop(0)
        return list
    
    def stage(self,rout,pvs_pva):
        clk_total = self.clk1
        queue = []
        dup_queue = []
        routing = rout
        self.add_instruction(list_of_instructions, routing,pvs_pva)

        for clock_cycle in range(clk_total):
            global delay_now            
            delay_now += delay_max
            queue = dup_queue.copy()
            x = self.find_instructions(clock_cycle)
            if len(x) > 0:
                for i in x:
                    queue.append(i)
            # print("clock cycle = ", clock_cycle, len(queue))
            
            for instruction in queue:
                
                # for i in queue:
                #     for j in range(len(i.route)):
                #         print(j,i.route[j].name,i.route[j].current_element)
                #     print("")
                dup_queue = queue.copy()
                if len(instruction.route) > 1 :
                    if(instruction.start_time==-1):
                        instruction.start_time=delay_now
                    instruction.route[0].update(instruction, clock_cycle,instruction.name, instruction.route[0], instruction.route[1],delay_now-instruction.start_time+delay_max)
                    if instruction.route[0].current_element==2 :
                        instruction.route.pop(0)
                        if len(instruction.route) == 1 and instruction.name==" Tail " :
                            key=str(instruction.source)+"-"+str(instruction.destination)
                            if pvs_pva==0:
                                latency_1[key]=delay_now-instruction.start_time+delay_max+instruction.tail_head_diff*delay_max
                            elif pvs_pva==1:
                                latency_2[key]=delay_now-instruction.start_time+delay_max+instruction.tail_head_diff*delay_max

           
print("enter the routing mode:(XY routing->1 , YX routing->2)")
rout=int(input())
n1 = NoC()
p1 = n1.stage(rout,0)
pelinks_pva=pelinks
links_pva=links
pelinks=[0 for i in range(9)]
links=[0 for i in range(12)]
n2 = NoC()
p2 = n2.stage(rout,1)
print(pelinks)
print(links)
print(latency_1)
print(latency_2)
link_names=["1-pe","2-pe","3-pe","4-pe","5-pe","6-pe","7-pe","8-pe","9-pe","1-2","2-3","3-4","4-9","8-9","7-8","6-7","1-6","5-2","5-4","5-8","5-6"]
new=pelinks_pva
new.extend(links_pva)
plt.subplot(221)
plt.bar(link_names,new, color='skyblue')
plt.title(f"graph 1 for PVA mode")
plt.xlabel("links")
plt.ylabel("no: of flits sent")
plt.tight_layout()
new=pelinks
new.extend(links)
plt.subplot(222)
plt.bar(link_names,new, color='blue')
plt.title(f"graph 1 for PVS mode")
plt.xlabel("links")
plt.ylabel("no: of flits sent")
plt.subplot(223)
plt.bar(latency_1.keys(),latency_1.values(), color='skyblue')
plt.title(f"graph 2 for PVA mode")
plt.xlabel("packets ")
plt.ylabel("latencies")
plt.subplot(224)
plt.bar(latency_2.keys(),latency_2.values(), color='blue')
plt.title(f"graph 2 for PVS mode")
plt.xlabel("packets ")
plt.ylabel("latencies")
plt.tight_layout()
plt.show()
