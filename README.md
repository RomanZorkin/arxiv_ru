[![GitHub](https://img.shields.io/badge/Репозиторий-GitHub-blue?style=flat&logo=github&logoColor=white)](https://github.com/RomanZorkin/arxiv_ru)


## Russian arXiv Digest | arxiv_ru

Русскоязычные переводы и краткие разборы arXiv статей  по AI, ML, multi-agent systems и orchestration.
Новости о еженедельных обновлениях публикуются в сообществе https://t.me/pythonbarnaul

---

🤖 LLM / Agents

Для навигации по репозиторию используйте:

[repository_map.json](https://github.com/RomanZorkin/arxiv_ru/blob/main/repository_map.json) — структура проекта и правила навигации

[knowledge_index.json](https://github.com/RomanZorkin/arxiv_ru/blob/main/knowledge_index.json) — индекс всех статей и метаданные


LLM должна начинать работу с этих файлов, а не с обхода каталога articles/.

---


## Структура проекта
```
├── README.md                     # Главная страница репозитория и навигация по статьям
├── articles/                     # Каталог со всеми обработанными статьями
│   ├── 2403.08386/               # Каталог отдельной arXiv статьи
│   │   ├── [2403.08386]...       # Служебные CSS/JS/изображения для рэндэринга HTML
│   │   ├── 2403.08386.html       # Оригинальная HTML версия статьи с arXiv
│   │   ├── 2403.08386_ru.html    # Переведённая русскоязычная HTML версия статьи
│   │   ├── article_rag.json      # Структурированное AI/RAG представление статьи
│   │   ├── metadata.json         # Метаданные статьи, теги, summary и ссылки
│   │   └── README.md             # Краткий разбор статьи и основные выводы
│   ├── 2503.13754/               # Каталог другой статьи в аналогичном формате
```

В каждом каталоге находится зеркало оригинальной статьи, её перевод на русский язык и метаданные. 

Источником является **ar5iv.labs.arxiv.org** — проект, который предоставляет статьи arXiv в удобном responsive HTML5 формате (а не только PDF). Если свежая статья ещё не обработана ar5iv, оригинальный HTML берётся напрямую с arxiv.org.

Основной механизм перевода — автоматический перевод оригинального HTML в русскоязычную HTML-версию. Такой подход позволяет сохранить форматирование, формулы и изображения.

<p align="center">
  <img src="assets/arxiv_en.png" width="49%">
  <img src="assets/arxiv_ru.png" width="49%">
</p>

## Тезисы

- Перевод на ~98% формируется автоматически
- Явные ошибки и несогласованности дорабатываются вручную
- Полученный перевод **не является** точным техническим переводом, часть недочётов сохраняется
- **Рекомендуется** читать вместе с оригиналом для получения полного контекста

## Сила Rag

В каталоге статьи находится файл article_rag.json — это структурированное AI/RAG-представление статьи.

При изучении статьи я прикрепляю этот файл к чату (ChatGPT, DeepSeek, и т.д.), объясняю, что это контекст нашей беседы, и по мере возникновения вопросов прошу модель просто объяснить мне интересующие моменты.

Результат — просто пушка 🚀
Ниже приведен скрин одной из таких бесед:
<p align="center">
  <img src="assets/arxiv_rag.png" width="80%">
</p>

В LLM был загружен только JSON-файл статьи [RoSHAP](https://arxiv.org/html/2605.15154), после чего был задан вопрос, вырванный из контекста.

Обратите внимание, насколько подробно и структурированно был получен ответ, включая объяснения и формулы.

## Возможность участия

Вы можете предлагать интересные статьи для перевода, присылать свои исправления, замечания по качеству переводов и активно обсуждать материалы.

---

# 🔥 Последние статьи
> Новые переводы и разборы arXiv-статей
---

# Блок «Последние статьи»
# Вставить в README.md после заголовка «# 🔥 Последние статьи»

### Готовы ли LLM к реальному открытию материалов?
[2402.05200] дата публикации в arXiv - 02.2024  
📅 дата перевода 18.06.2026  
🏷 `materials science` `large language models` `domain-specific LLM` `multi-modal datasets` `hypothesis generation` `automated materials design` `self-driving labs`

LLMs обладают потенциалом ускорить открытие материалов, но пока не справляются с глубоким пониманием и рассуждениями в материаловедении. Для прогресса нужны специализированные модели MatSci-LLMs, обученные на больших мульти-модальных датасетах и интегрированные с экспериментальными и симуляционными инструментами.

- [📖 Русская HTML версия](https://romanzorkin.github.io/arxiv_ru/articles/2402.05200/2402.05200_ru.html)
- [📄 Оригинальная статья](https://arxiv.org/abs/2402.05200)
- [🧠 Summary / README](articles/2402.05200/README.md)
- [⚙ Metadata](articles/2402.05200/metadata.json)

---

### Банкинг, сделанный правильно: переосмысление розничного банкинга с помощью языко-ориентированного ИИ
[2510.07645] дата публикации в arXiv - 10.2025  
📅 дата перевода 21.06.2026  
🏷 `retail banking` `large language models` `multi-agent system` `conversational AI` `financial transactions` `regulatory compliance` `intent classification`

Представлена Ryt AI — первая в мире лицензированная банковская система, где крупная языковая модель (LLM) служит основным интерфейсом для выполнения финансовых операций через естественный язык. Система обеспечивает безопасность, соответствие регуляциям и заменяет многократные экраны диалогом с несколькими специализированными агентами.

- [📖 Русская HTML версия](https://romanzorkin.github.io/arxiv_ru/articles/2510.07645/2510.07645_ru.html)
- [📄 Оригинальная статья](https://arxiv.org/abs/2510.07645)
- [🧠 Summary / README](articles/2510.07645/README.md)
- [⚙ Metadata](articles/2510.07645/metadata.json)

---

### Цифровой двойник ИИ: возможности и вызовы от больших языковых моделей к моделям мира
[2601.01321] дата публикации в arXiv - 01.2026  
📅 дата перевода 17.06.2026  
🏷 `digital twins` `physics-informed AI` `large language models` `generative AI` `predictive maintenance` `autonomous management` `multimodal perception`

Статья предлагает унифицированную четырехэтапную структуру интеграции ИИ в жизненный цикл цифровых двойников, охватывающую моделирование, зеркалирование, вмешательство и автономное управление, с акцентом на синергию физического моделирования и генеративного ИИ, а также анализирует вызовы и применения в 11 областях.

- [📖 Русская HTML версия](https://romanzorkin.github.io/arxiv_ru/articles/2601.01321/2601.01321_ru.html)
- [📄 Оригинальная статья](https://arxiv.org/abs/2601.01321)
- [🧠 Summary / README](articles/2601.01321/README.md)
- [⚙ Metadata](articles/2601.01321/metadata.json)

---

### Масштабирование верификации медицинских рассуждений с помощью инструментально-интегрированного обучения с подкреплением
[2601.20221] дата публикации в arXiv - 01.2026  
📅 дата перевода 17.06.2026  
🏷 `medical reasoning` `reinforcement learning` `tool-augmented verification` `large language models` `retrieval-augmented generation` `medical question answering` `curriculum learning`

Предложена Med-TIV — агентная система верификации медицинских рассуждений, использующая итеративный поиск по медицинским корпусам и обучение с подкреплением с адаптивным курсом. Med-TIV значительно улучшает точность и эффективность по сравнению с существующими методами на четырёх медицинских бенчмарках.

- [📖 Русская HTML версия](https://romanzorkin.github.io/arxiv_ru/articles/2601.20221/2601.20221_ru.html)
- [📄 Оригинальная статья](https://arxiv.org/abs/2601.20221)
- [🧠 Summary / README](articles/2601.20221/README.md)
- [⚙ Metadata](articles/2601.20221/metadata.json)

---

### Автономные агенты, координирующие распределённый поиск посредством возникающего обмена артефактами
[2603.14312] дата публикации в arXiv - 03.2026  
📅 дата перевода 20.06.2026  
🏷 `autonomous scientific agents` `artifact provenance` `multi-agent coordination` `emergent collaboration` `scientific skill chaining` `distributed discovery` `cross-domain synthesis`

Представлен фреймворк ScienceClaw + Infinite для автономного научного исследования с независимыми агентами, которые координируются через обмен неизменяемыми артефактами и открытыми запросами, обеспечивая трассируемость, синтез и коллективное открытие без центрального планировщика.

- [📖 Русская HTML версия](https://romanzorkin.github.io/arxiv_ru/articles/2603.14312/2603.14312_ru.html)
- [📄 Оригинальная статья](https://arxiv.org/abs/2603.14312)
- [🧠 Summary / README](articles/2603.14312/README.md)
- [⚙ Metadata](articles/2603.14312/metadata.json)

---

### Баланс устойчивости и пластичности при последовательном обучении Раннее прекращение нейронных сетей
[2605.05358] дата публикации в arXiv - 05.2026  
📅 дата перевода 17.06.2026  
🏷 `early-exiting neural networks` `sequential training` `elastic weight consolidation` `learning without forgetting` `stability-plasticity trade-off` `CIFAR-100 benchmark` `resource-efficient inference`

Предложены два метода регуляризации для последовательного обучения нейросетей с ранним выходом, позволяющие сохранить производительность ранее обученных выходов при добавлении новых, что улучшает точность и снижает вычислительные затраты на стандартных бенчмарках.

- [📖 Русская HTML версия](https://romanzorkin.github.io/arxiv_ru/articles/2605.05358/2605.05358_ru.html)
- [📄 Оригинальная статья](https://arxiv.org/abs/2605.05358)
- [🧠 Summary / README](articles/2605.05358/README.md)
- [⚙ Metadata](articles/2605.05358/metadata.json)

---

### Прогнозирование кривой доходности с использованием машинного обучения и эконометрики: сравнительный анализ
[2605.09842] дата публикации в arXiv - 05.2026  
📅 дата перевода 17.06.2026  
🏷 `yield curve forecasting` `ARIMA` `TimeGPT` `deep learning` `econometrics` `transformers` `financial time series`

Сравнительный анализ методов прогнозирования кривой доходности казначейских облигаций США за 47 лет показал, что традиционные эконометрические модели ARIMA и наивные методы превосходят современные методы машинного обучения и глубокого обучения, за исключением одного временного блока, где лучше проявились трансформеры PatchTST и TFT.

- [📖 Русская HTML версия](https://romanzorkin.github.io/arxiv_ru/articles/2605.09842/2605.09842_ru.html)
- [📄 Оригинальная статья](https://arxiv.org/abs/2605.09842)
- [🧠 Summary / README](articles/2605.09842/README.md)
- [⚙ Metadata](articles/2605.09842/metadata.json)

---

### Динамическое управление жизненным циклом навыков в агентном обучении с подкреплением
[2605.10923] дата публикации в arXiv - 05.2026  
📅 дата перевода 21.06.2026  
🏷 `agentic reinforcement learning` `skill lifecycle management` `large language models` `hierarchical skill retrieval` `marginal external contribution` `leave-one-skill-out validation` `dynamic skill expansion`

Предложена SLIM — метод динамического управления активным набором внешних навыков в агентном обучении с подкреплением, который оценивает маргинальный вклад навыков и применяет операции сохранения, удаления и расширения навыков. SLIM превосходит существующие методы на ALFWorld и SearchQA, обеспечивая адаптивный, не монотонный жизненный цикл навыков.

- [📖 Русская HTML версия](https://romanzorkin.github.io/arxiv_ru/articles/2605.10923/2605.10923_ru.html)
- [📄 Оригинальная статья](https://arxiv.org/abs/2605.10923)
- [🧠 Summary / README](articles/2605.10923/README.md)
- [⚙ Metadata](articles/2605.10923/metadata.json)

---

### VideoMLA: Кэш KV скрытых признаков с низким рангом для авторегрессионной видеодиффузии с минутным масштабом
[2605.30351] дата публикации в arXiv - 05.2026  
📅 дата перевода 17.06.2026  
🏷 `video diffusion` `latent attention` `autoregressive model` `KV cache compression` `3D rotary embeddings` `long-horizon generation` `memory efficiency`

VideoMLA внедряет Multi-Head Latent Attention (MLA) в видео-диффузию, заменяя плотный per-head KV-кэш общим низкоранговым латентом и разделённым 3D-RoPE позиционным ключом, снижая память на 92.7% и сохраняя качество генерации минутных видео с улучшенной производительностью.

- [📖 Русская HTML версия](https://romanzorkin.github.io/arxiv_ru/articles/2605.30351/2605.30351_ru.html)
- [📄 Оригинальная статья](https://arxiv.org/abs/2605.30351)
- [🧠 Summary / README](articles/2605.30351/README.md)
- [⚙ Metadata](articles/2605.30351/metadata.json)

---

## О проекте


Проект — личный research digest и открытый архив интересных научных материалов.


## Архив статей

|id статьи|Месяц публикации|Дата перевода| Тема статьи | Ручной контроль|
|---|---|---|---|---|
| [2402.05200](articles/2402.05200/README.md) | 02.2024 | 18.06.2026 | Готовы ли LLM к реальному открытию материалов? (`Are LLMs Ready for Real-World Materials Discovery?`) ||
| [2510.07645](articles/2510.07645/README.md) | 10.2025 | 21.06.2026 | Банкинг, сделанный правильно: переосмысление розничного банкинга с помощью языко-ориентированного ИИ (`Banking Done Right: Redefining Retail Banking with Language-Centric AI`) ||
| [2601.01321](articles/2601.01321/README.md) | 01.2026 | 17.06.2026 | Цифровой двойник ИИ: возможности и вызовы от больших языковых моделей к моделям мира (`Digital Twin AI: Opportunities and Challenges from Large Language Models to World Models`) ||
| [2601.20221](articles/2601.20221/README.md) | 01.2026 | 17.06.2026 | Масштабирование верификации медицинских рассуждений с помощью инструментально-интегрированного обучения с подкреплением (`Scaling Medical Reasoning Verification via Tool-Integrated Reinforcement Learning`) ||
| [2603.14312](articles/2603.14312/README.md) | 03.2026 | 20.06.2026 | Автономные агенты, координирующие распределённый поиск посредством возникающего обмена артефактами (`Autonomous Agents Coordinating Distributed Discovery Through Emergent Artifact Exchange`) ||
| [2605.05358](articles/2605.05358/README.md) | 05.2026 | 17.06.2026 | Баланс устойчивости и пластичности при последовательном обучении Раннее прекращение нейронных сетей (`Balancing Stability and Plasticity in Sequentially Trained Early-Exiting Neural Networks`) ||
| [2605.09842](articles/2605.09842/README.md) | 05.2026 | 17.06.2026 | Прогнозирование кривой доходности с использованием машинного обучения и эконометрики: сравнительный анализ (`Yield Curve Forecasting using Machine Learning and Econometrics: A Comparative Analysis`) ||
| [2605.10923](articles/2605.10923/README.md) | 05.2026 | 21.06.2026 | Динамическое управление жизненным циклом навыков в агентном обучении с подкреплением (`Dynamic Skill Lifecycle Management for Agentic Reinforcement Learning`) ||
| [2605.30351](articles/2605.30351/README.md) | 05.2026 | 17.06.2026 | VideoMLA: Кэш KV скрытых признаков с низким рангом для авторегрессионной видеодиффузии с минутным масштабом (`VideoMLA: Low-Rank Latent KV Cache for Minute-Scale Autoregressive Video Diffusion`) ||
| [2005.09830](articles/2005.09830/README.md) | 05.2020 | 07.06.2026 | Глубокое обучение для облаков точек LiDAR в автономном вождении: обзор (`Deep Learning for LiDAR Point Clouds in Autonomous Driving: A Review`) |✅|
| [2511.18303](articles/2511.18303/README.md) | 11.2025 | 07.06.2026 | Иерархическое глубокое исследование с локальным–веб RAG: к автоматизированному системному поиску материалов (`Hierarchical Deep Research with Local–Web RAG: Toward Automated System-Level Materials Discovery`) |✅|
| [2601.11196](articles/2601.11196/README.md) | 01.2026 | 07.06.2026 | Искусственный интеллект и экономика США: бухгалтерский взгляд на инвестиции и производство (`Artificial Intelligence and the US Economy: An Accounting Perspective on Investment and Production`) |✅|
| [2601.20217](articles/2601.20217/README.md) | 01.2026 | 07.06.2026 | Учетная тождественность для алгоритмической справедливости (`An Accounting Identity for Algorithmic Fairness`) ||
| [2602.04813](articles/2602.04813/README.md) | 02.2026 | 07.06.2026 | Агентный ИИ в здравоохранении и медицине: семимерное таксономическое описание для эмпирической оценки агентов на основе LLM (`Agentic AI in Healthcare & Medicine: A Seven-Dimensional Taxonomy for Empirical Evaluation of LLM-based Agents`) |✅|
| [2605.10181](articles/2605.10181/README.md) | 05.2026 | 07.06.2026 | Сравнительное исследование машинного обучения и глубокого обучения для обнаружения выхода данных за пределы распределения (`A Comparative Study of Machine Learning and Deep Learning for Out-of-Distribution Detection`) ||
| [2605.14067](articles/2605.14067/README.md) | 05.2026 | 07.06.2026 | Сравнительная оценка подходов машинного обучения для прогнозирования финансового неблагополучия миноритарного класса при ограничениях дисбаланса классов (`Comparative Evaluation of Machine Learning Approaches for Minority-Class Financial Distress Prediction Under Class Imbalance Constraints`) |✅|
| [2501.19195](articles/2501.19195/README.md) | 01.2025 | 06.06.2026 | Переосмысление ранней остановки: уточните, затем откалибруйте (`Rethinking Early Stopping: Refine, Then Calibrate`) |✅|
| [2504.03629](articles/2504.03629/README.md) | 04.2025 | 01.06.2026 | SeGuE: Семантически управляемое исследование для мобильных роботов (`SeGuE: Semantic Guided Exploration for Mobile Robots`) |✅|
| [2512.12087](articles/2512.12087/README.md) | 12.2025 | 31.05.2026 | BLASST: динамическое блочное разрежение механизма внимания с использованием порогового отсечения Softmax (`BLASST: Dynamic BLocked Attention Sparsity via Softmax Thresholding`) |✅|
| [2512.13168](articles/2512.13168/README.md) | 12.2025 | 01.06.2026 | Finch: Бенчмаркинг финансов и бухгалтерии в корпоративных рабочих процессах, основанных на таблицах (`Finch: Benchmarking Finance & Accounting across Spreadsheet-Centric Enterprise Workflows`) |✅|
| [2603.16086](articles/2603.16086/README.md) | 03.2026 | 01.06.2026 | К парадигме «Зрение–Звук–Язык–Действие»: фреймворк HEAR для манипулирования, ориентированного на звук (`Towards the Vision-Sound-Language-Action Paradigm: The HEAR Framework for Sound-Centric Manipulation`) |✅|
| [2604.00835](articles/2604.00835/README.md) | 04.2026 | 01.06.2026 | Агентное использование инструментов в больших языковых моделях (`Agentic Tool Use in Large Language Models`) |✅|
| [2605.03823](articles/2605.03823/README.md) | 05.2026 | 06.06.2026 | Реализуемая Байесовская согласованность для общих функций потерь метрик (`Realizable Bayes-Consistency for General Metric Losses`) |✅|
| [2601.06707](articles/2601.06707/README.md) | 01.2026 | 25.05.2026 | Оценка способностей к бухгалтерским рассуждениям больших языковых моделей (`Evaluating Accounting Reasoning Capabilities of Large Language Models`) |✅|
| [2307.05845](articles/2307.05845/README.md) | 07.2023 | 25.05.2026 | PIGEON: Прогнозирование геолокаций изображений (`PIGEON: Predicting Image Geolocations`) ||
| [2605.06226](articles/2605.06226/README.md) | 05.2026 | 24.05.2026 | Универсальный ИИ-агент для диагностики редких заболеваний и приоритизации генов риска (`A Versatile AI Agent for Rare Disease Diagnosis and Risk Gene Prioritization`) |✅|
| [2605.15154](articles/2605.15154/README.md) | 05.2026 | 24.05.2026 | RoSHAP: распределительный фреймворк и робастная метрика для стабильной атрибуции признаков (`RoSHAP: A Distributional Framework and Robust Metric for Stable Feature Attribution`) |✅|
| [2605.02943](articles/2605.02943/README.md) | 05.2026 | 17.05.2026 | Healthcare AI GYM для медицинских агентов (`Healthcare AI GYM for Medical Agents`) |✅|
| [2601.12882](articles/2601.12882/README.md) | 01.2026 | 23.05.2026 | YOLO26: Анализ сквозной структуры без NMS для обнаружения объектов в реальном времени (`YOLO26: An Analysis of NMS-Free End to End Framework for Real-Time Object Detection`) |✅|
| [2601.16392](articles/2601.16392/README.md) | 01.2026 | 23.05.2026 | К агентивному управлению программными проектами: видение и дорожная карта (`Toward Agentic Software Project Management: A Vision and Roadmap`) |✅|
| [2510.08612](articles/2510.08612/README.md) | 10.2025 | 23.05.2026 | Влияние LLM на командное сотрудничество в разработке программного обеспечения (`Impact of LLMs on Team Collaboration in Software Development`) |✅|
| [2503.13754](articles/2503.13754/README.md) | 03.2025 | 23.05.2026 | От автономных агентов к интегрированным системам, новая парадигма: оркестрованный распределенный интеллект (`From Autonomous Agents to Integrated Systems, A New Paradigm: Orchestrated Distributed Intelligence`) ||
| [2403.08386](articles/2403.08386/README.md) | 03.2024 | 24.05.2026 | Оптимизация избегающих риска гибридных команд человек-ИИ (`Optimizing Risk-averse Human-AI Hybrid Teams`) |✅|
| [2503.09794](articles/2503.09794/README.md) | 03.2025 | 24.05.2026 | Усиление командной работы с помощью ИИ-агентов в качестве пространственных коллабораторов (`Augmenting Teamwork through AI Agents as Spatial Collaborators`) ||
| [2501.02368](articles/2501.02368/README.md) | 01.2025 | 24.05.2026 | Повышение продуктивности и благополучия на рабочем месте с помощью ИИ-агентов (`Enhancing Workplace Productivity and Well-Being using AI Agents`) ||
| [2504.14996](articles/2504.14996/README.md) | 04.2025 | 24.05.2026 | Распределенное познание для удаленных операций с поддержкой ИИ: вызовы и направления исследований (`Distributed Cognition for AI-supported Remote Operations: Challenges and Research Directions`) ||
| [2605.99001](articles/2605.99001/README.md) | 05.2026 | 24.05.2026 | DeepSeek-V4: На пути к высокоэффективному интеллекту контекста из миллиона токенов (`DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence`) ||
| [1810.04805](articles/1810.04805/README.md) | 10.2018 | 24.05.2026 | BERT : Предварительное обучение глубоких двунаправленных трансформеров для Понимание языка (`BERT : Pre-training of Deep Bidirectional Transformers for Language Understanding`) ||
| [1506.02640](articles/1506.02640/README.md) | 06.2015 | 24.05.2026 | Вы смотрите только один раз: Унифицированное обнаружение объектов в реальном времени (`You Only Look Once: Unified, Real-Time Object Detection`) ||
| [1706.03762](articles/1706.03762/README.md) | 06.2017 | 24.05.2026 | Внимание — это всё, что вам нужно (`Attention Is All You Need`) ||
| [1512.03385](articles/1512.03385/README.md) | 12.2015 | 24.05.2026 | Глубокое остаточное обучение для распознавания изображений (`Deep Residual Learning for Image Recognition`) ||
| [1710.10903](articles/1710.10903/README.md) | 10.2017 | 24.05.2026 | Графовые сети внимания (`Graph Attention Networks`) ||
| [1910.01736](articles/1910.01736/README.md) | 10.2019 | 24.05.2026 | Контекстно-зависимые графовые сети внимания (`Context-Aware Graph Attention Networks`) ||
| [2010.11929](articles/2010.11929/README.md) | 10.2020 | 24.05.2026 | Изображение стоит 16x16 слов: Трансформеры для распознавания изображений в масштабе (`An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale`) ||
| [2005.14165](articles/2005.14165/README.md) | 05.2020 | 24.05.2026 | Языковые модели — обучающиеся с несколькими примерами (`Language Models are Few-Shot Learners`) ||
