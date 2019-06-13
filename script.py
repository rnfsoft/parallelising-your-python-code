# import multiprocessing
# num_of_cpu = multiprocessing.cpu_count()
# print (num_of_cpu)

from multiprocessing import Pool
import time

def fibonacci_sequence_of(num):
    first_number = 0
    second_number = 1
    num = int(num)
    if num in (0,1):
        print('Fibonacci of {} is {}'.format(num, num))
    else:
        for i in range(2, num):
            new_number = first_number + second_number
            first_number = second_number
            second_number = new_number
        print('Fibonacci of {} is {}'.format(num, second_number))

if __name__ == '__main__':
    input_numbers = input('Provide multiple numbers: ')
    input_values = map(int, input_numbers.split())

    # start = time.time()
    # for i in input_values:
    #     fibonacci_sequence_of(i)
    # end = time.time()
    # time_taken = round((end-start)*1000,1)
    # print('It taeks {} milli-seconds to calcuate the fibonacci of {} currently'.format(time_taken, input_numbers))

    start = time.time()
    pool = Pool()
    result = pool.map(fibonacci_sequence_of, input_values)
    end = time.time()
    time_taken = round((end-start)*1000,1)
    print('It taeks {} milli-seconds to calcuate the fibonacci of {} currently'.format(time_taken, input_numbers))
    pool.close()
    pool.join()