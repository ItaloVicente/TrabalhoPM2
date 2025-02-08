# README: Programa de Otimização Linear

## **Descrição Geral**
Este programa foi desenvolvido para resolver problemas de otimização linear utilizando o método simplex. O programa aceita como entrada a função objetivo, as restrições e a direção da otimização (Maximização ou Minimização). É possível resolver problemas baseados em várias questões, onde os resultados de cada questão são exibidos sequencialmente ao pressionar Enter.

## **Principais Características**
1. **Função Personalizada**:
   - Permite passar como parâmetros:
     - A **função objetivo**.
     - As **restrições** do problema.
     - A direção da otimização (**Max** ou **Min**).

2. **Resolução Interativa**:
   - Os resultados são apresentados de forma interativa, onde o usuário pressiona Enter para avançar para a próxima questão.

3. **Resultados Detalhados**:
   - Para cada questão, o programa exibe os seguintes resultados:
     - **Status**: Indica se o problema foi resolvido com sucesso.
     - **Valor da Função Objetivo**: Resultado final de otimização.
     - **Valores das Variáveis de Decisão**: Valores ótimos encontrados para cada variável.

## **Como Funciona**
Ao executar o programa, ele solicita os parâmetros do problema e resolve as questões baseadas nos cenários fornecidos.

Os resultados das questões são exibidos conforme descrito abaixo:

### **Exemplo de Execução**

#### **Questão 1**
- O usuário pressiona **Enter** para iniciar a questão 1.
- O programa exibe:
  ```
  Resultados Questão 1: {'status': 'ok', 'objective': 9.0, 'x3': 2.0, 'x4': 0.0, 'x1': 2.0, 'x2': 1.0}
  ```

#### **Questão 2**
- Pressione **Enter** para iniciar a questão 2.
- O programa calcula os tempos de trabalho considerando que trabalham 8 horas por dia durante 5 dias:
  ```
  Corte: 25 x 8 x 5 x 60 = 60000 minutos
  Costura: 35 x 8 x 5 x 60 = 84000 minutos
  Embalagem: 5 x 8 x 5 x 60 = 12000 minutos
  ```
- Resultados:
  ```
  Resultados Questão 2: {'status': 'ok', 'objective': 13920.0, 'x1': 480.0, 'x2': 840.0}
  ```

#### **Questão 3**
- Pressione **Enter** para iniciar a questão 3.
- Resultados originais:
  ```
  Resultados Simplex (Original): {'status': 'ok', 'objective': 882.0, 'x3': 2.0, 'x1': 0.0, 'x2': 36.0}
  ```

**Resultados para cada variação:**

- **Item (a)**: Disponibilidade de couro aumentada para 45 pés:
  ```
  Resultados Simplex: {'status': 'ok', 'objective': 885.0, 'x3': 5.0, 'x1': 0.0, 'x2': 30.0}
  ```

- **Item (b)**: Disponibilidade de couro reduzida em 1 pé:
  ```
  Resultados Simplex: {'status': 'ok', 'objective': 881.0, 'x3': 1.0, 'x1': 0.0, 'x2': 38.0}
  ```

- **Item (c)**: Horas de costura alteradas para 38 horas:
  ```
  Resultados Simplex: {'status': 'ok', 'objective': 840.0, 'x3': 4.0, 'x1': 0.0, 'x2': 30.0}
  ```

- **Item (d)**: Horas de costura alteradas para 46 horas:
  ```
  Resultados Simplex: {'status': 'ok', 'objective': 924.0, 'x3': 0.0, 'x1': 0.0, 'x2': 42.0}
  ```

- **Item (e)**: Horas de acabamento reduzidas para 15 horas:
  ```
  Resultados Simplex: {'status': 'ok', 'objective': 672.0, 'x3': 12.0, 'x1': 0.0, 'x2': 6.0}
  ```

- **Item (f)**: Horas de acabamento aumentadas para 50 horas:
  ```
  Resultados Simplex: {'status': 'ok', 'objective': 882.0, 'x3': 2.0, 'x1': 0.0, 'x2': 36.0}
  ```

- **Item (g)**: Contratação de um trabalhador para costura:
  - Mais 8 horas diárias disponíveis (40 horas semanais).
  - Nova restrição de costura:
    ```
    {'expression': {'x1': 2, 'x2': 1, 'x3': 2}, 'rhs': 48, 'operator': '<='}
    ```
  - Avaliação: Vale a pena, pois o aumento no valor de \( Z \) supre mais de 15 reais:
    - Valor original: \( Z_{original} = 882.0 \)
    - Novo valor: \( Z_{novo} = 924.0 \)

## **Instruções para Execução**
1. Certifique-se de que você tem o Python instalado em sua máquina.
2. Instale as dependências necessárias executando:
   ```bash
   pip install pulp
   ```
3. Execute o programa e siga as instruções na tela.

## **Observações**
- Caso precise de suporte ou deseje adicionar novos cenários, entre em contato com o desenvolvedor.



