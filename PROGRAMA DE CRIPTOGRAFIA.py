# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 17:50:42 2019

@author: Bruno Felipe
"""
#Programa RSA definido em Classe
class Cliente(object):
     def setup(n=None, e=None, d=None):
       #Gerador do conjunto de números primos de interesse (com limites superior e inferior), foi adotado valores pequenos (maior abrangência, aleterar o limite superior, o inferior foi adorado 13 para garantir todas as condições de entrada do teclado). 
       def primos(inf=13,lim=99):
        conjpr=[]
        cont=0
        for num in range(inf,lim+1):
            for div in range(1,num+1):
                if num%div==0:
                    cont=cont+1
            if cont==2:
                conjpr.append(num)
            cont=0
        return(conjpr)
       conjpr=primos()
       #importar a biblioteca dos valores aleatórios(usar o randint, já que retorna valores inteiros aleatórios dentro de um intervalor)    
       import random
       #Verificar se argumentos foi digitado ou não no setup()
       if n!=None and e!=None and d!=None:
           n=str(n)
           d=str(d)
           e=str(e)
           #Verificar se os argumentos são algum dado numérico:
           if n.isnumeric() and e.isnumeric() and d.isnumeric():
               #Argumentos digitados pelo usuário:
                n=int(n)
                d=int(d)
                e=int(e)
               #Verificar se os dados introduzido pelo usuário é codificável e descodificável.
                A='se não obter essa STRING, então a chave digitada estará errada'
                B=[]
                for i in range(len(A)):
                   B.append(A[i])
                for i in range(len(B)):
                    B[i]=ord(B[i])
                codif=[]
                for i in range(len(B)):
                    codif.append((int(B[i])**e)%n)
                decodif=[]
                for i in range(len(codif)):
                    decodif.append((int(codif[i])**d%n))
                vetS=[]
                for i in range(len(decodif)):
                    vetS.append(chr(decodif[i]))
                C=''
                for i in range(len(decodif)):
                    C=C+vetS[i]
                if A==C:
                    #Chave Global
                    ch=(n,d)
                    #Chave Pública
                    chpul=(n,e)
                    return(chpul,ch)
                else:
                    print('Os parâmetros n,e,d não consistem em uma chave correta de codificação e decodificação. Por favor, verificar os dados da sua chave pública e privada.')
                    return(False)
           else:
                print('Argumentos inválidos.')
                return(False)
       #Condição do usuário querer gerar aleatoriamente da chave:             
       elif n==None and e==None and d==None:
            #Obtenção aleatória da chave pública e privada:
            #Expoente Adotado
            exp=primos(3,10)
            e=exp[random.randint(0,len(exp)-1)]
            #Gerar um número primo p e (p-1) não múltiplo do expoente
            cond=False
            k=random.randint(0,len(conjpr)-1)
            while cond==False:
                p=conjpr[k]
                if (p-1)%e==0:
                    cond==False
                    k=random.randint(0,len(conjpr)-1)
                else:
                    cond=True
            cond=False
            #Gerar um número primo q, distinto de p e (q-1) não múltiplo do expoente 
            k=random.randint(0,len(conjpr)-1)
            while cond==False:
              k=random.randint(0,len(conjpr)-1)
              q=conjpr[k]
              if (q-1)%e==0:
                  cond=False
              elif (q-1)%e!=0 and p!=q:
                  cond=True
            #Obtenção da chave pública n
            n=p*q
            #Obtenção do inverso multiplicativo:
            mod=(p-1)*(q-1)
            d=2
            while (e*d)%mod!=1:
                d=d+1
            #Fornecendo a tupla da chave pública
            chpul=(n,e)
            #chaveglobal
            ch=(n,d)
            return(chpul,ch)
       else:
           print('Argumentos inválidos.')
           return(False)
#----------------------------------------------------------------------------------------
     #Somente entrar com a chave pública
     def encrypt(S,chpul):
        #transformar os dados de strings em um vetor:
        vetS=[]
        for i in range(len(S)):
            vetS.append(S[i])
        #converter os elementos da lista em UTF-8 (comando ord) - precodificação
        precod=[]
        for i in range(len(vetS)):
            precod.append(int(ord(vetS[i])))
        #codificação dos elementos da lista pelo vetor associado
        codif=[]
        for i in range(len(precod)):
            codif.append((int(precod[i])**int(chpul[1]))%int(chpul[0]))
        #retornar a string codificada
        s=''
        for i in range(len(codif)):
            s=s+' '+str(codif[i])
        return(s)
#-----------------------------------------------------------------------------------------
    #Somente entrar com a chave privada
     def decrypt(s,chpriv):
        #precodificar os elementos da tupla de UTF-8 para números representativos:
        s=s.split()
        predecod=[]
        for i in range(len(s)):
            predecod.append(int(s[i])**int(chpriv[1])%int(chpriv[0]))
        #Decodificar os números referentes ao UTF-8 em caracteres:
        decodif=[]
        for i in range(len(predecod)):
            decodif.append(chr(predecod[i]))
        S=''
        #Retornar a string inicial:
        for i in range(len(decodif)):
            S=S+decodif[i]
        return(S)
#------------------------------------------------------------------------------------------------------
     import os.path
     condArq=False
     if os.path.isfile('C:/Users/Public/usuarios.txt'):
         condArq=True
         arq = open('C:/Users/Public/usuarios.txt', 'r')
         text = arq.readlines()
         if text==[]:
             condArq=False
     else:
         condArq=False
     if condArq==False:
        chave=setup()
        chavepublica=chave[0]
        chaveprivada=chave[1]
        dados=[]
        dados.append(chavepublica)
        dados.append(chaveprivada)
     if condArq==True:
         arq = open('C:/Users/Public/usuarios.txt', 'r')
         text = arq.readlines()
         for linha in text :
             print(linha)
         arq.close()
         pul=text[0].rstrip('\n')
         priv=text[1].rstrip('\n')
         dados=[]
         for i in range(len(text)):
             dados.append(text[i].rstrip('\n'))
         for i in range(len(pul)):
             if pul[i]=='(':
                 pos1=i
             if pul[i]==')':
                 pos2=i
             if pul[i]==',':
                 pos3=i
         pullist=''
         for i in range(len(pul)):
             if i!=pos1 and i!=pos2 and i!=pos3:
                 pullist=pullist+pul[i]
         for i in range(len(priv)):
             if priv[i]=='(':
                 pos1=i
             if priv[i]==')':
                 pos2=i
             if priv[i]==',':
                 pos3=i
         privlist=''
         for i in range(len(priv)):
             if i!=pos1 and i!=pos2 and i!=pos3:
                 privlist=privlist+priv[i]
         pullist=pullist.split()
         privlist=privlist.split()
         chavepublica=(int(pullist[0]),int(pullist[1]))
         chaveprivada=(int(privlist[0]),int(privlist[1]))
         dados[0]=chavepublica
         dados[1]=chaveprivada
     for i in range(len(dados)):
         if i>1:
             dados[i]=decrypt(dados[i],chaveprivada)
#--------------------------------------------------------------------------------------------------------
     print('')
#--------------------------------------------------------------------------------------------------------
     cond=False
     while cond==False:
        print('')
        print('selecione uma das seguintes opções: ')
        print('* digite 0 para sair do programa: ')
        print('* digite 1 para adição de usuários: ')
        print('* digite 2 para delação de usuários: ')
        print('* digite 3 para verificar existência de usuários: ')
        opcao=input('entre com a opção desejada: ')
        if opcao.isnumeric():
            opcao=int(opcao)
            #OPÇÃO DE SAIR DO PROGRAMA
            if opcao==0:
                cond=True
                arq = open('C:/Users/Public/usuarios.txt', 'w')
                usuarios = []
                cript=[]
                for i in range(len(dados)):
                    if i>1:
                        cript.append(encrypt(dados[i],dados[0]))
                    else:
                        cript.append(dados[i])
                for i in range(len(cript)):
                    usuarios.append('{}\n'.format(cript[i]))
                arq.writelines(usuarios)
                arq.close()
                break
            #OPÇÃO DE INSERIR USUÁRIOS:
            elif opcao==1:
                cond=False
                N=input('quantos usuários você deseja adicionar (caso não queira, digite 0)? digite a quantidade: ')
                if N.isnumeric():
                    if int(N)>=0:
                        for i in range(int(N)):
                            dados.append(input('digite o nome do usuário: '))
                            dados.append(input('digite a senha: '))
                    else:
                        print('entrada Inválida')
                else:
                    print('entrada Inválida')
            #OPÇÃO DE DELETAR USUÁRIOS:
            elif opcao==2:
                cond=False
                cond2=False
                print('')
                delet=input('digite o nome do usuário a ser apagado: ')
                for i in range(len(dados)):
                    if dados[i]==delet:
                        pos=i
                        cond2=True
                        break
                del dados[pos]
                del dados[pos]
                if cond2==True:
                    print('')
                    print('usuário apagado.')
                else:
                    print('')
                    print('usuário não existente.')
            #OPÇÃO DE PROCURA DE DADOS DE USUÁRIOS:
            elif opcao==3:
                cond==False
                cond3=False
                proc=input('digite o nome do usuário a ser procurado: ')
                for i in range(len(dados)):
                    if dados[i]==proc:
                        cond3=True
                        break
                if cond3==True:
                    print('')
                    print('usuário existe.')
                else:
                    print('')
                    print('usuário não existente.')
            else:
                print('opção Inválida! Digite uma opção válida.')
        else:
            print('opção Inválida! Digite uma opção válida.')
        