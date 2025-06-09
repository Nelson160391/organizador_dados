# Guia de Contribuição

Bem-vindo(a) ao nosso projeto! Agradecemos o seu interesse em contribuir. Este guia tem como objetivo facilitar o processo de contribuição, explicando os passos para realizar **commits**, **pushes** e **pull requests** no GitHub.

---

## 1. Antes de Começar

Certifique-se de que você tem:

* Uma conta no **GitHub**.
* **Git** instalado em sua máquina local.
* Conhecimento básico de linha de comando.

---

## 2. Fluxo de Contribuição Simplificado

Siga estes passos para fazer suas contribuições:

### 2.1. Faça um "Fork" do Repositório

O primeiro passo é criar uma cópia do nosso repositório para a sua conta GitHub.

1.  Vá até a página principal do nosso repositório no GitHub.
2.  Clique no botão **"Fork"** no canto superior direito.

### 2.2. Clone o Repositório "Forkado" para a Sua Máquina

Agora você precisa baixar a sua cópia do repositório para o seu computador.

1.  Na sua conta GitHub, vá para o repositório que você acabou de "forkar".
2.  Clique no botão verde **"Code"** e copie a URL (HTTPS ou SSH).
3.  Abra seu terminal ou prompt de comando.
4.  Execute:
    ```bash
    git clone <URL_DO_SEU_FORK>
    ```
    (Substitua `<URL_DO_SEU_FORK>` pela URL que você copiou).

### 2.3. Adicione o Repositório Original como "upstream"

É uma boa prática configurar uma referência para o nosso repositório original. Isso facilita a sincronização futura.

1.  Navegue até a pasta do projeto em seu terminal:
    ```bash
    cd <NOME_DO_REPOSITORIO>
    ```
2.  Adicione o remoto "upstream":
    ```bash
    git remote add upstream <URL_DO_REPOSITORIO_ORIGINAL>
    ```
    (Você encontra a URL do nosso repositório na página principal do projeto no GitHub).

### 2.4. Crie uma Nova Branch para Suas Alterações

Sempre trabalhe em uma branch separada para suas contribuições. Isso mantém o histórico limpo e evita conflitos.

1.  Sincronize sua branch `main` local com as últimas alterações do nosso repositório:
    ```bash
    git pull upstream main
    ```
2.  Crie e mude para uma nova branch com um nome descritivo (ex: `feat/nova-feature`, `fix/bug-login`):
    ```bash
    git checkout -b nome-da-sua-branch
    ```

### 2.5. Faça Suas Alterações e Comite

Agora é a hora de codificar!

1.  Faça as modificações nos arquivos do projeto.
2.  Quando terminar, veja o status das suas alterações:
    ```bash
    git status
    ```
3.  Adicione os arquivos modificados para o "staging area":
    ```bash
    git add .
    # ou para arquivos específicos:
    # git add caminho/do/arquivo.txt
    ```
4.  Crie um **commit** com uma mensagem clara e concisa. A mensagem deve explicar o que foi alterado e por quê.

    ```bash
    git commit -m "feat: Adiciona funcionalidade de cadastro de usuário"
    # ou para correções:
    # git commit -m "fix: Corrige erro de exibição na tela inicial"
    ```
    * **Dica:** Mensagens de commit curtas e descritivas são melhores!

### 2.6. Envie (Push) Suas Alterações para o GitHub

Depois de comitar, você precisa enviar suas alterações para o seu repositório "forkado" no GitHub.

```bash
git push origin nome-da-sua-branch
