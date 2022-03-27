import unittest
import random
import os
import subprocess

class TestBC(unittest.TestCase):
    def setUp(self):
        self.a = random.randint(-20000, 20000)
        self.b = random.randint(-20000, 20000)
        self.c = random.randint(-20000, 20000)
        self.f = round(random.uniform(0.0001, 0.00019), 4)

    def io_bc(self, input, l=''):
        subprocess_ = subprocess.Popen(f"echo \"{input}\" | bc {l}", shell=True, stdout=subprocess.PIPE)
        subprocess_.wait()
        subprocess_return = subprocess_.stdout.read()
        subprocess_.kill()
        print(subprocess_return)
        return int(subprocess_return)
    
    def return_code_bc(self, input, l=''):
        return os.system(f'echo {input} | bc {l}')

    def test_case_1(self):
        answer = self.a + self.b
        cmd = f'{self.a} + {self.b}'
        self.assertEqual(answer, self.io_bc(cmd))
    
    def test_case_2(self):
        answer = self.a * self.b
        cmd = f'{self.a} * {self.b}'
        self.assertEqual(answer, self.io_bc(cmd))
    
    def test_case_3(self):
        sq = self.a * self.a
        answer = self.a
        cmd = f'sqrt({sq})'
        self.assertEqual(answer, self.io_bc(cmd))
    
    def test_case_4(self):
        cmd = f'{self.a} / 0'
        self.assertEqual(0, self.return_code_bc(cmd))

    def test_case_5(self):
        answer = 0
        cmd = f"""  x = {self.a};
                    x = 0;  
                    x   """
        self.assertEqual(answer, self.io_bc(cmd))
    
    def test_case_6(self):
        answer = self.a + self.b
        cmd = f"""  a = {self.a};
                    b = {self.b};  
                    a + b   """
        self.assertEqual(answer, self.io_bc(cmd))
    
    def test_case_7(self):
        answer = self.a * self.b + self.c
        cmd = f"""  define fma(x, y, z) {{
                       return x * y + z
                    }};
                    fma({self.a}, {self.b}, {self.c})  """
        self.assertEqual(answer, self.io_bc(cmd))
    
    def test_case_8(self):
        answer = 1
        cmd = f"""  define abs(i) {{
                        if (i < 0) return (-i)
                        return (i)
                    }};
                    abs(l(e({self.a})) - {self.a}) < 0.000001   """
        self.assertEqual(answer, self.io_bc(cmd, '-l'))
    
    def test_case_9(self):
        answer = 4
        cmd = f"scale({self.f})"
        self.assertEqual(answer, self.io_bc(cmd, '-l'))
    
    def test_case_10(self):
        answer = 1
        cmd = f"""  define abs(i) {{
                        if (i < 0) return (-i)
                        return (i)
                    }};
                    abs(s(a)^2 + c(a)^2 - 1) < 0.00001   """
        self.assertEqual(answer, self.io_bc(cmd, '-l'))



if __name__ == "__main__":
  unittest.main()