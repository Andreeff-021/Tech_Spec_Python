# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

wikipedia_article = "Python (МФА: [ˈpʌɪθ(ə)n]; в русском языке встречаются названия пито́н[23] или па́йтон[24]) — " \
                    "высокоуровневый язык программирования общего назначения с динамической строгой типизацией и " \
                    "автоматическим управлением памятью[25][26], ориентированный на повышение производительности " \
                    "разработчика, читаемости кода и его качества, а также на обеспечение переносимости написанных " \
                    "на нём программ[27]. Язык является полностью объектно-ориентированным в том плане, что всё " \
                    "является объектами[25]. Необычной особенностью языка является выделение блоков кода пробельными " \
                    "отступами[28]. Синтаксис ядра языка минималистичен, за счёт чего на практике редко возникает " \
                    "необходимость обращаться к документации[27]. Сам же язык известен как интерпретируемый и " \
                    "используется в том числе для написания скриптов[25]. Недостатками языка являются зачастую более " \
                    "низкая скорость работы и более высокое потребление памяти написанных на нём программ по " \
                    "сравнению с аналогичным кодом, написанным на компилируемых языках, таких как C или C++[25][27]. " \
                    "Python является мультипарадигменным языком программирования, поддерживающим императивное, " \
                    "процедурное, структурное, объектно-ориентированное программирование[25], метапрограммирование[29] " \
                    "и функциональное программирование[25]. Задачи обобщённого программирования решаются за счёт " \
                    "динамической типизации[30][31]. Аспектно-ориентированное программирование частично поддерживается " \
                    "через декораторы[32], более полноценная поддержка обеспечивается дополнительными фреймворками[33]. " \
                    "Такие методики как контрактное и логическое программирование можно реализовать с помощью библиотек" \
                    " или расширений[34]. Основные архитектурные черты — динамическая типизация, автоматическое " \
                    "управление памятью[25], полная интроспекция, механизм обработки исключений, поддержка " \
                    "многопоточных вычислений с глобальной блокировкой интерпретатора (GIL)[35], высокоуровневые " \
                    "структуры данных. Поддерживается разбиение программ на модули, которые, в свою очередь, " \
                    "могут объединяться в пакеты[36]. Эталонной реализацией Python является интерпретатор CPython, " \
                    "который поддерживает большинство активно используемых платформ[37] и являющийся стандартом " \
                    "де-факто языка[38]. Он распространяется под свободной лицензией Python Software Foundation " \
                    "License, позволяющей использовать его без ограничений в любых приложениях, " \
                    "включая проприетарные[39]. CPython компилирует исходные тексты в высокоуровневый байт-код, " \
                    "который исполняется в стековой виртуальной машине[40]. К другим трём основным реализациям " \
                    "языка относятся Jython (для JVM), IronPython (для CLR/.NET) и PyPy[25][41]. PyPy написан на " \
                    "подмножестве языка Python (RPython) и разрабатывался как альтернатива CPython с целью " \
                    "повышения скорости исполнения программ, в том числе за счёт использования JIT-компиляции[41]. " \
                    "Поддержка версии Python 2 закончилась в 2020 году[42]. На текущий момент активно развивается " \
                    "версия языка Python 3[43]. Разработка языка ведётся через предложения по расширению языка PEP " \
                    "(англ. Python Enhancement Proposal), в которых описываются нововведения, делаются корректировки " \
                    "согласно обратной связи от сообщества и документируются итоговые решения[44]. Стандартная " \
                    "библиотека включает большой набор полезных переносимых функций, начиная с возможностей для " \
                    "работы с текстом и заканчивая средствами для написания сетевых приложений. Дополнительные " \
                    "возможности, такие как математическое моделирование, работа с оборудованием, написание " \
                    "веб-приложений или разработка игр, могут реализовываться посредством обширного количества " \
                    "сторонних библиотек, а также интеграцией библиотек, написанных на Си или C++, при этом и сам " \
                    "интерпретатор Python может интегрироваться в проекты, написанные на этих языках[25]. Существует " \
                    "и специализированный репозиторий программного обеспечения, написанного на Python, — PyPI[45]." \
                    " Данный репозиторий предоставляет средства для простой установки пакетов в операционную систему " \
                    "и стал стандартом де-факто для Python[46]. По состоянию на 2019 год в нём содержалось более 175 " \
                    "тысяч пакетов[45]. Python стал одним из самых популярных языков, он используется в анализе " \
                    "данных, машинном обучении, DevOps и веб-разработке, а также в других сферах, включая разработку" \
                    " игр. За счёт читабельности, простого синтаксиса и отсутствия необходимости в компиляции " \
                    "язык хорошо подходит для обучения программированию, позволяя концентрироваться на изучении" \
                    " алгоритмов, концептов и парадигм. Отладка же и экспериментирование в значительной степени " \
                    "облегчаются тем фактом, что язык является интерпретируемым[25][47]. Применяется язык многими " \
                    "крупными компаниями, такими как Google или Facebook[25]. По состоянию на сентябрь 2022 года" \
                    " Python занимает первое место в рейтинге TIOBE популярности языков программирования с" \
                    " показателем 15,74 %[48]. «Языком года» по версии TIOBE Python объявлялся в 2007, 2010," \
                    " 2018, 2020 и 2021 годах[49]."

list_article = wikipedia_article.replace('(', '').replace(')', '').replace('.', '').replace(',', '')\
    .replace(';', '').replace('-', '').lower().split()

dict_article = {item: list_article.count(item) for item in list_article}

sorted_dict = {}
sorted_keys = sorted(dict_article, key=dict_article.get, reverse=True)

for word in sorted_keys:
    sorted_dict[word] = dict_article[word]
    
print(list(sorted_dict.items())[:11])