import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file_lines = txt_importer(path_file)
    if any(item["nome_do_arquivo"] == path_file for item in instance._data):
        return False
    obj_enqueue = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_lines),
        "linhas_do_arquivo": file_lines,
    }
    instance.enqueue(obj_enqueue)

    return sys.stdout.write(str(obj_enqueue))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""


# new_queue = Queue()
# new_queue.enqueue(
#     {
#         "nome_do_arquivo": "teste.txt",
#         "qtd_linhas": 4,
#         "linhas_do_arquivo": ["Teste", "teste"],
#     }
# )
# new_queue.enqueue(
#     {
#         "nome_do_arquivo": "arquivo_teste.txt",
#         "qtd_linhas": 3,
#         "linhas_do_arquivo": ["Teste", "teste"],
#     }
# )

# # print(new_queue.search(1))
# print(process("statics/arquivo_teste.txt", new_queue))
# process("statics/nome_pedr.txt", new_queue)
# print(new_queue.data)
