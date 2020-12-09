# Goncalo Botelho Mateus, 99225
def eh_tabuleiro(tab):
    # eh_tabuleiro: universal -> booleano
    """
    A funcao recebe um argumento de qualquer tipo e devolve True se for um
    tabuleiro e False caso contrario, sem nunca gerar erros.
    """
    if type(tab) is tuple and len(tab) == 3:
        for tup in tab:
            if type(tup) is tuple and len(tup) == 3:
                for elem in tup:
                    if not (type(elem) == int and -1 <= elem <= 1):
                        return False
            else:
                return False
    else:
        return False
    return True


def eh_posicao(pos):
    # eh_posicao: universal -> booleano
    """
    A funcao recebe um argumento de qualquer tipo e devolve True se for uma
    posicao e False caso contrario, sem nunca gerar erros.
    """
    return type(pos) == int and 1 <= pos <= 9


def obter_coluna(tab, num):
    # obter_coluna: tabuleiro x inteiro -> vector
    """
    A funcao recebe um tabuleiro e um inteiro que representa o numero
    da coluna e devolve um vector com os valores da respetiva coluna.
    Se um dos argumentos for invalido gera um erro.
    """
    if eh_tabuleiro(tab) and type(num) is int and 1 <= num <= 3:
        coluna = ()
        for tup in tab:
            coluna += (tup[num - 1],)
    else:
        raise ValueError("obter_coluna: algum dos argumentos e invalido")
    return coluna


def obter_linha(tab, num):
    # obter_linha: tabuleiro x inteiro -> vector
    """
    A funcao recebe um tabuleiro e um inteiro que representa o numero
    da linha e devolve um vector com os valores da respetiva linha.
    Se um dos argumentos for invalido gera um erro.
    """
    if eh_tabuleiro(tab) and type(num) is int and 1 <= num <= 3:
        linha = tab[num - 1]
    else:
        raise ValueError("obter_linha: algum dos argumentos e invalido")
    return linha


def obter_diagonal(tab, num):
    # obter_diagonal: tabuleiro x inteiro -> vector
    """
    A funcao recebe um tabuleiro e um inteiro que representa o numero
    da diagonal e devolve um vector com os valores da respetiva diagonal.
    Se um dos argumentos for invalido gera um erro.
    """
    if eh_tabuleiro(tab) and type(num) is int and 1 <= num <= 2:
        diag = ()
        if num == 1:
            for i in range(3):
                diag += (tab[i][i],)
        else:
            for i in range(2, -1, -1):  # i vai tomar os valores de 2, 1, 0.
                diag += (tab[i][-i - 1],)
                # tab[2][-3] = pos 7, tab[1][-2] = pos 5, tab[0][-1] = pos 3
    else:
        raise ValueError("obter_diagonal: algum dos argumentos e invalido")
    return diag


def tabuleiro_str(tab):
    # tabuleiro_str: tabuleiro -> cad. carateres
    """
    A funcao recebe um tabuleiro e devolve uma cadeia de caracteres que
    o representa.
    Se o argumento for invalido gera um erro.
    """
    if eh_tabuleiro(tab):
        tab_simb = ()
        # transforma os numeros no tabuleiro nos respetivos simbolos
        for tup in tab:
            for elem in tup:
                if elem == -1:
                    tab_simb += ("O",)
                elif elem == 1:
                    tab_simb += ("X",)
                else:
                    tab_simb += (" ",)
    else:
        raise ValueError("tabuleiro_str: o argumento e invalido")
    return " " + tab_simb[0] + " | " + tab_simb[1] + " | " + tab_simb[2] + \
           " \n-----------\n" + \
           " " + tab_simb[3] + " | " + tab_simb[4] + " | " + tab_simb[5] + \
           " \n-----------\n" + \
           " " + tab_simb[6] + " | " + tab_simb[7] + " | " + tab_simb[8] + " "


def junta_tab(tab):
    # junta_tab: tabuleiro -> tuplo
    """
    A funcao recebe um tabuleiro e devolve um tuplo contendo os 9 valores
    inteiros do respetivo tabuleiro, a funcao transforma um tuplo com 3 tuplos
    (tabuleiro) num tuplo com 9 valores.
    """
    if eh_tabuleiro(tab):
        tab_junto = ()
        for i in range(3):
            tab_junto += tab[i]
    return tab_junto


