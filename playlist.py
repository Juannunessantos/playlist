#playlist compartilhada
usuário1="clauber"#conta usuário principal
usuário2="professor"#conta secundária
op=str(input("digite o Nick name da sua conta:")).lower()
if op==usuário1:
    print()
    print(f"bem vindo a sua conta,{op}\nvocê está logada na conta(usuário1)")
    
elif op==usuário2:
        print()
        print(f"bem vindo a sua conta,{op}\nvocê está logada na conta(usuário2)")

else:
    print ()
    print(f"essa conta {op},não existe\nVerifique se está escrito corretamente")
    exit()
    #fase de cadastro completa.

 #segunda fase
    
playlist1=[]
playlistConjunta=[]
playlist2=[]    
while True :
           op2=int(input("\n1.cadastrar música \n2.filtrar por inicial \n3.filtrar por cantor \n4.filtrar por genero \n5.ver playlist \n6.sair\n\n"))
           if op2==1:
               nome=str(input("qual o nome da música:")).lower()
               cantor=str(input("qual o nome do cantor:")).lower()
               genero=str(input("qual o gênero da música:")).lower()
               inicial=nome[0]
               conjunto={"nome":nome,"cantor": cantor,"genero":genero,"inicial":inicial}
               if op==usuário1:
                   playlist1.append(conjunto)
                   print()
                   print("musica adicionada a playlist1")
                   conta=int(input("deseja adicionar a música a playlistConjunta:\n1.sim\n2.nao\n"))
                   if conta==1:
                       playlistConjunta.append(conjunto)
                       print()
                       print(f"você adicionou a {nome} a playlistConjunta")
                   elif conta==2:
                       print("você n adicionou a música")
                   else:
                       print("erro!!!!")
               elif op==usuário2:
                   playlist2.append(conjunto)
                   print()
                   print("música adicionada a playlist2")
                   conta=int(input("deseja adicionar a música a playlistConjunta:\n1.sim\n2.nao\n"))
                   if conta==1:
                       playlistConjunta.append(conjunto)
                       print()
                       print(f"você adicionou a {nome} a playlistConjunta")
                   elif conta==2:
                       print("você n adicionou a música")
                   else:
                       print("erro!!!!")
           #terceira fase
           elif op2==2:
               filtro=str(input ("digite a inicial que deseja buscar:"))
               
               if op==usuário1:
                   for name in playlist1:
                       if name["inicial"]==filtro:
                           print()
                           print(f"músicas encontradas:{name}")
                           
               elif op==usuário2:
                   for name in playlist2:
                       if name["inicial"]==filtro:
                           print()
                           print(f"músicas encontradas:{name}")
                           
               op3=int(input ("deseja procurar na sua playlistConjunta:\n1.sim\n2.nao\n"))         
               if op3==1:
                           for name in playlistConjunta:
                               if name["inicial"]==filtro:
                                   print()
                                   print(f"músicas encontradas:{name}")
               elif op2==2:
                           print()
                           print("ta bem")
               else:
                      print("erro")
           #quarta fase
           elif op2==3:
               filtro=str(input ("digite o cantor que deseja buscar:"))
               
               if op==usuário1:
                   for name in playlist1:
                       if name["cantor"]==filtro:
                           print()
                           print(f"músicas encontradas:{name}")
                           
               elif op==usuário2:
                   for name in playlist2:
                       if name["cantor"]==filtro:
                           print()
                           print(f"músicas encontradas:{name}")
                           
               op3=int(input ("deseja procurar na sua playlistConjunta:\n1.sim\n2.nao\n"))         
               if op3==1:
                           for name in playlistConjunta:
                               if name["cantor"]==filtro:
                                   print()
                                   print(f"músicas encontradas:{name}")
               elif op2==2:
                           print()
                           print("ta bem")
               else:
                      print("erro")
           #quinta fase
           elif op2==4:
               filtro=str(input ("digite o generl que deseja buscar:"))
               
               if op==usuário1:
                   for name in playlist1:
                       if name["genero"]==filtro:
                           print()
                           print(f"músicas encontradas:{name}")
                           
               elif op==usuário2:
                   for name in playlist2:
                       if name["genero"]==filtro:
                           print()
                           print(f"músicas encontradas:{name}")
                           
               op3=int(input ("deseja procurar na sua playlistConjunta:\n1.sim\n2.nao\n"))         
               if op3==1:
                           for name in playlistConjunta:
                                if name["genero"]==filtro:
                                   print()
                                   print(f"músicas encontradas:{name}")
               elif op2==2:
                           print()
                           print("ta bem")
               else:
                      print("erro")  
           #ultima fase             
           elif op2==5:
                  if op==usuário1:
                      print()
                      print("playlist1",playlist1)
                      
                  elif op==usuário2:
                      print()
                      print("playlist2",playlist2)
                      
                  list=int(input ("deseja ver a playlistConjunta:\n1.sim\n2.nao\n\n"))
                  if list==1:
                      print()
                      print("playlistConjunta",playlistConjunta)
                  elif list==2:
                      print()
                      print("tá bom")
                  else :
                      print()
                      print("erro!!")
           #fim
           elif op2==6:
               print("você saiu")
               break
           else :
               print("erro")
