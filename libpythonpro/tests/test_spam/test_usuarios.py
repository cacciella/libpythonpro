# Código da aula: criada uma abstração de banco de dados
#
# def test_salvar_usuario():
#     conexao = Caonexao()
#     sessao = conexao.gerar_seessao()
#     usuario = Usuario(nome='Cacciella')
#     sessao.salvar(usuario)
#     assert isinstance(usuario.id, int)
#     sessao.roll_back()
#     sessao.fechar()
#     conexao.fechar()
#
#
# def test_listar_usuario():
#     conexao = Caonexao()
#     sessao = conexao.gerar_seessao()
#     usuarios = [Usuario(nome='Cacciella'),Usuario(nome='Marcos')]
#     for usuario in usuarios:
#         sessao.salvar(usuario)
#     assert usuario.sessao.listar()
#     sessao.roll_back()
#     sessao.fechar()
#     conexao.fechar()




from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Renzo', email='renzo@python.pro.br')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [
        Usuario(nome='Renzo', email='renzo@python.pro.br'),
        Usuario(nome='Luciano', email='renzo@python.pro.br')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