def eh_posicao_livre(tab, pos):
    # eh_posicao_livre: tabuleiro x posicao -> booleano
    """
    A funcao recebe um tabuleiro uma posicao e devolve True se corresponder
    a uma posicao livre ou False, caso contrario.
    Se um dos argumentos for invalido gera um erro.
    """
    if eh_tabuleiro(tab) and eh_posicao(pos):
        tab_junto = junta_tab(tab)
        return tab_junto[pos - 1] == 0
    else:
        raise ValueError("eh_posicao_livre: algum dos argumentos e invalido")


def obter_posicoes_livres(tab):
    # obter_posicoes_livres: tabuleiro -> vector
    """
    A funcao recebe um tabuleiro e devolve um vetor com as posicoes livres
    do respetivo tabuleiro.
    Se o argumento for invalido gera um erro.
    """
    pos_livres = ()
    if eh_tabuleiro(tab):
        tab_junto = junta_tab(tab)
        for pos in range(9):
            if tab_junto[pos] == 0:
                pos_livres += (pos + 1,)
    else:
        raise ValueError("obter_posicoes_livres: o argumento e invalido")
    return pos_livres


def jogador_ganhador(tab):
    # jogador_ganhador: tabuleiro -> inteiro
    """
    A funcao recebe um tabuleiro e devolve um inteiro que representa
    o vencedor do jogo (1: 'X', -1: 'O').
    Se o argumento for invalido gera um erro.
    """
    if eh_tabuleiro(tab):
        for i in range(1, 4):  # linha1 - linha 3
            linha = obter_linha(tab, i)
            if linha == (1, 1, 1):
                return 1
            if linha == (-1, -1, -1):
                return -1
            coluna = obter_coluna(tab, i)
            if coluna == (1, 1, 1):
                return 1
            if coluna == (-1, -1, -1):
                return -1
        for k in range(1, 3):  # diagonal 1 - diagonal 2
            diagonal = obter_diagonal(tab, k)
            if diagonal == (1, 1, 1):
                return 1
            if diagonal == (-1, -1, -1):
                return -1
        return 0  # enquanto ou se nao houver nenhum vencedor, retorna 0
    else:
        raise ValueError("jogador_ganhador: o argumento e invalido")


def eh_jogador(num):
    # eh_jogador: inteiro -> booleano
    """
    A funcao recebe um inteiro e devolve True se for um jogador e False, caso
    contrario.
    """
    return type(num) == int and (num == 1 or num == -1)


def separar(tup):
    # separar: tuplo -> tabuleiro
    """
    A funcao recebe um tuplo contendo 9 valores inteiros e devolve o
    respetivo tabuleiro.
    """
    # divisao do tuplo em 3 tuplos
    tab = ()
    tup1 = ()
    for i in range(3):
        tup1 += (tup[i],)
    tab += (tup1,)
    tup2 = ()
    for j in range(3, 6):
        tup2 += (tup[j],)
    tab += (tup2,)
    tup3 = ()
    for k in range(6, 9):
        tup3 += (tup[k],)
    tab += (tup3,)  # juncao dos 3 tuplos para formar o tabuleiro
    return tab


def marcar_posicao(tab, num, pos):
    # marcar_posicao: tabuleiro x inteiro x posicao -> tabuleiro
    """
    A funcao recebe um tabuleiro, um inteiro que representa um jogador
    (1: 'X', -1: 'O') e uma posicao livre e devolve um tabuleiro atualizado
    com a marca do jogador nessa posicao.
    Se um dos argumentos for invalido gera um erro.
    """
    if (eh_tabuleiro(tab) and eh_jogador(num) and eh_posicao(pos)
            and eh_posicao_livre(tab, pos)):
        tab_junto = junta_tab(tab)
        tup = ()
        # cpia o tabuleiro original ate a posicao dada como argumento
        for i in range(pos - 1):
            tup += (tab_junto[i],)
        # adicao do novo inteiro na posicao desejada
        tup += (num,)
        # copia o resto do tabuleiro original
        for j in range(pos, 9):
            tup += (tab_junto[j],)
        tab_novo = separar(tup)
    else:
        raise ValueError("marcar_posicao: algum dos argumentos e invalido")
    return tab_novo


