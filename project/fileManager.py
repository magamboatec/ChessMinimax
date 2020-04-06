import re
class FileManager():
    # metodo para grabar un mapa en el file
    # E: el path del file, un string con el mensaje
    def save (file, message):
            fo = open(file, "w") #abre en forma de sobrrescribirlo, si no existe lo crea
            fo.write(message)
            fo.close()

    # metodo para read una file
    # E: el path del file
    # S: un string con el contenido del file
    def read (file):
            fo = open(file, "r") #abre en forma de solo lectura
            res = fo.read()
            fo.close()
            #retorna lo que leyo del file
            return res

    #load file
    #lee un file y hace las validaciones para colocarlo en la lista
    #salida: retorna una lista de lo leido
    def loadfile(file):
            strRes = read(file)
            if strRes != "":
                    return eval(strRes)
            else:
                    return []


    def convertPosCol(let):
        if let=="a":
            return 0
        elif let=='b':
            return 1
        elif let=="c":
            return 2
        elif let=="d":
            return 3
        elif let=="e":
            return 4
        elif let=="f":
            return 5
        elif let=="g":
            return 6
        elif let=="h":
            return 7
        
    def convertPosFil(num):
        if num=="1":
            return 7
        elif num=="2":
            return 6
        elif num=="3":
            return 5
        elif num=="4":
            return 4
        elif num=="5":
            return 3
        elif num=='6':
            return 2
        elif num=="7":
            return 1
        elif num=="8":
            return 0
    def getStartColor():
        strFile=FileManager.read("config.txt")
        listPos=strFile.split("\n")
        startColor=listPos[0]
        return startColor.split(" ")[1]
    
    def getAIColor():
        strFile=FileManager.read("config.txt")
        listPos=strFile.split("\n")
        startColor=listPos[1]
        return startColor.split(" ")[1]

    def getMatrix():
        strFile=FileManager.read("config.txt")
        listPos=strFile.split("\n")
        matrix=[["","","","","","","",""],
                ["","","","","","","",""],
                ["","","","","","","",""],
                ["","","","","","","",""],
                ["","","","","","","",""],
                ["","","","","","","",""],
                ["","","","","","","",""],
                ["","","","","","","",""]]
        pattern = re.compile("(N|B) .*")
        for i in listPos:
            match = re.search(pattern, i)
            if(match):
                pos = i.split(" ")
                x=FileManager.convertPosFil(pos[3])
                y=FileManager.convertPosCol(pos[2])
                matrix[x][y]=pos[0]+pos[1]
            
        return matrix
    

