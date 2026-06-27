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

### Справедливость в найме с применением ИИ: проблемы, показатели, методы и будущие направления
[2405.19699] дата публикации в arXiv - 05.2024  
📅 дата перевода 27.06.2026  
🏷 `AI fairness` `recruitment bias` `fairness metrics` `bias mitigation` `large language models` `hiring automation` `algorithmic transparency`

Статья систематически рассматривает проблему справедливости в системах AI-рекрутмента, анализирует виды предвзятости, метрики оценки, методы устранения и законодательные аспекты, а также выделяет ключевые вызовы и направления будущих исследований.

- [📖 Русская HTML версия](https://romanzorkin.github.io/arxiv_ru/articles/2405.19699/2405.19699_ru.html)
- [📄 Оригинальная статья](https://arxiv.org/abs/2405.19699)
- [🧠 Summary / README](articles/2405.19699/README.md)
- [⚙ Metadata](articles/2405.19699/metadata.json)

---

### Чем больше, тем веселее: логические и многоступенчатые процессоры в скоринге кредитоспособности
[2503.23979] дата публикации в arXiv - 03.2025  
📅 дата перевода 27.06.2026  
🏷 `fairness metrics` `credit scoring` `logical processors` `multistage processors` `adversarial debiasing` `bias mitigation` `machine learning fairness`

Предложены логические процессоры для обработки нескольких чувствительных переменных и многоступенчатые процессоры, комбинирующие методы справедливости на разных этапах ML-пайплайна. Эксперименты на симуляциях и реальных данных показывают улучшение точности и справедливости моделей кредитного скоринга.

- [📖 Русская HTML версия](https://romanzorkin.github.io/arxiv_ru/articles/2503.23979/2503.23979_ru.html)
- [📄 Оригинальная статья](https://arxiv.org/abs/2503.23979)
- [🧠 Summary / README](articles/2503.23979/README.md)
- [⚙ Metadata](articles/2503.23979/metadata.json)

---

### Управление человеческими ресурсами и ИИ: контекстная база данных для прозрачности
[2511.03916] дата публикации в arXiv - 11.2025  
📅 дата перевода 27.06.2026  
🏷 `human resource management` `AI transparency` `HR technology` `recruiting AI` `contextual transparency` `practitioner-centered design` `AI clarity assessment`

Статья представляет TARAI Index — базу данных, которая через анализ функциональности, заявлений, предположений и ясности ИИ в HR Tech продуктах обеспечивает контекстную прозрачность ИИ в практике рекрутинга, основанную на эмпирических данных и профессиональных практиках.

- [📖 Русская HTML версия](https://romanzorkin.github.io/arxiv_ru/articles/2511.03916/2511.03916_ru.html)
- [📄 Оригинальная статья](https://arxiv.org/abs/2511.03916)
- [🧠 Summary / README](articles/2511.03916/README.md)
- [⚙ Metadata](articles/2511.03916/metadata.json)

---

### Алгоритмическое управление и будущее человеческого труда: последствия для автономии, сотрудничества и инноваций
[2511.14231] дата публикации в arXiv - 11.2025  
📅 дата перевода 27.06.2026  
🏷 `algorithmic management` `human-computer interaction` `employee autonomy` `organizational innovation` `sociotechnical systems` `algorithmic accountability` `workplace surveillance`

Статья анализирует влияние алгоритмического управления на практики HRM, выделяя риски для автономии сотрудников, прозрачности процедур и инновационной деятельности. Предлагается социотехнический подход к ответственности алгоритмов, балансирующий эффективность и справедливость.

- [📖 Русская HTML версия](https://romanzorkin.github.io/arxiv_ru/articles/2511.14231/2511.14231_ru.html)
- [📄 Оригинальная статья](https://arxiv.org/abs/2511.14231)
- [🧠 Summary / README](articles/2511.14231/README.md)
- [⚙ Metadata](articles/2511.14231/metadata.json)

---

### Повышение безопасности и надежности
медицинского ИИ с помощью циклов оценки многими агентами
[2601.13268] дата публикации в arXiv - 01.2026  
📅 дата перевода 27.06.2026  
🏷 `medical AI safety` `multi-agent system` `large language models` `ethical alignment` `iterative refinement` `MedSafetyBench` `AMA principles`

Предложена многоагентная система для итеративной оценки и доработки ответов медицинских LLM с использованием этических принципов AMA и пятиуровневой оценки риска. Метод снижает этические нарушения на 89% и понижает риск в 92% случаев без необходимости дообучения моделей.

- [📖 Русская HTML версия](https://romanzorkin.github.io/arxiv_ru/articles/2601.13268/2601.13268_ru.html)
- [📄 Оригинальная статья](https://arxiv.org/abs/2601.13268)
- [🧠 Summary / README](articles/2601.13268/README.md)
- [⚙ Metadata](articles/2601.13268/metadata.json)

---

### Агентный ИИ и вытеснение с рабочих мест: многорегиональный анализ экспозиции задач развивающимся нарушениям на рынке труда
[2604.00186] дата публикации в arXiv - 04.2026  
📅 дата перевода 27.06.2026  
🏷 `agentic AI` `occupational displacement` `task exposure` `workflow automation` `labor market` `AI capability scoring` `regional adoption velocity`

Статья вводит показатель Agentic Task Exposure (ATE) для оценки риска вытеснения профессий агентными ИИ, способными выполнять полные рабочие процессы. Анализ 236 профессий в пяти регионах США показывает, что к 2030 году более 90% информационно-интенсивных профессий достигнут умеренного риска вытеснения, при этом появляются новые роли, связанные с управлением и сотрудничеством с ИИ.

- [📖 Русская HTML версия](https://romanzorkin.github.io/arxiv_ru/articles/2604.00186/2604.00186_ru.html)
- [📄 Оригинальная статья](https://arxiv.org/abs/2604.00186)
- [🧠 Summary / README](articles/2604.00186/README.md)
- [⚙ Metadata](articles/2604.00186/metadata.json)

---

### Глубокое обучение для ценообразования конвертируемых облигаций с зависящими от пути условиями сброса и оговорками о досрочном погашении по требованию
[2605.12189] дата публикации в arXiv - 05.2026  
📅 дата перевода 27.06.2026  
🏷 `convertible bonds` `path-dependent PDE` `deep learning` `neural networks` `financial derivatives` `stochastic volatility` `dynamic programming`

Предложена глубокая нейросетевая методика для оценки конвертируемых облигаций с путём-зависимыми условиями ресета цены конверсии и колла эмитентом. Модель основана на решении PPDE с использованием динамического программирования и аппроксимации условных ожиданий нейросетями, что обеспечивает стабильные и точные цены на примере облигаций China CITIC Bank.

- [📖 Русская HTML версия](https://romanzorkin.github.io/arxiv_ru/articles/2605.12189/2605.12189_ru.html)
- [📄 Оригинальная статья](https://arxiv.org/abs/2605.12189)
- [🧠 Summary / README](articles/2605.12189/README.md)
- [⚙ Metadata](articles/2605.12189/metadata.json)

---

### Какой капитал после труда? Прогнозирование перехода к возврату инвестиций в таланты
в эпоху человек–ИИ
[2606.19846] дата публикации в arXiv - 06.2026  
📅 дата перевода 27.06.2026  
🏷 `talent ROI` `AI augmentation` `firm overhead` `output-based accounting` `convergence capacity` `multitask agency` `labor-time regulation`

Разрыв между временем труда и продуктивным вкладом из-за ИИ требует перехода от учёта затрат на труд по времени к учёту по результатам. На примере Южной Кореи показан рост накладных расходов при сохранении временного учёта, что служит ранним сигналом предстоящего перехода к учёту ROI талантов на основе результатов.

- [📖 Русская HTML версия](https://romanzorkin.github.io/arxiv_ru/articles/2606.19846/2606.19846_ru.html)
- [📄 Оригинальная статья](https://arxiv.org/abs/2606.19846)
- [🧠 Summary / README](articles/2606.19846/README.md)
- [⚙ Metadata](articles/2606.19846/metadata.json)

---

## О проекте


Проект — личный research digest и открытый архив интересных научных материалов.


## Архив статей

|id статьи|Месяц публикации|Дата перевода| Тема статьи | Ручной контроль|
|---|---|---|---|---|
| [2405.19699](articles/2405.19699/README.md) | 05.2024 | 27.06.2026 | Справедливость в найме с применением ИИ: проблемы, показатели, методы и будущие направления (`Fairness in AI-Driven Recruitment: Challenges, Metrics, Methods, and Future Directions`) ||
| [2503.23979](articles/2503.23979/README.md) | 03.2025 | 27.06.2026 | Чем больше, тем веселее: логические и многоступенчатые процессоры в скоринге кредитоспособности (`The more the merrier: logical and multistage processors in credit scoring`) ||
| [2511.03916](articles/2511.03916/README.md) | 11.2025 | 27.06.2026 | Управление человеческими ресурсами и ИИ: контекстная база данных для прозрачности (`Human Resource Management and AI: A Contextual Transparency Database`) ||
| [2511.14231](articles/2511.14231/README.md) | 11.2025 | 27.06.2026 | Алгоритмическое управление и будущее человеческого труда: последствия для автономии, сотрудничества и инноваций (`Algorithmic Management and the Future of Human Work: Implications for Autonomy, Collaboration, and Innovation`) ||
| [2601.13268](articles/2601.13268/README.md) | 01.2026 | 27.06.2026 | Повышение безопасности и надежности медицинского ИИ с помощью циклов оценки многими агентами (`Improving the Safety and Trustworthiness of Medical AI via Multi-Agent Evaluation Loops`) ||
| [2604.00186](articles/2604.00186/README.md) | 04.2026 | 27.06.2026 | Агентный ИИ и вытеснение с рабочих мест: многорегиональный анализ экспозиции задач развивающимся нарушениям на рынке труда (`Agentic AI and Occupational Displacement: A Multi-Regional Task Exposure Analysis of Emerging Labor Market Disruption`) ||
| [2605.12189](articles/2605.12189/README.md) | 05.2026 | 27.06.2026 | Глубокое обучение для ценообразования конвертируемых облигаций с зависящими от пути условиями сброса и оговорками о досрочном погашении по требованию (`A deep learning approach for pricing convertible bonds with path-dependent reset and call provisions`) ||
| [2606.19846](articles/2606.19846/README.md) | 06.2026 | 27.06.2026 | Какой капитал после труда? Прогнозирование перехода к возврату инвестиций в таланты в эпоху человек–ИИ (`What Capital After Labor? Forecasting the Talent ROI Transition in the Human-AI Era`) ||
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
