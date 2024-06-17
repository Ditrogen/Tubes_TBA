def kataSubjek(kata)->bool:
    #Subjek = {"saya", "dia", "kamu", "kita", "kami"}
    stateSekarang = 0
    for huruf in kata:
        match stateSekarang:
            case -1: break
            case 0:
                if huruf == "s" : stateSekarang = 1
                elif huruf == "d" : stateSekarang = 5
                elif huruf == "k" : stateSekarang = 7
                else: stateSekarang = -1
            case 7:
                if huruf == "i" : stateSekarang = 12
                elif huruf == "a" :stateSekarang = 8
                else: stateSekarang = -1
            case 9:
                if huruf == "i" : stateSekarang = 10 #Final state
                elif huruf == "u" : stateSekarang = 11 #Final state
                else: stateSekarang = -1
            case 1: stateSekarang = 2 if huruf == "a" else -1
            case 2: stateSekarang = 3 if huruf == "y" else -1
            case 3: stateSekarang = 4 if huruf == "a" else -1 #Final state
            case 5: stateSekarang = 6 if huruf == "i" else -1
            case 6: stateSekarang = 4 if huruf == "a" else -1 #Final state
            case 8: stateSekarang = 9 if huruf == "m" else -1
            case 12: stateSekarang = 13 if huruf == "t" else -1
            case 13: stateSekarang = 4 if huruf == "a" else -1
            case _: stateSekarang = -1
    return stateSekarang == 4 or stateSekarang == 10 or stateSekarang == 11
            
def kataPredikat(kata)->bool:
    #Predikat = {"memakan", "meminum", "membuat", "melihat", "menulis"}
    stateS = 0
    for huruf in kata:
        match stateS:
            case -1: break
            case 0: stateS = 1 if huruf == "m" else -1
            case 1: stateS = 3 if huruf == "e" else -1
            case 3:
                if huruf == "m" : stateS = 2
                elif huruf == "l" : stateS = 8
                elif huruf == "n" :stateS = 4
                else: stateS = -1
            case 2:
                if huruf == "a" : stateS = 5
                elif huruf == "i" : stateS = 6
                elif huruf == "b" :stateS = 7
                else: stateS = -1
            case 5: stateS = 10 if huruf == "k" else -1
            case 10: stateS = 15 if huruf == "a" else -1
            case 15: stateS = 20 if huruf == "n" else -1
            case 6: stateS = 11 if huruf == "n" else -1
            case 11: stateS = 16 if huruf == "u" else -1
            case 16: stateS = 21 if huruf == "m" else -1
            case 7: stateS = 12 if huruf == "u" else -1
            case 12: stateS = 17 if huruf == "a" else -1
            case 17: stateS = 22 if huruf == "t" else -1
            case 8: stateS = 13 if huruf == "i" else -1
            case 13: stateS = 18 if huruf == "h" else -1
            case 18: stateS = 17 if huruf == "a" else -1
            case 4: stateS = 9 if huruf == "u" else -1
            case 9: stateS = 14 if huruf == "l" else -1
            case 14: stateS = 19 if huruf == "i" else -1
            case 19: stateS = 23 if huruf == "s" else -1
            case _: stateS = -1
    return stateS == 20 or stateS == 21 or stateS == 22 or stateS == 23

def kataObjek(kata)->bool:
    #Objek = {"mie", "air", "telur", "jus", "buku"}
    stateS = 0
    for huruf in kata:
        match stateS:
            case -1: break
            case 0:
                if huruf == "b" : stateS = 1
                elif huruf == "m" : stateS = 5
                elif huruf == "a" : stateS = 8
                elif huruf == "t" : stateS = 11
                elif huruf == "j" : stateS = 16
                else: stateS = -1
            case 1: stateS = 2 if huruf == "u" else -1
            case 2: stateS = 3 if huruf == "k" else -1
            case 3: stateS = 4 if huruf == "u" else -1
            case 5: stateS = 6 if huruf == "i" else -1
            case 6: stateS = 7 if huruf == "e" else -1
            case 8: stateS = 9 if huruf == "i" else -1
            case 9: stateS = 10 if huruf == "r" else -1
            case 11: stateS = 12 if huruf == "e" else -1
            case 12: stateS = 13 if huruf == "l" else -1
            case 13: stateS = 14 if huruf == "u" else -1
            case 14: stateS = 15 if huruf == "r" else -1
            case 16: stateS = 17 if huruf == "u" else -1
            case 17: stateS = 18 if huruf == "s" else -1
            case _: stateS = -1
    return stateS == 4 or stateS == 7 or stateS == 10 or stateS == 15 or stateS == 18

