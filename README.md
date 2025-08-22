# Exercícios de Programação Python

Este repositório contém 4 exercícios práticos de programação em Python, focados em estruturas condicionais, entrada de dados e lógica de programação.

## 📋 Exercícios Incluídos

### 1. Classificador de Idade
**Objetivo:** Criar um programa que classifica usuários por faixa etária.

**Descrição:** O programa solicita a idade do usuário e o classifica em uma das seguintes categorias:
- **Criança:** 0-12 anos
- **Adolescente:** 13-17 anos  
- **Adulto:** 18-59 anos
- **Idoso:** 60 anos ou mais

**Conceitos aplicados:** Estruturas condicionais (if/elif/else), entrada de dados, validação de intervalos.

---

### 2. Calculadora de IMC
**Objetivo:** Desenvolver uma calculadora de Índice de Massa Corporal com classificação.

**Descrição:** O programa solicita peso (kg) e altura (metros) do usuário, calcula o IMC e fornece a classificação baseada na tabela padrão:
- **< 18.5:** Abaixo do peso
- **< 25:** Peso normal  
- **< 30:** Sobrepeso
- **≥ 30:** Obeso

**Fórmula:** IMC = peso / (altura²)

**Conceitos aplicados:** Operações matemáticas, formatação de números, classificação por faixas.

---

### 3. Conversor de Temperatura
**Objetivo:** Criar um conversor entre diferentes escalas de temperatura.

**Descrição:** O programa permite conversão entre Celsius, Fahrenheit e Kelvin. O usuário informa:
- Temperatura a ser convertida
- Unidade de origem
- Unidade de destino

**Fórmulas de conversão:**
- Celsius → Fahrenheit: `F = C × 9/5 + 32`
- Celsius → Kelvin: `K = C + 273.15`
- Fahrenheit → Celsius: `C = (F - 32) × 5/9`
- Fahrenheit → Kelvin: `K = (F - 32) × 5/9 + 273.15`
- Kelvin → Celsius: `C = K - 273.15`
- Kelvin → Fahrenheit: `F = (K - 273.15) × 9/5 + 32`

**Conceitos aplicados:** Menu de opções, múltiplas conversões, funções matemáticas.

---

### 4. Verificador de Ano Bissexto
**Objetivo:** Determinar se um ano é bissexto conforme as regras do calendário gregoriano.

**Descrição:** O programa verifica se um ano inserido pelo usuário é bissexto baseado nas seguintes regras:
- **É bissexto se:** divisível por 4
- **Exceção:** anos centenários (divisíveis por 100) só são bissextos se também forem divisíveis por 400

**Exemplos:**
- 2024 → Bissexto (divisível por 4)
- 1900 → Não bissexto (divisível por 100, mas não por 400)
- 2000 → Bissexto (divisível por 400)

**Conceitos aplicados:** Operadores lógicos, operador módulo (%), lógica booleana.

---

## 🚀 Como Executar

1. Certifique-se de ter Python 3.x instalado
2. Clone este repositório ou baixe os arquivos
3. Execute cada programa individualmente:
   ```bash
   python classificador_idade.py
   python calculadora_imc.py
   python conversor_temperatura.py
   python verificador_bissexto.py
   ```

## 🎯 Objetivos de Aprendizagem

Estes exercícios foram projetados para praticar:
- Entrada e validação de dados do usuário
- Estruturas condicionais (if, elif, else)
- Operações matemáticas básicas
- Classificação por faixas de valores
- Lógica booleana e operadores
- Formatação de saída
- Tratamento de diferentes casos de uso

## 📚 Recursos Adicionais

Para aprofundar seus conhecimentos, estude:
- Tratamento de exceções (try/except)
- Validação robusta de entrada
- Funções para organizar o código
- Interface gráfica com tkinter
- Testes unitários

---

**Nível:** Iniciante
**Linguagem:** Python 3.x
**Tipo:** Exercícios práticos de lógica de programação