def escolher_posicao_manual(tab):
    # escolher_posicao_manual: tabuleiro -> posicao
    """
    A funcao recebe um tabuleiro como argumento e le uma posicao introduzida
    pelo jogador e devolve esta memsma posicao.
    Se o argumento ou a posicao introduzida for invalida gera um erro.
    """
    if eh_tabuleiro(tab):
        pos_livre = int(input("Turno do jogador. Escolha uma posicao livre: "))
        if eh_posicao(pos_livre) and eh_posicao_livre(tab, pos_livre):
            return pos_livre
        else:
            raise ValueError("escolher_posicao_manual: a posicao introduzida "
                             "e invalida")
    else:
        raise ValueError("escolher_posicao_manual: o argumento e invalido")


def pos_iguais(tab, pos1, pos2, num):
    # pos_iguais: tabuleiro x posicao x posicao x inteiro -> booleano
    """
    A funcao recebe um tabuleiro, duas posicoes e um inteiro que representa um
    jogador (1: 'X', -1: 'O') e devolve True se as posicoes forem iguais e
    False, caso contrario.
    """
    tab_junto = junta_tab(tab)
    return tab_junto[pos1] == tab_junto[pos2] == num


def vitoria(tab, num):
    # vitoria: tabuleiro x inteiro -> posicao
    """
    A funcao recebe um tabuleiro e um inteiro que representa um jogador
    (1: 'X', -1: 'O') e devolve uma posicao livre caso o jogador tenha
    duas das suas pecas e uma posicao livre na mesma linha.
    """
    livre = obter_posicoes_livres(tab)
    for pos in livre:
        # verifica se as pecas em linha (linha, coluna, diagonal) a volta
        # das posicoes livres sao suas.
        if pos == 1:
            if (pos_iguais(tab, 1, 2, num) or pos_iguais(tab, 3, 6, num)
                    or pos_iguais(tab, 4, 8, num)):
                return pos
        if pos == 2:
            if pos_iguais(tab, 0, 2, num) or pos_iguais(tab, 4, 7, num):
                return pos
        if pos == 3:
            if (pos_iguais(tab, 0, 1, num) or pos_iguais(tab, 4, 6, num)
                    or pos_iguais(tab, 5, 8, num)):
                return pos
        if pos == 4:
            if pos_iguais(tab, 0, 6, num) or pos_iguais(tab, 4, 5, num):
                return pos
        if pos == 5:
            if (pos_iguais(tab, 0, 8, num) or pos_iguais(tab, 1, 7, num)
                    or pos_iguais(tab, 2, 6, num)
                    or pos_iguais(tab, 3, 5, num)):
                return pos
        if pos == 6:
            if pos_iguais(tab, 2, 8, num) or pos_iguais(tab, 3, 4, num):
                return pos
        if pos == 7:
            if (pos_iguais(tab, 0, 3, num) or pos_iguais(tab, 4, 2, num)
                    or pos_iguais(tab, 7, 8, num)):
                return pos
        if pos == 8:
            if pos_iguais(tab, 1, 4, num) or pos_iguais(tab, 6, 8, num):
                return pos
        if pos == 9:
            if (pos_iguais(tab, 2, 5, num) or pos_iguais(tab, 4, 0, num)
                    or pos_iguais(tab, 6, 7, num)):
                return pos


def pos_iguais_adv(tab, pos1, pos2, num):
    # pos_iguais_adv: tabuleiro x posicao x posicao x inteiro -> booleano
    """
    A funcao recebe um tabuleiro, duas posicoes e um inteiro que representa um
    jogador (1: 'X', -1: 'O') e devolve True se as posicoes forem iguais e
    tenham a marca do seu adversario e False, caso contrario.
    """
    tab_junto = junta_tab(tab)
    if num == -1:
        return tab_junto[pos1] == tab_junto[pos2] == 1
    else:
        return tab_junto[pos1] == tab_junto[pos2] == -1