def kataKeterangan(kata)->bool:
    #Keterangan = {"di rumah", "di sekolah", "di kos", "di warteg", "di kamar"}
    stateS = 0
    for huruf in kata:
        match stateS:
            case -1: break
            case 0: stateS = 1 if huruf == "d" else -1
            case 1: stateS = 2 if huruf == "i" else -1
            case 2: stateS = 3 if huruf == " " else -1
            case 3:
                if huruf == "r" : stateS = 4
                elif huruf == "s" : stateS = 9
                elif huruf == "k" : stateS = 14
                elif huruf == "w" : stateS = 21
                else: stateS = -1
            case 4: stateS = 5 if huruf == "u" else -1
            case 5: stateS = 6 if huruf == "m" else -1
            case 6: stateS = 7 if huruf == "a" else -1
            case 7: stateS = 8 if huruf == "h" else -1
            case 9: stateS = 10 if huruf == "e" else -1
            case 10: stateS = 11 if huruf == "k" else -1
            case 11: stateS = 12 if huruf == "o" else -1
            case 12: stateS = 13 if huruf == "l" else -1
            case 13: stateS = 7 if huruf == "a" else -1
            case 14:
                if huruf == "o" : stateS = 15
                elif huruf == "a" : stateS = 17
                else: stateS = -1
            case 15: stateS = 16 if huruf == "s" else -1
            case 17: stateS = 18 if huruf == "m" else -1
            case 18: stateS = 19 if huruf == "a" else -1
            case 19: stateS = 20 if huruf == "r" else -1
            case 21: stateS = 22 if huruf == "a" else -1
            case 22: stateS = 23 if huruf == "r" else -1
            case 23: stateS = 24 if huruf == "t" else -1
            case 24: stateS = 25 if huruf == "e" else -1
            case 25: stateS = 26 if huruf == "g" else -1
            case _: stateS = -1
    return stateS == 8 or stateS == 16 or stateS == 20 or stateS == 26

def tokenizer(kata):
    try:
        if kataSubjek(kata): return "S"
        elif kataPredikat(kata): return "P"
        elif kataObjek(kata): return "O"
        elif kataKeterangan(kata): return "K"
        else: raise Exception("Token tidak dikenal")
    except Exception as e:
        print(f"ERROR: {e}")
        print(f"Kata \"{kata}\" tidak dikenali")
        return "ERROR"  

def parser(kalimat):
    strukturStack = []
    parseStack = []
    i = 0
    ERROR = Exception("Parse Error")

    temp = kalimat
    kalimat = kalimat.lower() #Menyeragamkan kalimat menjadi huruf kecil semua
    kalimat = kalimat.split() #Memisahkan kalimat menjadi kata-kata tersendiri

    #Jika jumlah kata lebih dari 3, maka gabungkan 2 kata terakhir menjadi 1 kesatuan
    if len(kalimat) > 4:
        kalimat[-2] = kalimat[-2] + " " + kalimat[-1]
        kalimat = kalimat[:-1]
    
    print(kalimat, len(kalimat))

    parseStack.append("#") #Akhir dari stack
    parseStack.append("Start") #Untuk memulai parsing
    kalimat.append("End")

    try:
        while parseStack[-1] != "#":
            print(parseStack)
            kata = kalimat[i]
            if kata != "End":
                token = tokenizer(kata)
            print(i, token)
            match parseStack[-1]:
                case "Start":
                    if token == "S":
                        parseStack.pop()
                        parseStack.append("Y")
                        parseStack.append("P")
                        parseStack.append("S")
                    else:
                        raise ERROR
                case "Y":
                    if kata == "End":
                        parseStack.pop()
                    else:
                        if token == "O":
                            parseStack.pop()
                            parseStack.append("Z")
                            parseStack.append("O")
                        elif token == "K":
                            parseStack.pop()
                            parseStack.append("Z")
                        else:
                            raise ERROR
                case "Z":
                    if kata == "End":
                        parseStack.pop()
                    elif token == "K":
                        parseStack.pop()
                        parseStack.append('K')
                    else: 
                        raise ERROR
                case "S":
                    if token == "S":
                        strukturStack.append(parseStack.pop())
                        i += 1
                    else: 
                        raise ERROR
                case "P":
                    if token == "P":
                        strukturStack.append(parseStack.pop())
                        i +=1
                    else: 
                        raise ERROR
                case "O":
                    if token == "O":
                        strukturStack.append(parseStack.pop())
                        i += 1
                    else: 
                        raise ERROR
                case "K":
                    if token == "K":
                        strukturStack.append(parseStack.pop())
                        i += 1
                    else: 
                        raise ERROR
                case _:
                    if token != "ERROR":
                        parseStack.pop()
                        i += 1
                    else: 
                        raise ERROR
        print()
        parseStack.pop()

        print("Struktur: ", end='')
        for struktur in strukturStack[:-1]:
            print(f"{struktur} - ", end='')
        print(strukturStack[-1], "\n")

        return True
    except Exception as e:
        print(f"ERROR: {e}")
        print(f"Kalimat \"{temp}\" tidak sesuai")
        return False

kalimat = input("Masukkan Kalimat: ")
if parser(kalimat):
    print(f"Kalimat \"{kalimat}\" diterima")
else:
    print(f"Kalimat \"{kalimat}\" ditolak")