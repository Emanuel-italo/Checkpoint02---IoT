# Avaliação IA Generativa: Suporte Técnico de IoT

## Integrantes
- Emanuel Italo (RM 561337)
- Enzo Monteiro Maciel (RM 563734)
- Gabriel Bebé Silva (RM 562012)
- Matheus de Almeida Sousa (RM 563557)
- Paulo Estalise (RM 563811)

## Tema
**Tema 2: Suporte técnico de IoT.**

O **IoT Help** é um assistente de IA generativa que ajuda a diagnosticar problemas comuns com ESP32, Arduino, conexão Wi-Fi e sensores (DHT11/DHT22, HC-SR04, PIR, LDR). Ele cobre ligação elétrica, alimentação, bibliotecas e código, sugere testes simples para confirmar a causa do problema e recusa perguntas fora do tema. O assistente usa dois modelos: `meta-llama/Llama-3.1-8B-Instruct` (Hugging Face Inference API) e `gemini-2.5-flash-lite` (Google Gemini API).

## System prompt usado
```
Você é o IoT Help, um assistente de suporte técnico de IoT.
Ajude o usuário a diagnosticar problemas comuns com ESP32, Arduino, conexão Wi-Fi e sensores
(ex.: DHT11/DHT22, HC-SR04, PIR, LDR), incluindo ligação elétrica, alimentação, bibliotecas e código.
Responda sempre em português, de forma clara, em no máximo 5 frases.
Quando fizer sentido, sugira um teste simples para o usuário confirmar a causa do problema.
Se o problema envolver a rede elétrica da casa (127V/220V), recomende procurar um eletricista.
Se a pergunta não tiver relação com suporte técnico de IoT, diga educadamente que não pode ajudar.
```

## Etapas realizadas
- [ ] Etapa 1: Assistente com guardrails
- [ ] Etapa 2: Comparação com temperatura
- [ ] Etapa 3: Chat com memória e troca de modelo
- [ ] Etapa 4: Interface Gradio com temperatura
- [ ] Etapa 5 (bônus): API com sessões independentes

## Interface
![Interface Gradio](prints/gradio.png)
