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

### Глубокое обучение для облаков точек LiDAR в автономном вождении: обзор
[2005.09830] дата публикации в arXiv - 05.2020  
📅 дата перевода 07.06.2026  
🏷 `LiDAR point clouds` `deep learning` `3D segmentation` `3D object detection` `3D classification` `autonomous driving` `data representation`

Обзор современных глубоких архитектур для анализа LiDAR точечных облаков в автономном вождении, охватывающий задачи сегментации, детекции и классификации объектов с анализом датасетов, метрик и вызовов.

- [📖 Русская HTML версия](https://romanzorkin.github.io/arxiv_ru/articles/2005.09830/2005.09830_ru.html)
- [📄 Оригинальная статья](https://arxiv.org/abs/2005.09830)
- [🧠 Summary / README](articles/2005.09830/README.md)
- [⚙ Metadata](articles/2005.09830/metadata.json)

---

### Иерархическое глубокое исследование с локальным–веб RAG: к автоматизированному системному поиску материалов
[2511.18303] дата публикации в arXiv - 11.2025  
📅 дата перевода 07.06.2026  
🏷 `materials discovery` `hierarchical reasoning` `retrieval-augmented generation` `large language models` `autonomous agents` `computational materials science` `deep research orchestration`

Предложена локально развёртываемая система глубокого исследования (DR) с иерархической организацией (DToR), объединяющая локальный и веб-поиск с LLM-рассуждениями для решения сложных задач открытия материалов на системном уровне. Система превосходит коммерческие аналоги по качеству отчётов и проверена на 27 темах с последующей верификацией экспертами.

- [📖 Русская HTML версия](https://romanzorkin.github.io/arxiv_ru/articles/2511.18303/2511.18303_ru.html)
- [📄 Оригинальная статья](https://arxiv.org/abs/2511.18303)
- [🧠 Summary / README](articles/2511.18303/README.md)
- [⚙ Metadata](articles/2511.18303/metadata.json)

---

### Искусственный интеллект и экономика США: бухгалтерский взгляд на инвестиции и производство
[2601.11196] дата публикации в arXiv - 01.2026  
📅 дата перевода 07.06.2026  
🏷 `artificial intelligence` `macroeconomics` `data centers` `capital expenditure` `cloud infrastructure` `AI services` `national accounts`

Статья анализирует влияние текущей волны искусственного интеллекта на ВВП США через призму национальных счетов, выделяя ключевую роль дата-центров и показывая, что инвестиции в AI стимулируют спрос, но вклад в рост ВВП ограничен из-за высокого импорта оборудования.

- [📖 Русская HTML версия](https://romanzorkin.github.io/arxiv_ru/articles/2601.11196/2601.11196_ru.html)
- [📄 Оригинальная статья](https://arxiv.org/abs/2601.11196)
- [🧠 Summary / README](articles/2601.11196/README.md)
- [⚙ Metadata](articles/2601.11196/metadata.json)

---

### Учетная тождественность для алгоритмической справедливости
[2601.20217] дата публикации в arXiv - 01.2026  
📅 дата перевода 07.06.2026  
🏷 `algorithmic fairness` `calibration` `binary classification` `regression` `fairness metrics` `predictive accuracy` `fairness tradeoffs`

Статья выводит точную формулу, связывающую точность предсказаний и распространённые метрики справедливости для глобально откалиброванных моделей. Для бинарных исходов сумма взвешенных нарушений справедливости равна «бюджету несправедливости», пропорциональному среднеквадратичной ошибке и разнице в распространённости групп.

- [📖 Русская HTML версия](https://romanzorkin.github.io/arxiv_ru/articles/2601.20217/2601.20217_ru.html)
- [📄 Оригинальная статья](https://arxiv.org/abs/2601.20217)
- [🧠 Summary / README](articles/2601.20217/README.md)
- [⚙ Metadata](articles/2601.20217/metadata.json)

---

### Агентный ИИ в здравоохранении и медицине: семимерное таксономическое описание для эмпирической оценки агентов на основе LLM
[2602.04813] дата публикации в arXiv - 02.2026  
📅 дата перевода 07.06.2026  
🏷 `healthcare AI` `large language models` `agentic AI` `multi-agent systems` `knowledge integration` `clinical decision support` `adaptation mechanisms`

Обзор 49 исследований LLM-агентов в медицине с семимерной таксономией, выявляющей сильные стороны в интеграции внешних знаний и слабые — в адаптации, безопасности и оркестрации. Современные агенты хорошо справляются с информационно-консультационными задачами, но требуют улучшений для надежного клинического применения.

- [📖 Русская HTML версия](https://romanzorkin.github.io/arxiv_ru/articles/2602.04813/2602.04813_ru.html)
- [📄 Оригинальная статья](https://arxiv.org/abs/2602.04813)
- [🧠 Summary / README](articles/2602.04813/README.md)
- [⚙ Metadata](articles/2602.04813/metadata.json)

---

### Сравнительное исследование машинного обучения и глубокого обучения для обнаружения выхода данных за пределы распределения
[2605.10181] дата публикации в arXiv - 05.2026  
📅 дата перевода 07.06.2026  
🏷 `out-of-distribution detection` `fundus imaging` `machine learning` `deep learning` `ExtraTrees` `ResNet-18` `latency analysis`

Для задачи обнаружения выходящих за распределение (OOD) медицинских изображений глазного дна ML-модель ExtraTrees с набором интерпретируемых признаков достигает точности и AUROC, сопоставимых с DL-моделью ResNet-18, при значительно меньшей вычислительной задержке.

- [📖 Русская HTML версия](https://romanzorkin.github.io/arxiv_ru/articles/2605.10181/2605.10181_ru.html)
- [📄 Оригинальная статья](https://arxiv.org/abs/2605.10181)
- [🧠 Summary / README](articles/2605.10181/README.md)
- [⚙ Metadata](articles/2605.10181/metadata.json)

---

### Сравнительная оценка подходов машинного обучения для прогнозирования финансового неблагополучия меньшинственного класса при ограничениях дисбаланса классов
[2605.14067] дата публикации в arXiv - 05.2026  
📅 дата перевода 07.06.2026  
🏷 `financial distress prediction` `class imbalance` `ensemble learning` `SMOTE` `SHAP explainability` `gradient boosting` `minority-class sensitivity`

Статья сравнивает классические статистические, ансамблевые и нейронные модели для предсказания финансовых затруднений при сильном дисбалансе классов, используя SMOTE для балансировки и SHAP для объяснимости. Лучшие результаты показали градиентные бустинговые модели, особенно XGBoost, с акцентом на чувствительность к редким событиям.

- [📖 Русская HTML версия](https://romanzorkin.github.io/arxiv_ru/articles/2605.14067/2605.14067_ru.html)
- [📄 Оригинальная статья](https://arxiv.org/abs/2605.14067)
- [🧠 Summary / README](articles/2605.14067/README.md)
- [⚙ Metadata](articles/2605.14067/metadata.json)

---

## О проекте


Проект — личный research digest и открытый архив интересных научных материалов.


## Архив статей

|id статьи|Месяц публикации|Дата перевода| Тема статьи | Ручной контроль|
|---|---|---|---|---|
| [2005.09830](articles/2005.09830/README.md) | 05.2020 | 07.06.2026 | Глубокое обучение для облаков точек LiDAR в автономном вождении: обзор (`Deep Learning for LiDAR Point Clouds in Autonomous Driving: A Review`) |✅|
| [2511.18303](articles/2511.18303/README.md) | 11.2025 | 07.06.2026 | Иерархическое глубокое исследование с локальным–веб RAG: к автоматизированному системному поиску материалов (`Hierarchical Deep Research with Local–Web RAG: Toward Automated System-Level Materials Discovery`) |✅|
| [2601.11196](articles/2601.11196/README.md) | 01.2026 | 07.06.2026 | Искусственный интеллект и экономика США: бухгалтерский взгляд на инвестиции и производство (`Artificial Intelligence and the US Economy: An Accounting Perspective on Investment and Production`) |✅|
| [2601.20217](articles/2601.20217/README.md) | 01.2026 | 07.06.2026 | Учетная тождественность для алгоритмической справедливости (`An Accounting Identity for Algorithmic Fairness`) ||
| [2602.04813](articles/2602.04813/README.md) | 02.2026 | 07.06.2026 | Агентный ИИ в здравоохранении и медицине: семимерное таксономическое описание для эмпирической оценки агентов на основе LLM (`Agentic AI in Healthcare & Medicine: A Seven-Dimensional Taxonomy for Empirical Evaluation of LLM-based Agents`) ||
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
