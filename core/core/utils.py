import unittest

# ====================================================================
# FUNÇÕES DE UTILIDADE (O seu código 'utils.py' real)
# ====================================================================

def formata_nome(primeiro_nome, sobrenome):
    """
    Formata um nome e sobrenome, garantindo que a primeira letra 
    de cada um esteja em maiúsculo.
    """
    if not primeiro_nome or not sobrenome:
        return ""
        
    nome_formatado = f"{primeiro_nome.strip().capitalize()} {sobrenome.strip().capitalize()}"
    return nome_formatado

def calcular_area_retangulo(largura, altura):
    """Calcula a área de um retângulo."""
    if largura <= 0 or altura <= 0:
        raise ValueError("Largura e altura devem ser valores positivos.")
    return largura * altura

# ====================================================================
# TESTES UNITÁRIOS (Executados apenas se o arquivo for rodado diretamente)
# ====================================================================

class TestUtils(unittest.TestCase):
    """
    Classe de testes para as funções utilitárias dentro deste arquivo.
    """

    def test_formata_nome_sucesso(self):
        """
        Teste: Verifica a formatação correta de nomes.
        """
        nome_esperado = "Maria Silva"
        nome_obtido = formata_nome("maria", "silva")
        
        # 1. Verifica se o resultado é o esperado
        self.assertEqual(nome_esperado, nome_obtido, 
                         "O nome não foi formatado corretamente (capitalização).")
        
        # 2. O seu "echo de sucesso"
        self.assertTrue(True)
        print("\n*** TESTE UNITÁRIO FICTÍCIO DE SUCESSO EXECUTADO NO UTILS! (formata_nome OK) ***")
        
    def test_formata_nome_com_espacos(self):
        """
        Teste: Verifica se a função lida corretamente com espaços em branco.
        """
        self.assertEqual("Joao Souza", formata_nome("  joao  ", "souza"),
                         "Não removeu os espaços em branco extras.")
                         
    def test_calcular_area_positiva(self):
        """
        Teste: Verifica o cálculo da área para valores positivos.
        """
        self.assertEqual(calcular_area_retangulo(5, 10), 50,
                         "O cálculo da área está incorreto.")

    def test_calcular_area_zero_ou_negativa(self):
        """
        Teste: Verifica se levanta erro para valores não positivos.
        """
        # Verifica se um 'ValueError' é levantado quando a altura é zero
        with self.assertRaises(ValueError):
            calcular_area_retangulo(5, 0)
            
        # Verifica se um 'ValueError' é levantado quando a largura é negativa
        with self.assertRaises(ValueError):
            calcular_area_retangulo(-5, 10)


# ====================================================================
# PONTO DE ENTRADA (O que faz o teste rodar)
# ====================================================================

if __name__ == '__main__':
    # Roda todos os testes definidos na classe TestUtils
    unittest.main()