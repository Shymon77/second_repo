from pathlib import Path  
import sys 

def total_salary (path) :
    try :
        with open (path, 'r', encoding='UTF-8') as file :
            salaries = [float(line.strip().split(',')[1]) for line in file]
    except FileNotFoundError :
        print(f"Файл не знайдено: {path}")
        return 0, 0
    if not salaries :
        return 0, 0
    total = sum(salaries)
    average = total / len(salaries)
    return total, average   
total, average = total_salary("salaries.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")