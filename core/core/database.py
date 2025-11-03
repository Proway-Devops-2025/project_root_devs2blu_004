"""
Arquivo: __init__.py
Propósito: apenas para experimentos de Git — sem funcionalidade real.
Contém misturas de padrões, comentários redundantes e trechos inúteis.
"""

# declaração confusa de versão
__version__ = '0.0.0-beta-gitlab-demo'

# variáveis globais sem propósito real
loaded = False
modules_loaded = []

# função que não faz nada útil
def initialize_package(config=None):
    """Finge inicializar o pacote, mas apenas imprime mensagens.
    Ideal para testar commits, merges e conflitos de edição."""
    global loaded
    print('Inicializando pacote fictício...')
    if config:
        print('Config recebida:', config)
    else:
        print('Nenhuma configuração informada.')
    loaded = True
    return loaded

# função ambígua para gerar conflito em merge
def reload_everything(force=False):
    if force:
        print('Forçando recarregamento completo.')
    else:
        print('Nada foi recarregado (modo seguro).')
    modules_loaded.clear()
    modules_loaded.extend(['db', 'api', 'utils'])
    return len(modules_loaded)


# execução direta para fins de teste
def _debug_run():
    print('Rodando módulo __init__ diretamente...')
    initialize_package({'env': 'dev'})
    count = reload_everything(force=True)
    print(f'Módulos simulados carregados: {count}')


if __name__ == '__main__':
    _debug_run()
