<div align="center">

# 🏗️ Vigas 2D

### Simulação e representação gráfica de vigas biapoiadas em Python

Aplicação desktop desenvolvida para criação e visualização de **vigas 2D com apoios simples**, permitindo configurar a estrutura e inserir diferentes tipos de carregamentos através de uma interface gráfica.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Interface-Tkinter-4B8BBE?style=for-the-badge)
![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)
![Status](https://img.shields.io/badge/Status-Em%20desenvolvimento-yellow?style=for-the-badge)

</div>

---

## 📖 Sobre o projeto

O **Vigas 2D** é uma aplicação desenvolvida em **Python** para criação e representação gráfica de vigas biapoiadas.

O programa permite configurar o comprimento da estrutura e inserir diferentes tipos de carregamento por meio de uma interface gráfica, apresentando visualmente a viga, seus apoios e as forças aplicadas.

O projeto possui caráter acadêmico e busca integrar conceitos de **Engenharia de Computação**, programação e análise estrutural em uma única aplicação.

A implementação atual concentra-se na criação do modelo da viga, gerenciamento das cargas e representação gráfica da estrutura.

> **Status atual:** interface gráfica e sistema de modelagem funcionais. Os cálculos estruturais completos ainda estão em desenvolvimento.

---

## 🎯 Objetivos

O projeto tem como principais objetivos:

- Desenvolver uma aplicação para representação de vigas 2D;
- Criar uma interface gráfica simples e intuitiva;
- Permitir a configuração do comprimento da viga;
- Inserir cargas concentradas;
- Inserir cargas distribuídas;
- Representar visualmente os carregamentos;
- Permitir o gerenciamento das cargas adicionadas;
- Aplicar conceitos de Programação Orientada a Objetos;
- Relacionar programação com problemas de Engenharia;
- Preparar a aplicação para futura implementação de análise estrutural.

---

## ✨ Funcionalidades

### 📏 Configuração da viga

O usuário pode definir o comprimento da viga em metros.

A representação gráfica é atualizada de acordo com as características definidas no programa.

---

### ⬇️ Cargas concentradas

O sistema permite adicionar cargas pontuais informando:

- Magnitude da força em **N**;
- Posição `x` ao longo da viga em **m**;
- Ângulo da força em **graus**.

Representação simplificada:

```text
                 ↓ P
                 │
                 │
▲────────────────┼────────────────○
A                x                B
```

Onde:

```text
P = magnitude da força
x = posição da carga
A = apoio articulado
B = apoio móvel
```

---

### 📐 Cargas distribuídas

Também é possível inserir cargas uniformemente distribuídas.

Os principais parâmetros são:

- Intensidade `w` em **N/m**;
- Posição inicial `x1`;
- Posição final `x2`.

Representação simplificada:

```text
          ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
          ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
▲─────────┬──────────────┬────────○
A        x1              x2       B
```

---

## 🖥️ Interface gráfica

A aplicação possui uma interface responsável pela configuração e visualização da estrutura.

A organização geral pode ser representada por:

```text
┌───────────────────────────────────────────────────────┐
│                  CONFIGURAÇÃO DA VIGA                 │
├───────────────────┬───────────────────────────────────┤
│                   │                                   │
│     CONTROLES     │                                   │
│                   │                                   │
│ Comprimento       │                                   │
│                   │                                   │
│ Carga pontual     │             VIGA                  │
│                   │                                   │
│ Carga distribuída │      Representação gráfica        │
│                   │                                   │
│ Lista de cargas   │                                   │
│                   │                                   │
└───────────────────┴───────────────────────────────────┘
```

A área gráfica permite acompanhar visualmente as alterações realizadas pelo usuário.

---

## 📋 Gerenciamento de cargas

As cargas adicionadas à estrutura podem ser visualizadas e gerenciadas durante a utilização da aplicação.

Fluxo básico:

```text
Adicionar carga
      │
      ▼
Armazenar dados
      │
      ▼
Exibir na lista
      │
      ▼
Representar na viga
      │
      ▼
Remover quando necessário
```

---

## 🧠 Funcionamento geral

O programa recebe os parâmetros definidos pelo usuário e os utiliza para construir uma representação computacional da estrutura.

```text
                 USUÁRIO
                    │
                    ▼
          ┌───────────────────┐
          │ Interface gráfica │
          └─────────┬─────────┘
                    │
                    ▼
          ┌───────────────────┐
          │ Configuração      │
          │ da viga           │
          └─────────┬─────────┘
                    │
           ┌────────┴────────┐
           │                 │
           ▼                 ▼
     Carga pontual     Carga distribuída
           │                 │
           └────────┬────────┘
                    │
                    ▼
          ┌───────────────────┐
          │ Modelo da viga    │
          └─────────┬─────────┘
                    │
                    ▼
          ┌───────────────────┐
          │ Representação     │
          │ gráfica           │
          └───────────────────┘
```

---

## 🏗️ Modelo estrutural

O projeto trabalha com uma **viga biapoiada 2D**.

Representação conceitual:

```text
A                                   B
▲───────────────────────────────────○
│                                   │
Apoio                           Apoio
articulado                      móvel
```

Esse tipo de estrutura é utilizado em estudos introdutórios de:

- Estática;
- Resistência dos Materiais;
- Mecânica dos Sólidos;
- Análise estrutural.

---

## ⚙️ Tipos de carregamento

### Carga concentrada

```text
            P
            ↓
────────────┼────────────
            x
```

Parâmetros:

| Parâmetro | Unidade |
|---|---|
| Magnitude | N |
| Posição | m |
| Ângulo | graus |

---

### Carga distribuída

```text
             w
      ↓ ↓ ↓ ↓ ↓ ↓ ↓
──────┬─────────────┬──────
     x1             x2
```

Parâmetros:

| Parâmetro | Unidade |
|---|---|
| Intensidade | N/m |
| Posição inicial | m |
| Posição final | m |

---

## 💻 Tecnologias utilizadas

| Tecnologia | Aplicação |
|---|---|
| **Python** | Linguagem principal |
| **Tkinter** | Desenvolvimento da interface gráfica |
| **Programação Orientada a Objetos** | Organização do sistema |
| **Git** | Controle de versão |
| **GitHub** | Hospedagem e documentação |

---

## 📂 Estrutura do projeto

```text
vigas-2d/
│
├── controllers/
│   └── Controle das operações da aplicação
│
├── dao/
│   └── Camada relacionada aos dados
│
├── data/
│   └── Dados utilizados pelo programa
│
├── models/
│   └── Modelos utilizados pela aplicação
│
├── statics/
│   └── Recursos estáticos
│
├── utils/
│   └── Funções auxiliares
│
├── views/
│   └── Interface gráfica e representação
│
├── main.py
│   └── Ponto de entrada da aplicação
│
├── .gitignore
│
└── README.md
```

---

## 🧩 Organização do software

O projeto foi dividido em diferentes módulos para separar as responsabilidades da aplicação.

### Models

Responsáveis pela representação dos elementos utilizados pelo programa.

```text
Modelos
   │
   ├── Viga
   │
   └── Cargas
```

---

### Views

Responsáveis pela interação com o usuário e apresentação gráfica da estrutura.

```text
Views
   │
   ├── Interface
   │
   ├── Controles
   │
   └── Representação gráfica
```

---

### Controllers

Responsáveis pela comunicação entre a interface e os elementos internos da aplicação.

```text
Interface
    │
    ▼
Controller
    │
    ▼
Model
```

---

## 🔄 Fluxo da aplicação

```text
INICIAR PROGRAMA
       │
       ▼
Definir comprimento
       │
       ▼
Criar modelo da viga
       │
       ▼
Adicionar carregamentos
       │
       ├───────────────┐
       │               │
       ▼               ▼
Carga pontual     Carga distribuída
       │               │
       └───────┬───────┘
               │
               ▼
       Atualizar modelo
               │
               ▼
      Representar graficamente
               │
               ▼
       Gerenciar cargas
```

---

## 🚀 Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/Jonhmartines/vigas-2d.git
```

### 2. Acesse o diretório

```bash
cd vigas-2d
```

### 3. Execute o programa

```bash
python main.py
```

No Windows também pode ser utilizado:

```bash
py main.py
```

---

## 🛠️ Requisitos

É necessário possuir uma instalação do **Python 3**.

Para verificar a instalação:

```bash
python --version
```

ou:

```bash
py --version
```

---

## 🚧 Status do desenvolvimento

### ✅ Implementado

- [x] Interface gráfica;
- [x] Representação gráfica da viga;
- [x] Representação dos apoios;
- [x] Definição do comprimento;
- [x] Inserção de cargas concentradas;
- [x] Definição da magnitude das cargas;
- [x] Definição da posição das cargas;
- [x] Definição do ângulo das cargas concentradas;
- [x] Inserção de cargas distribuídas;
- [x] Definição do intervalo das cargas distribuídas;
- [x] Representação gráfica dos carregamentos;
- [x] Gerenciamento da lista de cargas;
- [x] Remoção de carregamentos;
- [x] Organização modular do projeto.

### 🔨 Em desenvolvimento

- [ ] Cálculo automático das reações nos apoios;
- [ ] Aplicação das equações de equilíbrio;
- [ ] Cálculo do esforço cortante;
- [ ] Diagrama de esforço cortante;
- [ ] Cálculo do momento fletor;
- [ ] Diagrama de momento fletor;
- [ ] Identificação dos esforços máximos;
- [ ] Apresentação dos resultados numéricos.

---

## 📈 Evolução planejada

A proposta futura é transformar o programa em uma ferramenta mais completa de análise de vigas.

```text
Criação da estrutura
        │
        ▼
Inserção das cargas
        │
        ▼
Representação gráfica
        │
        ▼
Cálculo das reações
        │
        ▼
Equações de equilíbrio
        │
    ┌───┴────┐
    │        │
    ▼        ▼
   V(x)     M(x)
    │        │
    ▼        ▼
Cortante   Momento
    │        │
    └───┬────┘
        │
        ▼
Diagramas estruturais
        │
        ▼
Resultados
```

Entre as possíveis expansões estão:

- Cálculo das reações de apoio;
- Diagrama de esforço cortante;
- Diagrama de momento fletor;
- Identificação automática dos valores máximos;
- Novos tipos de carregamento;
- Diferentes tipos de apoio;
- Exportação dos resultados;
- Geração automática de relatórios;
- Salvamento e carregamento de projetos;
- Melhorias na interface gráfica;
- Validação automática dos dados inseridos.

---

## 🎓 Contexto acadêmico

O projeto relaciona conhecimentos de **Engenharia de Computação** com conceitos aplicados em problemas estruturais.

Durante seu desenvolvimento são utilizados conhecimentos relacionados a:

- Programação;
- Programação Orientada a Objetos;
- Estruturas de dados;
- Desenvolvimento de interfaces;
- Arquitetura de software;
- Modelagem computacional;
- Estática;
- Resistência dos Materiais;
- Análise estrutural.

---

## 💡 Motivação

Problemas envolvendo vigas são tradicionalmente representados através de diagramas e resolvidos utilizando equações de equilíbrio.

A proposta deste projeto é criar uma ferramenta computacional capaz de representar esse processo de maneira visual e interativa.

A evolução planejada busca integrar:

```text
MODELAGEM
    +
VISUALIZAÇÃO
    +
CÁLCULOS
    +
DIAGRAMAS
    =
ANÁLISE ESTRUTURAL COMPUTACIONAL
```

---

## 🔗 Repositório

O código-fonte está disponível neste repositório:

[github.com/Jonhmartines/vigas-2d](https://github.com/Jonhmartines/vigas-2d)

---

## 👨‍💻 Autor

### João Pedro dos Santos Martins

Estudante de **Engenharia de Computação**

[![GitHub](https://img.shields.io/badge/GitHub-Jonhmartines-181717?style=for-the-badge&logo=github)](https://github.com/Jonhmartines)

---

<div align="center">

### 🏗️ Engenharia de Computação • Python • Estruturas • Modelagem Computacional

Desenvolvido como aplicação de conceitos de programação em problemas de Engenharia.

</div>
