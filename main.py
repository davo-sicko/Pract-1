import numpy as np

data_coffee = np.array([
    245, 310, 180, 260, 290, 3500, 220, 275, 240, 310,
    190, 265, 285, 210, 245, 300, 180, 4000, 290, 150,
    330, 220, 275, 240, 310, 190, 265, 285, 210, 245,
    300, 180, 260, 290, 150, 330, 220, 275, 240, 310,
    190, 265, 285, 210, 176, 300, 180, 260, 290, 150,
    330, 220, 275, 240, 310, 190, 265, 285, 210, 245
])

A = np.array([210, 245, 300, 180, 260, 290, 150, 330, 220, 275, 240, 310, 190, 265, 285])

mean_val = np.mean(data_coffee)
median_val = np.median(data_coffee)
std_val = np.std(data_coffee)
var_val = np.var(data_coffee)
max_val = np.max(data_coffee)
min_val = np.min(data_coffee)
ptp_val = np.ptp(data_coffee)

p25, p50, p75, p90, p99 = np.percentile(data_coffee, [25, 50, 75, 90, 99])
q1 = np.percentile(data_coffee, 25)
q3 = np.percentile(data_coffee, 75)
iqr = q3 - q1

lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
outliers = data_coffee[(data_coffee < lower_bound) | (data_coffee > upper_bound)]

print("\nРЕЗУЛЬТАТЫ ЗАДАНИЯ 1")
print(f"Среднее значение:               {mean_val}")
print(f"Медиана (50-й перцентиль):      {median_val}")
print(f"Стандартное отклонение:         {std_val}")
print(f"Дисперсия:                      {var_val}")
print(f"Максимальное значение:          {max_val}")
print(f"Минимальное значение:           {min_val}")
print(f"Размах данных:                  {ptp_val}")
print(f"25-й перцентиль (Q1):           {p25}")
print(f"50-й перцентиль (Q2):           {p50}")
print(f"75-й перцентиль (Q3):           {p75}")
print(f"90-й перцентиль:                {p90}")
print(f"99-й перцентиль:                {p99}")
print(f"Первый квартиль (Q1):           {q1}")
print(f"Третий квартиль (Q3):           {q3}")
print(f"Межквартильный размах (IQR):    {iqr}")
print(f"Допустимый интервал:            [{lower_bound}, {upper_bound}]")
print(f"Обнаруженные выбросы:           {outliers.tolist()}")

matrix_A = A.reshape(3, 5)
matrix_shape = matrix_A.shape
matrix_size = matrix_A.size
row_sums = matrix_A.sum(axis=1)
col_sums = matrix_A.sum(axis=0)
matrix_transposed = matrix_A.T

mean_A = np.mean(matrix_A)
std_A = np.std(matrix_A)
var_A = np.var(matrix_A)
q1_A, q2_A, q3_A = np.percentile(matrix_A, [25, 50, 75])

print("\nРЕЗУЛЬТАТЫ ЗАДАНИЯ 2 (Матрица A)")
print(f"Матрица 3x5:\n {matrix_A}")
print(f"Размерность: {matrix_shape}")
print(f"Общее количество элементов: {matrix_size}")
print(f"Сумма по строкам: {row_sums.tolist()}")
print(f"Сумма по столбцам: {col_sums.tolist()}")
print(f"Транспонированная матрица (5x3):\n {matrix_transposed}")
print(f"Среднее по элементам матрицы:       {mean_A}")
print(f"Стандартное отклонение матрицы:     {std_A}")
print(f"Дисперсия матрицы:                  {var_A}")
print(f"Квартили матрицы (Q1, Q2, Q3):      {q1_A}, {q2_A}, {q3_A}")

total_revenue = np.sum(data_coffee)
low_checks = data_coffee[data_coffee < 200]

print("\nИНДИВИДУАЛЬНЫЕ ВОПРОСЫ ВАРИАНТА 1")
print(f"Общая выручка за 60 дней: {total_revenue} руб.")
print(f"Количество дней с чеками ниже 200 руб.: {low_checks.size}")
print(f"Значения чеков в эти дни:               {low_checks.tolist()}")