
# 📘 Documentação da Aplicação Full Stack - Clone do Twitter

Este projeto tem como objetivo simular uma rede social semelhante ao Twitter, utilizando **Django Rest Framework** no backend e **Next.js** no frontend.

---

## 🛠 Tecnologias Utilizadas

- **Backend:** Django Rest Framework (DRF)
- **Frontend:** Next.js
- **Autenticação:** Token JWT (ex: `djangorestframework-simplejwt`)

> ⚠️ Todas as rotas da API devem ser protegidas por token, exceto login e registro.

---

## 🔐 Autenticação

### Registro

- **URL:** `/api/auth/register/`
- **Método:** `POST`
- **Descrição:** Criação de novo usuário com dados de perfil.
- **Exemplo de payload:**
```json
{
  "username": "fulano",
  "email": "fulano@example.com",
  "password": "senhaSegura123",
  "first_name": "Fulano",
  "last_name": "da Silva",
  "profile": {
    "foto": "url_da_foto",
    "descricao": "Breve descrição sobre o usuário"
  }
}
```

### Login

- **URL:** `/api/auth/login/`
- **Método:** `POST`
- **Descrição:** Autentica o usuário e retorna o token.
- **Exemplo de payload:**
```json
{
  "username": "fulano",
  "password": "senhaSegura123"
}
```

---

## 📝 Postagens

### Criar Postagem

- **URL:** `/api/posts/`
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

- **URL:** `/api/posts/`
- **Método:** `GET`
- **Token:** ✅

### Detalhar / Atualizar / Excluir Postagem

- **URL:** `/api/posts/{id}/`
- **Métodos:** `GET`, `PUT`, `PATCH`, `DELETE`
- **Token:** ✅

---

## 🏷 Categorias

### Criar Categoria

- **URL:** `/api/categories/`
- **Método:** `POST`
- **Token:** ✅
- **Payload:**
```json
{
  "nome": "tech"
}
```

### Listar Categorias

- **URL:** `/api/categories/`
- **Método:** `GET`
- **Token:** ✅

---

## 📰 Feed

### Listar Feed

- **URL:** `/api/feed/`
- **Método:** `GET`
- **Token:** ✅

**Filtros Disponíveis:**

- `?categoria=tech`
- `?seguindo=true`

---

## 👤 Perfil do Usuário

### Obter Perfil do Usuário Atual

- **URL:** `/api/profile/`
- **Método:** `GET`
- **Token:** ✅

### Atualizar Perfil

- **URL:** `/api/profile/`
- **Método:** `PUT` ou `PATCH`
- **Token:** ✅
- **Payload Exemplo:**
```json
{
  "nome_completo": "Fulano da Silva Atualizado",
  "descricao": "Nova descrição do perfil."
}
```

### Ver Perfil de Outro Usuário

- **URL:** `/api/users/{username}/`
- **Método:** `GET`
- **Token:** ✅

---

## 🔄 Seguir / Deixar de Seguir

- **URL:** `/api/users/{username}/follow/`
- **Método:** `POST`
- **Token:** ✅
- **Payload (opcional):**
```json
{
  "acao": "seguir"  // ou "deixar_seguir"
}
```

---

## 🔐 Segurança

- **Autenticação por Token:**
  - Header:
    ```
    Authorization: Token <seu_token_aqui>
    ```

- **Permissões:**
  - `IsAuthenticated` para rotas protegidas
  - Permissões customizadas para autores de postagens

---

## 🌐 Endpoints Resumo

```
POST   /api/auth/register/        -> Registro
POST   /api/auth/login/           -> Login
GET    /api/posts/                -> Listar posts
POST   /api/posts/                -> Criar post
GET    /api/posts/{id}/           -> Detalhar post
PUT    /api/posts/{id}/           -> Atualizar post
DELETE /api/posts/{id}/           -> Deletar post
GET    /api/categories/           -> Listar categorias
POST   /api/categories/           -> Criar categoria
GET    /api/feed/                 -> Listar feed com filtros
GET    /api/profile/              -> Perfil do usuário atual
PUT    /api/profile/              -> Atualizar perfil
GET    /api/users/{username}/     -> Ver perfil público
POST   /api/users/{username}/follow/ -> Seguir / deixar de seguir
```

---

## ✅ Fluxo de Uso no Frontend

1. **Usuário não autenticado:**
   - Acesso às páginas de login e registro.

2. **Após login:**
   - Armazenar o token e utilizar nas próximas requisições.

3. **Requisições autenticadas:**
   - Todas as operações com posts, categorias, feed e perfil exigem envio do token.

---

## 📌 Considerações Finais

Esse documento serve como base inicial para desenvolvimento e documentação técnica da aplicação. Pode ser expandido com diagramas de entidade, testes de API e instruções de deploy conforme o projeto evolui.
