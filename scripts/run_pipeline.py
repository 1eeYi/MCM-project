import subprocess
import sys

def run(cmd):
    print(f"\n[run_pipeline] $ {' '.join(cmd)}")
    subprocess.check_call(cmd)

def main():
    run([sys.executable, "scripts/fetch_data.py"])
    run([sys.executable, "scripts/clean_data.py"])
    # 后续你们把主程序接进来，例如：
    # run([sys.executable, "main.py"])

if __name__ == "__main__":
    main()
