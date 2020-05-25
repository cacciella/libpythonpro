import pytest

from libpythonpro.spam.enviador_de_email import EmailInvalido, Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['foo@bar.com.br', 'arc.mau@gmail.com']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'renzo@python.pro.br',
        'Curso Python Pro',
        'Primeira turma Luiz Vital aberta.'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'cacciella']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'renzo@python.pro.br',
            'Cursos Python Pro',
            'Primeira turma Luiz Vital aberta.'
        )
