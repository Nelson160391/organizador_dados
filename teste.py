# Criar diretório
if not os.path.exists('dados'):
os.mkdir('dados')
# Criar arquivo com dados
with open('dados/usuarios.txt', 'w') as arquivo:
arquivo.write('nome,idade\n')
arquivo.write('Débora,35\n')
arquivo.write('Lucas,30\n')
