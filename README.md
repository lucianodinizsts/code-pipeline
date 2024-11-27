
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
2. Role até **Bucket Policy** e insira a seguinte política json:

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

### **Criar o Pipeline no CodePipeline**

#### **Configuração Inicial**

1. Acesse o console do **AWS CodePipeline**.
2. Clique em **Create pipeline**.
3. Preencha os seguintes campos:
   - **Pipeline name**: `html-static-site-pipeline`.
   - **Service role**: 
     - Escolha **New service role** para criar uma nova.
     - Caso prefira usar uma existente, selecione **Existing service role**.
   - **Artifact store**: 
     - Escolha **Default location** para usar um bucket S3 criado automaticamente.
4. Clique em **Next**.

---

#### **Fonte (Source)**

1. Na seção **Source stage**, configure:
   - **Source provider**: GitHub (Version 2).
   - Clique em **Connect to GitHub** e autentique sua conta.
   - Escolha o **Repository** que contém os arquivos do projeto.
   - Selecione o **Branch** principal (por exemplo, `main`).
2. Clique em **Next** para avançar.

---

#### **Build**

1. Na seção **Build stage**, configure:
   - **Build provider**: AWS CodeBuild.
   - Clique em **Create a build project** e preencha:
     - **Project name**: `html-static-site-build`.
     - **Environment image**: Escolha **Managed image**.
     - **Operating system**: Amazon Linux 2.
     - **Runtime**: Standard.
     - **Image**: aws/codebuild/standard:5.0.
     - **Buildspec file**: Escolha **Use a buildspec file**. O arquivo `buildspec.yml` será lido automaticamente do repositório.
   - Clique em **Create build project**.
2. Retorne ao pipeline e clique em **Next**.

---

#### **Deploy**

1. Na seção **Deploy stage**, configure:
   - **Deploy provider**: Amazon S3.
   - **Bucket**: Selecione o bucket S3 criado anteriormente (`static-site-deploy`).
   - **Extract file before deploy**: Marque esta opção.
2. Clique em **Next**.

---

#### **Finalizar**

1. Revise todas as configurações do pipeline.
2. Clique em **Create pipeline** para concluir.
3. O pipeline será criado, e a primeira execução iniciará automaticamente.

---

### **Executar o Pipeline**

1. Após a criação, verifique o andamento da execução no console do **AWS CodePipeline**.
2. A execução deve passar pelas etapas:
   - **Source**: Código extraído com sucesso do GitHub.
   - **Build**: Testes realizados com sucesso usando Python.
   - **Deploy**: Arquivo HTML implantado no bucket S3.

Se ocorrerem erros, revise os logs disponíveis para cada etapa no console do pipeline.

---

### **Validar a Implantação**

1. Acesse o console do **Amazon S3**.
2. Navegue até o bucket `static-site-deploy`.
3. Na aba **Properties**, localize a seção **Static website hosting**.
4. Copie o **Bucket website endpoint** exibido.
5. Abra o endpoint em seu navegador. O site deve exibir a mensagem:

   ```html
   Bem-vindo ao Site Estático!
   Este site foi implantado usando AWS CodePipeline.

