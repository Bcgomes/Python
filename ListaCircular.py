class Filme: 
    def __init__(self, nome):
        self.nome = nome
        self.proximo = None

class ListaCircularFilmes:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def adicionar_filme(self, nome):
        novo_filme = Filme(nome)
        if not self.primeiro:
            self.primeiro = novo_filme
            self.ultimo = novo_filme
            self.ultimo.proximo = self.primeiro
        else:
            novo_filme.proximo = self.primeiro
            self.ultimo.proximo = novo_filme
            self.ultimo = novo_filme

    def buscar_filme(self, nome):
        atual = self.primeiro
        while atual:
            if atual.nome == nome:
                return atual
            atual = atual.proximo
            if atual == self.primeiro:
                break
        return None

    def contar_filmes(self):
        contador = 0
        atual = self.primeiro
        while atual:
            contador += 1
            atual = atual.proximo
            if atual == self.primeiro:
                break
        return contador

    def remover_filme(self, nome):
        alvo = self.buscar_filme(nome)
        if alvo:
            if alvo == self.primeiro:
                if self.primeiro == self.ultimo:
                    self.primeiro = None
                    self.ultimo = None
                else:
                    self.primeiro = alvo.proximo
                    self.ultimo.proximo = self.primeiro
            else:
                atual = self.primeiro
                while atual.proximo != alvo:
                    atual = atual.proximo
                atual.proximo = alvo.proximo
                if alvo == self.ultimo:
                    self.ultimo = atual

    def imprimir_lista(self):
        atual = self.primeiro
        while atual:
            print(atual.nome)
            atual = atual.proximo
            if atual == self.primeiro:
                break

# Exemplo de uso
lista_filmes = ListaCircularFilmes()
lista_filmes.adicionar_filme("Filme 1")
lista_filmes.adicionar_filme("Filme 2")
lista_filmes.adicionar_filme("Filme 3")

print("Lista de filmes:")
lista_filmes.imprimir_lista()

print("Quantidade de filmes:", lista_filmes.contar_filmes())

filme_remover = "Filme 2"
lista_filmes.remover_filme(filme_remover)
print(f"Filme '{filme_remover}' removido.")

print("Lista de filmes após remoção:")
lista_filmes.imprimir_lista()