def bloqueio(tab, num):
    # bloqueio: tabuleiro x inteiro -> posicao
    """
    A funcao recebe um tabuleiro e um inteiro que representa um jogador
    (1: 'X', -1: 'O') e devolve uma posicao livre caso o adversario tenha
    duas das suas pecas e uma posicao livre na mesma linha.
    """
    livre = obter_posicoes_livres(tab)
    for pos in livre:
        # verifica se as pecas em linha (linha, coluna, diagonal) a volta
        # das posicoes livres sao do seu adversario.
        if pos == 1:
            if (pos_iguais_adv(tab, 1, 2, num) or pos_iguais_adv(tab, 3, 6, num)
                    or pos_iguais_adv(tab, 4, 8, num)):
                return pos
        if pos == 2:
            if pos_iguais_adv(tab, 0, 2, num) or pos_iguais_adv(tab, 4, 7, num):
                return pos
        if pos == 3:
            if (pos_iguais_adv(tab, 0, 1, num) or pos_iguais_adv(tab, 4, 6, num)
                    or pos_iguais_adv(tab, 5, 8, num)):
                return pos
        if pos == 4:
            if pos_iguais_adv(tab, 0, 6, num) or pos_iguais_adv(tab, 4, 5, num):
                return pos
        if pos == 5:
            if (pos_iguais_adv(tab, 0, 8, num) or pos_iguais_adv(tab, 1, 7, num)
                    or pos_iguais_adv(tab, 2, 6, num)
                    or pos_iguais_adv(tab, 3, 5, num)):
                return pos
        if pos == 6:
            if pos_iguais_adv(tab, 2, 8, num) or pos_iguais_adv(tab, 3, 4, num):
                return pos
        if pos == 7:
            if (pos_iguais_adv(tab, 0, 3, num) or pos_iguais_adv(tab, 4, 2, num)
                    or pos_iguais_adv(tab, 7, 8, num)):
                return pos
        if pos == 8:
            if pos_iguais_adv(tab, 1, 4, num) or pos_iguais_adv(tab, 6, 8, num):
                return pos
        if pos == 9:
            if (pos_iguais_adv(tab, 2, 5, num) or pos_iguais_adv(tab, 4, 0, num)
                    or pos_iguais_adv(tab, 6, 7, num)):
                return pos


def obter_filas(tab, num):
    # obter_filas: tabuleiro x inteiro -> tuplo
    """
    A funcao recebe um tabuleiro e um inteiro que representa um jogador
    (1: 'X', -1: 'O') e devolve um tuplo com os numeros das filas que tenham
    apenas uma das posicoes preenchidas pela sua marca ou do adversario.
    """
    num_linha = ()
    num_coluna = ()
    num_diagonal = ()
    for i in range(1, 4):  # linha/coluna 1 - linha/coluna 3
        linha = obter_linha(tab, i)
        if (linha == (num, 0, 0) or linha == (0, num, 0)
                or linha == (0, 0, num)):
            num_linha += (i,)
        coluna = obter_coluna(tab, i)
        if (coluna == (num, 0, 0) or coluna == (0, num, 0)
                or coluna == (0, 0, num)):
            num_coluna += (i,)
    for j in range(1, 3):  # diagonal 1 - diagonal 2
        diagonal = obter_diagonal(tab, j)
        if (diagonal == (num, 0, 0) or diagonal == (0, num, 0)
                or diagonal == (0, 0, num)):
            num_diagonal += (j,)
    return num_linha, num_coluna, num_diagonal


def intersecao_linha_coluna(tab, filas):
    # intersecao_linha_coluna: tabuleiro x tuplo -> tuplo
    """
    A funcao recebe um tabuleiro e um tuplo com os numeros das filas que tenham
    apenas uma das posicoes preenchidas pela sua marca ou do adversario e
    retorna as posicoes livres onde as linhas e as colunas se intersetam.
    """
    pos_livres = ()
    for i in filas[0]:
        for j in filas[1]:
            # verifica se a posicao de intersecao entre a linha e a coluna
            # esta livre e se estiver adiciona-a a um tuplo
            if i == 1 and j == 1:
                if eh_posicao_livre(tab, 1):
                    pos_livres += (1,)
            if i == 1 and j == 2:
                if eh_posicao_livre(tab, 2):
                    pos_livres += (2,)
            if i == 1 and j == 3:
                if eh_posicao_livre(tab, 3):
                    pos_livres += (3,)
            if i == 2 and j == 1:
                if eh_posicao_livre(tab, 4):
                    pos_livres += (4,)
            if i == 2 and j == 2:
                if eh_posicao_livre(tab, 5):
                    pos_livres += (5,)
            if i == 2 and j == 3:
                if eh_posicao_livre(tab, 6):
                    pos_livres += (6,)
            if i == 3 and j == 1:
                if eh_posicao_livre(tab, 7):
                    pos_livres += (7,)
            if i == 3 and j == 2:
                if eh_posicao_livre(tab, 8):
                    pos_livres += (8,)
            if i == 3 and j == 3:
                if eh_posicao_livre(tab, 9):
                    pos_livres += (9,)
        return pos_livres


