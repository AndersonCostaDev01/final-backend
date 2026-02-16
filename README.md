
# 📘 Documentação da Aplicação Full Stack - Clone do Twitter

Este projeto tem como objetivo simular uma rede social semelhante ao Twitter, utilizando **Django Rest Framework** no backend.

---

## 🛠 Tecnologias Utilizadas

- **Backend:** Django Rest Framework (DRF)
- **Autenticação:** django-rest-passwordless

> ⚠️ Todas as rotas da API são protegidas por autenticação, exceto para as rotas de autenticação.

---

## 🔐 Autenticação

### Registro

- **URL:** `/api/auth/register/`
- **Método:** `POST`
- **Descrição:** Criação de novo usuário com dados de perfil.
- **Exemplo de payload:**
```json
{
  "username": "nome de usuario deve ser unico",
  "email": "email deve ser unico",
  "password": "senha forte com no minimo 5 caracteres",
  "first_name": "primeiro nome de ususario",
  "last_name": "ultimo nome de usuario"
}
```
- **Resposta:**
```json
{
  "user_id": "id do usuario",
  "username": "nome de usuario",
  "email": "email do usuario",
  "token": "ftoken de authenticação"
}
```

### Login

- **URL:** `/auth/login/`
- **Método:** `POST`
- **Descrição:** Autentica o usuário e retorna o token.
- **Exemplo de payload:**
```json
{
  "email": "email do usuario",
  "password": "senha forte do usuario"
}
```
- **Resposta:**
```json
{
  "token": "ftoken de authenticação",
  "user_id": "id do usuario",
  "username": "nome de usuario",
  "email": "email do usuario"
}
```

> ⚠️ O token de autenticação deve ser enviado em todos os requests subsequentes. Então é recomendado armazenar o token em um cookie ou localStorage.

### Exemplo de uso do token em um request

```javascript
const token = localStorage.getItem('token');

fetch(apiUrl, {
  method: 'GET',
  headers: {
    Authorization: `Token ${token}`,
    'Content-Type': 'application/json'
  }
})
  .then(response => {
    if (!response.ok) {
      throw new Error(`Erro: ${response.status}`);
    }
    return response.json();
  })
  .then(data => {
    console.log('Dados da API:', data);
  })
  .catch(error => {
    console.error('Erro ao fazer a requisição:', error);
  });
```

---

## 📝 Postagens

### Criar Postagem

- **URL:** `/posts/posts/`
- **Método:** `POST`
- **Token:** ✅
- **Payload:**
```json
{
  "conteudo": "Este é meu primeiro tweet!",
  "categorias": ["tech", "noticias"]
}
```

### Listar Postagens

- **URL:** `/posts/posts/`
- **Método:** `GET`
- **Token:** ✅

### Detalhar / Atualizar / Excluir Postagem

- **URL:** `/posts/posts/{id}/`
- **Métodos:** `GET`, `PUT`, `PATCH`, `DELETE`
- **Token:** ✅

### Buscar por Categorias

- **URL:** `/posts/por-categoria/{categoria_id}/`
- **Método:** `GET`
- **Token:** ✅

---

## 🏷 Categorias

### Criar Categoria

- **URL:** `/posts/categorias/`
- **Método:** `POST`
- **Token:** ✅
- **Payload:**
```json
{
  "id": 1,
  "nome": "tech",
  "descricao": "Categoria de tecnologia"
}
```

### Listar Categorias

- **URL:** `/posts/categorias/`
- **Método:** `GET`
- **Token:** ✅

### Detalhar / Atualizar / Excluir Categoria

- **URL:** `/posts/categorias/{id}/`
- **Métodos:** `GET`, `PUT`, `PATCH`, `DELETE`
- **Token:** ✅

---

## 📰 Comentários

### Criar Comentário

- **URL:** `/posts/comentarios/`
- **Método:** `POST`
- **Token:** ✅
- **Payload:**
```json
{
  "autor": 1,
  "conteudo": "muito bom post",
  "post": 32
}
```

### Detalhar / Atualizar / Excluir Comentário

- **URL:** `/posts/comentarios/{id}/`
- **Métodos:** `GET`, `PUT`, `PATCH`, `DELETE`
- **Token:** ✅

### Listar Comentários de um Post

- **URL:** `/posts/comentarios/por-post/{post_id}/`
- **Método:** `GET`
- **Token:** ✅

---

