import sys
sys.path.append('C:/Users/cobou/Documents/Python/adventOfCodeMisc/library')
from AoCLibrary import *

a = AdventInput("input16.txt")
real_inp = a.data

converts = {
    "0" : "0000",
"1" : "0001",
"2" : "0010",
"3" : "0011",
"4" : "0100",
"5" : "0101",
"6" : "0110",
"7" : "0111",
"8" : "1000",
"9" : "1001",
"A" : "1010",
"B" : "1011",
"C" : "1100",
"D" : "1101",
"E" : "1110",
"F" : "1111"
}

class Packet:
    def __init__(self, in_str="", as_bin=False) -> None:
        self.value = 0
        self.literal = 0
        self.version = 0
        self.type_id = None
        self.extra = ""
        self.children = []

        if not in_str or all(x == '0' for x in in_str):
            return
        if not as_bin:   
            new =""
            for i in range(len(in_str)):
                new += converts[in_str[i]]
            inp = new
        else:
            inp = in_str
        self.version = int(inp[:3], 2)
        self.type_id = int(inp[3:6], 2)
        self.inp = inp
        self.get_inside()
        self.get_literal()
    def __repr__(self) -> str:
        return f"{self.type_id=},{self.version=},{self.value=}"
    def get_inside(self):
        if self.type_id == 4:
            return
        #operator
        ltype = self.inp[6]
        if ltype =='0':
            #next 15 bits
            data = self.inp[7:7+15]
            length_in_bits = int(data, 2)
            self.total_children_length = length_in_bits
            
            remaining = self.inp[22:22+length_in_bits]
            # used = 0 
            times_run = 0
            while remaining:
                temp = Packet(remaining, True)
                self.children.append(temp)
                # used += len(remaining) - len(temp.extra)
                remaining = temp.extra
                times_run += 1
                # pritn(f"{times_run=}")

            all_packets.extend(self.children)
            self.extra = self.inp[22+length_in_bits:]

        elif ltype =='1':
            #next 11 bits
            data = self.inp[7:7+11]
            contains = int(data, 2)
            cur = self.inp[18:]
            self.num_children = contains
            used = 0
            for _ in range(contains):
                temp = Packet(cur, True)
                self.children.append(temp)
                cur = temp.extra
                used += len(cur)
            all_packets.extend(self.children)
            self.extra = cur
        else:
            assert False, ltype

        self.apply_operator()
        
    def apply_operator(self):
        match self.type_id:
            case 0:
                self.value = sum(x.value for x in self.children)
            case 1:
                self.value = prod(x.value for x in self.children)
            case 2:
                self.value = min(x.value for x in self.children)
            case 3:
                self.value = max(x.value for x in self.children)
            case 5:
                assert len(self.children) == 2
                self.value = int(self.children[0].value > self.children[1].value)
            case 6:
                assert len(self.children) == 2
                self.value = int(self.children[0].value < self.children[1].value)
            case 7:
                assert len(self.children) == 2
                self.value = int(self.children[0].value == self.children[1].value)
            case _:
                assert False


    def get_literal(self):
        if self.type_id != 4:
            return
        literal_val = self.inp[6:]
        groups4 = list(chunked((literal_val), 5))
        groups4 = list(split_after(groups4, lambda x: x[0] == '0'))[0]
        # groups4 = [x[0] for x in groups4]
        len_used = sum(len(x) for x in groups4)
        z = ["".join(x[1:]) for x in groups4]
        val = "".join(z)
        self.value = int(val, 2)
        self.extra = self.inp[len_used+6:]

all_packets = []

all_packets.append(Packet("8A004A801A8002F478"))
assert (sum(x.version for x in all_packets)) == 16
all_packets.clear()
all_packets.append(Packet("620080001611562C8802118E34"))
assert (sum(x.version for x in all_packets)) == 12
all_packets.clear()
all_packets.append(Packet("C0015000016115A2E0802F182340"))
assert (sum(x.version for x in all_packets)) == 23
all_packets.clear()
all_packets.append(Packet("A0016C880162017C3686B18A3D4780"))
assert (sum(x.version for x in all_packets)) == 31
all_packets.clear()

all_packets.append(Packet(a.data))
ans(sum(x.version for x in all_packets))
all_packets.clear()

assert Packet("C200B40A82").value == 3
assert Packet("04005AC33890").value == 54
assert Packet("880086C3E88112").value == 7
assert Packet("CE00C43D881120").value == 9
assert Packet("D8005AC2A8F0").value == 1
assert Packet("F600BC2D8F").value == 0
assert Packet("D2FE28").value == 2021
assert Packet("9C0141080250320F1802104A08").value == 1

ans(Packet(a.data).value)