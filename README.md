
# **Configuração de Pipeline para Site Estático**

Este documento descreve como configurar um pipeline CI/CD no AWS CodePipeline para hospedar um site estático em HTML no Amazon S3, incluindo testes unitários com Python.

---

## **Visão Geral**

O pipeline realiza as seguintes etapas:
1. **Fonte**: Código armazenado em um repositório GitHub.
2. **Build**: Executa testes no arquivo HTML usando Python.
3. **Deploy**: Implanta o arquivo HTML em um bucket S3 configurado para hospedagem estática.

---

## **Pré-requisitos**

Antes de começar, certifique-se de ter:
- Conta AWS com permissões para criar:
  - Buckets S3.
  - Projetos CodeBuild.
  - Pipelines CodePipeline.
- Repositório no GitHub para armazenar o código.
- **AWS CLI** instalado e configurado.
- Python 3.9+ instalado localmente.

---

## **Etapas de Configuração**

### **1. Configurar o Bucket S3**

#### **Criar o Bucket**

1. Acesse o console do **Amazon S3**.
2. Clique em **Create bucket**.
3. Configure:
   - **Bucket name**: `static-site-deploy`
   - **Region**: Escolha a região preferida.
4. Desative a opção de **Block all public access** e confirme.
5. Clique em **Create bucket**.

#### **Habilitar Hospedagem Estática**

1. Abra o bucket criado e vá para a aba **Properties**.
2. Role até a seção **Static website hosting**.
3. Clique em **Edit**:
   - **Enable** Static website hosting.
   - Preencha:
     - **Index document**: `index.html`.
4. Clique em **Save changes**.

#### **Configurar Permissões Públicas**

1. Acesse a aba **Permissions** do bucket.
2. Role até **Bucket Policy** e insira a seguinte política:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::static-site-deploy/*"
    }
  ]
}
