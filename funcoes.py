import msvcrt

def capturar_digitos():
    """
    Captura caracteres digitados pelo usuário em tempo real até que a tecla TAB seja pressionada.

    Comportamento:
    - BACKSPACE apaga o último caractere digitado.
    - ENTER insere um espaço no texto e pula uma linha no terminal.
    - TAB finaliza a captura e retorna o texto digitado.

    Retorna:
        str: O texto digitado pelo usuário
    """

    texto = ""
    print("Digite algo (pressione TAB para encerrar):")

    while True:
        if msvcrt.kbhit():
            teclado = msvcrt.getwch()

            if teclado == '\t':
                break
            elif teclado == '\r':                
                print()
                texto += ' '
            elif teclado == '\b':
                texto = texto[:-1]
                print("\b \b", end='', flush=True)
            else: 
                texto += teclado
                print(teclado, end='', flush=True)
    return texto