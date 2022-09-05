class Kaser:
    
    def __init__(self, code) -> None:

        self.code = code
        
    def encode_by_offset(self, offset) -> None:

        decode = ''
        for ch in self.code:
            
            ascii_code = ord(ch)
            kaser_code = 1
            if ascii_code >= 97 and ascii_code <= 122:
                # xiaoxie 
                kaser_code = (ascii_code + offset) % 123
                if kaser_code < 97:
                    kaser_code = kaser_code + 97

            elif ascii_code >= 65 and ascii_code <= 90:
                # daxie 
                kaser_code = (ascii_code + offset) % 91
                if kaser_code < 65:
                    kaser_code = kaser_code + 65

            else:
                # else condition
                kaser_code = ascii_code

            decode += chr(kaser_code)

        print('offset:', offset, 'result:',decode)

    
    def encode_all(self) -> None:
        # endode by offset all
        for i in range(27):
            self.encode_by_offset(i)


if __name__ == '__main__':

    kaser = Kaser('abcde')
    kaser.encode_by_offset(1)

    kaser.encode_all()