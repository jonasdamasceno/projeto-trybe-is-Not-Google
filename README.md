Ting File Management
Este repositório contém implementações relacionadas à gestão de arquivos em Python. Aqui estão os detalhes dos recursos e funcionalidades implementados:

Pacote ting_file_management
Classe Queue: Implementação de uma fila para armazenar arquivos que serão lidos. A fila segue a política FIFO (First In, First Out), onde o primeiro arquivo a entrar é o primeiro a ser removido. A classe Queue implementa os métodos de inserção (enqueue), remoção (dequeue) e busca (search), além de expor o tamanho da fila através do método __len__.

Função txt_importer: Capaz de importar notícias a partir de um arquivo TXT, utilizando "\n" como separador. Esta função exibe mensagens de erro caso o arquivo não seja encontrado ou tenha uma extensão diferente de .txt.

Função process: Transforma o conteúdo da lista gerada pela função txt_importer em um dicionário que é armazenado dentro da fila. Esta função ignora arquivos que já foram processados anteriormente.

Função remove: Remove o primeiro arquivo processado da fila. Em caso de sucesso, emite uma mensagem informando o arquivo removido.

Função file_metadata: Apresenta informações superficiais de um arquivo processado, como o nome e o caminho do arquivo.

Testes
Implementação dos testes para a classe PriorityQueue, capaz de armazenar arquivos pequenos de forma prioritária. Arquivos com menos de 5 linhas são armazenados de forma prioritária na fila, impactando nos resultados dos métodos dequeue e search.
Pacote ting_word_searches
Função exists_word: Verifica a existência de uma palavra em todos os arquivos processados. Retorna uma lista com as informações de cada arquivo e suas linhas em que a palavra foi encontrada.

Função search_by_word: Busca uma palavra em todos os arquivos processados, incluindo o conteúdo das linhas onde a palavra foi encontrada.

Como usar
Clone este repositório para o seu sistema local.
Instale as dependências necessárias.
Execute os testes para garantir que tudo está funcionando corretamente.
Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests ou abrir issues com sugestões e melhorias.

Licença
Este projeto está licenciado sob a MIT License.






-->
