# list directories in results
import os

html = '<html><head><title>Report</title><script src="https://cdn.tailwindcss.com"></script><meta charset="utf-8"></head><body>'

html += '<div class="p-4 m-4 border border-gray-400 rounded-lg shadow-lg">'
html += '<h2 class="font-semibold text-lg">Genetic programming report</h2><br>'
html += 'Authors: <br>'
html += '- Krzysztof Czechowicz<br>'
html += '- Mateusz Woźniak<br>'
html += '</div>'

grammar = open('gramatyka.g4').read()

html += '<div class="p-4 m-4 border border-gray-400 rounded-lg shadow-lg">'
html += '<h2 class="font-semibold text-lg">Grammar</h2>'
html += f'<div class="mt-2 bg-gray-100 rounded-lg p-4"><pre>{grammar}</pre></div>'
html += '</div>'

tests = os.listdir('results')
for test in sorted(tests):
    if test.startswith('.'):
        continue
    if not os.path.exists(f'results/{test}/best_fitness.txt'):
        continue
    if not os.path.exists(f'results/{test}/best_program.txt'):
        continue
    if not os.path.exists(f'results/{test}/fitness_function.py'):
        continue
    print(test)
    html += '<div class="p-4 m-4 border border-gray-400 rounded-lg shadow-lg">'
    html += f'<h1 class="font-semibold text-lg">Test: {test}</h1>'
    best_fitness = open(f'results/{test}/best_fitness.txt').read()
    best_program = open(f'results/{test}/best_program.txt').read()
    fitness_function = open(f'results/{test}/fitness_function.py').read()
    if best_fitness == '0.0':
        best_fitness = '9999'
    if best_fitness == '0':
        html += '<h4 class="text-green-500">Problem solved!</h4>'
    else:
        html += '<h4 class="text-red-500">Problem not solved.</h4>'

    html += f'<h4>Fitness function:</h4>'
    html += f'<div class="mt-2 bg-gray-100 rounded-lg p-4"><pre>{fitness_function}</pre></div>'
    html += f'<h4>Best fitness: {best_fitness}</h4>'
    html += f'<h4>Best program:</h4>'
    html += f'<div class="mt-2 bg-gray-100 rounded-lg p-4"><pre>{best_program}</pre></div>'

    if os.path.exists(f'results/{test}/fitness.png'):
        html += f'<img src="results/{test}/fitness.png" alt="fitness" class="mt-4">'

    html += '</div>'

html += '</body></html>'

open('report.html', 'w', encoding='utf-8').write(html)