def intersecao_diagonal_linha(tab, filas):
    # intersecao_diagonal_linha: tabuleiro x tuplo -> tuplo
    """
    A funcao recebe um tabuleiro e um tuplo com os numeros das filas que tenham
    apenas uma das posicoes preenchidas pela sua marca ou do adversario e
    retorna as posicoes livres onde as diagonais e as linhas se intersetam.
    """
    pos_livres = ()
    for i in filas[0]:
        for j in filas[2]:
            # verifica se a posicao de intersecao entre a diagonal e a linha
            # esta livre e se estiver adiciona-a a um tuplo
            if i == 1 and j == 1:
                if eh_posicao_livre(tab, 1):
                    pos_livres += (1,)
            if i == 2 and j == 1:
                if eh_posicao_livre(tab, 5):
                    pos_livres += (5,)
            if i == 3 and j == 1:
                if eh_posicao_livre(tab, 9):
                    pos_livres += (9,)
            if i == 1 and j == 2:
                if eh_posicao_livre(tab, 3):
                    pos_livres += (3,)
            if i == 2 and j == 2:
                if eh_posicao_livre(tab, 5):
                    pos_livres += (5,)
            if i == 3 and j == 2:
                if eh_posicao_livre(tab, 7):
                    pos_livres += (7,)
    return pos_livres


def intersecao_diagonal_col(tab, filas):
    # intersecao_diagonal_col: tabuleiro x tuplo -> tuplo
    """
    A funcao recebe um tabuleiro e um tuplo com os numeros das filas que tenham
    apenas uma das posicoes preenchidas pela sua marca e retorna as posicoes
    livres onde as diagonais e as colunas se intersetam.
    """
    pos_livres = ()
    for i in filas[1]:
        for j in filas[2]:
            # verifica se a posicao de intersecao entre a diagonal e a coluna
            # esta livre e se estiver adiciona-a a um tuplo
            if i == 1 and j == 1:
                if eh_posicao_livre(tab, 1):
                    pos_livres += (1,)
            if i == 2 and j == 1:
                if eh_posicao_livre(tab, 5):
                    pos_livres += (5,)
            if i == 3 and j == 1:
                if eh_posicao_livre(tab, 9):
                    pos_livres += (9,)
            if i == 1 and j == 2:
                if eh_posicao_livre(tab, 7):
                    pos_livres += (7,)
            if i == 2 and j == 2:
                if eh_posicao_livre(tab, 5):
                    pos_livres += (5,)
            if i == 3 and j == 2:
                if eh_posicao_livre(tab, 3):
                    pos_livres += (3,)
    return pos_livres


def bifurcacao_aux(tab, num):
    # bifurcacao_aux: tabuleiro x inteiro -> tuplo
    """
    A funcao recebe um tabuleiro e um inteiro que representa um
    jogador (1: 'X', -1: 'O') e devolve um tuplo com as posicoes livres
    das intersecoes entre as filas.
    """
    filas = obter_filas(tab, num)
    col_linha = intersecao_linha_coluna(tab, filas)
    diagonal_linha = intersecao_diagonal_linha(tab, filas)
    diagonal_col = intersecao_diagonal_col(tab, filas)
    # se nao houver intersecoes entre filas a funcao retorna None
    if col_linha is None or diagonal_linha is None or diagonal_col is None:
        return None
    pos = col_linha + diagonal_linha + diagonal_col
    return pos


def bifurcacao(tab, num):
    # bifurcacao: tabuleiro x inteiro -> posicao
    """
    A funcao recebe um tabuleiro e um inteiro que representa um
    jogador (1: 'X', -1: 'O') e devolve a menor posicao livre das
    intersecoes entre as filas.
    """
    if num == 1:
        pos = bifurcacao_aux(tab, num)
    elif num == -1:
        pos = bifurcacao_aux(tab, num)
    if not (pos is None or pos == ()):
        return min(pos)  # retorna a menor posicao livre das intersecoes


