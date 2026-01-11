 ### Detecção de Fraudes com Machine Learning

Este projeto desenvolve um modelo de detecção de fraudes em transações financeiras utilizando técnicas de aprendizado supervisionado.
 O foco é identificar transações fraudulentas em meio a uma base altamente desbalanceada, 
 garantindo alta taxa de detecção (recall) sem aumentar demasiadamente os falsos positivos.
________________________________________________________________________________________________________________________________________________________

*  Objetivos
Construir um pipeline completo e automatizado de detecção de fraudes.
Corrigir o desbalanceamento de classes e evitar data leakage.


___________________________________________________________________________________________________________________________________________________

*  Pipeline de Modelagem

O projeto foi estruturado a partir de um pipeline completo de Machine Learning, garantindo reprodutibilidade, escalabilidade e ausência de vazamento de dados. O pipeline contempla as etapas de pré-processamento, redução de dimensionalidade com PCA e modelagem preditiva, permitindo que todas as transformações aplicadas nos dados de treino sejam reproduzidas de forma consistente em novos dados.
________________________________________________________________________________________________________________________________________________________

*  Balanceamento de Classes

Como o problema de detecção de fraude apresenta alto desbalanceamento entre classes, foram adotadas estratégias específicas para mitigar esse efeito durante o treinamento do modelo. O balanceamento foi tratado diretamente no processo de modelagem, de forma a melhorar a capacidade do modelo em identificar a classe minoritária (fraude), sem comprometer a taxa de falsos positivos.
______________________________________________________________________________________________________________________________________________________________
*  Modelagem

O modelo final selecionado foi uma Regressão Logística, integrada ao pipeline. A escolha se deu por sua robustez, interpretabilidade e bom desempenho em cenários de classificação binária desbalanceada, além de ser amplamente utilizada em aplicações reais de detecção de fraude. A utilização de PCA contribuiu para reduzir ruído e multicolinearidade entre as variáveis de entrada.
______________________________________________________________________________________________________________________________________________________________
*  Resultados

O modelo apresentou boa capacidade de generalização, mantendo desempenho consistente tanto no conjunto de validação quanto na avaliação fora da amostra. A análise das curvas ROC e Precision-Recall demonstrou que o modelo é capaz de separar adequadamente transações legítimas de transações fraudulentas, mesmo em um cenário realista de produção.
As principais Métricas utilizadas foram ROC-AUC: utilizada como métrica global de discriminação do modelo ,Precision e Recall da classe fraude: priorizando a redução de fraudes não detectadas , F1-score: para equilibrar precisão e sensibilidade , Matriz de confusão: para análise operacional de falsos positivos e falsos negativos.

Essas métricas foram utilizadas tanto na escolha do threshold ótimo quanto na simulação do comportamento do modelo em produção.