## 👤 Perfil do Usuário

### Obter Perfil do Usuário Atual

- **URL:** `/users/buscar-usuarios/{id_usuario}` ou `{username}`
- **Método:** `GET`
- **Token:** ✅

### Atualizar Perfil

- **URL:** `/users/profile/{username}/`
- **Método:** `PUT` ou `PATCH`
- **Token:** ✅
- **Payload Exemplo:**
```json
{
  "foto": "https://exemplo.com/foto.jpg",
  "descricao": "Descrição do usuário"
}
```
> ⚠️ Apenas estes dois campos podem ser alterados, e apenas pelo próprio usuário.

### Ver Perfil de Outro Usuário

- **URL:** `/users/buscar-usuarios/{id_usuario}` ou `{username}`
- **Método:** `GET`
- **Token:** ✅

### Buscar por parte do nome

- **URL:** `/users/buscar-usuarios/?search={nome}`
- **Método:** `GET`
- **Token:** ✅

---

## 🔐 Segurança

- **Autenticação por Token:**
  - Header:
    ```
    Authorization: Token <seu_token_aqui>
    ```

- **Permissões:**
  - `IsAuthenticated` aplicada em todas as rotas protegidas.
  - Permissões personalizadas para autores de postagens e comentários.

---

## 🌐 Endpoints - Resumo Geral

### 🔑 Autenticação
```
POST   /auth/register/                  -> Registrar novo usuário
POST   /auth/login/                     -> Login e obtenção de token
```

### 📝 Postagens
```
GET    /posts/posts/                        -> Listar todas as postagens
POST   /posts/posts/                        -> Criar nova postagem
GET    /posts/posts/{id}/                   -> Ver detalhes de uma postagem
PUT    /posts/posts/{id}/                   -> Atualizar postagem
PATCH  /posts/posts/{id}/                   -> Atualizar parcialmente
DELETE /posts/posts/{id}/                   -> Excluir postagem
GET    /posts/por-categoria/{categoria_id}/ -> Buscar postagens por categoria
```

### 🏷 Categorias
```
GET    /posts/categorias/                   -> Listar categorias
POST   /posts/categorias/                   -> Criar nova categoria
GET    /posts/categorias/{id}/              -> Ver detalhes da categoria
PUT    /posts/categorias/{id}/              -> Atualizar categoria
PATCH  /posts/categorias/{id}/              -> Atualizar parcialmente
DELETE /posts/categorias/{id}/              -> Excluir categoria
```

### 💬 Comentários
```
POST   /posts/comentarios/                  -> Criar novo comentário
GET    /posts/comentarios/{id}/             -> Detalhar comentário
PUT    /posts/comentarios/{id}/             -> Atualizar comentário
PATCH  /posts/comentarios/{id}/             -> Atualizar parcialmente
DELETE /posts/comentarios/{id}/             -> Excluir comentário
GET    /posts/comentarios/por-post/{post_id}/ -> Listar comentários de um post
```

### 👤 Usuário / Perfil
```
GET    /users/buscar-usuarios/{id}/         -> Buscar perfil por ID
GET    /users/buscar-usuarios/{username}/   -> Buscar perfil por nome de usuário
GET    /users/buscar-usuarios/?search=abc   -> Buscar por parte do nome
GET    /users/profile/{username}/           -> Obter perfil do usuário atual
PUT    /users/profile/{username}/           -> Atualizar perfil (foto e descrição)
PATCH  /users/profile/{username}/           -> Atualizar parcialmente perfil
```

---

## ✅ Fluxo de Uso no Frontend

1. **Usuário não autenticado:**
   - Tem acesso apenas ao registro e login.

2. **Após login:**
   - O token retornado deve ser salvo no `localStorage` ou cookies.
   - Esse token será usado para autenticar todas as requisições protegidas.

3. **Requisições autenticadas:**
   - Posts, categorias, comentários e perfis exigem token no header:
     ```http
     Authorization: Token seu_token_aqui
     ```

---

## 📌 Considerações Finais

Este documento é uma referência para o consumo da API do projeto **Clone do Twitter** com Django Rest Framework.  
A estrutura está preparada para ser utilizada por frontends modernos (React, Next.js, etc.) e pode ser facilmente integrada com ferramentas como Postman ou Thunder Client para testes.

> Para produção, recomenda-se usar variáveis de ambiente e um controle mais refinado de CORS, permissões e logs.