def bloqueio_bifurcacao(tab, num):
    # bloqueio_bifurcacao: tabuleiro x inteiro -> posicao
    """
    A funcao recebe um tabuleiro e um inteiro que representa um
    jogador (1: 'X', -1: 'O') e devolve a menor posicao livre das
    intersecoes entre as filas do seu adversario.
    """
    # verifica se o adversario tem bifurcacoes
    if num == 1:
        pos = bifurcacao_aux(tab, -num)
    elif num == -1:
        pos = bifurcacao_aux(tab, -num)
    if not (pos is None or pos == ()):
        return min(pos)  # retorna a menor posicao livre das intersecoes


def centro(tab):
    # centro: tabuleiro -> posicao
    """
    A funcao recebe um tabuleiro e devole a posicao livre que equivale
    ao centro do tabuleiro(5).
    """
    if eh_posicao_livre(tab, 5):
        return 5


def canto_oposto_aux(tab, num):
    # canto_oposto_aux: tabuleiro -> posicao
    """
    A funcao recebe um tabuleiro e devole a posicao livre que equivale
    ao menor dos cantos opostos a um dos cantos ja preenchido.
    """
    if tab[2][2] == -num and eh_posicao_livre(tab, 1):
        return 1
    if tab[2][0] == -num and eh_posicao_livre(tab, 3):
        return 3
    if tab[0][2] == -num and eh_posicao_livre(tab, 7):
        return 7
    if tab[0][0] == -num and eh_posicao_livre(tab, 9):
        return 9


def canto_oposto(tab, num):
    # canto_oposto: tabuleiro -> posicao
    """
    A funcao recebe um tabuleiro e devole a posicao livre que equivale
    ao menor dos cantos opostos a um dos cantos ja preenchido.
    """
    if num == -1:
        return canto_oposto_aux(tab, num)
    else:
        return canto_oposto_aux(tab, num)


def canto_vazio(tab):
    # canto_vazio: tabuleiro -> posicao
    """
    A funcao recebe um tabuleiro e devole a posicao livre que equivale
    ao menor dos cantos vazios do tabuleiro.
    """
    if eh_posicao_livre(tab, 1):
        return 1
    elif eh_posicao_livre(tab, 3):
        return 3
    elif eh_posicao_livre(tab, 7):
        return 7
    elif eh_posicao_livre(tab, 9):
        return 9


def lateral_vazia(tab):
    # lateral_vazia: tabuleiro -> posicao
    """
    A funcao recebe um tabuleiro e devole a posicao livre que equivale
    a menor lateral vazia do tabuleiro.
    """
    if eh_posicao_livre(tab, 2):
        return 2
    elif eh_posicao_livre(tab, 4):
        return 4
    elif eh_posicao_livre(tab, 6):
        return 6
    elif eh_posicao_livre(tab, 8):
        return 8


def basico(tab):
    # basico: tabuleiro -> posicao
    """
    A funcao recebe um tabuleiro e efetua o modo de jogo 'basico' retornando
    uma posicao livre.
    """
    if centro(tab):
        return centro(tab)
    elif canto_vazio(tab):
        return canto_vazio(tab)
    elif lateral_vazia(tab):
        return lateral_vazia(tab)


def normal(tab, num):
    # normal: tabuleiro -> posicao
    """
    A funcao recebe um tabuleiro e efetua o modo de jogo 'normal' retornando
    uma posicao livre.
    """
    if vitoria(tab, num):
        return vitoria(tab, num)
    elif bloqueio(tab, num):
        return bloqueio(tab, num)
    elif centro(tab):
        return centro(tab)
    elif canto_oposto(tab, num):
        return canto_oposto(tab, num)
    elif canto_vazio(tab):
        return canto_vazio(tab)
    elif lateral_vazia(tab):
        return lateral_vazia(tab)


def perfeito(tab, num):
    # perfeito: tabuleiro -> posicao
    """
    A funcao recebe um tabuleiro e efetua o modo de jogo 'perfeito' retornando
    uma posicao livre.
    """
    if vitoria(tab, num):
        return vitoria(tab, num)
    elif bloqueio(tab, num):
        return bloqueio(tab, num)
    elif bifurcacao(tab, num):
        return bifurcacao(tab, num)
    elif bloqueio_bifurcacao(tab, num):
        return bloqueio_bifurcacao(tab, num)
    elif centro(tab):
        return centro(tab)
    elif canto_oposto(tab, num):
        return canto_oposto(tab, num)
    elif canto_vazio(tab):
        return canto_vazio(tab)
    elif lateral_vazia(tab):
        return lateral_vazia(tab)


