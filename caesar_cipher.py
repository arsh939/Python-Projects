def encypt_func(txt, s):  
    result = ""  
  
    for i in range(len(txt)):  
        char = txt[i]  
        if (char.isupper()):  
            result += chr((ord(char) + s - 64) % 26 + 65)  
        else:  
            result += chr((ord(char) + s - 96) % 26 + 97)  
    return result  

txt = "python projects, @v-apor"  
s = 2  
  
print("Plain txt : " + txt)  
print("Shift pattern : " + str(s))  
print("Cipher: " + encypt_func(txt, s))  
