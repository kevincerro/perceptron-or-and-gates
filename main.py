import random

train_or_data = (
    (0, 0, 0),
    (0, 1, 1),
    (1, 0, 1),
    (1, 1, 1),
)

train_and_data = (
    (0, 0, 0),
    (0, 1, 0),
    (1, 0, 0),
    (1, 1, 1),
)

test_data = (
    (0, 0),
    (0, 1),
    (1, 0),
    (1, 1),
)


class Perceptron:

    b = 1
    a = 0.1

    def __init__(self, gate_type, train_data):
        self.gate_type = gate_type
        self.train_data = train_data
        self.w0 = random.uniform(0, 1)
        self.w1 = random.uniform(0, 1)
        self.w2 = random.uniform(0, 1)

    def activation(self, result):
        if result >= 0:
            return 1
        else:
            return 0

    def perceptron(self, x1, x2):
        psum = (self.b * self.w0) + (x1 * self.w1) + (x2 * self.w2)

        return self.activation(psum)

    def calculate_weights(self, error, data):
        self.w0 = self.w0 + (self.a * error * self.b)
        self.w1 = self.w1 + (self.a * error * data[0])
        self.w2 = self.w2 + (self.a * error * data[1])


    def train(self):
        trained = False

        while not trained:
            ok = True

            for data in self.train_data:
                result = self.perceptron(data[0], data[1])
                error = data[2] - result

                if error != 0:
                    self.calculate_weights(error, data)
                    ok = False
                    break

            if ok:
                trained = True
                print()
                print('Training finished:')
                print(f'- Bias = {self.b}')
                print(f'- W0 = {self.w0}')
                print(f'- W1 = {self.w1}')
                print(f'- W2 = {self.w2}')
                print(f'- A = {self.a}')
                print()

    def test(self):
        print('Test started:')
        print()
        for data in test_data:
            print(f"{data[0]} {self.gate_type} {data[1]} => {self.perceptron(data[0], data[1])}")

    def start(self):
        print()
        print(f'## {self.gate_type} gate ##')

        self.train()

        self.test()


# OR GATE
p = Perceptron('OR', train_or_data)
p.start()

# AND GATE
p = Perceptron('AND', train_and_data)
p.start()