def eh_estrategia(estrategia):
    # eh_estrategia: cad. carateres -> booleano
    """
    A funcao recebe uma cadeia de caracteres e devolve True se for uma
    estrategia e False caso contrario, sem nunca gerar erros.
    """
    return (estrategia == "basico" or estrategia == "normal"
            or estrategia == "perfeito")


def escolher_posicao_auto(tab, num, estrategia):
    # escolher_posicao_auto: tabuleiro x inteiro x cad. carateres -> posicao
    """
    A funcao recebe um tabuleiro um inteiro que representa um jogador
    (1: 'X', -1: 'O') e uma cadeia de carateres correspondente a estrategia
    e devolve uma posicao escolhida automaticamente de acordo com a estrategia.
    Se um dos argumentos for invalido gera um erro.
    """
    if eh_tabuleiro(tab) and eh_jogador(num) and eh_estrategia(estrategia):
        if estrategia == "basico":
            return basico(tab)
        elif estrategia == "normal":
            return normal(tab, num)
        else:
            return perfeito(tab, num)
    else:
        raise ValueError("escolher_posicao_auto: algum dos argumentos "
                         "e invalido")


def jogo_do_galo_aux(simb, estrategia):
    # jogo_do_galo_aux: cad. carateres x cad. carateres -> tabuleiro
    """
    A funcao recebe duas cadeias de carateres correspondentes a estrategia e ao
    simbolo do jogador e devolve um tabuleiro. Esta funcao ira imprimir os
    sucessivos tabuleiros de jogo conforme as jogadas.
    """
    tab = ((0, 0, 0), (0, 0, 0), (0, 0, 0))
    if simb == "O":
        print("Bem-vindo ao JOGO DO GALO.\nO jogador joga com 'O'.")
        # o ciclo continua enquanto nao ha vencedor
        while jogador_ganhador(tab) == 0:
            turno = "Turno do computador (" + estrategia + "):"
            print(turno)
            posic_auto = escolher_posicao_auto(tab, 1, estrategia)
            tab = marcar_posicao(tab, 1, posic_auto)
            print(tabuleiro_str(tab))
            livres = obter_posicoes_livres(tab)
            ganhador = jogador_ganhador(tab)
            if ganhador != 0:  # verificacao se ja houve vencedor
                continue
        # verificacao se ja nao existem posicoes livres, ou seja houve empate
            if livres == ():
                break
            posic_manual = escolher_posicao_manual(tab)
            tab = marcar_posicao(tab, -1, posic_manual)
            print(tabuleiro_str(tab))
    if simb == "X":
        print("Bem-vindo ao JOGO DO GALO.\nO jogador joga com 'X'.")
        while jogador_ganhador(tab) == 0:
            posic_manual = escolher_posicao_manual(tab)
            tab = marcar_posicao(tab, 1, posic_manual)
            print(tabuleiro_str(tab))
            livres = obter_posicoes_livres(tab)
            ganhador = jogador_ganhador(tab)
            if ganhador != 0:
                continue
            if livres == ():
                break
            turno = "Turno do computador (" + estrategia + "):"
            print(turno)
            posic_auto = escolher_posicao_auto(tab, 1, estrategia)
            tab = marcar_posicao(tab, -1, posic_auto)
            print(tabuleiro_str(tab))
    return tab


def jogo_do_galo(simb, estrategia):
    # jogo_do_galo: cad. carateres x cad. carateres -> cad. carateres
    """
    A funcao recebe duas cadeias de carateres correspondentes a estrategia e ao
    simbolo do jogador e devolve uma cadeia de carateres que indica o vencedor
    do jogo ou o empate.
    """
    if (simb == "O" or simb == "X") and eh_estrategia(estrategia):
        if estrategia == "basico":
            tab = jogo_do_galo_aux(simb, estrategia)
        elif estrategia == "normal":
            tab = jogo_do_galo_aux(simb, estrategia)
        elif estrategia == "perfeito":
            tab = jogo_do_galo_aux(simb, estrategia)

    if jogador_ganhador(tab) == -1:
        return "O"
    elif jogador_ganhador(tab) == 1:
        return "X"
    elif jogador_ganhador(tab) == 0:
        return "EMPATE"

print(jogo_do_galo('O', 'basico'))