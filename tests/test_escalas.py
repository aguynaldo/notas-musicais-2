from pytest import raises

from notas_musicais_2.escalas import ESCALAS, NOTAS, escala


def test_deve_funcionar_com_notas_minusculas():
    # Arrange - Arrumar
    tonica = 'c'
    tonalidade = 'maior'

    # Act - Agir (Chamo o que devo testar)
    result = escala(tonica, tonalidade)

    # Assert - Garantir
    assert result


def test_deve_retornar_erro_dizendo_que_a_nota_nao_existe():
    tonica = 'X'
    tonalidade = 'maior'

    mensagem_de_erro = f'Essa nota não existe, tente uma dessas {NOTAS}'

    with raises(ValueError) as error:
        escala(tonica, tonalidade)

    assert mensagem_de_erro == error.value.args[0]


def test_deve_retornar_erro_dizendo_que_a_escala_nao_existe():
    tonica = 'c'
    tonalidade = 'tonalidade'

    mensagem_de_erro = f'Essa escala não existe ou não foi implementada. Tente uma dessas {list(ESCALAS.keys())}'

    with raises(KeyError) as error:
        escala(tonica, tonalidade)

    assert mensagem_de_erro == error.value.args[0]
