import numpy as np

def input_matrix():
    rows = int(input("Введіть кількість рядків матриці: "))
    cols = int(input("Введіть кількість стовпців матриці: "))
    matrix = []
    
    print("Введіть елементи матриці по рядках:")
    for i in range(rows):
        row = list(map(int, input(f"Рядок {i+1}: ").split()))
        matrix.append(row)
    
    return np.array(matrix)

def add_matrices(A, B):
    if A.shape != B.shape:
        print("Матриці повинні бути однакових розмірів для додавання!")
        return None
    return A + B

def subtract_matrices(A, B):
    if A.shape != B.shape:
        print("Матриці повинні бути однакових розмірів для віднімання!")
        return None
    return A - B

def multiply_matrix_by_scalar(A, scalar):
    return A * scalar

def multiply_matrices(A, B):
    if A.shape[1] != B.shape[0]:
        print("Кількість стовпців першої матриці повинна бути рівною кількості рядків другої матриці!")
        return None
    return np.dot(A, B)

def play():
    print("Калькулятор для роботи з матрицями\n")
    
    print("Матриця 1:")
    matrix1 = input_matrix()
    
    print("Матриця 2:")
    matrix2 = input_matrix()
    
    print("\nОберіть операцію:")
    print("1. Додавання матриць")
    print("2. Віднімання матриць")
    print("3. Множення матриці на число")
    print("4. Множення двох матриць")
    
    choice = int(input("\nВаш вибір (1/2/3/4): "))
    
    if choice == 1:
        result = add_matrices(matrix1, matrix2)
    elif choice == 2:
        result = subtract_matrices(matrix1, matrix2)
    elif choice == 3:
        scalar = int(input("Введіть число для множення: "))
        result = multiply_matrix_by_scalar(matrix1, scalar)
    elif choice == 4:
        result = multiply_matrices(matrix1, matrix2)
    else:
        print("Невірний вибір!")
        return
    
    if result is not None:
        print("\nРезультат операції:")
        print(result)


play()
