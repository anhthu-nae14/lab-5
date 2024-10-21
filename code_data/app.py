from flask import Flask, render_template
import subprocess

app = Flask(__name__)

# Hàm để chạy file Python và lấy kết quả đầu ra
def run_script(script_name):
    result = subprocess.run(['python', script_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0:
        return result.stdout  # Trả về đầu ra nếu chạy thành công
    else:
        return f"Error running {script_name}: {result.stderr}"  # Trả về lỗi nếu có

@app.route('/')
def index():
    # Chạy 2 file script1.py và script2.py
    output1 = run_script('bai1.py')
    output2 = run_script('bai2.py')

    # Truyền kết quả vào template HTML
    return render_template('index.html', output1=output1, output2=output2)

if __name__ == '__main__':
    app.run(debug=True)
