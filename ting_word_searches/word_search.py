def exists_word(word, instance):
    results = []

    for item in instance._data:
        if any(
            word.lower() in line.lower() for line in item["linhas_do_arquivo"]
        ):
            occurrences = [
                {"linha": i + 1}
                for i, line in enumerate(item["linhas_do_arquivo"])
                if word.lower() in line.lower()
            ]
            result_item = {
                "palavra": word,
                "arquivo": item["nome_do_arquivo"],
                "ocorrencias": occurrences,
            }
            results.append(result_item)

    return results


def search_by_word(word, instance):
    results = []

    for item in instance._data:
        if any(
            word.lower() in line.lower() for line in item["linhas_do_arquivo"]
        ):
            occurrences = [
                {"linha": i + 1, "conteudo": line}
                for i, line in enumerate(item["linhas_do_arquivo"])
                if word.lower() in line.lower()
            ]
            result_item = {
                "palavra": word,
                "arquivo": item["nome_do_arquivo"],
                "ocorrencias": occurrences,
            }
            results.append(result_item)

    return results
